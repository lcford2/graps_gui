subroutine constr_res(nparam,index_cons, decision_var,gcons)!,id_output,value_output,constraints,cons_id,cons_mag,&
	! min_rel,max_rel,user_id,spill_values,deficit_values,res_ids_for_spdef)
USE My_variables
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal

double precision, dimension(nparam) :: decision_var
! double precision, dimension(nparam) :: value_output, spill_values, deficit_values
! integer :: id_output(nparam), cons_id(ncons-nres_level)
! ! double precision, dimension(nparam) :: value_output
! double precision, dimension(ncons) :: constraints
! double precision, dimension(nres) :: cons_mag
! integer, dimension(nparam) :: res_ids_for_spdef
! double precision, dimension(nuser) :: min_rel, max_rel
! integer, dimension(nuser) :: user_id
double precision, dimension(nensem) :: total_deficit
! integer ifinal
! check whether the current value of iteration is same as that of previous iteration
! If so , just return the current value of the constraint using the variable index_cons.

!gcons = -0.1

!returnco

! this is for terminal output, we do not want terminal output during optimization
! print *, ('-', i=1,75)
! print *, "Starting Simulation"
! print *, ('-', i=1,75)

ivar_status = icheck_var_status(nparam,decision_var,temp_decision_var)
! ! if (ifinal.eq.1) ivar_status =1
if(ivar_status.eq.0)then
! 	! print *, cons_global(index_cons)
! 	! gcons = cons_global(index_cons)
	gcons = lukes_cons(index_cons)
! !	gcons = -0.1
  return
end if
! if the decision_variable value has changed then perform simulation

nsimul_block = nres +nfnode

!call array_int_ini(ntemp,isimul_status,0)

itemp_type = 0
itemp_id = 0


iflow_set = 0
icurrent_id = 0
icurrent_type = 0

	! do i=1,84
	! 	value_output(i) = 1.0
	! 	id_output(i) = 1
	! end do

 call array_ini(nensem,total_deficit,0.0d0)
 call array_ini(nensem,value_net,0.0d0)
 call array_ini(ncons,cons_global,0.0d0)


 do i = 1, nparam
	spill_values(i) = 0.0
	deficit_values(i) = 0.0
	res_ids_for_spdef(i) = 0
 enddo
!  call array_ini(nparam,id_output,0)
!  call array_ini(nparam,value_output,0.0d0)
! Initialize controlled and uncontrolled flows for each watershed

do i = 1,nwatershed

		call array_ini(ntime,my_flow_set(i)%controlled_flows,0.0d0)

		do j = 1,nensem

			call array_ini(ntime,my_flow_set(i)%uncontrolled_flows(1,j),0.0d0)

		end do

		parallel_track(i)%order_type = 0

		parallel_track(i)%order_id = 0

end do


icount = 0

! Loop for simulation at each junction node and reservoir

! print *, nsimul_block
!call solution_path()
!print *, (k1, my_network_order(k1)%order_type, my_network_order(k1)%order_id, k1=1, nsimul_block)

do i = 1, nsimul_block


								   !    iprev_type, nparam, decision_var)
	iprev_id = icurrent_id
	iprev_type = icurrent_type

	icurrent_type = my_network_order(i)%order_type
	icurrent_id = my_network_order(i)%order_id


	!    iprev_type,nparam,decision_var,total_deficit,nend_cons,id_output,value_output, &
	!    min_rel, max_rel, user_id,spill_values,deficit_values,res_ids_for_spdef)
	
	if (icurrent_type.eq.5) then
		call node_simul_module(icurrent_type,icurrent_id,iprev_id, &
							   iprev_type, nparam, decision_var)
	end if
	
        !icurrent_type = 3

	if(icurrent_type.eq.3)call reservoir_simul_module(icurrent_type,icurrent_id, iprev_id, &
	   iprev_type,nparam,decision_var,total_deficit,nend_cons)!,id_output,value_output, &
	!    min_rel, max_rel, user_id, spill_values,deficit_values,res_ids_for_spdef)
	!print *, 'I am Here', icurrent_type, icurrent_id
	if(icurrent_type.eq.3)icount = icount +1
	ensem = nensem
	! Calculation for end of time steps storage constraints
	if(icurrent_type.eq.3) then
		cons_global(icount) = (nend_cons/ensem) - my_reservoir(icurrent_id)%storage_prob
		constraints(icount) = cons_global(icount)
		cons_mag(icount) = my_reservoir(icurrent_id)%final_storage - my_reservoir(icurrent_id)%target_storage
		cons_id(icount) = icurrent_id
		4444 format(5x,a,F3.1,2x,F3.1,2x,F3.1)
		! if (cons_global(icount).gt.0) then
		! 	write(*,4444) my_reservoir(icurrent_id)%name, cons_global(icount), (nend_cons/ensem), my_reservoir(icurrent_id)%storage_prob
		! end if
	end if
end do

do i=1,nuser
	user_id(i) = my_user(i)%ID
	min_rel(i) = my_user(i)%minimum_release
	max_rel(i) = my_user(i)%maximum_release
end do

call deficit_splitter(total_deficit,decision_var,nparam)!,constraints,cons_id)
! do i = 1,nparam
! 	print *, value_output(i)
! end do
! gcons = cons_global(index_cons)
gcons = lukes_cons(index_cons)

return
end

subroutine optimize(nparam, ncons, decision_var, func_flag)
	use path_vars
	implicit double precision(a-h, o-z)
	common /final_print/ifinal
	double precision, dimension(nparam) :: decision_var, decision_var_lb, decision_var_ub
	double precision bigbnd, eps, epseqn, udelta, gcons
	double precision, allocatable :: f(:), g(:), w(:)
	integer nf, neqn, nineqn, nineq, neq, mode, iprint, miter, inform, iwsize, nwsize, ncheck, ncons
	integer, allocatable :: iw(:)
	integer func_flag
	external constr_decision_extract, constr_res, ffsqp, grobfd, grcnfd
	external expected_benefits, max_hydropower, min_spill_deficit, max_hydro_benefits, max_release

	open(unit =32, file=trim(input_path)//'model_para.dat',ACTION = 'READ', STATUS = 'OLD')
	read(32,*) nf
	read(32,*) mode
	read(32,*) iprint
	read(32,*) miter
	read(32,*) bigbnd 
	read(32,*) eps
	read(32,*) epseqn
	read(32,*) udelta 

	call constr_decision_extract(decision_var_lb,decision_var_ub, decision_var, nparam)

	ifinal = 1
	index_cons = 1
	call constr_res(nparam, index_cons, decision_var, gcons)
	
	nineqn = ncons
	nineq = ncons
	neqn = 0
	neq = 0
	iwsize = 6*nparam + 8*max(1, nineq+neq) + 7*max(1, nf) + 30 + 100 ! add 100 to make it large enough
	nwsize = 4*nparam*nparam + 5*max(1, nineq+neq)*nparam
	nwsize = nwsize + 3*nf*nparam + 26*(nparam*max(1, nf)) + 45*(nineq + neq) + 100
	ncheck = nineq+neq

	print *, "Running FFSQP with the following parameters:"
	print *, "nineqn = ", nineqn
	print *, "nineq  = ", nineq
	print *, "neqn   = ", neqn 
	print *, "neq    = ", neq
	print *, "iwsize = ", iwsize
	print *, "nwsize = ", nwsize 
	print *, "ncheck = ", ncheck 
	read(*,*) 

	ALLOCATE(iw(iwsize), w(nwsize), g(ncheck), f(nf))

	ifinal = 0
	inform = 0
	index_cons = 1
	constraint_tolerance = 1e-3

	
	!      map for func_flags
	! ----------------------------------
	!   func_flag  |     objective
	! ----------------------------------
	!       1      | max_hydro_benefits
	!       2      | max_hydropower
	!       3      | min_spill_deficit
	!       4      | max_release

	if (func_flag.eq.1) then
		write (*, "(A)") "Maximizing Hydro Benefits"
		call FFSQP(nparam, nf, nineqn, nineq, neqn, neq, mode, iprint, miter, inform, &
				bigbnd, eps, epsneq, udelta, decision_var_lb, decision_var_ub, &
				decision_var, f, g, iw, iwsize, w, nwsize, max_hydro_benefits, &
				constr_res, grobfd, grcnfd)
	else if (func_flag.eq.2) then
		write (*, "(A)") "Maximizing Hydropower"
		call FFSQP(nparam, nf, nineqn, nineq, neqn, neq, mode, iprint, miter, inform, &
				bigbnd, eps, epsneq, udelta, decision_var_lb, decision_var_ub, &
				decision_var, f, g, iw, iwsize, w, nwsize, max_hydropower, &
				constr_res, grobfd, grcnfd)
	else if (func_flag.eq.3) then
		write (*, "(A)") "Minimizing Spill and Deficit"
		call FFSQP(nparam, nf, nineqn, nineq, neqn, neq, mode, iprint, miter, inform, &
				bigbnd, eps, epsneq, udelta, decision_var_lb, decision_var_ub, &
				decision_var, f, g, iw, iwsize, w, nwsize, min_spill_deficit, &
				constr_res, grobfd, grcnfd)
	else if (func_flag.eq.4) then
		write (*, "(A)") "Maximizing Release"
		call FFSQP(nparam, nf, nineqn, nineq, neqn, neq, mode, iprint, miter, inform, &
				bigbnd, eps, epsneq, udelta, decision_var_lb, decision_var_ub, &
				decision_var, f, g, iw, iwsize, w, nwsize, max_release, &
				constr_res, grobfd, grcnfd)
	end if

	ifinal = 1
	call constr_res(nparam, index_cons, decision_var, gcons)

end subroutine optimize


subroutine python_simulate(nparam,index_cons,decision_var,gcons,py_hydro_benefit,py_id_output,py_value_output,py_constraints,py_cons_id,py_cons_mag,&
						   py_min_rel,py_max_rel,py_user_id,py_spill_values,py_deficit_values,py_res_ids_for_spdef,func_flag)
	Use My_variables
	double precision, dimension(nparam) :: decision_var
	integer nparam, index_cons
	double precision gcons

	! python variables
	double precision py_value_output(nparam), py_spill_values(nparam), py_deficit_values(nparam)
	double precision py_cons_mag(nres), py_min_rel(nuser), py_max_rel(nuser), py_constraints(ncons)
	double precision py_hydro_benefit(nparam)
	integer py_id_output(nparam), py_cons_id(ncons - nres_level), py_res_ids_for_spdef(nparam), py_user_id(nuser)
	integer func_flag
	external constr_res

	! passing hydro prices from temoa
	hydro_benefit = py_hydro_benefit

	call constr_res(nparam, index_cons, decision_var, gcons)

	! assigning return values
	py_value_output = value_output
	py_spill_values = spill_values
	py_deficit_values = deficit_values
	py_id_output = id_output
	py_res_ids_for_spdef = res_ids_for_spdef
	py_min_rel = min_rel
	py_max_rel = max_rel
	py_user_id = user_id
	py_cons_mag = cons_mag
	py_constraints = constraints
	py_cons_id = cons_id

end subroutine python_simulate


subroutine python_optimize(nparam,index_cons,decision_var,gcons,py_hydro_benefit,py_id_output,py_value_output,py_constraints,py_cons_id,py_cons_mag,&
						   py_min_rel,py_max_rel,py_user_id,py_spill_values,py_deficit_values,py_res_ids_for_spdef,func_flag)
	Use My_variables
	double precision, dimension(nparam) :: decision_var
	integer nparam, index_cons
	double precision gcons
	! python variables
	double precision py_value_output(nparam), py_spill_values(nparam), py_deficit_values(nparam)
	double precision py_cons_mag(nres), py_min_rel(nuser), py_max_rel(nuser), py_constraints(ncons)
	double precision py_hydro_benefit(nparam)
	integer py_id_output(nparam), py_cons_id(ncons - nres_level), py_res_ids_for_spdef(nparam), py_user_id(nuser)
	integer func_flag
	external optimize
	
	! passing hydro prices from temoa
	hydro_benefit = py_hydro_benefit
	
	call optimize(nparam, lukes_ncons, decision_var, func_flag)

	! setting up return values
	py_value_output = value_output
	py_spill_values = spill_values
	py_deficit_values = deficit_values
	py_id_output = id_output
	py_res_ids_for_spdef = res_ids_for_spdef
	py_min_rel = min_rel
	py_max_rel = max_rel
	py_user_id = user_id
	py_cons_mag = cons_mag
	py_constraints = constraints
	py_cons_id = cons_id
		
end subroutine python_optimize

subroutine reservoir_simul_module(icurrent_type,icurrent_id, iprev_id, &
	   iprev_type,nparam,decision_var,total_deficit,nend_cons)!id_output,value_output, &
	!    min_rel, max_rel, user_id, spill_values,deficit_values,res_ids_for_spdef)
	USE My_variables
	implicit doubleprecision(a-h,o-z)
	common /final_print/ifinal

	! integer :: id_output(nparam)
	integer :: spill_count(ntime), def_count(ntime)
	! double precision, dimension(nparam) :: value_output, spill_values, deficit_values
	! integer, dimension(nparam) :: res_ids_for_spdef

	double precision decision_var(nparam),q(ntime),simul_deficit(ntime),simul_evapo(ntime), spill_tot(ntime), def_tot(ntime)
	double precision simul_stor(ntime), simul_spill(ntime),rate_area(ntime),release(ntime),act_release(ntime)
	double precision storage_tot(ntime), release_tot(ntime), hydro_tot(ntime)
	double precision total_deficit(nensem)
	! double precision, dimension(nuser) :: min_rel, max_rel
	! integer, dimension(nuser) :: user_id

	nparent = my_reservoir(icurrent_id)%nparent

	ijump = 0
	iadd = 0

	do i1 = 1,nparent
			
		if((iprev_type.eq.my_reservoir(icurrent_id)%parent_type(i1)).and. &
			(iprev_id.eq.my_reservoir(icurrent_id)%parent_id(i1)))ijump = 1

	end do

	if(ijump.eq.0)then
	
		if((iprev_type.ne.0).and.(iprev_id.ne.0))then

			parallel_track(iflow_set)%order_id = iprev_id
			parallel_track(iflow_set)%order_type = iprev_type

		end if

		iflow_set = iflow_set +1
        
	end if 

	do i = 1,nensem
		do j = 1,ntime
			my_flow_set(iflow_set)%uncontrolled_flows(j,i) = 0
		end do
	end do

inodeparent = 0

	do i1 = 1,nparent

		iparent_type = my_reservoir(icurrent_id)%parent_type(i1)
		if (iparent_type == 5)  then 
						inodeparent =1
		else 
						inodeparent = 0
		end if               

	end do

!print *, 'HEREEEEEEE'        

if (inodeparent.ne.1) then
	do j = 1,ntime
		my_flow_set(iflow_set)%controlled_flows(j) = 0
	end do
end if

!print *, 'HEREEEEEEEE2222'

        ! Loop for adding controlled and uncontrolled flow from parents
	do i1 = 1,nparent

		iparent_type = my_reservoir(icurrent_id)%parent_type(i1)
		iparent_id   = my_reservoir(icurrent_id)%parent_id(i1)
! Prepare the inflow sets

		iadd = 0

		if(iparent_type.eq.1)call add_uncontrolled_flows  &
		  (iparent_type,iparent_id,decision_var,nparam)


		if(iparent_type.eq.3) then

!		    do j1 = 1,nwatershed

!				if((parallel_track(j1)%order_type.eq.iparent_type).and. &
!				  (parallel_track(j1)%order_id.eq.iparent_id))call add_all_flows &
!				  (j1,iparent_type,iparent_id,decision_var,nparam)

!			end do
			call add_controlled_flows(iparent_type,iparent_id, decision_var,nparam)

		end if
		 
		if(iparent_type.eq.5) then
			
		    do j1 = 1,nwatershed

				if((parallel_track(j1)%order_type.eq.iparent_type).and. &
				  (parallel_track(j1)%order_id.eq.iparent_id))call add_all_flows &
				  (j1,iparent_type,iparent_id,decision_var,nparam)

			end do

            if((iparent_type.ne.iprev_type).and.(iparent_id.ne.iprev_id))call  &
			add_controlled_flows(iparent_type,iparent_id, decision_var,nparam)

		end if

		if((iparent_type.eq.4).or.(iparent_type.eq.13))call add_controlled_flows  &
		  (iparent_type,iparent_id, decision_var,nparam)

	end do

!print *, 'TAGGG 229'

! Prepare the outflow sets

call array_ini(ntime,release, 0.0d0)
call array_ini(ntime,act_release, 0.0d0)


	nchild = my_reservoir(icurrent_id)%nchild

!print *, 'TAGGG 237'

        
! Loop for adding the releases to child nodes
	do i1 = 1,nchild

		ichild_type = my_reservoir(icurrent_id)%child_type(i1)
		ichild_id   = my_reservoir(icurrent_id)%child_id(i1)
		call calculate_outflows(ichild_type,ichild_id,icurrent_id, icurrent_type, release,decision_var,nparam)
	end do

!print *, 'TAGGG 250'

	storage_max = my_reservoir(icurrent_id)%storage_max
	storage_ini = my_reservoir(icurrent_id)%current_storage

!print *, ntime, icurrent_id

do j = 1,ntime
!print *, 'TAGGG 258', j
	rate_area(j) = my_reservoir(icurrent_id)%evaporation_rate(j)

end do


! Variable for counting the number of time not meeting target storage constraints
nend_cons = 0

! Loop for reservoir simulation

!print *, my_reservoir(icurrent_id)%name

!print *, 'HERE000'


do j = 1,ntime
	spill_tot(j) = 0.0
	def_tot(j) = 0.0
	storage_tot(j) = 0.0
	release_tot(j) = 0.0
	hydro_tot(j) = 0.0
	spill_count(j) = 0
	def_count(j) = 0
end do

do i = 1,nensem

	do j = 1,ntime
		q(j) = my_flow_set(iflow_set)%uncontrolled_flows(j,i) + &
		       my_flow_set(iflow_set)%controlled_flows(j)
	end do


	call reser_simul(icurrent_id, q, ntime,release,storage_max, storage_ini,rate_area, &
					 simul_stor,simul_spill, simul_evapo, simul_deficit,iflag, nparam)
	
    do j = 1, ntime
		spill_values((icurrent_id-1)*ntime + j) = simul_spill(j)
		deficit_values((icurrent_id-1)*ntime + j) = simul_deficit(j)
		res_ids_for_spdef((icurrent_id-1)*ntime + j) = icurrent_id
	enddo
	

	do j=1,ntime
		act_release(j) = release(j)+simul_spill(j)-simul_deficit(j)
		if(act_release(j).le.0.0)act_release(j) = 0.0
		all_release((icurrent_id-1)*ntime + j) = act_release(j)
	end do

	do j=1,ntime
		spill_tot(j) = spill_tot(j) + simul_spill(j)
		def_tot(j) = def_tot(j) + simul_deficit(j)
		if (simul_spill(j).ge.0) then
			spill_count(j) = spill_count(j) + 1
		end if
		if (simul_deficit(j).ge.0) then
			def_count(j) = def_count(j) + 1
		end if
	end do

	my_reservoir(icurrent_id)%final_storage = simul_stor(ntime)

  	if (ifinal.eq.1) then 
   		write(31,15) my_reservoir(icurrent_id)%name, (simul_stor(j), j=1,ntime)        
		15 format(a,2x, 999(2x,F12.2))
		write(28,15) my_reservoir(icurrent_id)%name, (act_release(j), j=1,ntime)
		write(44,15) my_reservoir(icurrent_id)%name, (simul_deficit(j), j=1,ntime)
		write(30,15) my_reservoir(icurrent_id)%name, (simul_spill(j), j=1, ntime)
		! if (nensem.eq.1)  then
		! 	! CHARACTER(LEN=*), PARAMETER :: FMT1 = "(A,A,F.2)"
		! 	125 format(A,A,F10.2)
		! 	126 format(A,A,F12.2)
		! 	write(*,125) my_reservoir(icurrent_id)%name, 'Final Storage:', simul_stor(ntime)
		! 	write(*,126) my_reservoir(icurrent_id)%name, 'Total Spill:', sum(simul_spill)
		! end if
	end if  
	
	do i1 = 1,nchild
		ichild_type = my_reservoir(icurrent_id)%child_type(i1)
		ichild_id   = my_reservoir(icurrent_id)%child_id(i1)
		if (ichild_type == 4)  then
			if (my_user(ichild_id)%user_type == 4) then
				call hydropower(ichild_type,ichild_id,icurrent_id, icurrent_type, simul_stor, release, nensem, hydro_tot, nparam)
			end if
		end if 
	end do

	do j=1,ntime
		spill_tot(j) = spill_tot(j) + simul_spill(j)
		def_tot(j) = def_tot(j) + simul_deficit(j)
		storage_tot(j) = storage_tot(j) + simul_stor(j)
		release_tot(j) = release_tot(j) + act_release(j)
		if (simul_spill(j).ge.0) then
			spill_count(j) = spill_count(j) + 1
		end if
		if (simul_deficit(j).ge.0) then
			def_count(j) = def_count(j) + 1
		end if
	end do

	if(iflag.eq.1)then
		do k=1,ntime
			total_deficit(i) = total_deficit(i)+simul_deficit(k)
		end do
	end if

	if(simul_stor(ntime).lt.my_reservoir(icurrent_id)%target_storage) then
		nend_cons = nend_cons + 1
	endif
end do

if ((nensem.gt.1.0).and.(ifinal.eq.1)) then
	print *, my_reservoir(icurrent_id)%name, "Target Storage Reliability =", 100*(1-(real(nend_cons)/real(nensem))),'%'
	print *, my_reservoir(icurrent_id)%name, "Probability of Spill =", 100*(real(spill_count)/real(nensem)), "%"
	print *, my_reservoir(icurrent_id)%name, "Probability of Deficit =", 100*(real(def_count)/real(nensem)), "%"
	write(100, 15) my_reservoir(icurrent_id)%name, (spill_tot(j)/real(nensem), j=1,ntime)
	write(101, 15) my_reservoir(icurrent_id)%name, (def_tot(j)/real(nensem), j=1,ntime)
	write(102, 15) my_reservoir(icurrent_id)%name, (spill_count(j)/real(nensem), j=1,ntime)
	write(103, 15) my_reservoir(icurrent_id)%name, (def_count(j)/real(nensem), j=1,ntime)
	write(104, 15) my_reservoir(icurrent_id)%name, (hydro_tot(j)/real(nensem), j=1,ntime)
	write(105, 15) my_reservoir(icurrent_id)%name, (storage_tot(j)/real(nensem), j=1,ntime)
	write(106, 15) my_reservoir(icurrent_id)%name, (release_tot(j)/real(nensem), j=1,ntime)
end if

return
end


! Subroutine for hydropwer calculation
subroutine hydropower(iblock_type,iblock_id,icurrent_id, icurrent_type,simul_stor,release,nensemble, hydro_tot, nparam)!id_output,value_output, nparam, hydro_tot)
Use My_variables
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal
double precision simul_hydropower(ntime), simul_stor(ntime), release(ntime), hydro_tot(ntime)
double precision head_elevation(ntime)
double precision Unit_Conv
integer :: array_index
! integer, intent(out) :: id_output(nparam)
! double precision, dimension(nparam), intent(out) :: value_output


       IF(my_user(icurrent_id)%name=="Douglas H") THEN
       	my_user(icurrent_id)%name = "Douglas_HY_TN"
	   ELSE IF(my_user(icurrent_id)%name=="Watuga H") THEN
       	my_user(icurrent_id)%name = "Watauga_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Wilbur H") THEN
       	my_user(icurrent_id)%name = "Wilbur_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="SHolston H") THEN
       	my_user(icurrent_id)%name = "SouthHolston_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Boone H") THEN
       	my_user(icurrent_id)%name = "Boone_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="FtPatrick H ") THEN
       	my_user(icurrent_id)%name = "FortPatrick_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Cherokee H") THEN
       	my_user(icurrent_id)%name = "Cherokee_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="FtLoudoun H") THEN
       	my_user(icurrent_id)%name = "FortLoudoun_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Fontana H") THEN
       	my_user(icurrent_id)%name = "Fontana_HY_NC"
       ELSE IF(my_user(icurrent_id)%name=="Norris H") THEN
       	my_user(icurrent_id)%name = "Norris_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="MeltonH H") THEN
       	my_user(icurrent_id)%name = "MeltonHill_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="WattsBar H") THEN
       	my_user(icurrent_id)%name = "WattsBar_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Chatuge H") THEN
       	my_user(icurrent_id)%name = "Chatuge_HY_NC"
       ELSE IF(my_user(icurrent_id)%name=="Nottely H") THEN
       	my_user(icurrent_id)%name = "Nottely_HY_GA"
       ELSE IF(my_user(icurrent_id)%name=="Hiwassee H") THEN
       	my_user(icurrent_id)%name = "Hiwassee_HY_NC"
       ELSE IF(my_user(icurrent_id)%name=="Apalachia H") THEN
       	my_user(icurrent_id)%name = "Apalachia_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="BlueRidge H") THEN
       	my_user(icurrent_id)%name = "BlueRidge_HY_GA"
       ELSE IF(my_user(icurrent_id)%name=="Ocoee3 H") THEN
       	my_user(icurrent_id)%name = "Ocoee3_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Ocoee1 H") THEN
       	my_user(icurrent_id)%name = "Ocoee1_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Chikamauga H") THEN
       	my_user(icurrent_id)%name = "Chickamauga_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="RacoonMt H") THEN
       	my_user(icurrent_id)%name = "RaccoonMt_Storage_TN"
       ELSE IF(my_user(icurrent_id)%name=="Nikajack H") THEN
       	my_user(icurrent_id)%name = "Nickajack_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Guntersville H") THEN
       	my_user(icurrent_id)%name = "Guntersville_HY_AL"
       ELSE IF(my_user(icurrent_id)%name=="TimsFord H") THEN
       	my_user(icurrent_id)%name = "TimsFord_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Wheeler H") THEN
       	my_user(icurrent_id)%name = "Wheeler_HY_AL"
       ELSE IF(my_user(icurrent_id)%name=="Wilson H") THEN
       	my_user(icurrent_id)%name = "Wilson_HY_AL"
       ELSE IF(my_user(icurrent_id)%name=="Pickwick H") THEN
       	my_user(icurrent_id)%name = "PickwickLanding_HY_TN"
       ELSE IF(my_user(icurrent_id)%name=="Kentucky H") THEN
       	my_user(icurrent_id)%name = "Kentucky_HY_KY"        
       ENDIF
        
				! output in MWh/month
        ! Unit_Conv = 62.4*43560*0.746/3600/550 ! Amir's Unit Conv =  62.4*43560*1000/0.74/3600/1000/1000  ! Yi's Unit_Conv = 62.5*1.356*1000/2/31/1000000
				! Unit_Conv = 9.81*1000/3600 ! [9.81 KN/m^3]*[10^6m^3/hm^3]/[3600 KJ/KWh]*[1000 KWh/MWh] Input in thousand cubic meters per month -Lucas
			 	Unit_Conv = 62.4*43560*1000/2.655E9 ! [62.4 lb/ft^3]*[43560 ft^2/acre]*[1000 acre/thousand acre]/[2.665E9 ft-lb/MWh] Input in thousand acre ft per month - Lucas
		
        stor_uni = my_reservoir(icurrent_id)%current_storage
        do j = 1, ntime
            !Calculating head Elevation
                
						tmp = (stor_uni + simul_stor(j)) /2
						! print *, 'tmp:',tmp
            head_elevation(j)=my_reservoir(icurrent_id)%elevation_storage_coeff(1)*(tmp**2)+&
                        my_reservoir(icurrent_id)%elevation_storage_coeff(2)*tmp+ &
                        my_reservoir(icurrent_id)%elevation_storage_coeff(3)
						! print *, 'head_elevation:', head_elevation(j)
						!Calculating Simulated Hydropower
						! print *, 'gen_eff:', my_user(iblock_id)%generator_efficiency
						! print *, 'release:', release(j)
						! print *, 'head-tail:', (head_elevation(j)-my_user(iblock_id)%tail_elevation(j))

            simul_hydropower(j) =  my_user(iblock_id)%generator_efficiency*release(j)*& 
            	(head_elevation(j) - my_user(iblock_id)%tail_elevation(j))*Unit_Conv
						! print *, my_reservoir(icurrent_id)%name, simul_hydropower
                
						if (simul_hydropower(j).ne.simul_hydropower(j)) then
							print *, my_user(iblock_id)%name
							print *, 'release:', release(j)
							print *, 'Head elevation:', head_elevation(j)
							print *, 'Tail elevation:', my_user(iblock_id)%tail_elevation(j)
						END IF
            IF  (simul_hydropower(j) .LT. 0.0)then 
                    simul_hydropower(j) = 0.0
            END IF 

            itemp = 2010 + j !Index the time periods for creating the Temoa information below
            !Printing to file the Maximum hydropower for each month to be used by Temoa

            !write (54,18),itemp,my_user(icurrent_id)%name,simul_hydropower(j)        
						stor_uni = simul_stor(j)
        END do
        
        !Printing hydropower information to the screen             
!        print *, my_user(icurrent_id)%name
!        print *, 'power(MW)'
!        do k = 1, ntime 
!            print *, simul_hydropower(k)                                   
!        END do
	do j = 1,ntime
		array_index = (icurrent_id - 1)*ntime+j
			! write(*,123) array_index, simul_hydropower(j), icurrent_id
		id_output(array_index) = icurrent_id
		value_output(array_index) = simul_hydropower(j)
	enddo

	 if (ifinal.eq.1) then 
		! call array_ini()
		! print *, 'Writing hydro..................'
		write(54,19) my_user(icurrent_id)%name, (simul_hydropower(j), j=1,ntime)

		do j = 1, ntime
			hydro_tot(j) = hydro_tot(j) + simul_hydropower(j)
			! 123 format(i,f,i)
			array_index = (icurrent_id - 1)*ntime+j
			! write(*,123) array_index, simul_hydropower(j), icurrent_id
			id_output(array_index) = icurrent_id
			value_output(array_index) = simul_hydropower(j)
		end do
		! 18 format (i4,2x,a,f16.10)
		19 format(a,2x, 999(2x,F10.3))
	end if
	return
! if (ifinal.eq.1) print *, "Exiting hydropower......" 
end

! Subroutine for simulation at each junction node

subroutine node_simul_module(icurrent_type,icurrent_id,iprev_id, &
	   iprev_type, nparam,decision_var)
USE My_variables
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal
double precision decision_var(nparam),release(ntime),inflow(ntime)


	nparent = my_node(icurrent_id)%nparent


ijump = 0
iadd = 0

	do i1 = 1,nparent
			
		if((iprev_type.eq.my_node(icurrent_id)%parent_type(i1)).and. &
			(iprev_id.eq.my_node(icurrent_id)%parent_id(i1)))ijump = 1

	end do

	if(ijump.eq.0)then
	
		if((iprev_type.ne.0).and.(iprev_id.ne.0))then

			parallel_track(iflow_set)%order_id = iprev_id
			parallel_track(iflow_set)%order_type = iprev_type

		end if

			iflow_set = iflow_set +1
        

	end if 
if (iflow_set .NE. 1) then
        do j = 1,ntime

        	my_flow_set (iflow_set-1)%controlled_flows(j) = 0.0

        end do
end if 

do j = 1,ntime

	my_flow_set (iflow_set)%controlled_flows(j) = 0.0

end do






! Add controlled and uncontrolled flows from parents
	do i1 = 1,nparent

		iparent_type = my_node(icurrent_id)%parent_type(i1)
		iparent_id   = my_node(icurrent_id)%parent_id(i1)

! Prepare the inflow sets

		iadd = 0

 		if(iparent_type.eq.1)call add_uncontrolled_flows  &
		  (iparent_type,iparent_id,decision_var,nparam)

!	if(iparent_type.eq.3) then

!	    do j1 = 1,nwatershed

!			if((parallel_track(j1)%order_type.eq.iparent_type).and. &
!			  (parallel_track(j1)%order_id.eq.iparent_id))call add_all_flows &
!			  (j1,iparent_type,iparent_id,decision_var,nparam)

!		end do

!            call  add_controlled_flows(iparent_type,iparent_id, decision_var,nparam)

!		end if

		if(iparent_type.eq.5) then

		    do j1 = 1,nwatershed

				if((parallel_track(j1)%order_type.eq.iparent_type).and. &
				  (parallel_track(j1)%order_id.eq.iparent_id))call add_all_flows &
				  (j1,iparent_type,iparent_id,decision_var,nparam)

			end do

            if((iparent_type.ne.iprev_type).and.(iparent_id.ne.iprev_id))call  &
			add_controlled_flows(iparent_type,iparent_id, decision_var,nparam)

		end if



		if((iparent_type.eq.4).or.(iparent_type.eq.13))call add_controlled_flows  &
		  (iparent_type,iparent_id, decision_var,nparam)

	end do
!write(28, *) iflow_set, (my_flow_set(iflow_set)%controlled_flows(i), i=1,ntime)
!write(28, *) iflow_set, ((my_flow_set(iflow_set)%uncontrolled_flows(i,j), i=1,ntime), j=1,nensem)
! Prepare the outflow sets from uses

call array_ini(ntime,release, 0.0d0)
nchild = my_node(icurrent_id)%nchild

! Loop for adding releases to child nodes
	do i1 = 1,nchild

		ichild_type = my_node(icurrent_id)%child_type(i1)
		ichild_id   = my_node(icurrent_id)%child_id(i1)


		if(ichild_type.eq.4)then

			do j  = 1,ntime
!       fract = my_user(ichild_id)%demand_fract(j)
!		    if(ichild_type.eq.4)release (j) = release(j) + fract*decision_var(ichild_id)
				if(ichild_type.eq.4) then
					! print *, my_user(ichild_id)%name, decision_var((ichild_id-1)*ntime+j), (ichild_id-1)*ntime+j
					release (j) = release(j) + decision_var(((ichild_id-1)*ntime)+j)
				end if
			end do
		end if

!		if((ichild_type.eq.5).and.(ichild_id.eq.3))then
!			
!				do j  = 1,ntime

!					release(j) = release(j) + (0.0/12)

!				end do
!		end if

	end do
15 format(a,2x, 999(2x,F12.2))
if (ifinal.eq.1) write(29,15) my_node(icurrent_id)%name, (release(j), j=1,ntime)
! Loop for flow mass balance
do j= 1,ntime

	temp = my_flow_set(iflow_set)%controlled_flows(j)

	temp = temp - release(j)

	if(temp.le.0)then 
		
		my_flow_set(iflow_set)%controlled_flows(j)= 0.0

	else
		my_flow_set(iflow_set)%controlled_flows(j)= temp

	end if


end do

return
if (ifinal.eq.1) print*, 'Exiting node simul module .................'
end

subroutine add_uncontrolled_flows(iblock_type,iblock_id, decision_var,nparam)
Use My_variables
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal
integer nparam, iblock_id, iblock_type
double precision, dimension(nparam) :: decision_var
! Loop for adding natural flow 
do i = 1,nensem

	do j = 1,ntime
		temp = my_flow_set(iflow_set)%uncontrolled_flows(j,i) 
		temp = temp + my_watershed(iblock_id)%natural_inflows(j,i)
		my_flow_set(iflow_set)%uncontrolled_flows(j,i) = temp

	end do

end do

return
if (ifinal.eq.1) print *, "Exiting uncontrolled flow.........."
end

subroutine add_controlled_flows(iblock_type,iblock_id,decision_var,nparam)
Use My_variables
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal
double precision decision_var(nparam)

    
! Loop for adding controlled flows
do j = 1,ntime

  if(iblock_type.eq.4)then

  nlags = my_user(iblock_id)%nlags

    if(j.gt.nlags)then
		   
			temp1 = 0.0d0
			if (nlags == 0) then
										!temp1 = my_user(iblock_id)%demand_fract(j) &
			!			*decision_var(iblock_id)
									!       print *, iblock_id-1, temp1
				temp1 = decision_var((iblock_id-1)*ntime+j)
										!  temp1 = 0
										!print *,'XXXX', iblock_id-1, temp1    
			else 
				do k = 1,my_user(iblock_id)%nlags
					
					fract = (1-my_user(iblock_id)%ffraction(k))
					rflow = my_user(iblock_id)%demand_fract(j-k) &
									*decision_var(iblock_id)*fract

					temp1 = temp1 + rflow

				end do

			end if 
			temp = temp1

		else
		  
	  	temp = 0.0
		  
    end if 

  end if 

   if(iblock_type.eq.13)temp = my_interbasin(iblock_id)%average_flow(j)
   if(iblock_type.eq.3)temp = 0.0 !decision_var(iblock_id+nuser*ntime)/12

!	if((iblock_type.eq.5).and.(iblock_id.eq.3))then
!	      temp = 0.0
!		  GO to 15
!	endif

   if(iblock_type.eq.5)temp = my_flow_set(iflow_set)%controlled_flows(j)

15	my_flow_set(iflow_set)%controlled_flows(j) = temp +my_flow_set(iflow_set)%controlled_flows(j)
               !print *, iblock_type, iblock_id, my_flow_set(iflow_set)%controlled_flows(j), temp

end do

return
if (ifinal.eq.1) print *, 'Exiting controlled flow.......'
end

subroutine calculate_outflows(iblock_type,iblock_id,icurrent_id, icurrent_type,release,decision_var,nparam)
Use My_variables
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal
double precision decision_var(nparam),release(ntime)

! Loop for release calculation
	do j = 1,ntime
!       if(iblock_type.eq.4)temp = my_user(iblock_id)%demand_fract(j) &
!					*decision_var(iblock_id)
		! I made 3,5, and 12 equal to 0.0 because the current method of indexing decision_var results in NaN sometimes. 
		! There are only decision variables for users currently, i think this is how it should be. 
		! Need to change some requirments so that reservoirs can only be connected to users and from that back to reservoirs.
		! - Lucas
		if(iblock_type.eq.3)temp = 0.0 ! decision_var(icurrent_id+nuser*ntime)/12
		if(iblock_type.eq.4)temp = decision_var((iblock_id-1)*ntime + j)
	  if(iblock_type.eq.5)temp = 0.0 ! decision_var(icurrent_id+nuser*ntime)/12
		! if(iblock_type.eq.12)temp = decision_var(icurrent_id+nuser)/12
		if(iblock_type.eq.12)temp = 0.0
    temp1 = release(j)
		temp = temp + temp1
		release(j) = temp
	end do

return

end

! Add controlled and uncontrolled flows from another flowset
subroutine add_all_flows(iadd_set,iparent_type,iparent_id,decision_var,nparam)
Use My_variables
implicit doubleprecision(a-h,o-z)

double precision decision_var(nparam)

! Add uncontrolled_flows

do j = 1,ntime

!	do k = 1,nensem


!		temp = my_flow_set(iadd_set)%uncontrolled_flows(j,k)
!		temp1 = my_flow_set(iflow_set)%uncontrolled_flows(j,k)
!		my_flow_set(iflow_set)%uncontrolled_flows(j,k) = temp + temp1

!	end do

		temp = my_flow_set(iadd_set)%controlled_flows(j)
		temp1 = my_flow_set(iflow_set)%controlled_flows(j)
		my_flow_set(iflow_set)%controlled_flows(j) = temp + temp1

end do

return

end


! Check to ensure decision_var and temp_decision_var are the same

Integer function icheck_var_status(nparam, decision_var,temp_decision_var)
implicit doubleprecision (a-h,o-z)
common /final_print/ifinal
double precision decision_var(nparam),temp_decision_var(nparam)

icheck_var_status = 0
do i = 1, nparam
	if (decision_var(i).ne.temp_decision_var(i)) goto 12
End do
return

12   icheck_var_status = 1

do i = 1,nparam

	temp_decision_var(i) = decision_var(i)

End do
! if (ifinal.eq.1) print *,'exiting icheck_var_status..........'
return

end 
! Subroutine for reservoir simulation
subroutine reser_simul(icurrent_id,q, ntime,release,storage_max, storage_ini,rate_area, &
					 simul_stor,simul_spill, simul_evapo, simul_deficit,iflag,nparam)
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal
integer nparam
double precision q(ntime), rate_area(ntime),release(ntime) 
double precision simul_stor(ntime),simul_evapo(ntime)
double precision simul_deficit(ntime), simul_spill(ntime)

common/et_est/et_rate,storage_pre,current_flow,current_release,bal_net, iwrite


iflag = 0

storage_pre = storage_ini


! Loop for reservoir mass balance
do j = 1, ntime
                  
	sum_release = release(j) 
	bal_net = q(j) - sum_release 
	current_flow  = q(j)
	! print *, current_flow
	! print *, sum_release
	current_release = sum_release

	et_rate  = rate_area(j)

!print *,'et_rate = ', et_rate
!print *, 'evapo_current = ',evapo_current
	call evaporation_iter(icurrent_id, storage_current, storage_max,evapo_current, spill, deficit, j, nparam) 			 
!print *, 'after evaporation iter : evapo_current = ',evapo_current
	simul_stor(j) = storage_current
	simul_evapo(j) = evapo_current
	simul_spill(j) = spill
	simul_deficit(j) = deficit

	if (current_release.ne.sum_release) THEN
		release(j) = current_release
	end if


	if(deficit.gt.0.0)iflag = 1

	storage_pre = storage_current

end do
!print*, storage_current

return

end


Subroutine deficit_splitter(total_deficit,decision_var,nparam)!constraints,cons_id)
Use My_variables
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal
double precision total_deficit(nensem),simul_def_user(nuser)
double precision deficit_split_user(nres_level,nuser),decision_var(nparam)
! double precision ben_net
! double precision, dimension(ncons) :: constraints

Integer ilevel_fail(nres_level),idef_user(nuser)!,cons_id(ncons-nres_level)

! Loop for distributing deficit among users
do k1 = 1,nensem

	call array_ini(nuser,simul_def_user,0.0d0)
	call array_ini_two(nres_level,nuser,deficit_split_user,0.0d0)
	call array_int_ini(nres_level,ilevel_fail,0)
	call array_int_ini(nuser,idef_user,0)

	if(total_deficit(k1).ne.0)then

		account_def = 0.0


		do i = 1,nres_level

			current_def = 0.0
			ilevel_fail(i) = ilevel_fail(i)+1.0
				
			do j = 1,nuser

				temp = my_user(j)%restr_fract(i)*decision_var(j)
				simul_def_user(j) = simul_def_user(j)+temp
				current_def = current_def+ temp
			
				deficit_split_user(i,j) = temp
				! print *, my_user(j)%name, 'deficit:', deficit_split_user(i,j)
			end do
						
			account_def = account_def+current_def

					

			if(account_def.ge.total_deficit(k1))then
				ilevel = i
				adjust_def = account_def - total_deficit(k1)
				go to 17
			end if		

		end do 

		Go to 25
		!if(account_def.lt.total_deficit(k1))then

		!	Write(*,*)'Increase the Restriction Level or the Restriction fraction'
		!	Stop

		!end if 

						!distribute deficits to users
		17    do j = 1,nuser

						temp1 = adjust_def/current_def
						temp = my_user(j)%restr_fract(ilevel)*decision_var(j)*temp1
						simul_def_user(j) = simul_def_user(j) - temp
						deficit_split_user(ilevel,j) = my_user(j)%restr_fract(ilevel)*decision_var(j) - temp
					end do

		25 continue


			do j = 1,nuser

					if(simul_def_user(j).ge.my_user(j)%con_res_vol)idef_user(j) = idef_user(j)+ 1.0

			end do

	end if


	call functn(decision_var,nparam,idef_user,ilevel_fail,deficit_split_user,simul_def_user)

	value_net(k1) = ben_net

end do


k2 = nres

ensem = nensem
4444 format(5x,a,F3.1,2x,F3.1,2x,F3.1)

! Loop for calculating failure probability constraints
do i = 1,nuser

	k2 = k2 + 1
	cons_global(k2) = (idef_user(i)/ensem) - my_user(i)%failure_prob
	constraints(k2) = cons_global(k2)
	cons_id(k2) = my_user(i)%ID
	if (cons_global(k2).gt.0) then
		write(*,4444) my_user(i)%name, cons_global(k2), (idef_user(i)/ensem), my_user(i)%failure_prob
	end if
end do

! Loop for calculating target restriction constraints
do i = 1,nres_level

	k2 = k2 + 1
	  cons_global(k2) = (ilevel_fail(i)/ensem)-my_reservoir(1)%tar_restr_prob(i)
	  constraints(k2) = cons_global(k2)
	! if (cons_global(k2).gt.0) then
	! 	write(*,4445) 'Target Restriction level', i, cons_global(k2), (ilevel_fail(i)/ensem), my_reservoir(1)%tar_restr_prob(i)
	! end if

end do

! undesired terminal output
! if (ifinal.eq.1) print *, 'Exiting deficit splitter........ '

return
end

! subroutine for calculating net benefits
subroutine functn(decision_var,nparam,idef_user,ilevel_fail,deficit_split_user,simul_def_user)
Use my_variables
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal
double precision decision_var(nparam),deficit_split_user(nres_level,nuser)
double precision simul_def_user (nuser)


Integer idef_user(nuser),ilevel_fail(nres_level)

ben_net = 0.0

do i = 1,nuser

  if(idef_user(i).ne.1)then
	ben_net = ben_net + my_user(i)%tariff*decision_var(i)			
  else
		! ben_net = ben_net + my_user(i)%tariff*decision_var(i) 
        temp1 = simul_def_user(i) - my_user(i)%con_res_vol
		temp = my_user(i)%penalty + temp1*my_user(i)%penalty_compen
		ben_net = ben_net - temp
  end if
  do k = 1,nres_level

	if(ilevel_fail(k).eq.1)then

		temp = my_user(i)%res_compensation(k)*deficit_split_user(k,i)
       	ben_net = ben_net - temp

	endif

  end do
	 

end do

return

end

subroutine max_hydropower(nparam, j, decision_var, fj)
	Use My_variables
	implicit double precision(a-h, o-z)
	common /final_print/ifinal

	double precision decision_var(nparam), fj, x1a, x1b, x1c, x1cs

	call constr_res(nparam,j,decision_var,gcons)

	fj = 0.0
	do i = 1, nparam
		fj = fj + value_output(i)
	end do

	fj = -fj
	print *, "Hydropower: ", -fj
	return	
end subroutine max_hydropower

subroutine max_release(nparam, j, decision_var, fj)
	Use My_variables
	implicit double precision(a-h, o-z)
	common /final_print/ifinal

	double precision decision_var(nparam), fj, x1a, x1b, x1c, x1cs

	call constr_res(nparam,j,decision_var,gcons)

	fj = 0.0
	do i = 1, nparam
		fj = fj + all_release(i)
	end do

	fj = -fj
	print *, "Total Release: ", -fj
	return	
end subroutine max_release

subroutine max_hydro_benefits(nparam, j, decision_var, fj)
	Use My_variables
	implicit double precision(a-h, o-z)
	common /final_print/ifinal

	double precision decision_var(nparam), fj, x1a, x1b, x1c, x1cs

	call constr_res(nparam, j, decision_var, gcons)

	fj = 0.0
	do i = 1, nparam
		fj = fj + value_output(i) * hydro_benefit(i)
	end do 
	print *, "Hydropower Benefit: ", fj
	fj = -fj
	return
end subroutine max_hydro_benefits

subroutine min_spill_deficit(nparam, j, decision_var, fj)
	Use My_variables
	implicit double precision(a-h, o-z)
	common /final_print/ifinal

	double precision decision_var(nparam), fj, x1a, x1b, x1c, x1cs

	call constr_res(nparam,1,decision_var,gcons)

	fj = 0.0
	do i = 1, nparam
		fj = fj + spill_values(i) + deficit_values(i)
	end do

	fj = -fj
	print *, "Spill and Deficit: ", -fj
	return
end subroutine min_spill_deficit

subroutine expected_benefits(nparam,j,decision_var,fj)
Use My_variables
implicit doubleprecision(a-h,o-z)
common /final_print/ifinal

doubleprecision decision_var(nparam),fj,x1a,x1b,x1c,x1cs


fj=0.0

!ben_net = 0.0

do i = 1,nuser

		ben_net = ben_net + my_user(i)%tariff*(decision_var(i)**2)			

end do

call constr_res(nparam,1,decision_var,gcons)


!call stat_(nensem,value_net,x1a,x1s,x1cv,x1cs)

!x1a = ben_net
total_value = 0

do i =1, nensem
        
        total_value =  total_value+value_net(i)
       
END do
print *, 'total_value', total_value
!fj = -x1a
fj = -total_value

return
if (ifinal.eq.1) print *, 'Exiting expected benefits.......'
end


Subroutine evaporation_iter(icurrent_id,storage_current,storage_max,evapo_current, spill,deficit, time_step, nparam) 			 
! Use NUmerical_libraries
USE My_variables


implicit doubleprecision(a-h,o-z)
external et_function,lsjac
integer time_step, spill_con_index, deficit_con_index, target_con_index, nparam
double precision bottom_bound, upper_bound, target_storage
Character*2 st_flag, lbound_type, ubound_type
common/et_est/et_rate,storage_pre,current_flow,current_release,bal_net, iwrite

alpha = my_reservoir(icurrent_id)%storage_area_coeff(1)
beta = my_reservoir(icurrent_id)%storage_area_coeff(2)

upper_curve = my_reservoir(icurrent_id)%rule_curve_upper(time_step)
lower_curve = my_reservoir(icurrent_id)%rule_curve_lower(time_step)*0.95 ! allow reservoir to dip 5% below supply curve

spill_con_index = (icurrent_id - 1)*ntime+time_step
deficit_con_index = (icurrent_id - 1)*ntime+time_step + nparam
target_con_index =  nparam * 2 + icurrent_id
target_storage = my_reservoir(icurrent_id)%target_storage


! alpha = 0.001
! beta = 0.002

! alpha = 0.0
! beta = 0.0

 
	if(storage_pre.lt.0.001)storage_pre=0.0

	temp = current_flow - current_release + storage_pre

	storage_min = my_reservoir(icurrent_id)%storage_min

	temp_min = (storage_pre + storage_min)/2.0

	rmin = storage_min + et_cal(et_rate,temp_min, alpha, beta)

	temp_max = (storage_pre + storage_max)/2.0

	rmax = storage_max+ et_cal(et_rate,temp_max, alpha, beta)

if(rmin.gt.temp)then
		x=0.0
		go to 12
end if

if(rmax.lt.temp)then
	  x= storage_max
	  go to 12
end if
 
	storage_current = storage_pre*0.6

!	errel = 0.001

 	  errel = 0.000001
      nvar = 1
      itmax = 5000
      icrit = 0

    x1=storage_current
    x2 = storage_pre*1.1+2 
    xacc=1.0E-06

!10	call DNEQNF(et_function,errel,nvar,itmax,storage_current,x,fnorm)

    x=rtsec(x1,x2,xacc, alpha, beta)

12     continue  
	
! Cases for when the storage is greater than the maximum, less than the minimum
! or in between, respectively.
if (lower_curve.lt.storage_min) then
	bottom_bound = storage_min
	lbound_type = "mn"
else
	bottom_bound = lower_curve
	lbound_type = "lc"
end if

if (upper_curve.gt.storage_max) then
	upper_bound = storage_max
	ubound_type = "mx"
else
	upper_bound = upper_curve
	ubound_type = "uc"
end if


max_release = my_user(icurrent_id)%maximum_release
min_release = my_user(icurrent_id)%minimum_release
! 	storage_current = upper_curve
! 	temp = 0.5*(storage_current+storage_pre)
! 	evapo_current = et_cal(et_rate, temp, alpha, beta)
! 	spill = current_flow - current_release + storage_pre - upper_curve - evapo_current
! 	if (spill.lt.0) spill = 0
	!!!! This assumes that there is no flexibility in the release
	! if (upper_bound.eq.storage_max) then
	! 	spill = current_flow - current_release + storage_pre - storage_max &
	! 		- evapo_current
	! else
	! 	spill = 0
if(x.ge.upper_bound)then
	st_flag = 'ge'
	storage_current = upper_bound
	temp = 0.5*(storage_current+storage_pre)
	evapo_current = et_cal(et_rate,temp, alpha, beta)
	deficit = 0.0
	spill = 0.0

	!!!! This assumes that there is no flexibility in the release
	! if (upper_bound.eq.storage_max) then
	! 	spill = current_flow - current_release + storage_pre - storage_max &
	! 		- evapo_current
	! else
	! 	spill = 0
	! end if
	! if (storage_current.gt.upper_bound) spill = current_flow - current_release + storage_pre - storage_max - evapo_current

	!!!! This assumes that the release can be changed as long as it is less than the max release
	!!!! if it is greater, spill becomes the difference
	current_release = current_flow + storage_pre - storage_current - evapo_current
	if (current_release.gt.max_release) then
		spill = abs(current_release) - max_release
		current_release = max_release
		! if (spill.gt.constraint_tolerance) then
		! 	write(*,  "(A, 2X, A, A, I4, F10.4)") "SPILL", my_reservoir(icurrent_id)%name, "NTIME", ntime, spill
		! 	! print *, "SPILL", my_reservoir(icurrent_id)%name, spill
		! 	! do k = 1, my_reservoir(icurrent_id)%nparent
		! 	! 	parent_type = my_reservoir(icurrent_id)%parent_type(k)
		! 	! 	parent_id = my_reservoir(icurrent_id)%parent_id(k)
		! 	! 	if (parent_type.eq.3) then
		! 	! 		print *, "		PARENT  ", my_reservoir(parent_id)%name
		! 	! 	endif
		! 	! enddo
		! endif
	end if
	
end if 

if(x.le.bottom_bound)then 
	st_flag = 'le'
	storage_current = bottom_bound
	spill = 0.0
	temp = 0.5*(storage_current+storage_pre)
	evapo_current = et_cal(et_rate,temp, alpha, beta)
	deficit = 0.0

	!!!! Again, the assumption that the release is not flexible
	! if (bottom_bound.eq.storage_min) then
	! 	deficit = current_release - current_flow  - storage_pre + evapo_current + storage_min
	! else
	! 	deficit = 0
	! end if
	! if (storage_current.lt.bottom_bound) deficit = current_release - current_flow  - storage_pre + evapo_current + storage_min

	!!!! Assuming the release is flexible
	current_release = current_flow + storage_pre  - evapo_current - storage_current
	if (current_release.lt.min_release) then
		deficit = min_release - current_release
		current_release = min_release
		! if (deficit.gt.constraint_tolerance) then
		! 	write(*, "(A, 2X, A, A, I4, F10.4)"), "DEFICIT", my_reservoir(icurrent_id)%name, "NTIME", ntime, deficit
		! endif
	end if

	! lukes_cons(deficit_con_index) = deficit
		
end if 

if((x.lt.upper_bound).and.(x.gt.bottom_bound))then		
	st_flag = 'mi'
	storage_current = x
	spill = 0.0
	temp = 0.5*(storage_current+storage_pre)
	evapo_current = et_cal(et_rate,temp, alpha, beta)
	deficit = 0.0
end if 
  ! check mass balance
    check1 = current_flow + storage_pre + deficit - spill - &
				current_release - evapo_current - storage_current
	45678 format(A, I2)
	1072 format(A30, F10.2, F10.2, F10.2, F10.2, F10.2, F10.2, F10.2, F10.2, A10, A10, A10)	

	
	write(107, 1072) my_reservoir(icurrent_id)%name, current_flow, storage_pre, deficit, spill, current_release, evapo_current, storage_current, check1, st_flag, lbound_type, ubound_type
	

	if (abs(check1).gt.0.01) print *, my_reservoir(icurrent_id)%name, "  Check  ", check1
	if ((check1.gt.0.01).or.(check1.lt.-0.01)) THEN
		current_release = current_release + check1
		max_release = my_user(icurrent_id)%maximum_release
		min_release = my_user(icurrent_id)%minimum_release
		if (current_release.gt.max_release) then
			spill = current_release - max_release
			current_release = max_release
		end if

		if (current_release.lt.min_release) then
			deficit = min_release - current_release
			current_release = min_release
		end if
	end if

	check2 = current_flow + storage_pre + deficit - spill - &
				current_release - evapo_current - storage_current

	if ((check2.gt.0.01).or.(check2.lt.-0.01)) print *, check2

	if(iwrite.eq.1)write(42,14)check1

	if (spill.gt.constraint_tolerance) then
		lukes_cons(spill_con_index) = spill
	else
		lukes_cons(spill_con_index) = 0.0
	end if

	if (deficit.gt.constraint_tolerance) then
		lukes_cons(deficit_con_index) = deficit
	else
		lukes_cons(deficit_con_index) = 0.0
	end if

	if (time_step.eq.ntime) then
		! lukes_cons(target_con_index) = abs(storage_current - target_storage) - 0.1*target_storage
		! print *, storage_current, target_storage, lukes_cons(target_con_index)
		lukes_cons(target_con_index) = 0
	endif

14   format(F14.4)

return
end

subroutine evap_solve(storage_pre,et_rate,alpha,current_flow,current_release,x)
implicit doubleprecision(a-h,o-z)

	temp1 = et_rate*alpha/2.0
	temp = current_flow-current_release


	temp2 = (storage_pre*(1-temp1) + temp)/(1+temp1)

	x = temp2

return
end



subroutine et_function(storage_current,fnorm,nvar, alpha, beta)
implicit doubleprecision(a-h,o-z)

common/et_est/et_rate,storage_pre,current_flow,current_release,bal_net, iwrite

    temp = (storage_pre+storage_current)/2.0

	tmp = current_flow  - current_release + storage_pre - storage_current 

	temp1 = et_cal(et_rate,temp, alpha, beta)

	fnorm = tmp - temp1

return

end


double precision function et_cal(et_rate,storage, alpha, beta)
implicit doubleprecision(a-h,o-z)

!	alpha = 0.3376373
!	beta = 0.842674
!	alpha*(storage[1000 acre-ft]**beta) gives area on acre
!	et_rate is in feet
!	divide by 1000 to get to thousand-acre-feet
    et_cal = et_rate*alpha*(storage**beta)/1000
return
end




! Secant method for root finding
    double precision FUNCTION rtsec(x1,x2,xacc, alpha, beta)
      implicit real*8 (a-h,o-z)
      INTEGER MAXIT
      PARAMETER (MAXIT=30)
      INTEGER j
      REAL*8 dx,f,fl,swap,xl

      call et_function(x1,fl,1, alpha, beta)
      call et_function(x2,f,1, alpha, beta)
      if(dabs(fl).lt.dabs(f))then
        rtsec=x1
        xl=x2
        swap=fl
        fl=f
        f=swap
      else
        xl=x1
        rtsec=x2
      endif
      do 11 j=1,MAXIT
        dx=(xl-rtsec)*f/(f-fl)
        xl=rtsec
        fl=f
        rtsec=rtsec+dx
      call et_function(rtsec,f,1, alpha, beta)

        if(dabs(dx).lt.xacc.or.f.eq.0.)then
    rtsec = rtsec
        return
        endif
11    continue
!      pause 'rtsec exceed maximum iterations'
      END


subroutine array_ini(ntime,arr, assigned_value)
implicit doubleprecision(a-h,o-z)

double precision arr(ntime),assigned_value

 do i = 1, ntime
	  arr(i) = assigned_value
end do
	

return
end				

subroutine array_ini_two(ndim1,ndim2, arr, assigned_value)
implicit doubleprecision(a-h,o-z)

doubleprecision arr(ndim1,ndim2),assigned_value

do j = 1,ndim1

	do i = 1, ndim2
	  arr(j,i) = assigned_value
	end do

end do
	

return
end


subroutine array_int_ini(ntime,arr,my_value)
Integer arr(ntime)

do i = 1, ntime
    arr(i) = my_value
end do

return
end				

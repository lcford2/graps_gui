program format
    character*100 string1, string2, string3
    integer ntime, nensem, i
    double precision, dimension(:), allocatable :: array

    ntime = 12
    allocate(array(ntime))
    15 format(a, 100(F12.3))
    do i=1,ntime
        array(i) = i*21.8/3.5
    end do
    open(unit=100, file="array_out.out", action="WRITE")
    write(100, 15) "Luke", (array(i), i=1,ntime)
    ! 15 format(F12.3)
    ! write(*,15) 123456.345

    ! 16 format(A)
    ! string1 = "/home/lcford2/temoaMultiRes/TVA_Res_Model"
    ! string2 = "/input.dat"
    ! string3 = trim(string1)//trim(string2)
    ! write(*, 16) string1
    ! write(*, 16) string2
    ! write(*, 16) string3
    ! open(unit=10, file = string3, ACTION = 'READ', STATUS = 'OLD')
    ! read(10,*) ntime,nensem
    ! write(*,*) ntime, nensem
end program format
@ECHO OFF
cd ../source
mkdir build
cp *.f* build
cd build
ifort /dll path_vars.f90 definitions.f90 My_variables.f90 ffsqp.f qld.f init.f90 all_simul.f90 /link /out:res_model.dll
rm *.f*
mv * ../../windows
cd ..
rm -r build
cd ../windows
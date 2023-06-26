#!/usr/bin/python
if __name__ == '__main__':
  import sys
  import os
  sys.path.insert(0, os.path.abspath('config'))
  import configure
  configure_options = [
    '--download-chaco',
    '--download-cmake',
    '--download-hdf5',
    '--download-hypre',
    '--download-mumps',
    '--download-ptscotch',
    '--download-scalapack',
    '--download-superlu_dist',
    '--with-c2html=0',
    '--with-cxx-dialect=C++11',
    '--with-debugging=1',
    '--with-fortran-bindings=0',
    '--with-shared-libraries=1',
    '--with-scalar-type=complex',
    '--with-mpi-dir=/opt/mpich',
    'PETSC_ARCH=arch-complex-debug',
  ]
  configure.petsc_configure(configure_options)

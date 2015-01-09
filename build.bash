#!/bin/bash
pushd cspice
  ./get_cspice.bash
popd
pushd data
  ./get_smap_kernels.bash
popd
mkdir -p build
pushd build
  cmake ..
  make
popd
./ctypes_test.py


#!/bin/bash
mkdir -p SMAP/ck SMAP/fk SMAP/lsk SMAP/pck SMAP/sclk SMAP/spk
pushd SMAP/ck
  curl -O http://naif.jpl.nasa.gov/pub/naif/SMAP/kernels/ck/smap_at_1411030151_1411030930_v01.bc
popd
pushd SMAP/fk
  curl -O http://naif.jpl.nasa.gov/pub/naif/SMAP/kernels/fk/smap_pf_v12.tf
popd
pushd SMAP/lsk
curl -O http://naif.jpl.nasa.gov/pub/naif/SMAP/kernels/lsk/naif0010.tls
popd
pushd SMAP/pck
  curl -O http://naif.jpl.nasa.gov/pub/naif/SMAP/kernels/pck/pck00010.tpc
popd
pushd SMAP/sclk
curl -O http://naif.jpl.nasa.gov/pub/naif/SMAP/kernels/sclk/smap_cl_v00000.tsc
popd
pushd SMAP/spk
  curl -O http://naif.jpl.nasa.gov/pub/naif/SMAP/kernels/spk/SMAP_ref_141031-171101.bsp
  curl -O http://naif.jpl.nasa.gov/pub/naif/SMAP/kernels/spk/de421.bsp
popd


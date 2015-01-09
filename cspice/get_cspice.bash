#!/bin/bash

# Possible platforms:
# - MacIntel_OSX_AppleC_32bit
# - MacIntel_OSX_AppleC_64bit
# - PC_Cygwin_GCC_32bit
# - PC_Cygwin_GCC_64bit
# - PC_Linux_GCC_32bit
# - PC_Linux_GCC_64bit
# - PC_Windows_VisualC_32bit
# - PC_Windows_VisualC_64bit
# - SunIntel_Solaris_SunC_32bit
# - SunIntel_Solaris_SunC_64bit
# - SunSPARC_Solaris_GCC_32bit
# - SunSPARC_Solaris_GCC_64bit
# - SunSPARC_Solaris_SunC_32bit
# - SunSPARC_Solaris_SunC_64bit
PLATFORM=MacIntel_OSX_AppleC_64bit

mkdir -p download
pushd download

curl -O http://naif.jpl.nasa.gov/pub/naif/toolkit/C/$PLATFORM/packages/README
curl -O http://naif.jpl.nasa.gov/pub/naif/toolkit/C/$PLATFORM/packages/cspice.tar.Z
curl -O http://naif.jpl.nasa.gov/pub/naif/toolkit/C/$PLATFORM/packages/dscriptn.txt
curl -O http://naif.jpl.nasa.gov/pub/naif/toolkit/C/$PLATFORM/packages/importCSpice.csh
curl -O http://naif.jpl.nasa.gov/pub/naif/toolkit/C/$PLATFORM/packages/whats.new

csh importCSpice.csh
popd
mv download/cspice/* .


Python `ctypes` with CSPICE
===========================

This is just a little test repository to show the use of [Python `ctypes`](https://docs.python.org/2/library/ctypes.html) to run [CSPICE](http://naif.jpl.nasa.gov/naif/toolkit_C.html).

Instructions
------------

Just run `./build.bash` to build the shared library in the right place (`./build/lib/cspice.dylib`) and then run `./ctypes_test.py`. That script shows the use of `ctypes` to [`furnsh_c`](http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/furnsh_c.html) some [SMAP kernels](http://naif.jpl.nasa.gov/pub/naif/SMAP/kernels/) and obtain a frame name with [`frmnam_c`](http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/furnsh_c.html), convert a datetime string to J2000 epoch with [`str2et_c`](http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/str2et_c.html), get SMAP's position relative to the Earth in the J2000 reference frame using [`spkgeo_c`](http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/spkgeo_c.html), and get the transformation matrix from SMAP spacecraft frame to `IAU_EARTH` using [`pxform_c`](http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/pxform_c.html).

Caveats
-------

This is just a simply static demo which was run on Mac OS X so the path to the CSPICE shared library is hard coded in `./ctypes_test.py` to `build/lib/libcspice.dylib`. The extension will be different on different platforms (likely `.so` for Linux).

There doesn't seem to be a way to create [SPICE Cells](ftp://naif.jpl.nasa.gov/pub/naif/misc/toolkit_docs_N0062/MATLAB/req/cells.html) because the C API to create cells consists of macros which don't show up as functions available in the shared library. Simply wrapping the macros with C functions might be sufficient.


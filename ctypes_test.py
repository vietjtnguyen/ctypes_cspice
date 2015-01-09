#!/usr/bin/env python2.7

# https://docs.python.org/2/library/ctypes.html
import ctypes
from os.path import join

# Load the cspice shared library.
cspice = ctypes.cdll.LoadLibrary('build/lib/libcspice.dylib')

# Use furnsh_c to load kernels.
data_path = './data/SMAP'
kernels = [
    'ck/smap_at_1411030151_1411030930_v01.bc',
    'fk/smap_pf_v12.tf',
    'lsk/naif0010.tls',
    'pck/pck00010.tpc',
    'sclk/smap_cl_v00000.tsc',
    'spk/SMAP_ref_141031-171101.bsp',
    'spk/de421.bsp',
]
for kernel in kernels:
    # http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/furnsh_c.html
    cspice.furnsh_c(join(data_path, kernel))

# Use frmnam_c to get the name from a frame ID.
frame_id = ctypes.c_int(-205001)
out_buf_len = ctypes.c_int(256)
out_buf = ctypes.create_string_buffer('\000'*out_buf_len.value)
# http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/frmnam_c.html
cspice.frmnam_c(frame_id, out_buf_len, out_buf)
print(out_buf.value)

# Create some double array types.
ThreeDoubles = ctypes.c_double * 3
ThreeThreeDoubles = ThreeDoubles * 3
SixDoubles = ctypes.c_double * 6

# Convert the start time string for SMAP_ref_141031-171101.bsp (obtained with brief -c) to a J2000 seconds epoch time.
target_epoch = ctypes.c_double(0.0)
# http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/str2et_c.html
cspice.str2et_c(ctypes.c_char_p('2014 OCT 31 15:36:26.389'), ctypes.byref(target_epoch))

# Use spkgeo_c to get the geometric state of SMAP (-205) relative to EARTH (399) in the J2000 reference frame.
target_body = ctypes.c_int(-205)
reference_frame = ctypes.c_char_p('J2000')
observing_body = ctypes.c_int(399)
out_state = SixDoubles()
out_ltd = ctypes.byref(ctypes.c_double(0))
# http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/spkgeo_c.html
cspice.spkgeo_c(target_body, target_epoch, reference_frame, observing_body, out_state, out_ltd)
print(tuple(out_state))

# Convert the start time string for smap_at_1411030151_1411030930_v01.bc (obtained with ckbrief) to a J2000 seconds epoch time.
target_epoch = ctypes.c_double(0.0)
# http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/str2et_c.html
cspice.str2et_c(ctypes.c_char_p('2014-NOV-03 01:52:40.545'), ctypes.byref(target_epoch))

# Use pxform_c to get the rotation matrix from SMAP_SC to IAU_EARTH.
from_frame = ctypes.c_char_p('SMAP_SC')
to_frame = ctypes.c_char_p('IAU_EARTH')
out_rotate = ThreeThreeDoubles()
# http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/pxform_c.html
cspice.pxform_c(from_frame, to_frame, target_epoch, out_rotate)
for row in map(tuple, out_rotate):
    print(row)


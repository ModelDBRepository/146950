#! /usr/bin/python

import sys

filename_out = None

try:
    filename = sys.argv[1]
except:
    print 'run as: "python %s FILENAME_IN [FILENAME_OUT] [dx] [nouniform]"' % sys.argv[0]
    print 'if the last argument is nouniform, CTNG will not force a unique diameter at each point'
    sys.exit(-1)

lastarg = sys.argv[-1]
if lastarg == 'nouniform':
    nouniform = True
    dx_loc = -2
else:
    nouniform = False
    dx_loc = -1

try:
    dx = float(sys.argv[dx_loc])
    has_dx = True
except:
    # default discretization
    dx = 0.25
    has_dx = False

if len(sys.argv) > 3 or (not has_dx and len(sys.argv) == 3):
    filename_out = sys.argv[2]

from neuron import h
from mayavi import mlab
import geometry3d
import time

h.load_file('stdlib.hoc')
h.load_file('import3d.hoc')

if filename.lower()[-4:] == '.swc':
    cell = h.Import3d_SWC_read()
else:
    cell = h.Import3d_Neurolucida3()
cell.input(filename)

start = time.time()
tri_mesh = geometry3d.surface(cell, dx, n_soma_step=100, nouniform=nouniform)
mlab.triangular_mesh(tri_mesh.x, tri_mesh.y, tri_mesh.z, tri_mesh.faces, color=(1, 0, 0))
print 'time to construct mesh:', time.time() - start

start = time.time()
area = tri_mesh.area
print 'area: ', area
print 'time to compute area:', time.time() - start

start = time.time()
vol = tri_mesh.enclosed_volume
print 'volume: ', vol
print 'time to compute volume:', time.time() - start


if filename_out:
    triangles = tri_mesh.data
    with open(filename_out, 'w') as output:
        output.write('%d, %g\n' % (len(triangles), area))
        for i in xrange(len(triangles) / 9):
            output.write('%g, %g, %g,    %g, %g, %g,    %g, %g, %g\n' % tuple(triangles[i : i + 9]))


mlab.show()     


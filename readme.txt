CTNG (Constructive Tessellated Neuronal Geometry) is a tool for
constructing a 3d tesselation of a neuron's surface from
point-diameter data.

Before use: compile the C and Cython routines:

    cd geometry3d
    python setup.py build_ext --inplace

To use (for now displays the neuron, but could easily write data to a file):

    python ctng.py FILENAME_IN [FILENAME_OUT] [dx]
    
where neuron_file is the name of the source morphology.

e.g.

    python ctng.py Vn03082006-0-D.ASC out.tri 0.25

The first line of an output file lists the number of triangles and the area.

Each triangle is listed on its own line in the following format:

    x1, y1, z1,    x2, y2, z2,    x3, y3, z3

Requires:
    g++
    cython
    python
        numpy
        mayavi
    NEURON


Most of the figures for the CTNG paper were made using the morphology from

http://neuromorpho.org/neuroMorpho/neuron_info.jsp?neuron_name=Vn03082006-0-D

Changelog:

2012-12-10    sphere tests for contains_surface is primary
              bugfix for case where no output file specified
              lowered minimum chunk width from 100 to 20 voxels

2013-01-21    refactoring, bugfixes
              surfaces now provably watertight (last change introduced holes)

2013-10-05    fix to extreme points of soma (was using axis, not the soma data)

2016-05-31    commented out some printfs and changed a tuple to a list to make
              it compile with current cython and python code

              now checking filenames and using the SWC loader if a .swc file
              is loaded


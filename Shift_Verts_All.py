#!BPY
"""
Name: 'Random shift verts (On Normal)'
Blender: 277
Group: 'Mesh'
Tooltip: 'Move all the verts on a selected object a random distance on the normal z axis'
"""

import bpy
import bmesh
import random

me = bpy.context.object.data

bm = bmesh.new()
bm.from_mesh(me)

for v in bm.verts:
    r = random.uniform(-0.075,0.075)
    v.co += v.normal * r

bm.to_mesh(me)
bm.free()

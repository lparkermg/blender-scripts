#!BPY
"""
Name: 'Move vert on Z'
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
    v.co.z += v.normal.z * r
    v.co.y += v.normal.y * r
    v.co.x += v.normal.x * r

bm.to_mesh(me)
bm.free()

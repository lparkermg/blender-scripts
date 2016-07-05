"""
Name: 'Move vert on Z'
Blender: 277
Group: 'Mesh'
Tooltip: ''
"""



import bpy
import bmesh
import random

me = bpy.context.object.data

bm = bmesh.new()
bm.from_mesh(me)

for v in bm.verts:
  v.co.z += random.uniform(-0.25,0.25)

bm.to_mesh(me)
bm.free()

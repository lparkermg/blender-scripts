#!BPY
"""
Name: 'Random shift selected verts (On Normal)'
Blender: 277
Group: 'Mesh'
Tooltip: 'Move the selected verts on a selected object a random distance on the normal z axis'
"""

import bpy
import bmesh
import random

me = bpy.context.object.data
mode = bpy.context.active_object.mode

bpy.ops.object.mode_set(mode='OBJECT')
selectedVerts = [v for v in me.vertices if v.select]

for v in selectedVerts:
    r = random.uniform(-0.075,0.075)
    v.co += v.normal * r

bm.to_mesh(me)
bm.free()

bpy.ops.object.mode_set(mode=mode)

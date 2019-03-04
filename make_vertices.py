import bpy
from bpy.props import IntProperty, FloatProperty
from bpy.props import EnumProperty, FloatVectorProperty

import numpy as np

class Make(bpy.types.Operator):
	bl_idname = "object.make_vertices"
	bl_label = "NOP"
	bl_description = "make"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):	
		make()
		return {'FINISHED'}


def make():
	scene = bpy.context.scene
	

	# cube vertex and index
	cube_vertices = np.array([
		[-1.0, -1.0, -1.0], 
		[-1.0, -1.0, 1.0], 
		[-1.0, 1.0, -1.0], 
		[-1.0, 1.0, 1.0], 
		[1.0, -1.0, -1.0], 
		[1.0, -1.0, 1.0], 
		[1.0, 1.0, -1.0], 
		[1.0, 1.0, 1.0]])
	cube_polygons = np.array([
		[0, 1, 3, 2],
		[2, 3, 7, 6],
		[6, 7, 5, 4],
		[4, 5, 1, 0],
		[2, 6, 4, 0],
		[7, 3, 1, 5]])

	
	# それぞれの頂点をcube化する処理したObjectを作成
	vertices = []
	polygons = []
	for obj in bpy.context.scene.objects:
		if obj.type == 'MESH':
			for i,bv in enumerate(obj.data.vertices):
				vertices.extend(cube_vertices[:]*scene.diameter/2.0+bv.co)
				polygons.extend(cube_polygons+i*8)
				print(i)
		
	msh = bpy.data.meshes.new("cube")
	msh.from_pydata(vertices, [], polygons)
	msh.update()
	obj = bpy.data.objects.new("cube", msh)
	scene = bpy.context.scene
	scene.objects.link(obj)


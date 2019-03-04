if 'bpy' in locals():
	import imp
	imp.reload(make_vertices)
	imp.reload(py_render)
else:
	from . import make_vertices
	from . import py_render


import bpy
from bpy.props import IntProperty, FloatProperty, StringProperty
from bpy.props import EnumProperty, FloatVectorProperty

import mathutils


class Menu(bpy.types.Panel):
	bl_label = 'vertex to box'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = 'Project Yamato'
	bl_context = 'objectmode'

	# このクラスの処理が実行可能かを判定
	@classmethod
	def poll(cls, context):
		return True

	# ヘッダーのカスタマイズ
	def draw_header(self, context):
		layout = self.layout
		layout.label(text='', icon='PLUGIN')

	# メニュー
	def draw(self, context):
		layout = self.layout
		scene = context.scene
		
		layout.label(text='BoxSize:')
		layout.prop(scene, 'diameter', text='Cubeの1辺の長さ')
		layout.separator()

		layout.operator(make_vertices.Make.bl_idname, text='頂点をCube化')
		layout.separator()
		

class DepthMap(bpy.types.Panel):
	bl_label = 'depth_map'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = 'Project Yamato'
	bl_context = 'objectmode'
	

	# このクラスの処理が実行可能かを判定
	@classmethod
	def poll(cls, context):
		return True

	# ヘッダーのカスタマイズ
	def draw_header(self, context):
		layout = self.layout
		layout.label(text='', icon='PLUGIN')

	# メニュー
	def draw(self, context):
		layout = self.layout
		scene = context.scene

		layout.label(text='Blenderと現実の長さの比率:')
		layout.prop(scene, 'length_blender_exsample', text='Blender')
		layout.prop(scene, 'length_real_exsample', text='real')
		layout.separator()

		layout.label(text='デプス画像の正規化の幅(実際のメートル):')
		layout.prop(scene, 'real_near_distance', text='Near')
		layout.prop(scene, 'real_far_distance', text='Far')
		layout.separator()

		layout.label(text='解像度:')
		layout.prop(scene, 'output_resolution_x', text='x')
		layout.prop(scene, 'output_resolution_y', text='y')
		layout.prop(scene, 'resolution_percentage', text='%')
		layout.separator()

		col = layout.column()
		col.prop(context.scene, 'save_path', text='')
		layout.separator()
		
		layout.operator(py_render.Render.bl_idname, text='render depth images')
		layout.separator()
		

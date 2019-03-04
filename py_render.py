import bpy
from bpy.props import IntProperty, FloatProperty
from bpy.props import EnumProperty, FloatVectorProperty

import numpy as np

class Render(bpy.types.Operator):
	bl_idname = "object.py_render"
	bl_label = "NOP"
	bl_description = "render"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):	
		render()
		return {'FINISHED'}


def render():
	scene = bpy.context.scene
	
	# 解像度を設定
	bpy.context.scene.render.resolution_x = scene.output_resolution_x
	bpy.context.scene.render.resolution_y = scene.output_resolution_y
	bpy.context.scene.render.resolution_percentage = scene.resolution_percentage
	
	# node を切り替えて、作成したnodeにレンダリング結果を出力
	bpy.context.scene.use_nodes = True
	tree = bpy.context.scene.node_tree
	links = tree.links
	# default node をクリア
	for n in tree.nodes:
		tree.nodes.remove(n)
	# input render layer node 作成
	rl = tree.nodes.new('CompositorNodeRLayers')
	rl.location = 180,280
	# output node 作成
	v = tree.nodes.new('CompositorNodeViewer')   
	v.location = 750,210
	v.use_alpha = False
	
	links.new(rl.outputs[2], v.inputs[0])


	for o in scene.objects:
		if o.type=='CAMERA':
			# turning FOV
			#o.data.angle = 1.026 * o.data.angle

			# set active camera
			bpy.context.scene.camera = o
			
			# render
			bpy.ops.render.render()
			# get rendering result image
			pixels = np.array(bpy.data.images['Viewer Node'].pixels)
			
			# 現実とBlender内の長さの比率を導出
			real_far_distance = scene.real_far_distance	# メートル
			real_near_distance = scene.real_near_distance	# メートル
			blender = scene.length_blender_exsample
			real = scene.length_real_exsample
			blender_real_ratio = blender / real


			blender_far_distance = blender_real_ratio * real_far_distance
			blender_near_distance = blender_real_ratio * real_near_distance
			distance = blender_far_distance - blender_near_distance
			#print('blender_real_ratio ', blender_real_ratio)
			#print('blender_far_distance ',blender_far_distance)
			#print('blender_near_distance ',blender_near_distance)
			
			# デプス(カメラからの距離情報)を色データとして画素に保存
			for i in range(np.shape(pixels)[0]):
				if pixels[i] > blender_far_distance:
					pixels[i] = 1.0
				elif pixels[i] < blender_near_distance:
					pixels[i] = 0.0
				else:
					pixels[i] = (pixels[i] - blender_near_distance) / distance
					if i%4 == 0:
						print('pixels[i] ',pixels[i])

			# gamma 補正を除去
			pixels[0::4] = np.power(pixels[0::4], 2.27195)
			pixels[1::4] = np.power(pixels[1::4], 2.27195)
			pixels[2::4] = np.power(pixels[2::4], 2.27195)
			
			# alpha = 1.0
			pixels[3::4] = 1.0
			bpy.data.images['Viewer Node'].pixels = pixels
			bpy.data.images['Viewer Node'].save_render(filepath = scene.save_path+o.name+'.png')


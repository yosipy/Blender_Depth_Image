bl_info = {
	"name": "create depth image",
	"author": "yosi",
	"version": (3, 0.0),
	"blender": (2, 79, 0),
	"location": "3Dビュー > ツールシェルフ",
	"description": "yamato",
	"warning": "VTV Warning",
	"support": "TESTING",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Render"
}


if "bpy" in locals():
	import imp
	imp.reload(mp_menu)
else:
	from . import mp_menu

import bpy
from bpy.props import IntProperty, FloatProperty
from bpy.props import EnumProperty, FloatVectorProperty


# プロパティ初期化
def init_props():
	scene = bpy.types.Scene
	scene.diameter = FloatProperty(
		name="diameter",
		description="Float Property",
		default=0.03,
		min=0.0,
		max=0.1
	)

	scene.save_path = bpy.props.StringProperty(
		name = "save_path",
		default = "",
		description = "Define the save path of the project",
		subtype = 'DIR_PATH'
	)

	scene.output_resolution_x = IntProperty(
		name="output_resolution_x",
		description="Int Property",
		default=1920,
		min=1,
		max=50000
	)

	scene.output_resolution_y = IntProperty(
		name="output_resolution_y",
		description="Int Property",
		default=1080,
		min=1,
		max=50000
	)

	scene.resolution_percentage = IntProperty(
		name="resolution_percentage",
		description="Int Property",
		default=100,
		min=1,
		max=100
	)

	scene.length_blender_exsample = FloatProperty(
		name="length_blender_exsample",
		description="Float Property",
		default=1.73,
		min=0.1,
		max=100
	)

	scene.length_real_exsample = FloatProperty(
		name="length_real_exsample",
		description="Float Property",
		default=1.0,
		min=1.0,
		max=100
	)

	scene.real_far_distance = FloatProperty(
		name="real_far_distance",
		description="Float Property",
		default=10.0,
		min=0.0,
		max=100
	)

	scene.real_near_distance = FloatProperty(
		name="real_near_distance",
		description="Float Property",
		default=1.0,
		min=0.0,
		max=100
	)



# プロパティ削除
def clear_props():
	scene = bpy.types.Scene
	del scene.diameter
	del scene.save_path
	del scene.output_resolution_x
	del scene.output_resolution_y
	del scene.resolution_percentage
	del scene.length_blender_exsample
	del scene.length_real_exsample
	del scene.real_far_distance
	del scene.real_near_distance


# アドオン有効化時の処理
def register():
	bpy.utils.register_module(__name__)
	init_props()
	print("Project Yamato: アドオン「Project Yamato」が有効化されました。")


# アドオン無効化時の処理
def unregister():
	clear_props()
	bpy.utils.unregister_module(__name__)
	print("Project Yamato: アドオン「Project Yamato」が無効化されました。")


if __name__ == "__main__":
	register()


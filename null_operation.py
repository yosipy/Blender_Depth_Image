import bpy
from bpy.props import IntProperty, FloatProperty
from bpy.props import EnumProperty, FloatVectorProperty


class NullOperation(bpy.types.Operator):

	bl_idname = "object.null_operation"
	bl_label = "NOP"
	bl_description = "何もしない"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		return {'FINISHED'}

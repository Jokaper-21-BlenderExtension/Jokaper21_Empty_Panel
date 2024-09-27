import bpy

bl_info = {
    "name": "Material Pro Tools",
    "blender": (4, 2, 0),
    "category": "Object",
}

class Material_Pro_Tools(bpy.types.Panel):
    bl_label = "Material Pro Tools"
    bl_idname = "MPT_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'AJO'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("wm.url_open", text="", icon="GHOST_ENABLED").url = "https://www.cgtrader.com/designers/jokaper21"
        row.separator(factor=1)
        row.label(text="JOKAPER 21")

def register():
    bpy.utils.register_class(Material_Pro_Tools)
    # Load and register the second script
    try:
        import mesh_material_replacer  # Change this to your second script's name
        mesh_material_replacer.register()
    except Exception as e:
        print(f"Failed to load mesh_material_replacer: {e}")

def unregister():
    bpy.utils.unregister_class(Material_Pro_Tools)
    try:
        import mesh_material_replacer
        mesh_material_replacer.unregister()
    except Exception as e:
        print(f"Failed to unload mesh_material_replacer: {e}")

if __name__ == "__main__":
    register()


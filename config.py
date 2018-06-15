import bpy

# https://blender.stackexchange.com/questions/5281/blender-sets-compute-device-cuda-but-doesnt-use-it-for-actual-render-on-ec2
bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
bpy.context.user_preferences.addons['cycles'].preferences.devices[0].use = True

bpy.context.scene.cycles.device = 'GPU'

bpy.data.scenes["Scene"].render.filepath = "/tmp/output.png"
bpy.ops.render.render(write_still=True)

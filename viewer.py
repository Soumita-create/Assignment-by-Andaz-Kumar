
import trimesh
import pyrender

def display_3d_model(model_path):
    mesh = trimesh.load(model_path)
    scene = pyrender.Scene()
    scene.add(pyrender.Mesh.from_trimesh(mesh))
    pyrender.Viewer(scene, use_raymond_lighting=True, run_in_thread=True)


def generate_3d_model_from_text(prompt):
    print(f"Generating 3D model for: '{prompt}'")
    dummy_model_path = "demo_model.obj"
    with open(dummy_model_path, "w") as f:
        f.write("# Dummy 3D Model\n")
        f.write("v 0 0 0\nv 1 0 0\nv 1 1 0\nv 0 1 0\nf 1 2 3 4\n")
    return dummy_model_path

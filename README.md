# Assignment-by-Andaz-Kumar

# Text or Photo to 3D Model Generator
This project is a prototype that takes a text prompt (and optionally a photo) and generates a 3D model in .obj format. It also provides basic functionality for visualizing the generated 3D models.

# My Thoughts 
The goal of this assignment is to demonstrate a pipeline that connects a natural input (text/photo) to a 3D output. Since real 3D model generation is complex, this prototype uses a placeholder (.obj file) to simulate the behavior. The focus is on structuring the logic, handling input/output and rendering.

# Steps to Run
1. download the repository.

2. Install required libraries.

3. Run the Jupyter notebook (ASSIGNMENT.ipynb) or you can use the Python script to:

Enter a text prompt.

Generate a dummy .obj file.

View the file in a 3D viewer.

# Libraries Used
numpy : General numerical operations

trimesh : 3D model handling and parsing

pyrender : 3D model rendering and visualization


# Project Structure
ASSIGNMENT.ipynb       : Main Jupyter Notebook for the prototype

text_to_3d.py          : Contains model generation logic

viewer.py              : Contains model visualization code

demo_model.obj         : Sample output 3D model

requirements.txt       : Required Python packages

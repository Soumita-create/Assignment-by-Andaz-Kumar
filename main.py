
from text_to_3d import generate_3d_model_from_text
from viewer import display_3d_model

if __name__ == "__main__":
    prompt = input("Enter a text prompt: ")
    model_path = generate_3d_model_from_text(prompt)
    display_3d_model(model_path)

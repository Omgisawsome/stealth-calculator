import google.generativeai as genai
import PIL.Image
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def solve_math(image_path):
    model = genai.GenerativeModel('gemini-1.5-flash')
    img = PIL.Image.open(image_path)
    
    prompt = "You are a calculator assistant. Solve the math problems in this image. Provide only the final answers clearly."
    
    response = model.generate_content([prompt, img])
    print("Gemini Result:", response.text)
    return response.text
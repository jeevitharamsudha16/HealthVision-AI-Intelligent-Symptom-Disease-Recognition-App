### Health Management APP — Disease / Symptom Recognition

from dotenv import load_dotenv
load_dotenv()  # load all environment variables

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to call Gemini Vision Model
def get_gemini_response(system_prompt, image, user_prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")   # Updated model
    response = model.generate_content([system_prompt, image[0], user_prompt])
    return response.text

# Convert uploaded image to Gemini-compatible format
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# ---------------- Streamlit UI ---------------- #

st.set_page_config(page_title="Gemini Disease Recognition App")

st.header("🩺 Gemini Disease Recognition App")

# User input question
user_question = st.text_input("Ask something about the medical image:", key="input")

# Upload image
uploaded_file = st.file_uploader("Upload a medical image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Submit button
submit = st.button("Analyze Image")

# Medical disease analysis expert prompt
system_prompt = """
You are a medical image analysis expert.
You will receive an image that may contain a visible symptom, skin issue, wound,
infection, or unusual health condition.

Your tasks:
1. Identify possible diseases or conditions visible in the image.
2. Describe the visible symptoms clearly.
3. Provide possible causes.
4. Suggest recommended next steps:
   - Whether to see a doctor
   - What tests may be needed
   - What immediate precautions can be taken
5. If image is unclear or uncertain, say: "A professional medical diagnosis is required."

Be accurate, safe, and responsible. Do NOT provide medications unless clearly visible.
"""

# When user clicks submit
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(system_prompt, image_data, user_question)
    st.subheader("🩻 Analysis Result")
    st.write(response)

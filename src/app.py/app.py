import streamlit as st
import os
from dotenv import load_dotenv
import boto3
import google.generativeai as genai

# --- Configuration and Key Loading Section ---
# This section runs only once at the start of the program

# Load environment variables from .env file
load_dotenv()

# Configure AWS Rekognition
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

# Note: If you have run aws configure, boto3 will automatically find the keys.
# But for added certainty, we can create the client like this:
rekognition_client = boto3.client(
    'rekognition',
    region_name='us-east-1', # The region you entered in aws configure
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Configure Google Gemini
try:
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
except TypeError:
    st.error("Google API key not found. Please check the .env file.")
    st.stop() # Stops the program execution

# --- Main Project Functions ---
# These functions are copied from previous scripts

def analyze_image_with_rekognition(image_bytes):
    try:
        response = rekognition_client.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=15,
            MinConfidence=75
        )
        return [label['Name'] for label in response['Labels']]
    except Exception as e:
        st.error(f"Error in connecting to AWS Rekognition: {e}")
        return None

def clean_ingredient_list(labels):
    generic_labels = ['Food', 'Fruit', 'Produce', 'Plant', 'Vegetable', 'Dish', 'Meal', 'Cuisine']
    return [label for label in labels if label not in generic_labels]

def create_recipe_with_gemini(ingredient_list):
    if not ingredient_list:
        return "Unfortunately, no recognizable ingredients were found in the image to create a recipe."
    
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    ingredients_str = ", ".join(ingredient_list)
    
    prompt = f"""
    You are a skilled and creative chef. Your task is to create an exciting and delicious recipe in English based on the provided list of ingredients.

    Available ingredients: {ingredients_str}

    Please provide a complete recipe with the following format:

    **Title:** (An appealing name for the dish)
    **Description:** (One or two short sentences about the dish)
    **Ingredients:**
    - (List of ingredients)
    **Preparation Steps:**
    1. (First step)
    2. (Second step)
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error in connecting to Google AI: {e}")
        return None

# --- Building the User Interface with Streamlit ---

st.set_page_config(page_title="AI Recipe Generator", page_icon="🍳")

st.title("👨‍🍳 AI Recipe Generator")
st.write("Upload a photo of your ingredients to receive a creative recipe!")

# File upload widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image_bytes = uploaded_file.getvalue()
    st.image(image_bytes, caption="Uploaded Image", use_container_width=True)

    # Button to start the process
    if st.button("Generate Recipe!"):
        
        # Step 1: Analyze image with AWS
        with st.spinner("Analyzing image and detecting ingredients..."):
            detected_labels = analyze_image_with_rekognition(image_bytes)

        if detected_labels:
            st.success("Ingredients successfully detected!")
            
            # Step 2: Clean the ingredient list
            cleaned_ingredients = clean_ingredient_list(detected_labels)
            st.write("**Detected Ingredients:**", ", ".join(cleaned_ingredients))

            # Step 3: Generate recipe with Gemini
            with st.spinner("Creating a delicious recipe..."):
                recipe = create_recipe_with_gemini(cleaned_ingredients)
            
            if recipe:
                st.success("Your recipe is ready!")
                st.markdown("---")
                # Use st.markdown for better text formatting display
                st.markdown(recipe)
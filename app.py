import streamlit as st
import google.generativeai as genai
from googletrans import Translator  # For translation (optional)
import asyncio

# Set background image URL (change it to your preferred image URL or local image path)
background_image_url = "https://i.pinimg.com/736x/13/20/49/1320494d508b9da8ff0e8c1447732eea.jpg"  # Replace with your image URL

# Custom CSS to set the background image
background_css = f"""
    <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
    </style>
"""

# Inject the custom CSS into the Streamlit app
st.markdown(background_css, unsafe_allow_html=True)

# Load API key securely from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

async def generate_recipe_async(ingredients, language):
    """Generates a recipe using Gemini AI based on input ingredients."""
    model = genai.GenerativeModel("gemini-2.0-flash-exp")

    prompt = f"""
    Generate an authentic **Indian recipe** using these ingredients: {', '.join(ingredients)}.
    The recipe should follow Indian cooking styles and traditional flavors.
    
    Format:
    - Recipe Name
    - Ingredients List (with Indian spices if applicable)
    - Step-by-step Cooking Instructions
    - Cooking Time
    - Serving Size
    - Optional: Regional variations (e.g., North Indian, South Indian, Bengali, etc.)
    """
    try:
        response = model.generate_content(prompt)
        recipe = response.text if response else "Sorry, no recipe found."

        if language != "English":
            translator = Translator()
            translated_recipe = await translator.translate(recipe, src='en', dest=language.lower())
            recipe = translated_recipe.text  # Get the translated text
        
        return recipe
    except Exception as e:
        return f"Error: {str(e)}"

def generate_recipe(ingredients, language):
    """Wrapper to run the async function in the normal flow of Streamlit."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(generate_recipe_async(ingredients, language))

# Streamlit UI
st.title("🍽️ AI-Powered Recipe Generator")
st.write("Enter ingredients, and AI will generate a unique recipe for you!")

# User Input
ingredients = st.text_input("Enter ingredients (comma-separated):", "")
language = st.selectbox("Select Output Language", ["English", "Hindi", "Telugu"])

if st.button("Generate Recipe"):
    if ingredients:
        ingredient_list = [item.strip() for item in ingredients.split(",")]
        with st.spinner("Generating recipe..."):
            recipe = generate_recipe(ingredient_list, language)
        st.subheader(f"🍲 Your {language} AI-Generated Recipe:")
        st.write(recipe)
    else:
        st.warning("Please enter at least one ingredient.")

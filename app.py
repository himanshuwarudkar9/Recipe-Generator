import streamlit as st
import google.generativeai as genai
from googletrans import Translator  # For translation (optional)
import asyncio

# Set background image URL (change it to your preferred image URL or local image path)
image_base64 = get_base64_image("assets/ripe-products-colored-vitamine-riched-salad-vegetables-dark-floor.jpg")  # Path to your image
# Custom CSS to set the background image
background_css = """
    <style>
        /* Apply background to the entire page */
        .stApp {
            background: url("data:image/jpg;base64,{image_base64}") no-repeat center center fixed;
            background-size: cover;
        }
        
        /* Style text input fields */
        .stTextInput>div>div>input {
            background-color: rgba(255, 255, 255, 0.7);  
            color: black;
        }
        
        /* Style select box */
        .stSelectbox>div>div>input {
            background-color: rgba(255, 255, 255, 0.7);  
            color: black;
        }
        
        /* Style buttons */
        .stButton>button {
            background-color: #ff7f50;
            color: white;
            border-radius: 8px;
        }

        /* Improve readability of text */
        .stMarkdown, .stTitle, .stHeader, .stSubheader {
            color: white;  /* Ensures text remains readable */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
    </style>
"""

# Inject the CSS into the Streamlit app
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

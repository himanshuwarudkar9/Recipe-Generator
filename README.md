# AI-Powered Recipe Generator
Welcome to the AI-Powered Recipe Generator! This project leverages the Google Gemini AI model to generate unique recipes based on user-provided ingredients. It offers real-time recipe suggestions and allows users to translate the recipe into different languages.

Features:
1. Recipe Generation: AI generates authentic Indian recipes based on ingredients.
2. Language Support: Recipe output can be generated in multiple languages (English, Hindi, Telugu).
3. AI Model: Powered by the Google Gemini AI model (gemini-2.0-flash-exp).
4. Translation: Optionally translate recipes to different languages using Google Translate.

## Project Setup
### Prerequisites
To run this project, you need to have the following installed:

1. Python 3.7+
2. Streamlit
3. Google Generative AI Python client (google-generativeai)
4. Google Translate API (for translations)
5. Installation Steps
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/recipe-generator.git
cd recipe-generator
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
.\venv\Scripts\activate   # For Windows
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up Streamlit secrets for API keys:

Go to Streamlit → Settings → Secrets Management.
Add your Google API key under GOOGLE_API_KEY.
Run the app:

bash
Copy
Edit
streamlit run app.py
How It Works
Recipe Generation
The application uses Google Gemini AI to generate recipes based on the ingredients you provide. The process involves:

User inputs ingredients in a comma-separated list.
The AI generates an authentic Indian recipe, including:
Recipe name
Ingredients list (with spices)
Cooking instructions
Cooking time
Serving size
Regional variations (optional)
Language Support
Recipes can be translated into the following languages:

English
Hindi
Telugu
UI Customization
Background Image: You can customize the background of the app with a local image (JPEG format).
Input fields and buttons are styled to enhance the UI/UX.
Code Structure
app.py
Main file where the Streamlit app runs.
Handles recipe generation, translation, and UI rendering.
Loads and sets a local background image for the UI.
requirements.txt
Contains all the dependencies required for the project.
streamlit
google-generativeai
googletrans==4.0.0-rc1
base64
assets/
This directory contains the images used in the app (background image, etc.).
README.md
This file. Contains project information and instructions.
Contributing
We welcome contributions to this project! To contribute:

Fork the repository.
Create a new branch.
Make changes and commit them.
Open a Pull Request for review.
License
This project is licensed under the MIT License - see the LICENSE file for details.

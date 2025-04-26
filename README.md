# AI-Powered Recipe Generator
Welcome to the **AI-Powered Recipe Generator**! This project leverages the **Google Gemini AI** model to generate unique recipes based on user-provided ingredients. It offers real-time recipe suggestions and allows users to translate the recipe into different languages.

![Screenshot 2025-04-26 124736](https://github.com/user-attachments/assets/eb6dc807-0090-4b71-b848-1af0f383a379)


## Features:
- **Recipe Generation**: AI generates authentic Indian recipes based on ingredients.
- **Language Support**: Recipe output can be generated in multiple languages (English, Hindi, Telugu).
- **AI Model**: Powered by the Google Gemini AI model (`gemini-2.0-flash-exp`).
- **Translation**: Optionally translate recipes to different languages using Google Translate.

You can visit the app directly [here](https://himanshu-recipe-generator.streamlit.app/).

## Project Setup

### Prerequisites
To run this project, you need to have the following installed:
- Python 3.7+
- Streamlit
- Google Generative AI Python client (`google-generativeai`)
- Google Translate API (for translations)
   
## Installation Steps
1. Clone the repository:
   
- git clone https://github.com/your-username/recipe-generator.git
- cd recipe-generator

2. Create and activate a virtual environment:

- python3 -m venv venv
- source venv/bin/activate  For macOS/Linux
- .\venv\Scripts\activate   For Windows

3. Install the required dependencies:

- pip install -r requirements.txt

4. Set up Streamlit secrets for API keys:

- Go to Streamlit → Settings → Secrets Management.
- Add your Google API key under GOOGLE_API_KEY.

5. Run the app:
   
- streamlit run app.py

## How It Works
### Recipe Generation

The application uses Google Gemini AI to generate recipes based on the ingredients you provide. The process involves:

1. User inputs ingredients in a comma-separated list.
2. The AI generates an authentic Indian recipe, including:
- Recipe name
- Ingredients list (with spices)
- Cooking instructions
- Cooking time
- Serving size
- Regional variations (optional)
  
### Language Support
Recipes can be translated into the following languages:
- English
- Hindi
- Telugu

## Code Structure
### app.py
- Main file where the Streamlit app runs.
- Handles recipe generation, translation, and UI rendering.
### requirements.txt
Contains all the dependencies required for the project.
- streamlit
- google-generativeai
- googletrans==4.0.0-rc1
### README.md
- This file. Contains project information and instructions.

## Contributing
We welcome contributions to this project! To contribute:

- Fork the repository.
- Create a new branch.
- Make changes and commit them.
- Open a Pull Request for review.
  
## License
This project is licensed under the MIT License - see the LICENSE file for details.



import streamlit as st
import google.generativeai as genai

# Initialize API key for Gemini
gemini_api_key = st.secrets["GEMINI_API_KEY"]

# Configure the Gemini API
genai.configure(api_key=gemini_api_key)

@st.cache_resource
def load_gemini_model():
    return genai.GenerativeModel('gemini-1.5-pro-latest')

def generate_recipe_suggestions(user_input, selected_diets, model):
    # Construct a detailed prompt using user input and dietary preferences
    diet_str = ", ".join(selected_diets) if selected_diets else "no specific dietary preferences"
    prompt = (f"You are a master chef AI. Based on the following dietary preferences: {diet_str}, "
              f"and the user's request: '{user_input}', suggest some creative and delicious recipe ideas. "
              "For each recipe, include the name, a brief description, key ingredients, and any relevant notes "
              "on preparation or serving. Please do not include any unnecessary details or explanations; just the recipes.")
    
    # Generate the content using the Gemini model
    response = model.generate_content(prompt)
    return response.text

st.title("Dish Decoder - AI Meal Planner")

# Checkbox for dietary preferences
st.header("Select Your Dietary Preferences")
diet_options = [
    "Vegan", 
    "Vegetarian", 
    "Gluten-Free", 
    "Low-Carb", 
    "All Meat", 
    "High Protein", 
    "Gym Friendly", 
    "Keto"
]

# Create a grid layout for checkboxes with 4 columns
selected_diets = []
columns = st.columns(4)
for i, option in enumerate(diet_options):
    with columns[i % 4]:
        if st.checkbox(option):
            selected_diets.append(option)

# User input for natural language preferences
st.header("Tell us about your meal preference")
user_input = st.text_area("Enter any specific requests or dietary goals:")

if st.button("Get Recipes"):
    # Load the Gemini model (cached)
    model = load_gemini_model()

    # Generate recipe suggestions using Gemini
    recipe_suggestions = generate_recipe_suggestions(user_input, selected_diets, model)

    # Display the generated recipe suggestions
    st.markdown(recipe_suggestions)

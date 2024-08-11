# app.py
import streamlit as st
import os
from spoonacular import SpoonacularClient
import google.generativeai as genai

# Initialize API clients with API keys
spoonacular_api_key = os.environ.get("SPOONACULAR_API_KEY")
gemini_api_key = os.environ.get("GOOGLE_API_KEY")
client = SpoonacularClient(spoonacular_api_key)

genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel('gemini-1.5-pro-latest')

st.title("Dish Decoder - AI Meal Planner")

# Sidebar for dietary preferences
st.sidebar.header("Select Dietary Preferences")
diet_options = ["None", "Vegan", "Vegetarian", "Gluten-Free", "Low-Carb"]
selected_diets = st.sidebar.multiselect("Choose your diet:", diet_options)

# Text input for natural language preferences
st.header("Tell us about your meal preference")
user_input = st.text_area("Enter any specific requests or dietary goals:")

def fetch_recipes(diets, ingredients, user_input):
    """
    Fetch recipes based on dietary preferences, ingredients, and user input.
    """
    try:
        # Use dietary filters and user input to search for recipes
        recipes = client.get_recipes_by_diet(diets, number=5) if diets else client.get_recipes_by_ingredients(ingredients)
        return recipes
    except Exception as e:
        st.write(f"Error fetching recipes: {e}")
        return []

def process_natural_language_input(user_input):
    """
    Analyze the natural language input using the Gemini API.
    """
    try:
        response = gemini_model.generate_content(f"Analyze this input for meal preferences: {user_input}")
        return response.text
    except Exception as e:
        st.write(f"Error processing input with Gemini: {e}")
        return "Could not process input."

if st.button("Find Recipes"):
    # Process natural language input
    if user_input:
        analysis = process_natural_language_input(user_input)
        st.write(f"Analysis: {analysis}")

    # User input for ingredients
    ingredients = [item.strip() for item in ingredients_input.split(",")]

    # Fetch and display recipes
    recipes = fetch_recipes(selected_diets, ingredients, user_input)
    if recipes:
        for recipe in recipes:
            st.subheader(recipe['title'])
            st.image(recipe['image'])
            st.markdown(f"[View Full Recipe]({recipe['sourceUrl']})")
    else:
        st.write("No recipes found. Try different preferences or ingredients.")

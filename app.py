# app.py

import streamlit as st
from spoonacular import SpoonacularClient
import google.generativeai as genai
import os

# Initialize API keys
spoonacular_api_key = st.secrets["SPOONACULAR_API_KEY"]
gemini_api_key = st.secrets("GOOGLE_API_KEY")



# Configure the Gemini API
genai.configure(api_key=gemini_api_key)

# Initialize the Spoonacular API client
spoonacular_client = SpoonacularClient(spoonacular_api_key)

st.title("Dish Decoder - AI Meal Planner")

# Sidebar for dietary preferences
st.sidebar.header("Select Dietary Preferences")
diet_options = ["None", "Vegan", "Vegetarian", "Gluten-Free", "Low-Carb"]
selected_diets = st.sidebar.multiselect("Choose your diet:", diet_options)

# User input for natural language preferences
st.header("Tell us about your meal preference")
user_input = st.text_area("Enter any specific requests or dietary goals:")

if st.button("Get Recipes"):
    # Analyze natural language input with Gemini
    def process_natural_language_input(user_input):
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content(f"Analyze this input for meal preferences: {user_input}")
        return response.text

    # Fetch recipes from Spoonacular
    def fetch_recipes(diets, user_input):
        # Combine dietary preferences with user input
        query = " ".join(diets) + " " + user_input
        # Fetch recipes from Spoonacular API
        recipes = spoonacular_client.get_recipes_by_diet(diets, number=5)
        return recipes

    # Display the analysis
    analysis = process_natural_language_input(user_input)
    st.write(f"Analysis: {analysis}")

    # Fetch and display recipes
    recipes = fetch_recipes(selected_diets, user_input)
    if recipes:
        for recipe in recipes:
            st.subheader(recipe['title'])
            st.image(recipe['image'])
            st.markdown(f"[View Full Recipe]({recipe['sourceUrl']})")
    else:
        st.write("No recipes found for the given preferences.")

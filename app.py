import streamlit as st
from spoonacular import SpoonacularClient
import os

# Initialize API client
api_key = os.environ.get("SPOONACULAR_API_KEY")
client = SpoonacularClient(api_key)

st.title("Dish Decoder")

# User input for ingredients
ingredients_input = st.text_input("Enter ingredients (comma-separated):")
if st.button("Find Recipes"):
    ingredients = [item.strip() for item in ingredients_input.split(",")]
    recipes = client.get_recipes_by_ingredients(ingredients)
    
    # Display recipe suggestions
    if recipes:
        for recipe in recipes:
            st.subheader(recipe['title'])
            st.image(recipe['image'])
            st.write(f"Recipe ID: {recipe['id']}")
    else:
        st.write("No recipes found. Try different ingredients.")

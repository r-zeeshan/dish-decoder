import streamlit as st
from spoonacular import SpoonacularClient
import google.generativeai as genai

# Initialize API keys
spoonacular_api_key = st.secrets["SPOONACULAR_API_KEY"]
gemini_api_key = st.secrets["GEMINI_API_KEY"]

# Configure the Gemini API
genai.configure(api_key=gemini_api_key)

# Initialize the Spoonacular API client
spoonacular_client = SpoonacularClient(spoonacular_api_key)

@st.cache_resource
def load_gemini_model():
    # Cache the Gemini model to avoid reloading on every interaction
    return genai.GenerativeModel('gemini-1.5-pro-latest')

def generate_recipe_names(user_input, model):
    # Use Gemini API to generate a list of recipe names only
    prompt = f"Suggest some recipe names based on these preferences: {user_input}. Only list the recipe names."
    response = model.generate_content(prompt)
    # Assuming the response is a newline-separated list of recipe names
    recipe_names = response.text.split('\n')
    return [name.strip() for name in recipe_names if name.strip()]

def fetch_recipe_details(recipe_name):
    # Fetch recipe details from Spoonacular API by recipe name
    # Note: Spoonacular's API requires searching by ingredient or other criteria. Adjusting to find a close match.
    query_params = {"query": recipe_name, "number": 1}
    response = spoonacular_client.get_recipes_by_diet(query_params["query"], number=1)
    if response:
        return response[0]  # Return the first matching recipe
    return None

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
columns = st.columns(4)  # 4 columns for grid layout
for i, option in enumerate(diet_options):
    with columns[i % 4]:  # Position each checkbox in the correct column
        if st.checkbox(option):
            selected_diets.append(option)

# User input for natural language preferences
st.header("Tell us about your meal preference")
user_input = st.text_area("Enter any specific requests or dietary goals:")

if st.button("Get Recipes"):
    # Load the Gemini model (cached)
    model = load_gemini_model()

    # Generate recipe names using Gemini
    recipe_names = generate_recipe_names(user_input, model)
    
    if recipe_names:
        st.write(f"Suggested Recipes: {', '.join(recipe_names)}")

        # Fetch and display recipe details from Spoonacular
        for recipe_name in recipe_names:
            recipe_details = fetch_recipe_details(recipe_name)
            if recipe_details:
                st.subheader(recipe_details['title'])
                st.image(recipe_details['image'])
                source_url = recipe_details.get('sourceUrl', 'URL not available')
                st.markdown(f"[View Full Recipe]({source_url})")
            else:
                st.write(f"Details not found for recipe: {recipe_name}")
    else:
        st.write("No recipes could be generated from the input.")

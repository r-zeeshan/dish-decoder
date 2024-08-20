import streamlit as st
import google.generativeai as genai

# Initialize API key for Gemini
gemini_api_key = st.secrets["GEMINI_API_KEY"]

# Configure the Gemini API
genai.configure(api_key=gemini_api_key)

@st.cache_resource
def load_gemini_model():
    return genai.GenerativeModel('gemini-1.5-pro-latest')

def generate_detailed_recipe(user_input, selected_diets, model):
    # Construct a detailed prompt using user input and dietary preferences
    diet_str = ", ".join(selected_diets) if selected_diets else "no specific dietary preferences"
    prompt = (f"You are a master chef AI. Based on the following dietary preferences: {diet_str}, "
              f"and the user's request: '{user_input}', suggest a creative and delicious recipe. "
              "Provide a step-by-step guide including: \n"
              "1. A list of all ingredients with exact quantities.\n"
              "2. Detailed, sequential cooking instructions from preparation to serving.\n"
              "The instructions should be clear and easy to follow for someone cooking at home.")
    
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

    # Generate detailed recipe instructions using Gemini
    detailed_recipe = generate_detailed_recipe(user_input, selected_diets, model)

    # Display the generated detailed recipe instructions
    st.markdown(detailed_recipe)


st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    .footer {visibility: visible; position: relative; bottom: 10px; text-align: center;}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="footer">Developed by Zeeshan Hameed</div>', unsafe_allow_html=True)
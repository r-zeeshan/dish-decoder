import streamlit as st
import google.generativeai as genai

gemini_api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=gemini_api_key)

@st.cache_resource
def load_gemini_model():
    """
    Loads the Gemini model.
    Returns:
        genai.GenerativeModel: The loaded Gemini model.
    """
    return genai.GenerativeModel('gemini-1.5-pro-latest')

def generate_detailed_recipe(user_input, selected_diets, model):
    """
    Generates a detailed recipe based on user input, selected diets, and a model.
    Args:
        user_input (str): The user's request for a recipe.
        selected_diets (list): A list of selected dietary preferences.
        model: The model used to generate the recipe.
    Returns:
        str: The generated recipe as a text.
    """
    diet_str = ", ".join(selected_diets) if selected_diets else "no specific dietary preferences"
    prompt = (f"You are a master chef AI. Based on the following dietary preferences: {diet_str}, "
              f"and the user's request: '{user_input}', suggest a creative and delicious recipe. "
              "Provide a step-by-step guide including: \n"
              "1. A list of all ingredients with exact quantities.\n"
              "2. Detailed, sequential cooking instructions from preparation to serving.\n"
              "The instructions should be clear and easy to follow for someone cooking at home.")
    
    response = model.generate_content(prompt)
    return response.text


### Streamlit App ###
st.title("Dish Decoder - AI Meal Planner")

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

selected_diets = []
columns = st.columns(4)
for i, option in enumerate(diet_options):
    with columns[i % 4]:
        if st.checkbox(option):
            selected_diets.append(option)

st.header("Tell us about your meal preference")
user_input = st.text_area("Enter any specific requests or dietary goals:")

if st.button("Get Recipes"):
    model = load_gemini_model()

    detailed_recipe = generate_detailed_recipe(user_input, selected_diets, model)

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
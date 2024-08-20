# Dish Decoder - AI Meal Planner Chat

## Overview

**Dish Decoder** is an AI-powered meal planning chat application that allows users to interact with a master chef AI to receive personalized recipe suggestions and cooking instructions. The application leverages Google's Gemini AI to understand user preferences, dietary restrictions, and specific requests, providing tailored recipe recommendations in an interactive chat format.

**Live Application:** [https://dish-decoder.streamlit.app/](https://dish-decoder.streamlit.app/)

## Features

- **Interactive Chat Interface:** Engage in a back-and-forth conversation with the AI to explore different recipe ideas, ask for cooking instructions, and refine your meal planning based on your dietary needs.
  
- **Dietary Preference Integration:** The application allows you to select from a variety of dietary preferences (e.g., Vegan, Gluten-Free, Keto) and combines them with your custom requests to generate the most relevant recipes.

- **Step-by-Step Instructions:** The AI provides detailed recipes, including a list of ingredients with quantities and step-by-step cooking instructions, making it easy to follow along.

- **Persistent Chat History:** The chat maintains a conversation history, enabling context-aware interactions and allowing you to ask follow-up questions or modify your preferences.

## How It Works

1. **Select Dietary Preferences:** Choose your dietary preferences from a list of options, including Vegan, Vegetarian, Gluten-Free, Low-Carb, and more.

2. **Enter Your Requests:** Type in any specific requests or goals you have for your meal, such as "I need a high-protein dinner with chicken."

3. **Receive Recipe Suggestions:** The AI will process your input and generate personalized recipe suggestions, complete with ingredients and cooking instructions.

## How to Use

1. **Visit the Live Application:** Head over to [https://dish-decoder.streamlit.app/](https://dish-decoder.streamlit.app/) to start using Dish Decoder.

2. **Interact with the AI:** Begin by selecting your dietary preferences and entering your meal planning requests in the chat interface.

3. **Explore Recipes:** Read through the AI's recipe suggestions, complete with detailed cooking instructions.

## Getting Started with Development

To run this application locally or contribute to its development:

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Google Generative AI Python Client (`google-generativeai`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/r-zeeshan/dish-decoder.git
   cd dish-decoder
   ```

2. Install the required Python packages:
    ``` bash
    pip install -r requirements.txt
    ```

3. Set up your environment:
    * Create a secrets.toml file in the .streamlit directory with your Gemini API key.
    ```bash
    [default]
    GEMINI_API_KEY = "your_gemini_api_key_here"
    ```

4. Run the application:
    ```bash
    streamlit run app.py
    ```

## Contributions
Contributions are welcome! Feel free to fork the repository, make enhancements, and submit a pull request. Please ensure your code follows best practices and is well-documented.


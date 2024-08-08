import requests

class SpoonacularClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.spoonacular.com"

    def get_recipes_by_ingredients(self, ingredients, number=5):
        """Fetch recipes based on a list of ingredients."""
        endpoint = f"{self.base_url}/recipes/findByIngredients"
        params = {
            "apiKey": self.api_key,
            "ingredients": ",".join(ingredients),
            "number": number,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def get_recipes_by_diet(self, diet, intolerances=None, number=5):
        """Fetch recipes based on dietary preferences and intolerances."""
        endpoint = f"{self.base_url}/recipes/complexSearch"
        params = {
            "apiKey": self.api_key,
            "diet": diet,
            "intolerances": ",".join(intolerances) if intolerances else None,
            "number": number,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json().get('results', [])
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def get_nutritional_info(self, recipe_id):
        """Fetch detailed nutritional information for a recipe."""
        endpoint = f"{self.base_url}/recipes/{recipe_id}/nutritionWidget.json"
        params = {
            "apiKey": self.api_key,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
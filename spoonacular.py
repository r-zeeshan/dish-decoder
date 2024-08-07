import requests

class SpoonacularClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.spoonacular.com"

    def get_recipes_by_ingredients(self, ingredients, number=5):
        endpoint = f"{self.base_url}/recipes/findByIngredients"
        params = {
            "apiKey": self.api_key,
            "ingredients": ",".join(ingredients),
            "number": number,
        }
        response = requests.get(endpoint, params=params)
        return response.json()

    def get_recipe_information(self, recipe_id):
        endpoint = f"{self.base_url}/recipes/{recipe_id}/information"
        params = {
            "apiKey": self.api_key,
        }
        response = requests.get(endpoint, params=params)
        return response.json()


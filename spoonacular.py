import requests

class SpoonacularClient:
    """
    A client for interacting with the Spoonacular API, providing methods to search for recipes,
    get nutritional information, generate meal plans, and more.
    """
    
    def __init__(self, api_key):
        """
        Initialize the SpoonacularClient with the provided API key.
        
        :param api_key: The API key for accessing Spoonacular services.
        """
        self.api_key = api_key
        self.base_url = "https://api.spoonacular.com"

    def get_recipes_by_ingredients(self, ingredients, number=5):
        """
        Fetch recipes based on a list of ingredients.
        
        :param ingredients: A list of ingredient names to search for.
        :param number: The number of recipes to return (default is 5).
        :return: A list of recipes that match the provided ingredients.
        """
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
        """
        Fetch recipes based on dietary preferences and intolerances.
        
        :param diet: The type of diet (e.g., "vegetarian", "vegan").
        :param intolerances: A list of ingredient intolerances (optional).
        :param number: The number of recipes to return (default is 5).
        :return: A list of recipes that match the provided diet and intolerances.
        """
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
        """
        Fetch detailed nutritional information for a recipe.
        
        :param recipe_id: The ID of the recipe for which to get nutritional information.
        :return: A dictionary with detailed nutritional information for the recipe.
        """
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

    def generate_meal_plan(self, target_calories, diet=None, time_frame="day"):
        """
        Generate a meal plan based on calorie targets and dietary preferences.
        
        :param target_calories: The target number of calories for the meal plan.
        :param diet: The type of diet (e.g., "vegetarian", "vegan") (optional).
        :param time_frame: The time frame for the meal plan ("day", "week") (default is "day").
        :return: A meal plan with recipes to meet the calorie target and dietary preferences.
        """
        endpoint = f"{self.base_url}/mealplanner/generate"
        params = {
            "apiKey": self.api_key,
            "targetCalories": target_calories,
            "diet": diet,
            "timeFrame": time_frame,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_recipe_instructions(self, recipe_id):
        """
        Fetch step-by-step cooking instructions for a recipe.
        
        :param recipe_id: The ID of the recipe for which to get cooking instructions.
        :return: A list of steps with detailed instructions for preparing the recipe.
        """
        endpoint = f"{self.base_url}/recipes/{recipe_id}/analyzedInstructions"
        params = {
            "apiKey": self.api_key,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            instructions = response.json()
            return instructions[0]['steps'] if instructions else []
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def search_recipes_by_nutrients(self, min_protein=0, max_carbs=100, max_calories=2000, number=5):
        """
        Search recipes based on nutritional content.
        
        :param min_protein: The minimum amount of protein (in grams) (default is 0).
        :param max_carbs: The maximum amount of carbohydrates (in grams) (default is 100).
        :param max_calories: The maximum number of calories (default is 2000).
        :param number: The number of recipes to return (default is 5).
        :return: A list of recipes that match the nutritional criteria.
        """
        endpoint = f"{self.base_url}/recipes/findByNutrients"
        params = {
            "apiKey": self.api_key,
            "minProtein": min_protein,
            "maxCarbs": max_carbs,
            "maxCalories": max_calories,
            "number": number,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def get_ingredient_substitutes(self, ingredient_name):
        """
        Get possible substitutes for an ingredient.
        
        :param ingredient_name: The name of the ingredient to find substitutes for.
        :return: A list of substitute ingredient names.
        """
        endpoint = f"{self.base_url}/food/ingredients/substitutes"
        params = {
            "apiKey": self.api_key,
            "ingredientName": ingredient_name,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json().get('substitutes', [])
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def convert_ingredient_amount(self, ingredient_name, source_amount, source_unit, target_unit):
        """
        Convert ingredient amounts between different units.
        
        :param ingredient_name: The name of the ingredient to convert.
        :param source_amount: The amount of the ingredient to convert.
        :param source_unit: The current unit of the ingredient amount.
        :param target_unit: The target unit to convert the ingredient amount to.
        :return: The converted amount in the target unit, or None if an error occurs.
        """
        endpoint = f"{self.base_url}/recipes/convert"
        params = {
            "apiKey": self.api_key,
            "ingredientName": ingredient_name,
            "sourceAmount": source_amount,
            "sourceUnit": source_unit,
            "targetUnit": target_unit,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json().get('targetAmount', None)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_similar_recipes(self, recipe_id, number=5):
        """
        Fetch similar recipes to a given recipe.
        
        :param recipe_id: The ID of the recipe to find similar recipes for.
        :param number: The number of similar recipes to return (default is 5).
        :return: A list of recipes similar to the provided recipe.
        """
        endpoint = f"{self.base_url}/recipes/{recipe_id}/similar"
        params = {
            "apiKey": self.api_key,
            "number": number,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

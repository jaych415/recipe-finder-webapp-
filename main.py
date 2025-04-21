import requests

# Replace with your real API key
API_KEY = "5f16e3cbbd254a30ac46edde0bba1e29"
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def find_recipes(ingredients):
    params = {
        "apiKey": API_KEY,
        "ingredients": ingredients,
        "number": 5,  # number of recipes to return
        "ranking": 1
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        recipes = response.json()
        for i, recipe in enumerate(recipes):
            print(f"\nRecipe {i+1}: {recipe['title']}")
            print(f"Used Ingredients: {[item['name'] for item in recipe['usedIngredients']]}")
            print(f"Missing Ingredients: {[item['name'] for item in recipe['missedIngredients']]}")
            print(f"Recipe Link: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}")
    else:
        print("Error fetching recipes:", response.status_code)

if __name__ == "__main__":
    user_input = input("Enter ingredients (comma-separated): ")
    find_recipes(user_input)

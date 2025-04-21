import streamlit as st
import requests

# Replace with your real API key
API_KEY = "5f16e3cbbd254a30ac46edde0bba1e29"
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"

st.title("🥗 Recipe Finder Bot")
st.write("Enter ingredients you have, and I'll suggest some recipes!")

ingredients = st.text_input("Enter ingredients (comma-separated):", "tomato, cheese, bread")

if st.button("Find Recipes"):
    with st.spinner("Searching..."):
        params = {
            "apiKey": API_KEY,
            "ingredients": ingredients,
            "number": 5,
            "ranking": 1
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            recipes = response.json()
            for recipe in recipes:
                st.subheader(recipe['title'])
                st.image(recipe['image'], width=300)
                st.markdown(f"🔗 [View Recipe](https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']})")
                used = ", ".join([i['name'] for i in recipe['usedIngredients']])
                missed = ", ".join([i['name'] for i in recipe['missedIngredients']])
                st.write(f"✅ Used Ingredients: {used}")
                st.write(f"❌ Missing Ingredients: {missed}")
                st.write("---")
        else:
            st.error("Could not fetch recipes. Check your API key or try again later.")

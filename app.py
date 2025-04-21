import streamlit as st
import requests
import pyttsx3

# Directly use API key (not recommended for public repos)
API_KEY = "5f16e3cbbd254a30ac46edde0bba1e29"

BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients"
INFO_URL = "https://api.spoonacular.com/recipes/{}"  # For detailed recipe info

st.set_page_config(page_title="🍽️ Recipe Finder", layout="centered")
st.title("🥗 Recipe Finder")
st.write("Enter ingredients you have, and I'll suggest some recipes!")

# Input section
ingredients = st.text_input("Enter ingredients (comma-separated):", "tomato, cheese, bread")
diet = st.selectbox("Choose a diet (optional):", ["", "vegetarian", "vegan", "keto", "gluten free"])
count = st.slider("Number of recipes", 1, 10, 5)

if st.button("Find Recipes"):
    with st.spinner("Searching for recipes..."):
        params = {
            "apiKey": API_KEY,
            "ingredients": ingredients,
            "number": count,
            "ranking": 1
        }
        if diet:
            params["diet"] = diet

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            recipes = response.json()
            if not recipes:
                st.warning("No recipes found. Try different ingredients.")
            for recipe in recipes:
                st.subheader(recipe['title'])
                st.image(recipe['image'], width=300)
                recipe_url = f"https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}"
                st.markdown(f"🔗 [View Recipe]({recipe_url})")

                used = ", ".join([i['name'] for i in recipe['usedIngredients']])
                missed = ", ".join([i['name'] for i in recipe['missedIngredients']])
                st.write(f"✅ Used Ingredients: {used}")
                st.write(f"❌ Missing Ingredients: {missed}")

                # Text-to-speech button
                if st.button(f"🔊 Read Recipe Title - {recipe['id']}"):
                    engine = pyttsx3.init()
                    engine.say(recipe['title'])
                    engine.runAndWait()

                # Save to favorites
                if st.button(f"⭐ Save to favorites - {recipe['id']}"):
                    with open("favorites.txt", "a") as f:
                        f.write(f"{recipe['title']} - {recipe_url}\n")
                    st.success("Saved to favorites!")

                # Extra info fetch (optional bonus)
                more_info = st.expander("🔍 See more details")
                with more_info:
                    info_response = requests.get(f"https://api.spoonacular.com/recipes/{recipe['id']}/information", params={"apiKey": API_KEY})
                    if info_response.status_code == 200:
                        info = info_response.json()
                        st.write(f"⏱️ Ready in {info['readyInMinutes']} minutes")
                        st.write(f"🔥 {info['calories'] if 'calories' in info else 'Calories not listed'}")
                        if info.get("summary"):
                            st.markdown(info["summary"], unsafe_allow_html=True)
                    else:
                        st.write("No additional info available.")
                st.write("---")
        else:
            st.error("Failed to fetch recipes. Check your API key or try again later.")

# Chatbot style interaction (Streamlit 1.30+)
message = st.chat_input("Ask for a recipe using natural language...")
if message:
    st.write("🔍 You said:", message)
    st.write("💬 Natural language processing not set up yet, but you can try the ingredient input above! 😊")


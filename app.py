

import streamlit as st
import pickle
import pandas as pd

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    books = pickle.load(open("books.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return books, similarity

books, similarity = load_data()

st.title("📚 Book Recommendation System")
st.write("Start typing a book name to see matching results…")

book_titles = books['title'].tolist()

# ---------- CUSTOM AUTOCOMPLETE ----------
user_input = st.text_input("Search Book Name")

# Show suggestions while typing
suggestions = []
if user_input:
    user_input_lower = user_input.lower()
    suggestions = [t for t in book_titles if user_input_lower in t.lower()][:10]  # top 10 matches

# Display suggestions + unique keys
selected_book = None
if suggestions:
    st.write("### 🔍 Matching Books:")
    for idx, title in enumerate(suggestions):
        if st.button(title, key=f"suggestion_{idx}"):  # unique key
            selected_book = title

# If the user clicked a suggestion, show recommendations
if selected_book:
    st.success(f"Showing books similar to **{selected_book}**")

    index = books[books['title'] == selected_book].index[0]
    distances = similarity[index]
    book_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:11]

    st.write("### 📖 Recommended Books:")

    for i in book_list:
        row = books.iloc[i[0]]
        st.markdown(f"""
        **📘 {row['title']}**  
        👤 *{row['authors']}*  
        🏢 {row['publisher']}  
        🌐 Language: {row['language_code']}
        ---
        """)


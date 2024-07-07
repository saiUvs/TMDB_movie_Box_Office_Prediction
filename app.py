
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import joblib

try:
    model = joblib.load('model.joblib')
except FileNotFoundError:
    print("Model file not found. Please check the file path.")
except Exception as e:
    print(f"Error loading model: {e}")
else:
    print("Model loaded successfully.")

with open( "/work/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.title("TMDB Revenue Prediction")

st.header("Input Features")
title = st.text_input("Movie Title")
budget = st.number_input("Budget", min_value=0.0, value=0.0, step=1000000.0)
popularity = st.number_input("Popularity", min_value=0.0, value=0.0, step=0.1)
runtime = st.number_input("Runtime", min_value=0.0, value=0.0, step=1.0)
languages = ['Afrikaans', 'Bahasa indonesia', 'Bahasa melayu', 'Bosanski', 'Català', 'Cymraeg', 'Dansk', 'Deutsch', 'Eesti', 'English', 'Español', 'Esperanto', 'Français', 'Fulfulde', 'Gaeilge', 'Hrvatski', 'Italiano', 'Kiswahili', 'Latin', 'Lietuvių', 'Magyar', 'Nederlands', 'No Language', 'Norsk', 'Polski', 'Português', 'Pусский', 'Română', 'Slovenčina', 'Somali', 'Srpski', 'Tiếng Việt', 'Türkçe', 'euskera', 'isiZulu', 'shqip', 'suomi', 'svenska', 'Íslenska', 'Český', 'ελληνικά', 'Український', 'български език', 'עִבְרִית', 'اردو', 'العربية', 'فارسی', 'پښتو', 'हिन्दी', 'বাংলা', 'ਪੰਜਾਬੀ', 'தமிழ்', 'සිංහල', 'ภาษาไทย', 'ქართული', '广州话 / 廣州話', '日本語', '普通话', '한국어/조선말']
genre =  ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western']
countrys =['Aruba', 'Australia', 'Austria', 'Bahamas', 'Belgium', 'Botswana', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'China', 'Colombia', 'Cyprus', 'Czech Republic', 'Denmark', 'Dominican Republic', 'Finland', 'France', 'Germany', 'Greece', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Kenya', 'Kuwait', 'Lebanon', 'Libyan Arab Jamahiriya', 'Luxembourg', 'Malaysia', 'Malta', 'Mexico', 'Montenegro', 'Morocco', 'Netherlands', 'New Zealand', 'Norway', 'Peru', 'Poland', 'Portugal', 'Puerto Rico', 'Romania', 'Russia', 'Saudi Arabia', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Soviet Union', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Turkey', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Venezuela', 'Zimbabwe']
selected_genres = st.multiselect("Genres", genre)
selected_languages = st.multiselect("Languages", languages)
selected_countries= st.multiselect("Movie Countries", countrys)
overview = st.text_input("Movie Overview")
crew_info = st.text_input("Crew Information")
cast_info = st.text_input("Cast Information")

status_options = {
        3: 'Released',
        2: 'Post Production',
        0: 'In Production',
        1: 'Planned'
    }
status_label = st.selectbox("Status", list(status_options.values()))
status = list(status_options.keys())[list(status_options.values()).index(status_label)]

year = st.number_input("Year", 2000)
month = st.number_input("Month", 1, 12)
day = st.number_input("Day", 1, 31)

# Function to one-hot encode selected genres
def encode_genres(selected_genres, genre):
    encoded = [1 if gen in selected_genres else 0 for gen in genre]
    return encoded

# Function to one-hot encode selected languages
def encode_languages(selected_languages, languages):
    encoded = [1 if language in selected_languages else 0 for language in languages]
    return encoded

def encode_countries(selected_countries, countrys):
    encoded = [1 if country in selected_countries else 0 for country in countrys]
    return encoded

# Preprocess the input features as needed by your model
genres_encoded = encode_genres(selected_genres, genre)
languages_encoded = encode_languages(selected_languages, languages)
countrys_encoded = encode_countries(selected_countries, countrys)

# Combine all features

features = np.array([[budget, popularity, runtime, status] + languages_encoded + genres_encoded + countrys_encoded + [year, month, day]])

# Predict button
if st.button("Predict Revenue"):
    prediction = model.predict(features)
    st.write(f"Predicted Revenue: ${prediction[0]:,.2f}")



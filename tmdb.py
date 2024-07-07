
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import joblib
import sklearn
from sklearn import *
def main():
    model = joblib.load('model.joblib')
    st.set_page_config(page_title='Movie App', page_icon='🎬')
    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    st.sidebar.title("Navigation")
    pages = ["Home", "About", "1-Phase 📥", "2-Phase 🧹 🔍", "3-Phase 🏗️  🎓  🧪 ",
    "4-Phase 🚀 "]
    selection = st.sidebar.radio("Go to", pages)
    with open("files/create_dataset.html", "r", encoding="utf-8") as f:
       Data_html = f.read()
    with open("files/cleaning.html", "r", encoding="utf-8") as f:
       clean_html = f.read()
    with open("files/create_dataset.html", "r", encoding="utf-8") as f:
       Data_html = f.read()
    if selection == "Home":
        home_page()
    elif selection == "About":
        About()
    elif selection == "1-Phase 📥":
        phase1(Data_html)
    elif selection == "2-Phase 🧹 🔍":
        phase2(clean_html)
    elif selection == "3-Phase 🏗️  🎓  🧪 ":
        phase3()
    elif selection == "4-Phase 🚀 ":
        phase4(model)

def home_page():
    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    st.title("🎥 Box Office Prediction Project 🍿")
    st.markdown("""
    Welcome to the **TMDB Movie Data Analysis Project**! This interactive app allows you to explore and analyze the fascinating world of movies using data from [The Movie Database (TMDB)](https://www.themoviedb.org/). Let's dive into the world of movies, data, and insights! 🌟

    ## 🚀 Features
    - **Interactive Visualizations**: Dive deep into the data with interactive charts and graphs.
    - **Customizable Filters**: Filter movies by genre, release year, language, and more.
    - **Detailed Insights**: Gain detailed insights into individual movies, including cast, crew, and production companies.

    ## 🛠️ How to Use
    - **Navigation**: Use the sidebar to navigate through different sections of the app.

    ## 🌟 Highlights
    - **You get the revenue prediction for your move 🎬.**

    ## 🎉 Let's Get Started!
    Use the sidebar to explore the different sections of this app. We hope you enjoy this journey through the Box Office Prediction of movies as much as we enjoyed creating it! 🍿

    ---
    Happy Exploring! 🎉
    """)

def About():
    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    st.subheader("📖 About This Project")

    st.write("""
    The **TMDB Movie Prediction Project** is a data science and machine learning task involving the use of the TMDB (The Movie Database) dataset to predict certain attributes of movies. TMDB is a popular, community-built movie and TV database that provides a variety of movie-related data, such as movie details, ratings, casts, crews, and more.

    In this project, the primary goal is to predict the **revenue** a movie will generate based on various features like:

    - 💰 Budget
    - 🎥 Production companies
    - 🌍 Movie countries
    - ⏱️ Runtime
    - 📅 Release date
    - 📊 Status
    - 🎭 Genre
    - 🎬 Cast and crew details

    By leveraging these features, we aim to build a robust model that can accurately forecast the financial success of a movie.
    """)

def phase1(Data_html):
    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    st.title("Welcome to Phase 1 ")
    st.header("Data Collection")
    st.write("""
    This **Box Office Prediction Project** will utilize the TMDB dataset to predict the revenue of a movie. 

    🔍 **Data Fetching:**
    We'll fetch data from the TMDB dataset using the API.""")

    st.markdown("Visit [create_dataset.ipynb](https://github.com/Springboard-Internship-2024/TMDB-Box-Office-Prediction_May_2024/blob/U-V-Sai-Praneeth/create_dataset.ipynb) for more information.")

    components.html(Data_html, height=1000, scrolling=True)

def phase2(clean_html):

    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    st.title("🚀 Welcome to Phase 2: The Adventure Continues! 🎉")
    st.header("🧼 Data Cleaning,   🎨 Visualization, and 📊 Normalization")

    st.write("""
    **Data cleaning** is a crucial step in preparing the TMDB (The Movie Database) dataset for analysis or machine learning tasks. The TMDB dataset typically contains various attributes about movies, such as:
    - 🎬 Titles
    - 💰 Budgets
    - 📈 Revenue
    - 🎭 Genres
    - 🎥 Cast
    - 🎬 Crew
    - And much more!

    In this phase, we'll roll up our sleeves and get to work on:

    1. **Data Cleaning** 🧹: Removing the junk and filling in the gaps to ensure our data is spotless.
    2. **Data Visualization** 🎨: Creating eye-catching charts and graphs to uncover hidden patterns.
    3. **Normalization** 📊: Preparing our train data to ensure all features are on a level playing field.

    Get ready for a thrilling journey through the world of data as we clean, visualize, and normalize our way to insightful analysis and powerful predictions!
    """)
    st.subheader("Plots --> EDA")

    bar_chart_img = Image.open('images/newplot (2).png')
    histogram_img = Image.open('images/newplot (1).png')
    scatterplot_img = Image.open('images/newplot.png')
    correlation_matrix_img = Image.open('images/newplot (3).png')

    # Display each plot using st.image
    st.subheader("Plots --> EDA")

    st.markdown('## 📊 Number of Movies by Genre')
    st.image(bar_chart_img, use_column_width=True)

    st.markdown('## 💰 Distribution of Budget for TMDB Movies')
    st.image(histogram_img, use_column_width=True)

    st.markdown('## 📈 Scatter Plot of Revenue vs Budget')
    st.image(scatterplot_img, use_column_width=True)

    st.markdown('## 🔍 Correlation Matrix: Revenue vs Budget')
    st.image(correlation_matrix_img, use_column_width=True)


    st.markdown("Visit [Phase2.ipynb](https://colab.research.google.com/drive/1XFMMvg6RdCffijJa08NF6PAduQ1vIK_m?usp=sharing) for more information.")
    components.html(clean_html, height=1000, scrolling=True)

def phase3():
    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    st.title("🏁 Welcome to Phase 3: The Final Countdown! 🚀")
    st.header("🤖 Training and Testing the Model 📊")

    st.write("""
    Welcome to the most thrilling part of our journey! In **Phase 3**, we'll dive into:

    1. **Training the Model** 🏋️‍♂️:
    - Using our clean and normalized dataset, we’ll train powerful machine learning models.
    - Fine-tuning hyperparameters to squeeze out the best performance.

    2. **Testing the Model** 🧪:
    - Evaluating our models on unseen data to ensure they can generalize well.
    - Comparing different models to find the champion that will predict movie revenues like a pro.

    Get ready to see the magic of machine learning in action as we transform our data into a prediction powerhouse!
    """)
    st.markdown("Visit [Phase3.ipynb](https://github.com/Springboard-Internship-2024/TMDB-Box-Office-Prediction_May_2024/blob/U-V-Sai-Praneeth/infosys_W5_Milestone3.ipynb) for more information.")
    

def phase4(model):
    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.metrics import mean_squared_error
    import joblib
    
    st.title("Welcome to Phase 4 🚀 ")

    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    st.header("🎥 TMDB Revenue Prediction")

    st.subheader("Input Features")
    title = st.text_input("Movie Title")
    budget = st.number_input("💰 Budget", min_value=0.0, value=0.0, step=1000000.0)
    popularity = st.number_input("Popularity", min_value=0.0, value=0.0, step=0.1)
    runtime = st.number_input("⏱️ Runtime", min_value=0.0, value=0.0, step=1.0)
    languages = ['Afrikaans', 'Bahasa indonesia', 'Bahasa melayu', 'Bosanski', 'Català', 'Cymraeg', 'Dansk', 'Deutsch', 'Eesti', 'English', 'Español', 'Esperanto', 'Français', 'Fulfulde', 'Gaeilge', 'Hrvatski', 'Italiano', 'Kiswahili', 'Latin', 'Lietuvių', 'Magyar', 'Nederlands', 'No Language', 'Norsk', 'Polski', 'Português', 'Pусский', 'Română', 'Slovenčina', 'Somali', 'Srpski', 'Tiếng Việt', 'Türkçe', 'euskera', 'isiZulu', 'shqip', 'suomi', 'svenska', 'Íslenska', 'Český', 'ελληνικά', 'Український', 'български език', 'עִבְרִית', 'اردو', 'العربية', 'فارسی', 'پښتو', 'हिन्दी', 'বাংলা', 'ਪੰਜਾਬੀ', 'தமிழ்', 'සිංහල', 'ภาษาไทย', 'ქართული', '广州话 / 廣州話', '日本語', '普通话', '한국어/조선말']
    genre =  ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western']
    countrys =['Aruba', 'Australia', 'Austria', 'Bahamas', 'Belgium', 'Botswana', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'China', 'Colombia', 'Cyprus', 'Czech Republic', 'Denmark', 'Dominican Republic', 'Finland', 'France', 'Germany', 'Greece', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Kenya', 'Kuwait', 'Lebanon', 'Libyan Arab Jamahiriya', 'Luxembourg', 'Malaysia', 'Malta', 'Mexico', 'Montenegro', 'Morocco', 'Netherlands', 'New Zealand', 'Norway', 'Peru', 'Poland', 'Portugal', 'Puerto Rico', 'Romania', 'Russia', 'Saudi Arabia', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Soviet Union', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Turkey', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Venezuela', 'Zimbabwe']
    selected_genres = st.multiselect(" 🎭 Genres", genre)
    selected_languages = st.multiselect("💬 Languages", languages)
    selected_countries= st.multiselect("🌍 Movie Countries", countrys)
    overview = st.text_input("Movie Overview")
    crew_info = st.text_input("🎬 Crew Information")
    cast_info = st.text_input("🎬 Cast Information")

    status_options = {
            3: 'Released',
            2: 'Post Production',
            0: 'In Production',
            1: 'Planned'
        }
    status_label = st.selectbox(" 📊 Status", list(status_options.values()))
    status = list(status_options.keys())[list(status_options.values()).index(status_label)]

    year = st.number_input("📅 Year", 2000)
    month = st.number_input("📅 Month", 1, 12)
    day = st.number_input("📅 Day", 1, 31)

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
if __name__ == "__main__":
    main()

# e-Book-Recommendation-System
A machine learning–based Book Recommendation System built using Python. This project uses cosine similarity to recommend books based on user-selected input. It involves data cleaning, exploratory data analysis (EDA), feature engineering, and building a similarity-based recommendation engine.

### Project Overview
The goal of this project is to build a recommendation system that suggests books similar to a selected book.
The model analyzes the features of each book and calculates similarity scores between them using sklearn’s cosine similarity.

### Tech Stack
Python
Pandas, NumPy
Matplotlib, Seaborn
Scikit-Learn
Jupyter Notebook

### Approach
- Data Preprocessing
Loaded dataset using pandas
Renamed inconsistent columns
Dropped unnecessary fields such as "Unnamed: 12"
Cleaned missing data
Extracted relevant book features

- Feature Engineering
Converted categorical text data into numerical feature vectors
Prepared a matrix suitable for similarity calculation

- Cosine Similarity Model
Compute all similarity scores
Sort them
Return the top 10 most similar books


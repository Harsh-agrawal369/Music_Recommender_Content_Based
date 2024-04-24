# Music Recommender System

## Overview

This project implements a content-based music recommender system specifically designed for Hindi songs. The system utilizes natural language processing techniques to analyze song metadata and generate personalized recommendations based on user preferences.

## Techniques Used

1. **Data Preprocessing:**
   - Loading the dataset using pandas and performing data cleaning operations such as handling missing values and removing duplicates.
   - Processing text attributes like singer, genre, album/movie, and user rating to remove unnecessary characters and spaces.

2. **Feature Engineering:**
   - Creating a new attribute 'tags' by combining relevant song attributes to represent features used for similarity calculation.

3. **Text Vectorization:**
   - Converting textual data into numerical vectors using CountVectorizer from scikit-learn.

4. **Similarity Calculation:**
   - Computing cosine similarity between song vectors to measure the similarity between songs based on their features.

5. **Recommendation Generation:**
   - Selecting the top 5 most similar songs to a given query song based on cosine similarity and presenting them as recommendations.

## Deployment

- The project can be deployed using Streamlit for creating a user-friendly interface.
- A pickle file containing preprocessed data and similarity matrix is generated and used during deployment.

## Instructions for Deployment

1. Clone the repository containing the code for the music recommender system.
2. Install all necessary dependencies, including pandas, numpy, scikit-learn, and Streamlit.
3. Run the Streamlit app script to start the local server.
4. Access the application through the provided URL to interact with the music recommender system.

## Conclusion

This content-based music recommender system enhances users' music discovery experience by providing personalized song recommendations based on their preferences. By leveraging machine learning and natural language processing techniques, the system offers tailored suggestions that align with users' tastes.

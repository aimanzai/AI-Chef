# AI-Chef (Recipe Recommendation System)

## Overview
This project is a group assignment that implements an AI-based recipe recommendation system using ingredient similarity.
The system suggests recipes based on user-provided ingredients by applying TF-IDF vectorization and cosine similarity to match user input with recipes in the dataset.

It serves as an introduction to practical applications of machine learning, natural language processing, and information retrieval within a simple command-line interface.

## Features
1. Recommend recipes based on user-specified ingredients.
2. Similarity scoring using TF-IDF and cosine similarity.
3. View full recipe details, including:
  * Recipe name
  * List of ingredients
  * Step-by-step directions
4. Cleans and preprocesses missing values automatically.

## Dataset
This project uses the “Better Recipes for a Better Life” dataset from Kaggle, created by thedevastator.

Dataset link: [Recipes.csv](https://www.kaggle.com/datasets/thedevastator/better-recipes-for-a-better-life)

For this system, only the columns recipe_name, ingredients, and directions are required. Missing values are automatically filled to ensure smooth text processing. 
Please ensure you download the dataset from the link above and place recipes.csv in the same directory as main.py.

## My Contribution
For this group assignment, my responsibilities focused on the core model development, specifically:
* Implementing the recipe recommendation logic using TF-IDF vectorization and cosine similarity.
* Developing the key functions that compute similarity scores and generate recommended recipe results.

## Output
After running the program, the system produces two main types of output:

1. Recommended Recipes Table
Based on the number of recommendations requested and the ingredients provided by the user, the system displays a table containing:
  * Recipe Title
  * Recipe Similarity (%)
2. Full Recipe Details
When the user selects one of the recommended recipes, the system displays:
  * Recipe Name
  * Numbered list of ingredients
  * Numbered step-by-step directions
<p align="center">
<img width="1303" height="749" alt="image" src="https://github.com/user-attachments/assets/3c635a77-a4de-4475-8336-7c5ad1c49988"/>
</p>
This output helps users clearly view both summary recommendations and detailed cooking instructions.

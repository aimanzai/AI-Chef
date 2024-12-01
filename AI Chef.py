import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the resipes dataset
recipes_data = pd.read_csv('recipes.csv')

# Preprocess by fill missing values in the 'ingredients' column
recipes_data['ingredients'] = recipes_data['ingredients'].fillna('')
recipes_data['directions'] = recipes_data['directions'].fillna('')

# Vectorize the ingredients using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')  # Remove common words like 'and', 'the', etc.
ingredient_vectors = vectorizer.fit_transform(recipes_data['ingredients'])

# Recommend recipes based on input ingredients
def recommend_recipes(user_ingredients, num):
    # Transform the user input into the same vector space
    user_vector = vectorizer.transform([user_ingredients])

    # Compute cosine similarity between user input and all recipes
    similarity_scores = cosine_similarity(user_vector, ingredient_vectors).flatten()

    # Get the indices of the user input and find similar recipes to it
    top_indices = similarity_scores.argsort()[-num:][::-1]

    # Fetch the recommended recipes with the names and similarity scores
    top_recipes = recipes_data.iloc[top_indices][['recipe_name', 'ingredients']].copy()
    top_recipes['similarity_score'] = (similarity_scores[top_indices] * 100).round(2)

    # To change the name of the columns(recipe name and similiarity)
    top_recipes.rename(columns={'recipe_name': 'Recipe Title'}, inplace=True)
    top_recipes.rename(columns={'similarity_score': "Recipe Similarity (%)"}, inplace=True)

    return top_recipes, top_indices

# Display full recipe
def full_recipe(recipe_index):
    #Assign value of recipe dataset based on the user input of the recommended recipes's index
    recipe = recipes_data.iloc[recipe_index]

    print("Here's the full recipes:\n")
    print("Recipe Name::" + recipe['recipe_name']) #To show the specific name based on the index that user choose

    #Split all the data in the ingredient column  in dataset by '.' to make sure after the '.' it will create new line
    ingredients = recipe['ingredients'].split(',')
    new_ingredients = ""
    print("\nIngredients:")
    print("*" * 12)
    #To put a number before showing the ingredients
    for i, ingredient in enumerate(ingredients, start = 1):
        new_ingredients += f"{i}. {ingredient.strip().capitalize()}\n"
    print(new_ingredients)

    # Split all the data in the directions column in dataset by ',' to make sure after the ',' it will create new line
    directions = recipe['directions'].split('.')
    new_directions = ""
    print("Directions:")
    print("*" * 12)
    # To put a number before showing the directions
    for i, directions in enumerate(directions, start=1):  # Pass `ingredients` as the iterable
        new_directions += f"{i}. {directions.strip().capitalize()}\n"
    print(new_directions)

# Main program
def main():
    print("*" * 36)
    print('*Welcome to AI-Recommended recipes:*')
    print("*" * 36)
    top_menu_num = int(input('\nEnter how many recipes that you want to be recommended: ')) # To get how many recipes that user recommneded
    user_input = input('Enter the ingredients that you want to use in your cooking: ') # To ask the user ingredients that he want to choose

    # Get recommendations based on the num of reciped that user want to be recommended as well as user input for ingredients
    recommended_recipes, top_indices = recommend_recipes(user_input, top_menu_num)

    # Display the results
    print("\n")
    print("*" * 52)
    print("*Top Recommended Recipes Based on Your Ingredients:*")
    print("*" * 52)
    print(recommended_recipes[['Recipe Title', "Recipe Similarity (%)"]])

    get_recipes = int(input("\nEnter the number (1-{}) based on the table to see the full recipes: ".format(top_menu_num)))

    # To convert the user input to the index in the dataset, (for example index of recipes display might be '771' but its new index in the table
    # is '1' so from that, tha program will take value of '1' and convert it to the same index
    if 1 <= get_recipes <= top_menu_num:
        recipe_index = top_indices[get_recipes - 1]
        full_recipe(recipe_index) #it will display all the full recipe, once it foung the index
    else:
        print("Invalid number entered!")

main()
"""
Module for cleaaning the CSV file containing the data from the elections.
"""
import pandas

def generation_cleaning(generation, data):
    """
    Given the data from the elections, return the data for the specified generation.

    Parameters
        generation (str): Generation to clean.
        data (pandas.DataFrame): DataFrame with the data.

    Returns
        cleaned_generation (pandas.DataFrame): DataFrame with the cleaned data.
    """
    # Mantain only the rows with the votes of the given generation.
    generation_data = data[data['generation'] == generation]

    # Only mantain the columns for the candidates for the given generation.
    if generation == 2021:
        generation_data = generation_data[['g21_option_1', 'g21_option_2', 'g21_option_3', 'g21_option_4']]
    elif generation == 2022:
        generation_data = generation_data[['g22_option_1', 'g22_option_2', 'g22_option_3', 'g22_option_4', 'g22_option_5']]
    elif generation == 2023:
        generation_data = generation_data[['g23_option_1', 'g23_option_2', 'g23_option_3', 'g23_option_4', 'g23_option_5', 'g23_option_6', 'g23_option_7']]
    elif generation == 2024:
        generation_data = generation_data[['g24_option_1', 'g24_option_2', 'g24_option_3', 'g24_option_4', 'g24_option_5', 'g24_option_6', 'g24_option_7', 'g24_option_8', 'g24_option_9', 'g24_option_10', 'g24_option_11', 'g24_option_12', 'g24_option_13']]
    
    return generation_data

def clean_data(file_path):
    """
    Clean the data from the CSV file containing the data from the elections and save it to a new CSV file for each generation.

    Parameters
        file_path (str): Path to the CSV file.
    """
    data = pandas.read_csv(file_path)

    # Drop the columns with the timestamp, username, RUT, and email.
    columns_to_drop = ['Timestamp', 'Username', 'Indica tu RUT ej: 21570316-9', 'Indica tu correo institucional UC']
    data = data.drop(columns=columns_to_drop)
    
    # Save 4 different CSV files, one for each generation.

    # First, rename the columns to make it easier to work with them.
    data.columns = ['generation', 'g21_option_1', 'g21_option_2', 'g21_option_3', 'g21_option_4', 'g22_option_1', 'g22_option_2', 'g22_option_3', 'g22_option_4', 'g22_option_5', 'g23_option_1', 'g23_option_2', 'g23_option_3', 'g23_option_4', 'g23_option_5', 'g23_option_6', 'g23_option_7', 'g24_option_1', 'g24_option_2', 'g24_option_3', 'g24_option_4', 'g24_option_5', 'g24_option_6', 'g24_option_7', 'g24_option_8', 'g24_option_9', 'g24_option_10', 'g24_option_11', 'g24_option_12', 'g24_option_13']

    # Second, clean the data for each generation and save it to a CSV file.
    generations = [2021, 2022, 2023, 2024]
    for generation in generations:
        cleaned_generation = generation_cleaning(generation, data)
        cleaned_generation.to_csv(f'cleaned_data_{generation}.csv', index=False)

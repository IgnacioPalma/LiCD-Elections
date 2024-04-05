"""
Module for the functions related to the ranking system for the elections.
"""
import pandas as pd

def count_ranked_votes(file_name):
    """
    Counts the number of votes for each option in a ranked voting system.
    
    Parameters:
        file_name (str): The name of the CSV file containing the ranked votes.
        
    Returns:
        dict: A dictionary where the keys are the options and the values are the vote counts.
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_name)
    
    # Get the number of options
    num_options = len(df.columns)
    
    # Initialize a dictionary to store the vote counts
    vote_counts = {option: 0 for option in df.values.flatten() if pd.notna(option)}
    
    # Iterate over each column (rank) in the DataFrame
    for i, column in enumerate(df.columns):
        # Calculate the weights for each vote based on the rank
        weights = df[column].apply(lambda x: num_options - i if pd.notna(x) else 0)
        
        # Group the weights by option and sum them up
        weighted_counts = weights.groupby(df[column]).sum()
        
        # Update the vote counts dictionary with the weighted counts
        for option, count in weighted_counts.items():
            if pd.notna(option):
                vote_counts[option] += count

    # Order the dictonary by vote counts
    vote_counts = dict(sorted(vote_counts.items(), key=lambda x: x[1], reverse=True))

    # Print the vote counts
    print("Vote counts:")
    for option, count in vote_counts.items():
        print(f"{option}: {count}")

    return vote_counts

"""
Main module for the ranking system.
"""
from data_cleaning import clean_data
from ranking import count_ranked_votes

def main():
    clean_data('votes.csv')
    count_ranked_votes('cleaned_data_2021.csv')

if __name__ == '__main__':
    main()

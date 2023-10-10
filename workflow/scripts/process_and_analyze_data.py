#!/usr/bin/env python

import json
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import sys

# Download the vader_lexicon resource from NLTK
nltk.download('vader_lexicon')

# Input and output file paths
input_file = snakemake.input[0]
processed_output_file = snakemake.output[0]
sentiment_output_file = snakemake.output[1]

# Function to perform sentiment analysis on text
def perform_sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

# Load the fetched JSON data
with open(input_file, "r", encoding="utf-8") as json_file:
    buffy_data = json.load(json_file)

# Process the data and perform sentiment analysis
processed_data = []
sentiment_analysis_results = []

for episode in buffy_data:
    episode_name = episode["episodeName"]
    description = episode["description"]
    
    # Perform sentiment analysis on the episode description
    sentiment_scores = perform_sentiment_analysis(description)
    
    # Append processed data and sentiment analysis results
    processed_data.append({
        "EpisodeName": episode_name,
        "Description": description,
        # Add more processed fields as needed
    })
    
    sentiment_analysis_results.append({
        "EpisodeName": episode_name,
        "SentimentPositive": sentiment_scores["pos"],
        "SentimentNegative": sentiment_scores["neg"],
        "SentimentNeutral": sentiment_scores["neu"],
        "SentimentCompound": sentiment_scores["compound"],
    })

# Create DataFrames from the processed data and sentiment analysis results
processed_df = pd.DataFrame(processed_data)
sentiment_df = pd.DataFrame(sentiment_analysis_results)

# Save the DataFrames as CSV files
processed_df.to_csv(processed_output_file, index=False)
sentiment_df.to_csv(sentiment_output_file, index=False)

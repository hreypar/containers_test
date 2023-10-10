#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import sys

# Input files
processed_data_file = snakemake.input.processed_data
sentiment_results_file = snakemake.input.sentiment_results

# Output files
sentiment_plot_file = snakemake.output.sentiment_plot
interaction_network_file = snakemake.output.interaction_network

# Load processed data and sentiment analysis results
processed_data = pd.read_csv(processed_data_file)
sentiment_results = pd.read_csv(sentiment_results_file)

# Generate Sentiment Analysis Plot
plt.figure(figsize=(8, 6))
plt.bar(sentiment_results["EpisodeName"], sentiment_results["SentimentCompound"], color='skyblue')
plt.xlabel("Episode Name")
plt.ylabel("Sentiment Compound Score")
plt.title("Sentiment Analysis of Buffy the Vampire Slayer Episodes")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(sentiment_plot_file)
plt.close()

# Generate Character Interaction Network (Example: Using processed data for demonstration)
interaction_network = nx.Graph()

# Add edges based on processed data (example: connecting episodes with similar descriptions)
for i in range(len(processed_data)):
    episode_name = processed_data.iloc[i]["EpisodeName"]
    description = processed_data.iloc[i]["Description"]
    similar_episodes = processed_data[processed_data["Description"] == description]["EpisodeName"].tolist()
    for similar_episode in similar_episodes:
        if episode_name != similar_episode:
            interaction_network.add_edge(episode_name, similar_episode)

# Draw and save the interaction network
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(interaction_network)
nx.draw(interaction_network, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')
plt.title("Character Interaction Network")
plt.axis("off")
#plt.tight_layout()
plt.savefig(interaction_network_file)
plt.close()

print("Visualizations generated successfully.")

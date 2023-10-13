#! /usr/bin/env Rscript --vanilla

# Retrieve command-line arguments
input_processed_data <- snakemake@input[['processed_data']]
input_sentiment_results <- snakemake@input[['sentiment_results']]
output_plotly_visualization <- snakemake@output[['plotly_visualization']]

# Load required R packages
library(plotly)
library(dplyr)
#library(pandoc)

# Read processed data and sentiment analysis results
processed_data <- read.csv(input_processed_data)
sentiment_results <- read.csv(input_sentiment_results)

# Create a plot_ly object
p <- plot_ly(data = sentiment_results, x = ~EpisodeName, y = ~SentimentCompound, text = ~paste("Episode: ", EpisodeName, "<br>Compound Score: ", SentimentCompound), type = "bar") %>%
	  layout(title = "Interactive Sentiment Analysis of Buffy the Vampire Slayer Episodes", xaxis = list(title = "Episode Name"), yaxis = list(title = "Sentiment Compound Score"))

# Save the interactive plot as an HTML file
htmlwidgets::saveWidget(p, file = output_plotly_visualization, selfcontained = TRUE)

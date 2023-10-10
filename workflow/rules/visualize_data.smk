#!/usr/bin/env python
# -*- coding: utf-8 -*-

rule visualize_data:
    '''
    rule to generate visualizations
    '''
    input:
        processed_data="results/analysis/processed_data.csv",
        sentiment_results="results/analysis/sentiment_analysis_results.csv"
    output:
        sentiment_plot="results/visualizations/sentiment_analysis_plot.png"
#        interaction_network="results/visualizations/character_interaction_network.png"
    conda:
        "../envs/visualization.yaml"
    script:
        "../scripts/generate_visualizations.py"

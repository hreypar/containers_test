#!/usr/bin/env python
# -*- coding: utf-8 -*-

rule generate_plotly_visualizations:
    '''
    Rule for sophisticated R-based visualization using plotly
    '''
    input:
        processed_data="results/analysis/processed_data.csv",
        sentiment_results="results/analysis/sentiment_analysis_results.csv"
    output:
        plotly_visualization="results/visualizations/plotly_visualization.html"
    container:
        "docker://hreypar/my-r-image:latest"
    script:
        "../scripts/generate_plotly_visualization.R"

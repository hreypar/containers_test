#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Rule to process and analyze data
rule analyze_data:
    input:
        "results/buffy_episodes.json"
    output:
        data="results/analysis/processed_data.csv",
        sentiment="results/analysis/sentiment_analysis_results.csv"
    conda:
        "../envs/sentiment_analysis.yaml" 
    script:
        "../scripts/process_and_analyze_data.py"

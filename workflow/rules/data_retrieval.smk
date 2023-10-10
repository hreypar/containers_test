#!/usr/bin/env python
# -*- coding: utf-8 -*-

rule fetch_data:
    '''
    Fetch data from the API
    '''
    output:
        "results/buffy_episodes.json"
    params:
        api_endpoint = config['buffy_data']['api_endpoint']
    conda:
        "../envs/download_json.yaml"
    script:
        "../scripts/fetch_data.py"


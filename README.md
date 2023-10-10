# Snakemake workflow: `containers_test`

[![Snakemake](https://img.shields.io/badge/snakemake-≥6.3.0-brightgreen.svg)](https://snakemake.github.io)

A Snakemake workflow for analyzing data from the Buffy the Vampire Slayer and Angel series using the [btvs-angel-api](https://github.com/Thatskat/btvs-angel-api).

## Overview

The main goal is to learn how to use containers for specific rules in a snakemake workflow (see [here](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#running-jobs-in-containers))

This workflow analyzes data from the Buffy the Vampire Slayer series, including episode information, cast details, and other relevant data, using the btvs-angel-api. It performs data fetching, processing, sentiment analysis, and generates visualizations for insights into the shows' content.

## Data Source

The data for this analysis was obtained from the [btvs-angel-api](https://github.com/Thatskat/btvs-angel-api) repository.

## Usage

The usage of this workflow is described in the [Snakemake Workflow Catalog](https://snakemake.github.io/snakemake-workflow-catalog/?usage=<owner>%2Fbtvs-angel-analysis>).

## Workflow Steps

1. **Fetch Data**: The workflow fetches data from the btvs-angel-api using a specified API endpoint.
2. **Process and Analyze Data**: Fetched data is processed, including sentiment analysis to gain insights into the shows' content.
3. **Generate Visualizations**: Visualizations such as sentiment analysis plots and character interaction networks are created for analysis.

## Prerequisites

- [Snakemake](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html)
- [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (for environment management)

## Installation

Clone the repository:

```bash
git clone git@github.com:hreypar/containers_test.git
cd containers_test
```

Run the workflow
```bash
conda activate snakemake
snakemake --cores <num_cores> --use-conda
```

# Use an official R runtime as a parent image
FROM r-base:latest

LABEL maintainer="Helena Reyes-Gopar <hreypar@gmail.com>"

# Install necessary system libraries
RUN apt-get update && apt-get install -y \
    librsvg2-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    pandoc

# Install necessary R packages
RUN R -e "install.packages(c('plotly', 'dplyr'), dependencies=TRUE, repos='https://cran.itam.mx/')"

# Set Bash as the default entry point
#ENTRYPOINT ["/bin/bash"]


# BD_Lab3
# Apache Hadoop MapReduce Project
This project is dedicated to working with Apache Hadoop, specifically implementing the MapReduce paradigm to analyze flight delay data. The goal is to find the top 5 airlines with the greatest average departure delay.

## Prerequisites
Make sure you have Docker and Docker Compose installed on your machine.

* [Docker 24+](https://www.docker.com/get-started)
* Docker-compose 2.21+

## Getting Started
Follow these steps to set up and run the project locally.

    git clone https://github.com/vladimirovich124/BD_Lab3

## Running the Environment
Use Docker Compose to set up the Hadoop environment

    docker-compose up -d

Wait for the initialization to complete before moving to the next step

## Set up Hadoop and Run the Code
Execute the following commands in the terminal:

    ./run.sh
    
This script installs Python 3 and the necessary packages on the Hadoop containers and copies the dataset into HDFS.

    docker exec -t apache-hadoop-namenode-1 chmod u+x /my_volume/main.py
    
## Run MapReduce Job
Execute the following command to run the MapReduce job:

    docker exec -t apache-hadoop-namenode-1 python3 /my_volume/main.py -r hadoop hdfs:///flights.csv

## Results
After the MapReduce job completes, the top 5 airlines with the greatest average departure delay will be displayed on the console.

## Additional Information
main.py: Python script containing the MapReduce implementation.
docker-compose.yml: Configuration file for Docker Compose.
run.sh: Bash script to install necessary packages and copy the dataset to HDFS.

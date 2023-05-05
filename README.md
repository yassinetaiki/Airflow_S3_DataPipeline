# introduction
In this project, we will be leveraging Airflow and Python to extract, transform, and load data from Twitter. Specifically, we will use the Twitter API to extract data, Python for data transformation, and deploy the code on Airflow/EC2. Finally, we will save the transformed data on Amazon S3. Through this project, we aim to showcase how to use Airflow and Python to build a scalable and reliable data pipeline for Twitter data.

# Architecture 
![text alternatif](https://github.com/yassinetaiki/Airflow_S3_DataPipline/blob/master/architecture.png)

## Repository Contents

- `dag_twitter_etl.py`: Airflow DAG for the data pipeline.
- `twitter_etl.py`: Python script for extracting and transforming data from Twitter.
- `list_tweet_musk.csv`: Example output file from the extract-transform process.

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from datetime import datetime
from twitter_etl import run_etl

#define default_args
default_args = {
    'owner': 'yassine',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['yasine-taici@hotmail.fr'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

#define dag 
dag = DAG(
    'ETL_Twitter_Dag',
    default_args=default_args,
    description='etl twitter dag',
    schedule_interval=timedelta(days=1),
)

#task 
run_etl_task = PythonOperator(
    task_id='twitter_etl',
    python_callable=run_etl,
    dag=dag, 
)

run_etl_task
from airflow.providers.amazon.aws.operators.s3 import S3FileTransformOperator
from airflow import DAG
from airflow.models.connection import Connection
from time import time_ns
from datetime import datetime
import os
import pendulum
import pandas as pd
import fastapi


with DAG(
    dag_id="new_dag",
    schedule="@once",
    start_date=datetime(2023, 1, 1),
    is_paused_upon_creation=False,
    catchup=False,
) as dag:
    pd.DataFrame({"A": [1, 2, 3]})
    print(pd)

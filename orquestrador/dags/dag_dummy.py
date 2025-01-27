from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='example_spark_job',
    default_args=default_args,
    description='Submeter job PySpark no cluster Spark',
    schedule_interval=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    run_pyspark_job = SparkSubmitOperator(
        task_id='run_pyspark_job',
        application='/app/pipelines/dummy_pipeline.py',  # Caminho para o script PySpark
        conn_id='spark_default',  # Conexão configurada no Airflow
        conf={
            'spark.master': 'spark://spark-master:7077',
            'spark.app.name': 'ExamplePySparkJob',
        },
        verbose=True,
    )

    run_pyspark_job

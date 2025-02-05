import pytest
from pyspark.sql.session import SparkSession

from pyspark_pipelines.core.client import SparkClient




class TestSparkClient:

    def test_create_client_successfully(self):
        spark_client = SparkClient()
        spark_client.create_session()
        session = spark_client.session

        assert isinstance(session, SparkSession)

    def test_create_client_with_packages_successfully(self):
        dependencies = [
            ("org.postgresql", "postgresql:42.4.0"),
            ("com.databricks", "spark-avro_2.12:3.0.1"),
            ("org.apache.hadoop", "hadoop-aws:3.2.0")
        ]

        spark_client = SparkClient(packages_list=dependencies)
        spark_client.create_session()
        session = spark_client.session

        assert isinstance(session, SparkSession)

import pytest
from pyspark.sql.session import SparkSession

from pyspark_pipelines.core.client import SparkClient




class TestSparkClient:

    def test_create_client_successfully(self):
        spark_client = SparkClient()
        spark_client.create_session()
        session = spark_client.session

        assert isinstance(session, SparkSession)
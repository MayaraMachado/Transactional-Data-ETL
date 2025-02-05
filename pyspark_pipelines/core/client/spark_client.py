"""SparkClient entity."""

from typing import Optional, List, Tuple

from pyspark.sql import SparkSession


class SparkClient:
    """Handle Spark session connection."""

    def __init__(
        self,
        session: Optional[SparkSession] = None,
        packages_list: Optional[List[Tuple[str, str]]] = None,
    ) -> None:
        self._session = session
        self._packages = packages_list

    @property
    def session(self) -> SparkSession:
        """Get a created an SparkSession.

        Returns:
            Spark session.

        Raises:
            AttributeError: if the session is not created yet.

        """
        if not self._session:
            raise AttributeError("Please create session first.")
        return self._session

    def create_session(self) -> None:
        """Create or get a live Spark Session for the SparkClient.

        When creating the session the function installs all third-party packages
        dependencies.

        """
        if not self._session:
            if self._packages:
                packages = ",".join([f"{org}:{pkg}" for org, pkg in self._packages])
                self._session = (
                    SparkSession.builder.appName("pyspark-pipeline")
                    .config("spark.jars.packages", packages)
                    .getOrCreate()
                )
            else:
                self._session = (
                    SparkSession.builder.appName("pyspark-pipeline")
                    .getOrCreate()
                )

            self._session.sparkContext.setLogLevel("ERROR")

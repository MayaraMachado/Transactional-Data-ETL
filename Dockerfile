FROM openjdk:8-jdk-slim

# Variáveis de versão do Spark
ARG SPARK_VERSION=3.2.0
ARG HADOOP_VERSION=3.2

# Instalar dependências
RUN apt-get update && \
    apt-get install -y curl bash procps && \  # Adicionando procps
    apt-get clean

# Baixar e instalar o Apache Spark
RUN curl -sL "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" \
    | tar -xz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark

# Definir variáveis de ambiente
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Expor as portas do Spark
EXPOSE 7077 8080 8081 8082

# Configuração para o Master ou Worker
CMD if [ "$SPARK_MODE" = "master" ]; then \
    /opt/spark/sbin/start-master.sh; \
  else \
    /opt/spark/sbin/start-worker.sh $SPARK_MASTER_URL; \
  fi

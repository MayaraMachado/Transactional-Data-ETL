from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

def main():
    # Inicializando a SparkSession
    spark = SparkSession.builder \
        .appName("Dummy PySpark Job") \
        .getOrCreate()

    # Criando um dataset dummy diretamente
    data = [
        ("Alice", 25, "F"),
        ("Bob", 30, "M"),
        ("Charlie", 35, "M"),
        ("Diana", 40, "F"),
    ]

    columns = ["Name", "Age", "Gender"]

    # Criando o DataFrame
    df = spark.createDataFrame(data, columns)

    # Transformação simples: Filtrar pessoas com idade maior que 30 e adicionar uma nova coluna
    transformed_df = df.filter(col("Age") > 30).withColumn("Status", lit("Filtered"))

    # Exibindo o DataFrame transformado (para fins de depuração)
    transformed_df.show()

    # Salvando o DataFrame transformado como arquivo CSV local
    output_path = "/app/output/dummy_output.csv"
    transformed_df.write.mode("overwrite").csv(output_path, header=True)

    print(f"Arquivo de saída salvo em: {output_path}")

    # Parando a SparkSession
    spark.stop()

if __name__ == "__main__":
    main()

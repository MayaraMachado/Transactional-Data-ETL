'''

Postgress

# Defina as propriedades do banco de dados
jdbc_url = "jdbc:postgresql://host:port/database"
properties = {
    "user": "seu_usuario",
    "password": "sua_senha",
    "driver": "org.postgresql.Driver"
}

# Leia dados do PostgreSQL para um DataFrame
df = spark.read.jdbc(url=jdbc_url, table="nome_da_tabela", properties=properties)

# Mostre as primeiras linhas do DataFrame
df.show()

'''
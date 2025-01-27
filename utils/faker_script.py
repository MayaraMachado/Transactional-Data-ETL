import random
from faker import Faker
import pandas as pd

# Inicializar o Faker
fake = Faker()

# Número de registros a serem gerados
NUM_SELLERS = 100
NUM_PRODUCTS = 50
NUM_TRANSACTIONS = 10000

# Gerar vendedores
sellers = []
for _ in range(NUM_SELLERS):
    sellers.append({
        'name': fake.company(),
        'region': random.choice(['North', 'South', 'East', 'West'])
    })

# Gerar produtos
products = []
for _ in range(NUM_PRODUCTS):
    products.append({
        'product_name': fake.word(),
        'category': random.choice(['Electronics', 'Clothing', 'Furniture', 'Groceries']),
        'price': round(random.uniform(10.0, 1000.0), 2)
    })

# Gerar transações
transactions = []
for _ in range(NUM_TRANSACTIONS):
    transaction_date = fake.date_this_year()
    product_id = random.randint(1, NUM_PRODUCTS)
    seller_id = random.randint(1, NUM_SELLERS)
    quantity = random.randint(1, 20)
    total_amount = round(quantity * random.uniform(10.0, 1000.0), 2)
    
    transactions.append({
        'transaction_date': transaction_date,
        'product_id': product_id,
        'seller_id': seller_id,
        'quantity': quantity,
        'total_amount': total_amount
    })

# Converter para DataFrame (opcional para visualização)
sellers_df = pd.DataFrame(sellers)
products_df = pd.DataFrame(products)
transactions_df = pd.DataFrame(transactions)

# Exportar para SQL (apenas para uso no banco de dados)
def generate_insert_sql(table_name, df):
    insert_statements = []
    for _, row in df.iterrows():
        columns = ', '.join(df.columns)
        values = ', '.join([f"'{v}'" if isinstance(v, str) else str(v) for v in row.values])
        insert_statements.append(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")
    return insert_statements

# Gerar os inserts
seller_inserts = generate_insert_sql('sellers', sellers_df)
product_inserts = generate_insert_sql('products', products_df)
transaction_inserts = generate_insert_sql('transactions', transactions_df)

# Escrever para um arquivo SQL
with open('init_data.sql', 'w') as f:
    f.write('\n'.join(seller_inserts) + '\n')
    f.write('\n'.join(product_inserts) + '\n')
    f.write('\n'.join(transaction_inserts) + '\n')

print("Data generation complete. SQL file saved as 'init_data.sql'.")

-- Criação das tabelas
CREATE TABLE IF NOT EXISTS sellers (
    seller_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    region VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    transaction_date TIMESTAMP NOT NULL DEFAULT current_timestamp,
    product_id INT REFERENCES products(product_id),
    seller_id INT REFERENCES sellers(seller_id),
    quantity INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL
);

-- Inserção de dados nas tabelas
INSERT INTO sellers (name, region) VALUES
('Seller A', 'North'),
('Seller B', 'South'),
('Seller C', 'East'),
('Seller D', 'West');

INSERT INTO products (product_name, category, price) VALUES
('Product 1', 'Electronics', 299.99),
('Product 2', 'Clothing', 59.99),
('Product 3', 'Furniture', 399.99),
('Product 4', 'Groceries', 19.99);

INSERT INTO transactions (product_id, seller_id, quantity, total_amount) VALUES
(1, 1, 5, 1499.95),
(2, 2, 3, 179.97),
(3, 3, 2, 799.98),
(4, 4, 10, 199.90),
(1, 2, 7, 2099.93),
(2, 3, 4, 239.96);

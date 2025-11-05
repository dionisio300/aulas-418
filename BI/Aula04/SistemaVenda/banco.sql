CREATE DATABASE IF NOT EXISTS fastphone CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; USE fastphone; -- dimensões CREATE TABLE IF NOT EXISTS 
produtos ( id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(120) NOT NULL, categoria VARCHAR(60) NOT NULL ); 

CREATE TABLE IF NOT EXISTS vendedores ( id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(120) NOT NULL ); -- fato simples de vendas 
CREATE TABLE IF NOT EXISTS vendas ( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    produto_id INT NOT NULL, 
    vendedor_id INT NOT NULL, 
    quantidade INT NOT NULL, 
    preco_unit DECIMAL(10,2) NOT NULL, 
    data_venda DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY (produto_id) REFERENCES produtos(id), 
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id) ); -- carga mínima para a demo 

INSERT INTO produtos (nome, categoria) VALUES 
('iPhone 14', 'Premium'), ('iPhone 15', 'Premium'), ('Samsung S23', 'Premium'), ('Samsung A34', 'Intermediário'), ('Xiaomi Redmi Note 13', 'Intermediário'); 

INSERT INTO vendedores (nome) VALUES 
('Ana Sousa'), ('Bruno Lima'), ('Carla Nunes'), ('Diego Melo');
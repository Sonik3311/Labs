CREATE TABLE shop (
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE,
balance FLOAT NOT NULL);

CREATE TABLE product (
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE,
price FLOAT NOT NULL);

CREATE TABLE warehouse (
shop_id INTEGER REFERENCES shop (id),
product_id INTEGER REFERENCES product (id),
quantity INTEGER NOT NULL,
PRIMARY KEY (shop_id, product_id));

INSERT INTO shop (id, name, balance) VALUES (1, 'пятерочка',31);
INSERT INTO shop (id, name, balance) VALUES (2, 'перекресток',133);
INSERT INTO product VALUES (1, 'молоко', 100);
INSERT INTO product VALUES (2, 'хлеб', 25);
INSERT INTO warehouse VALUES (1, 1, 20);
INSERT INTO warehouse VALUES (1, 2, 10);
INSERT INTO warehouse VALUES (2, 1, 30);

INSERT INTO worker VALUES (15, 1, "a", 62000, "manager");
INSERT INTO worker VALUES (53, 1, "b", 33000, "cashier");
INSERT INTO worker VALUES (12, 2, "c", 23000, "cashier");
INSERT INTO worker VALUES (52, 2, "d", 61000, "manager");
INSERT INTO worker VALUES (86, 2, "e", 59200, "manager");

SELECT position, avg(salary) as avg_salary FROM worker
GROUP BY position
ORDER BY avg_salary DESC;

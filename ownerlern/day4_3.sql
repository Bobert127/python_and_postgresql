CREATE DATABASE cinemas_db_day4;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
CREATE TABLE customers
(
    id serial PRIMARY KEY,
    name        varchar(255) NOT NULL
);


INSERT INTO customers (name)
VALUES ('Oliver'),
       ('Jake'),
       ('Amelia'),
       ('Margaret')
;


CREATE TABLE orders
(
    id      serial PRIMARY KEY,
    customer_id   int NOT NULL,
    order_details varchar(255),
    -- !! here we define foreign key
    FOREIGN KEY (customer_id) REFERENCES customers (id)
    -- ON DELETE CASCADE
);


INSERT INTO orders(customer_id, order_details)
VALUES (3, 'as soon as possible'),
       (3, 'faster then ASAP'),
-- (5,'Order2'),
       (1, 'do not send until tomorrow')
;

CREATE TABLE opinions
(
    id serial PRIMARY KEY,
    product_id int,
    description text,
    FOREIGN KEY (product_id) references products(id)
);

insert into opinions values (1, 'The best')
insert into opinions values (default, 'OK', 2)



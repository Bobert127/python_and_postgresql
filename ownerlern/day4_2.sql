CREATE DATABASE exercises_db_day4;

SELECT * FROM customer;

SELECT * FROM address;

SELECT * FROM customer, address;
SELECT * FROM customer, address WHERE customer.id = address.customer_id;
-- (SELECT * FROM) (customer, address)     WHERE   (customer.id = address.customer_id);
-- (SELECT * FROM) (customer JOIN address)   on    (customer.id = address.customer_id);
-- EXPLAIN ANALYZE SELECT * FROM customer, address WHERE customer.id = address.customer_id;
-- inner join
SELECT * FROM customer a INNER JOIN address b on a.id = b.customer_id;
-- EXPLAIN ANALYZE SELECT * FROM customer INNER JOIN address on customer.id = address.customer_id;
SELECT * FROM customer JOIN address on customer.id = address.customer_id;
-- EXPLAIN ANALYZE SELECT * FROM customer INNER JOIN address on customer.id = address.customer_id;


-- left join
SELECT * FROM customer LEFT JOIN address on customer.id = address.customer_id;
-- EXPLAIN ANALYZE SELECT * FROM customer LEFT JOIN address on customer.id = address.customer_id;

-- right join
SELECT * FROM customer RIGHT JOIN address on customer.id = address.customer_id;
-- EXPLAIN ANALYZE SELECT * FROM customer RIGHT JOIN address on customer.id = address.customer_id;

-- full join
SELECT * FROM customer FULL JOIN address on customer.id = address.customer_id;
-- EXPLAIN ANALYZE SELECT * FROM customer FULL JOIN address on customer.id = address.customer_id;

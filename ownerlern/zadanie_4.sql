CREATE DATABASE library_db

select * from clients

    CREATE TABLE Author
    (
        id   serial PRIMARY KEY,
        name VARCHAR(100)
    );
    CREATE TABLE Book (
        id   serial PRIMARY KEY,
        ISBN VARCHAR(17),
        name VARCHAR(50),
        description TEXT,
        is_loaned VARCHAR(1) default 0
        );
    CREATE TABLE Client (
        id   serial PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50)
        );
    CREATE TABLE  Category
    (
        id   serial PRIMARY KEY,
        name VARCHAR(50)
    );
drop table book

insert  into Author values(default, 'Adam Mickiewicz')
insert  into Author values(default, 'Bolesła Prus')
insert  into Author values(default, 'Zofia Naukowska')
insert  into Author values(default, 'Maria Konopnicka')
insert  into Author values(default, 'Olga Tokarczuk')

insert  into Book values(default, '978-83-1112-125-7', 'Pan Tadeusz', 'Poeamat', 0)
insert  into Book values(default, '978-83-1124-125-7', 'Granica', 'Powieśc')
insert  into Book values(default, '978-83-1212-125-7', 'Nasza Szkapa', 'Poeamat')
insert  into Book values(default, '978-83-8712-125-7', 'Cienka linia', 'Powieść', 0)
insert  into Book values(default, '978-83-992-125-7', 'Oddalenie', 'Poezja', 1)

insert  into Client values(default, 'Robert', 'Trzaska')
insert  into Client values(default, 'Jan', 'Nowak')
insert  into Client values(default, 'Krzysztof', 'Malinowski')

select name from Author

select name from Author where id = 2

select * from book


select * from book where id = 2

select * from Client
    

select * from Client where  id = 1   
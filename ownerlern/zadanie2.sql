     CREATE TABLE Products (
        id serial PRIMARY KEY,
        name varchar(100),
        description varchar(100),
        price decimal(5,2)
        );
    CREATE TABLE Orders (

        id serial PRIMARY KEY,
        description varchar(100)
    );
    CREATE TABLE Clients (

        id serial PRIMARY KEY,
        name varchar(100),
        surname varchar(100)
    );

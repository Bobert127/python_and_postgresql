drop table comments
create table  Comments
(
    id serial primary key,
    content text,
    movies_id int,
    FOREIGN KEY (movies_id) REFERENCES movies(id)

);

select * from Comments

insert into Comments values (default, 'do luftu', 2)

select drop table comments
create table  Comments
(
    id serial primary key,
    content text,
    movies_id int,
    FOREIGN KEY (movies_id) REFERENCES movies(id)

);

select * from Comments

insert into Comments values (default, 'do luftu', 2)

select distinct  movies.name, Comments.content from Comments, movies
where Comments.movies_id = movies.id movies.name, Comments.content from Comments, movies
where Comments.movies_id = movies.id
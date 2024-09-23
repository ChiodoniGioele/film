CREATE SCHEMA `film` ;
CREATE USER 'film_adm'@'%' IDENTIFIED BY 'Admin$00' ;
GRANT all privileges ON film.* TO 'film_adm'@'%';
FLUSH PRIVILEGES;
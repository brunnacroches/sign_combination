CREATE DATABASE sign_combinations_db;

USE sign_combinations_db;

CREATE TABLE person (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    name_user VARCHAR(50) NOT NULL,
    zodiac_sign VARCHAR(100) NOT NULL
);

INSERT INTO person(name_user, zodiac_sign)
VALUES
    ('Joao', 'Cancer'),
    ('Fabiana', 'Aries'),
    ('Pedro', 'Virgo'),
    ('Maria', 'Taurus');

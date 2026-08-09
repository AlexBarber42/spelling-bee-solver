CREATE DATABASE IF NOT EXISTS bee;
ALTER DATABASE bee CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE bee;

CREATE TABLE IF NOT EXISTS lexicon (
    lex_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS user_history (
    puzzle_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    required_letter CHAR(1),
    letters CHAR(7),
    puzzle_date DATE
);


LOAD DATA LOCAL INFILE "/docker-entrypoint-initdb.d/lexicon.txt"
    INTO TABLE lexicon
    (word);
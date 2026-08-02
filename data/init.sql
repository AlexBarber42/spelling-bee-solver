CREATE DATABASE IF NOT EXISTS bee;
ALTER DATABASE bee CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE bee;

CREATE TABLE IF NOT EXISTS lexicon (
    lex_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(15)
);


LOAD DATA LOCAL INFILE "/docker-entrypoint-initdb.d/lexicon.txt"
    INTO TABLE lexicon
    (word);
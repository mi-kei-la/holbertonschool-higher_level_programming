-- Create table and insert data.
CREATE TABLE IF NOT EXISTS second_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256), score INT);
INSERT INTO second_table (name, score) VALUES ('Jhon', 10);
INSERT INTO second_table (name, score) VALUES ('Alex', 3);
INSERT INTO second_table (name, score) VALUES ('Bob', 14);
INSERT INTO second_table (name, score) VALUES ('George', 8);

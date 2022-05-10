-- Query: Create 3 new dojos

INSERT INTO dojos (name) VALUES ('Burbank'),('Online'),('San Jose');

-- Query: Delete the 3 dojos you just created
SELECT * FROM dojos;

DELETE FROM dojos WHERE id > 3;

-- Query: Create 3 more dojos

INSERT INTO dojos (name) VALUES ('Burbank'),('Online'),('San Jose');

-- Query: Create 3 ninjas that belong to the first dojo

SELECT * from ninjas;

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Yo Han", "Song", 35, 7), ("Aaron", "Johnson", 23, 7), ("Davita", "Ford", 21, 7);

-- Query: Create 3 ninjas that belong to the second dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Frank", "Steglinski", 35, 8), ("Julien", "Salazar", 23, 8), ("Devin", "Brown", 21, 8);

-- Query: Create 3 ninjas that belong to the third dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Joe", "Coder", 35, 9), ("Julie", "Python", 23, 9), ("David", "Brown", 21, 9);
-- Query: Retrieve all the ninjas from the first dojo



SELECT * FROM ninjas WHERE dojo_id = (SELECT id FROM dojos LIMIT 1);

-- Query: Retrieve all the ninjas from the last dojo

SELECT * FROM ninjas WHERE dojo_id = (SELECT id FROM dojos ORDER BY id DESC LIMIT 1);

-- Query: Retrieve the last ninja's dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Tyler", "Maxwell", 39, 7);

SELECT dojo_id FROM ninjas ORDER BY id DESC LIMIT 1;

SELECT * FROM dojos WHERE id = (SELECT dojo_id FROM ninjas ORDER BY id DESC LIMIT 1) OR id = (SELECT dojo_id FROM ninjas ORDER BY id DESC LIMIT 1 OFFSET 1);
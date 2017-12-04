DROP TABLE IF EXISTS Login;


CREATE TABLE IF NOT EXISTS `Login` (
  `ID`		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `FirstName`	TEXT NOT NULL,
  `Surname`	TEXT NOT NULL,
  `Email` TEXT NOT NULL,
  'Username' TEXT NOT NULL Unique,
  `Password` CHAR NOT NULL
);

INSERT INTO 'Login'('FirstName','Surname', 'Email', 'Username', `Password` ) VALUES ('John', 'Doe', 'JohnDoe@adminwru.com', 'admin', 'password');



CREATE TABLE IF NOT EXISTS `Games`(
  `gameID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  `gameType` TEXT NOT NULL,
  `ageRange` TEXT NOT NULL
);

DROP TABLE IF EXISTS Events;
CREATE TABLE IF NOT EXISTS `Events`(
  `eventID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  `eventName` TEXT NOT NULL UNIQUE,
  `Address` TEXT NOT NULL UNIQUE,
  `Postcode` TEXT NOT NULL
);
INSERT INTO 'Events'('eventName','Address', 'Postcode') VALUES ('Touch Rugby', 'Cardiff University, Birchwood Road,', '‎CF23 5YB');


CREATE TABLE IF NOT EXISTS `Activities`(
  `activityID`INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  `date` DATE NOT NULL,
  `eventName` TEXT NOT NULL,
  `attendance`INTEGER NOT NULL,
  `Male` INTEGER NOT NULL,
  `Female` INTEGER NOT NULL,
  `gameID` INTEGER NOT NULL,
  FOREIGN KEY (`eventName`) REFERENCES Events(eventID),
  FOREIGN KEY (`gameID`) REFERENCES Games(gameID)
);



-- http://www.sqlitetutorial.net/sqlite-foreign-key/

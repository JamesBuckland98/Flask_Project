
DROP TABLE IF EXISTS Games;
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

DROP TABLE IF EXISTS Activities;
CREATE TABLE IF NOT EXISTS `Activities`(
  `activityID`INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  `date` DATE NOT NULL,
  `eventName` TEXT NOT NULL,
  `attendance`INTEGER NOT NULL,
  `EventType` TEXT NOT NULL,
  `Male` INTEGER NOT NULL,
  `Female` INTEGER NOT NULL,
  `gameID` INTEGER NOT NULL,
  FOREIGN KEY (`eventName`) REFERENCES Events(eventID),
  FOREIGN KEY (`gameID`) REFERENCES Games(gameID)
);


INSERT INTO 'Games'('gameID','gameType','ageRange')VALUES('1','Tag','Juniors (8-17)');
INSERT INTO 'Games'('gameID','gameType','ageRange')VALUES('2','Contact','Seniors (18+)');

INSERT INTO 'Events'(`eventID`,'eventName','Address', 'Postcode') VALUES ('1','Touch Rugby', 'Cardiff University, Birchwood Road,', '‎CF23 5YB');
INSERT INTO 'Events'(`eventID`,'eventName', 'Address', 'Postcode')VALUES('2','Scarlets Regional Event', 'Parc Pemberton, Llanelli', 'SA14 9UZ');
INSERT INTO 'Events'(`eventID`,'eventName', 'Address', 'Postcode')VALUES('3','Junior Beach Rugby', 'Barafundle Bay Beach', 'SA71 5LS');
INSERT INTO 'Events'(`eventID`,'eventName', 'Address', 'Postcode')VALUES('4','Mixed Ability Event', 'Jersey Park', 'SA1 8HN');

-- http://www.sqlitetutorial.net/sqlite-foreign-key/

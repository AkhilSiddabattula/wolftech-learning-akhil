-- CREATING TABLE
CREATE TABLE foxmapping(
  empId int,
  firstName varchar(30),
  lastName varchar(30),
  address varchar(30),
  mobileNo varchar(10)
);

-- INSERT VALUES INTO TABLE
INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (01, 'Akhil', 'Siddabattula', 'Andhra Pradesh', '7013093650');

INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (02, 'Faizan', 'Rahil', 'Telangana', '0123355698');

INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (03, 'Tirthiraj', 'Mukharji', 'Andhra Pradesh', '2245609781');

INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (04, 'Ratnanjali', 'Sastangi', 'Uttar Pradesh', '1567890345');

INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (05, 'Sindhu', 'Yepuri', 'Telangana', '6754590239');

INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (06, 'Akhil', 'Siddabattula', 'Andhra Pradesh', '7013093650');

INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (07, 'Faizan', 'Rahil', 'Telangana', '0123355698');

INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (08, 'Tirthiraj', 'Mukharji', 'Andhra Pradesh', '2245609781');

INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (09, 'Bipin', 'Yadav', 'Bihar', '0245890345');

INSERT INTO foxmapping (empId, firstName, lastName, address, mobileNo)
VALUES (10, 'Shubham', 'Rathore', 'Uttar Pradesh', '6754590239');


-- SELECT data from TABLE
SELECT * FROM foxmapping;

SELECT firstName, address FROM foxmapping;

SELECT firstName FROM foxmapping;

-- WHERE is used to filter records
SELECT * FROM foxmapping WHERE address='Andhra Pradesh';

SELECT * FROM foxmapping WHERE address='Telangana';

-- ORDER BY in ascending or descending
SELECT * FROM foxmapping ORDER BY address;

SELECT * FROM foxmapping ORDER BY address DESC;

-- DISTINCT is used to remove duplicate records from tabale
SELECT DISTINCT address FROM foxmapping;
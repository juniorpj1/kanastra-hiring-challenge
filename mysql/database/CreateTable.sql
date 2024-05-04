CREATE TABLE charges (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    governmentId VARCHAR(20),
    email VARCHAR(255),
    debtAmount DECIMAL(10, 2),
    debtDueDate VARCHAR(15)
);
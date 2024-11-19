-- Create a new database named "sample_db"
CREATE DATABASE sample_db;

-- Connect to the "sample_db" database
\ c sample_db;
-- Create a table named "employees"
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    hire_date DATE,
    job_title VARCHAR(50),
    salary NUMERIC(10, 2)
);
-- Insert data into the "employees" table
INSERT INTO employees (
        first_name,
        last_name,
        email,
        phone_number,
        hire_date,
        job_title,
        salary
    )
VALUES (
        'John',
        'Doe',
        'john.doe@example.com',
        '555-1234',
        '2023-01-10',
        'Software Engineer',
        80000.00
    ),
    (
        'Jane',
        'Smith',
        'jane.smith@example.com',
        '555-5678',
        '2022-07-15',
        'Project Manager',
        90000.00
    ),
    (
        'Alice',
        'Johnson',
        'alice.johnson@example.com',
        '555-9012',
        '2023-03-20',
        'UX Designer',
        75000.00
    );
-- Retrieve all records from the "employees" table
SELECT *
FROM employees;
-- Retrieve specific columns
SELECT first_name,
    last_name,
    email
FROM employees;
-- Retrieve records with a specific condition
SELECT *
FROM employees
WHERE salary > 80000.00;
-- Update the salary of the employee with employee_id = 1
UPDATE employees
SET salary = 85000.00
WHERE employee_id = 1;
-- Update multiple fields for an employee
UPDATE employees
SET phone_number = '555-4321',
    job_title = 'Senior Software Engineer'
WHERE employee_id = 1;
-- Delete a specific employee by employee_id
DELETE FROM employees
WHERE employee_id = 3;
-- Delete all employees with a salary less than 80000.00
DELETE FROM employees
WHERE salary < 80000.00;
-- Drop the "employees" table
DROP TABLE employees;
-- Drop the "sample_db" database
DROP DATABASE sample_db;
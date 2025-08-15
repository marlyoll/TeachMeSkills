-- 📄 Примеры команд SQL (подсказки):
-- ===========================
-- Как создать таблицу:
-- CREATE TABLE table_name (
--     column1 datatype,
--     column2 datatype,
--     ...
-- );

-- Как вставить данные:
-- INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2');

-- Как обновить данные:
-- UPDATE table_name SET column1 = 'new_value' WHERE some_condition;

-- Как добавить новый столбец:
-- ALTER TABLE table_name ADD COLUMN column_name datatype;

-- Как удалить таблицу:
-- DROP TABLE table_name;

-- ===========================
-- 📋 Задания (выполняйте TODO):
-- ===========================


-- ✅ TODO 1: Создайте таблицу "Employees" с полями:
-- Name (TEXT), Position (TEXT), Department (TEXT), Salary (NUMERIC)

CREATE TABLE Employees (
    Name TEXT,
    Position TEXT,
    Department TEXT,
    Salary NUMERIC
);


-- ✅ TODO 2: Вставьте несколько записей в таблицу "Employees"

INSERT INTO Employees (Name, Position, Department, Salary)
VALUES 
    ('Виктория Иванова', 'Биоинформатик', 'Научные исследования', 2500),
    ('Екатерина Климович', 'Биоинженер', 'Разработка продуктов', 2000),
    ('Бан Чан', 'Лаборант', 'Контроль качества', 1500);


-- ✅ TODO 3: Измените должность одного из сотрудников на более высокую

UPDATE Employees 
SET 
    Position = 'Senior Bioinformatician',
    Salary = 3500 
WHERE Name = 'Виктория Иванова';


-- ✅ TODO 4: Добавьте новое поле "HireDate" (DATE) в таблицу "Employees"

ALTER TABLE Employees ADD COLUMN HireDate DATE;


-- ✅ TODO 5: Добавьте дату приема на работу для всех сотрудников

UPDATE Employees SET HireDate = '2020-08-13' WHERE Name = 'Виктория Иванова';
UPDATE Employees SET HireDate = '2021-09-15' WHERE Name = 'Екатерина Климович';
UPDATE Employees SET HireDate = '2023-06-13' WHERE Name = 'Бан Чан';


-- ✅ TODO 6: Найдите всех сотрудников с должностью "Manager"

INSERT INTO Employees (Name, Position, Department, Salary, HireDate)
VALUES 
    ('Александр Васильев', 'Manager', 'Sales', 5500, '2021-08-10');

SELECT * FROM Employees 
WHERE Position = 'Manager';

-- ✅ TODO 7: Найдите всех сотрудников с зарплатой больше 5000

SELECT * FROM Employees 
WHERE Salary > 5000;


-- ✅ TODO 8: Найдите всех сотрудников, которые работают в отделе "Sales"

SELECT * FROM Employees WHERE Department = 'Sales';


-- ✅ TODO 9: Найдите среднюю зарплату всех сотрудников

SELECT AVG(Salary) AS AverageSalary FROM Employees;


-- ✅ TODO 10: Удалите таблицу "Employees"

--  DROP TABLE Employees;


-- 🎯 *Задание с повышенным уровнем сложности:*
-- Реализуйте задачи 6–9 в виде ХРАНИМЫХ ФУНКЦИЙ или ПРОЦЕДУР.

-- Подсказка:
-- CREATE FUNCTION или CREATE PROCEDURE
-- BEGIN ... END

-- Пример вызова:
-- CALL имя_процедуры();

-- 📝 Напишите здесь свои CREATE FUNCTION / PROCEDURE

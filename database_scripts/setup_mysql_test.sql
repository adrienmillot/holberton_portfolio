-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS ss_test_db;
CREATE USER IF NOT EXISTS 'ss_test'@'localhost' IDENTIFIED BY 'ss_test_pwd';
GRANT ALL PRIVILEGES ON `ss_test_db`.* TO 'ss_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'ss_test'@'localhost';
FLUSH PRIVILEGES;

-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS ss_test_db;
CREATE USER IF NOT EXISTS 'ss_test'@'172.20.0.3' IDENTIFIED BY 'ss_test_pwd';
GRANT ALL PRIVILEGES ON `ss_test_db`.* TO 'ss_test'@'172.20.0.3';
GRANT SELECT ON `performance_schema`.* TO 'ss_test'@'172.20.0.3';
FLUSH PRIVILEGES

-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS ss_dev_db;
CREATE USER IF NOT EXISTS 'ss_dev'@'172.20.0.4' IDENTIFIED BY 'ss_dev_pwd';
GRANT ALL PRIVILEGES ON `ss_dev_db`.* TO 'ss_dev'@'172.20.0.4';
GRANT SELECT ON `performance_schema`.* TO 'ss_dev'@'172.20.0.4';
FLUSH PRIVILEGES;

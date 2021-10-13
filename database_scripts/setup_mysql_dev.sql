-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS ss_dev_db;
CREATE USER IF NOT EXISTS 'ss_dev'@'172.18.0.1' IDENTIFIED BY 'ss_dev_pwd';
GRANT ALL PRIVILEGES ON `ss_dev_db`.* TO 'ss_dev'@'172.18.0.1';
GRANT SELECT ON `performance_schema`.* TO 'ss_dev'@'172.18.0.1';
FLUSH PRIVILEGES;

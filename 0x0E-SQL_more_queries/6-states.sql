-- This script will create databases --
-- hbtn_0d_usa, states --
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, 
	name VARCHAR(256)
);

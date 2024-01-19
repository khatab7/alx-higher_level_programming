-- This script converts a database to UTF8

-- Select databse htbn_0c_0
USE hbtn_0c_0;
-- Converts database to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Converts table first_table to utf8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

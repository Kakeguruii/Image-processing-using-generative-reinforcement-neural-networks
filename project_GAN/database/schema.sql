CREATE DATABASE IF NOT EXISTS mydatabase;

USE mydatabase;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255),
    upload_date DATE
);

CREATE TABLE IF NOT EXISTS processed_images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_id INT,
    style VARCHAR(100),
    processing_date DATE,
    FOREIGN KEY (image_id) REFERENCES images(id)
);

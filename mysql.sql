CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    last_test_score INT DEFAULT 0,
    best_test_score INT DEFAULT 0
);
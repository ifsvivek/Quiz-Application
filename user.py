def create_user_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE users (
            username VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL,
            last_test_score INT DEFAULT 0,
            best_test_score INT DEFAULT 0);"""
    )
    conn.commit()
    conn.close()


def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s);",
            (username, hashed_password),
        )
    except mysql.connector.errors.IntegrityError:
        return False
    conn.commit()
    conn.close()
    return True


def check_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
    stored_password = cursor.fetchone()
    conn.close()
    if stored_password and check_password_hash(stored_password[0], password):
        return True
    else:
        return False


def update_user_score(username, score):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET score = %s WHERE username = %s"
    cursor.execute(query, (score, username))
    conn.commit()
    cursor.close()
    conn.close()
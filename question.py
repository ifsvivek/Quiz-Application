

def convert_to_exam_format():
    import pandas as pd

    questions_list = []
    for question, details in interview_questions_mcq_dict.items():
        question_dict = {
            "Question": question,
            "Options": details["options"],
            "Answer Index": details["answer_index"],
            "Difficulty": details["difficulty"],
        }
        questions_list.append(question_dict)

    # Create a DataFrame from the list
    df = pd.DataFrame(questions_list)

    # Export the DataFrame to an Excel file
    df.to_excel("interview_questions_mcq.xlsx", index=False)
    print("Excel file created successfully with data in rows!")


def insert_into_table():
    import mysql.connector

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="appy",
    )

    cursor = connection.cursor()

    # Create a table to store the questions and answers
    create_table_query = """
    CREATE TABLE qa (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question TEXT,
        answer INT,
        difficulty VARCHAR(255),
        choice1 TEXT,
        choice2 TEXT,
        choice3 TEXT,
        choice4 TEXT
    )
    """
    cursor.execute(create_table_query)

    insert_query = """
    INSERT INTO qa (question, answer, difficulty, choice1, choice2, choice3, choice4)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    # Assuming 'interview_questions_mcq_dict' is defined elsewhere and contains the data
    for question, details in interview_questions_mcq_dict.items():
        # Preparing data tuple for insertion
        data_tuple = (
            question,
            details["answer_index"],
            details["difficulty"],
            details["options"][0],
            details["options"][1],
            details["options"][2],
            details["options"][3],
        )
        cursor.execute(insert_query, data_tuple)
    connection.commit()
    cursor.close()
    connection.close()

    print("Data inserted successfully into the database.")

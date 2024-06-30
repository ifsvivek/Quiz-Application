interview_questions_mcq_dict = {
    "What is polymorphism in OOP?": {
        "options": [
            "A programming language's ability to process objects differently depending on their data type or class.",
            "The process of creating complex data types.",
            "The concept of restricting access to certain components of an object.",
            "The ability of different objects to respond, each in its own way, to identical messages.",
        ],
        "answer_index": 3,
        "difficulty": "Medium",
    },
    "Explain the difference between == and === in JavaScript.": {
        "options": [
            "== compares only the values for equality.",
            "== compares both value and type for equality.",
            "=== compares only the values for equality after converting both sides to a common type.",
            "=== compares both value and type for equality, without doing type conversion.",
        ],
        "answer_index": 3,
        "difficulty": "Easy",
    },
    "What is a deadlock in operating systems?": {
        "options": [
            "A situation where a system can no longer perform any tasks.",
            "A situation in which two or more processes are unable to proceed because each is waiting for one of the others to release a resource.",
            "A type of error that occurs when the system runs out of memory.",
            "A condition where multiple processes are trying to access the same resource simultaneously.",
        ],
        "answer_index": 1,
        "difficulty": "Hard",
    },
    "Describe how a bubble sort algorithm works.": {
        "options": [
            "Selects the smallest element from an unsorted list in each iteration and moves it to the beginning.",
            "Divides the entire dataset into two parts, sorts them and then merges them.",
            "Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.",
            "Creates a tree structure and sorts the elements based on their heap property.",
        ],
        "answer_index": 2,
        "difficulty": "Easy",
    },
    "What is the Big O notation, and why is it important?": {
        "options": [
            "A mathematical notation that describes the execution time of an algorithm.",
            "A programming concept that deals with the efficiency of data structures.",
            "A mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity.",
            "A type of syntax used in programming languages to optimize code.",
        ],
        "answer_index": 2,
        "difficulty": "Medium",
    },
    "Explain RESTful APIs.": {
        "options": [
            "APIs designed based on SOAP standards.",
            "APIs that rely on a stateless, client-server, cacheable communications protocol — typically HTTP.",
            "APIs that require the client to maintain the state of the server.",
            "APIs that are designed for internal use within an organization.",
        ],
        "answer_index": 1,
        "difficulty": "Medium",
    },
    "What is a Git branch and how do you create one?": {
        "options": [
            "A separate line of development that can be merged into the main codebase, created with 'git branch branch_name'.",
            "A copy of the original codebase that cannot be modified, created with 'git clone branch_name'.",
            "A method to delete a part of the codebase, created with 'git delete branch_name'.",
            "A tool for merging different versions of a codebase, created with 'git merge branch_name'.",
        ],
        "answer_index": 0,
        "difficulty": "Easy",
    },
    "Explain the concept of inheritance in OOP.": {
        "options": [
            "A mechanism that allows a class to inherit properties and behavior from another class.",
            "The process of creating new classes from existing ones.",
            "A feature that allows objects to change their class during runtime.",
            "The ability of a program to process objects differently depending on their class or data type.",
        ],
        "answer_index": 0,
        "difficulty": "Medium",
    },
}













def get_questions():
    i = 1
    for question, details in interview_questions_mcq_dict.items():
        options = details["options"]
        answer_index = details["answer_index"]
        difficulty = details["difficulty"]
        # Convert difficulty from string to an integer representation if needed
        difficulty_map = {"Easy": 1, "Medium": 2, "Hard": 3}
        difficulty_level = difficulty_map.get(
            difficulty, 0
        )  # Default to 0 if not found

        query = "INSERT INTO qa (qno, question, answer, difficulty, choice1, choice2, choice3, choice4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        values = (
            i,
            question,
            answer_index,
            difficulty_level,
            options[0],
            options[1],
            options[2],
            options[3],
        )

        cursor.execute(query, values)
        cursor.execute("commit;")
        i += 1
    
    
    
    
    
    
def main():
    get_questions()
    cursor.execute("drop table if exists qa;")
    cursor.execute(
        "create table if not exists qa (qno int primary key, question varchar(255), answer int(1), difficulty int(1), choice1 varchar(255), choice2 varchar(255), choice3 varchar(255), choice4 varchar(255));"
    )
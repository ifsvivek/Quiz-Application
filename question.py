

# write a code to convert the dictionary to excel file

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

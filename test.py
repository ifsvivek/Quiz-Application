import openpyxl

# Load the workbook and select the active worksheet
wb = openpyxl.load_workbook("interview_questions_mcq.xlsx")
ws = wb.active

# Dictionary to store the questions
interview_questions_mcq_dict = {}

# Iterate over the rows in the worksheet, starting from the second row
for row in ws.iter_rows(min_row=2, values_only=True):
    question, options, answer_index, difficulty = row
    options_list = options.split("\n")
    interview_questions_mcq_dict[question] = {
        "options": options_list,
        "answer_index": int(answer_index),
        "difficulty": difficulty,
    }

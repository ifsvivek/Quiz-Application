from flask import *
import mysql.connector
import random

app = Flask(__name__)
app.secret_key = "secret"  # Required for session management

# Define your global variables and constants here
questions = []
score = 0
ADMIN_USERNAME = "ifsvivek"


# Database connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="1234", database="appy"
    )


# Database query execution
def query_db(query, args=(), one=False):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    conn.close()
    return (rv[0] if rv else None) if one else rv


# Fetch total number of questions
def get_total_questions():
    result = query_db("SELECT COUNT(*) as total FROM qa", one=True)
    return result["total"]


def select_random_question():
    total_questions = get_total_questions()
    all_questions = list(range(1, total_questions + 1))
    available_questions = [
        q for q in all_questions if not any(ques["qno"] == str(q) for ques in questions)
    ]
    if not available_questions:
        return random.choice(all_questions)
    ran = random.choice(available_questions)
    return ran


def check_answer(question, answer):
    if answer is None:
        return False

    try:
        answer_int = int(answer)
    except ValueError:
        return False

    data = query_db("SELECT answer FROM qa WHERE qno=%s;", (question,), one=True)
    return data and data["answer"] == answer_int


@app.route("/", methods=["GET", "POST"])
def home():
    global questions, score
    if request.method == "POST":
        login_type = request.form.get("login_type")
        if login_type == "user":
            return redirect(url_for("user_login"))
        elif login_type == "admin":
            return redirect(url_for("admin_login_form"))
        else:
            return "Invalid login choice"
    else:
        questions = []
        score = 0
        return render_template("index.html")


@app.route("/user_login", methods=["POST", "GET"])
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username  # Store username in session
        return redirect(url_for("quiz"))
    return render_template("user_login.html")


@app.route("/admin_authenticate", methods=["POST"])
def admin_authenticate():
    admin_username = request.form.get("admin_username")
    if admin_username != ADMIN_USERNAME:
        flash("Access Denied")
        return "Access Denied", 403
    session["username"] = admin_username  # Store admin username in session
    return redirect(url_for("admin"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global score, questions
    if "username" not in session:  # Check if username exists in session
        return redirect(url_for("home"))
    question = request.form.get("qno")
    user_answer = request.form.get("answer")
    count = int(request.form.get("count", 0)) + 1
    if question and user_answer and not any(q["qno"] == question for q in questions):
        correct = check_answer(question, user_answer)
        if correct:
            score += 1
        questions.append(
            {
                "qno": question,
                "user_answer": user_answer,
                "correct": correct,
                "data": query_db(
                    "SELECT * FROM qa WHERE qno=%s;", (question,), one=True
                ),
            }
        )
    total_questions = get_total_questions()
    if len(questions) >= total_questions:
        return render_template(
            "result.html",
            username=session["username"],
            score=score,
            questions=questions,
        )
    ran = select_random_question()
    data = query_db("SELECT * FROM qa WHERE qno=%s;", (ran,), one=True)
    return render_template(
        "quiz.html", data=data, count=count, total_questions=total_questions
    )


@app.route("/result", methods=["POST"])
def result():
    global score, questions
    if "username" not in session:  # Check if username exists in session
        return redirect(url_for("home"))
    return render_template(
        "result.html",
        username=session["username"],
        score=score,
        questions=questions,
    )


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "username" not in session or session["username"] != ADMIN_USERNAME:
        print("Access Denied in Admin Route")
        return "Access Denied", 403

    if request.method == "POST":
        action = request.form.get("action")
        qno = request.form.get("qno")
        question = request.form.get("question")
        answer = request.form.get("answer")
        choice1 = request.form.get("choice1")
        choice2 = request.form.get("choice2")
        choice3 = request.form.get("choice3")
        choice4 = request.form.get("choice4")

        if action == "add":
            query_db(
                "INSERT INTO qa (qno, question, answer, choice1, choice2, choice3, choice4) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                (qno, question, answer, choice1, choice2, choice3, choice4),
            )
            return "Question Added Successfully"
        elif action == "remove":
            query_db("DELETE FROM qa WHERE qno=%s;", (qno,))
            return "Question Removed Successfully"
        elif action == "modify":
            query_db(
                "UPDATE qa SET question=%s, answer=%s, choice1=%s, choice2=%s, choice3=%s, choice4=%s WHERE qno=%s;",
                (question, answer, choice1, choice2, choice3, choice4, qno),
            )
            return "Question Modified Successfully"
        else:
            return "Invalid Action", 400

    return render_template("admin.html")


@app.route("/admin/question/<qno>", methods=["GET"])
def get_question(qno):
    question = query_db("SELECT * FROM qa WHERE qno=%s;", (qno,), one=True)
    if question:
        return question
    return {}, 404


if __name__ == "__main__":
    app.run(debug=True)

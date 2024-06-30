# Quiz Application

This project is a web-based quiz application built with Flask and TailwindCSS. It allows users to log in as either an admin or a user. Admins can create quiz questions, while users can take quizzes and view their results.

## Features

-   **User Authentication**: Separate login forms for users and admins.
-   **Quiz Management**: Admins can add quiz questions.
-   **Dynamic Quiz Taking**: Users can take quizzes and get immediate feedback.

## Project Structure

-   `appy.py`: Flask application files.
-   `env/`: Virtual environment directory.
-   `static/`: Contains static files like CSS.
    -   `src/input.css`: TailwindCSS entry point.
-   `templates/`: HTML templates for the application.
    -   `admin.html`: Admin interface for managing quizzes.
    -   `index.html`: Landing page with login forms.
    -   `quiz.html`: Quiz taking interface for users.
    -   `result.html`: Displays quiz results to users.
-   `tailwind.config.js`: TailwindCSS configuration.
-   `package.json`: Node.js project file with dependencies.

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/ifsvivek/DBMS-Project
```

2. **Install dependencies**

Ensure you have Node.js installed, then run:

```bash
npm install
```

3. **Generate TailwindCSS**

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
```

4. **Activate the virtual environment**

```bash
python -m venv env  # Create a virtual environment
```


```bash
source env/Scripts/activate  # On Windows
source env/bin/activate  # On Unix or MacOS
```

5. **Install Python dependencies**

```bash
pip install -r requirements.txt
```

6. **Run the Flask application**

```bash
python appy.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

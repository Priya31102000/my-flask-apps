from flask import Flask, render_template, request

app = Flask(__name__)

worksheets = {
    "addition": {
        "title": "Worksheet 1: Addition",
        "instructions": "Add the numbers in each problem.",
        "problems": [
            {"problem": "12 + 35 = ", "answer": 47},
            {"problem": "27 + 11 = ", "answer": 38},
            {"problem": "48 + 21 = ", "answer": 69},
            {"problem": "36 + 53 = ", "answer": 89},
            {"problem": "62 + 18 = ", "answer": 80},
            {"problem": "55 + 25 = ", "answer": 80},
            {"problem": "19 + 70 = ", "answer": 89},
            {"problem": "34 + 46 = ", "answer": 80},
            {"problem": "73 + 17 = ", "answer": 90},
            {"problem": "81 + 9 = ", "answer": 90},
        ]
    },
    "subtraction": {
        "title": "Worksheet 2: Subtraction",
        "instructions": "Subtract the numbers in each problem.",
        "problems": [
            {"problem": "45 - 23 = ", "answer": 22},
            {"problem": "67 - 15 = ", "answer": 52},
            {"problem": "89 - 34 = ", "answer": 55},
            {"problem": "52 - 18 = ", "answer": 34},
            {"problem": "76 - 41 = ", "answer": 35},
            {"problem": "90 - 25 = ", "answer": 65},
            {"problem": "38 - 19 = ", "answer": 19},
            {"problem": "61 - 37 = ", "answer": 24},
            {"problem": "50 - 22 = ", "answer": 28},
            {"problem": "85 - 48 = ", "answer": 37},
        ]
    },
    "mixed": {
        "title": "Worksheet 3: Mixed Addition & Subtraction",
        "instructions": "Solve the following problems. Remember to add or subtract correctly!",
        "problems": [
            {"problem": "32 + 47 = ", "answer": 79},
            {"problem": "91 - 56 = ", "answer": 35},
            {"problem": "15 + 63 = ", "answer": 78},
            {"problem": "78 - 29 = ", "answer": 49},
            {"problem": "24 + 55 = ", "answer": 79},
            {"problem": "80 - 33 = ", "answer": 47},
            {"problem": "66 + 14 = ", "answer": 80},
            {"problem": "49 - 17 = ", "answer": 32},
            {"problem": "58 + 31 = ", "answer": 89},
            {"problem": "95 - 67 = ", "answer": 28},
        ]
    },
    "word_problems": {
        "title": "Worksheet 4: Word Problems",
        "instructions": "Solve the following word problems. Show your work!",
        "problems": [
            {"problem": "Sarah has 23 apples. John gives her 15 more. How many apples does Sarah have in total? ", "answer": 38},
            {"problem": "There are 56 birds in a tree. 24 birds fly away. How many birds are left in the tree? ", "answer": 32},
            {"problem": "A baker made 38 cookies in the morning and 27 cookies in the afternoon. How many cookies did the baker make in total? ", "answer": 65},
            {"problem": "A class has 45 students. 12 students are absent. How many students are present? ", "answer": 33},
            {"problem": "Maria collected 62 stamps. She gave 35 stamps to her friend. How many stamps does Maria have left? ", "answer": 27},
        ]
    }
}


@app.route('/')
def index():
    return render_template('index.html', worksheets=worksheets)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    worksheet_name = request.form['worksheet']
    problem_index = int(request.form['problem_index'])
    user_answer = request.form['answer']

    worksheet = worksheets[worksheet_name]
    correct_answer = worksheet['problems'][problem_index]['answer']

    try:
        user_answer_int = int(user_answer)  # Convert to integer for comparison
        is_correct = user_answer_int == correct_answer
    except ValueError:  # Handle non-integer input
        is_correct = False  # Treat non-integer input as incorrect

    return {'is_correct': is_correct}


if __name__ == '__main__':
    app.run(debug=True)
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

if __name__ == '__main__':
    questions = []
    for i in range(0, len(question_data)):
        question = Question(question_data[i]['text'], question_data[i]['answer'])
        questions.append(question)

    quiz = QuizBrain(questions)

    while quiz.still_has_question():
        quiz.next_question()
        print('\n')

    print("You've completed the quiz.")
    print(f'Your final score is: {quiz.score}/{quiz.question_num-1}')





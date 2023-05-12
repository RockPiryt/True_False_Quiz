from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

#1.Create question bank
question_bank =[]
for question in question_data:
    question_text = question["question"]#nie po question_data bo to lista,
    question_answer = question["correct_answer"]#samo question to linijka w question_data- słownik
    new_question = Question(q_text =question_text, q_answer = question_answer)
    question_bank.append(new_question) 

# print(question_bank)
# print(question_bank[0].text) # read text from first dict
# print(question_bank[1].text) # read text from first dict
# print(question_bank[2].text) # read text from first dict

#2. initialize a quiz
quiz = QuizBrain(question_bank)
gui = QuizInterface(quiz)


#still_got_question to metoda QuizBrain Boolean zwraca True lub False
#still got question to warunek dla pętli do działania 
# while loop wyłączyć bo w tkinter jest pętla mainloop
# while quiz.still_got_question() is True:
#     quiz.next_question()

# print("You've copleted the quiz.")
# print(f"Your final score is {quiz.score}/ {len(question_bank)}")
# print(f"Your final score is {quiz.score}/ {quiz.question_number}")

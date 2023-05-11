#TODO: asking the question
#TODO: checking if the answer is correct
#TODO: checking if we're the end of quiz



#TODO: asking the question

#stworznie obiektu quizu - zasady quizu - ile pytań i wyświetlanie pytań z banku
class QuizBrain():
    
    def __init__(self, q_bank):
        self.question_number = 0 #sprawdza które pytanie jest w kolejności
        self.question_list = q_bank # jako argument zostanie przekazy question bank
        self.score = 0 #dodanie punktacji za poprawne odpwiedzi
    
    #create question
    def next_question(self):
        current_question = self.question_list[self.question_number] #pierwsze pytanie bo index=0
        self.question_number += 1 #po każdym zadanym pytaniu wzrasta numeracja
        #curennt question to słownik ma text i answer, ale nie ma nadanego numeru, dlatego tworzę numerację
        user_answer = input(f'Q {self.question_number}: {current_question.text} True or False? ')
        self.check_answer(user_answer, current_question.answer)
    
    #condition for while loop
    def still_got_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        #or
        # return self.question_number < len(self.question_list)
        # #bo np pytanie nr 2 <12 i to zawsze True
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That is wrong.")
        print(f"Correct answer is {correct_answer}.")
        #-----------------------------ile zgadniętych na ile pytań zadanych 3/5
        print(f"Your current score is {self.score}/ {self.question_number}")
        print("\n") #pusta linia


# #initialize a quiz in main.py
# quiz = QuizBrain(question_bank)
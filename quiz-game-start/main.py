import random
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_q=Question(question_text,question_answer)
    # print(new_q.question+" "+new_q.answer)
    question_bank.append(new_q)


        
quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print(f"You completed te quiz and your score is : {quiz.final_score}/{quiz.question_number}")


from question_model import Question

class QuizBrain:

    def __init__(self,question_bank):
        self.question_number=0
        self.question_list=question_bank
        self.current_score=0
        self.final_score=0

    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False
    
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("you got it right")
            self.current_score+=1
            self.final_score=self.current_score
            print(f"your current score :{self.current_score}/{self.question_number}")
            
        else:
            print("you got it wrong")
            print(f"correct answer: {correct_answer}")

    
    def next_question(self):
        cur_que=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q{self.question_number} {cur_que.question} :(true/false) ")
        self.check_answer(user_answer,cur_que.answer)
        

        

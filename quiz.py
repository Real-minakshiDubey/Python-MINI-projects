qna ={
    "what is mini's fav color? ": "purple",
    "what is mini's fav food? ": "dimag",
    "what is mini's fav cartoon? ": "doraemon",
    "what is mini's fav friend? ": "Shreya",
    "whats her relationship status? ": "Single",
    "will she ever get marry?":"no"
}
score=0;
for question,answer in qna.items():
    user_ans=input(question +" ")
    if user_ans.lower()==answer.lower():
        print("correct!")
        score +=1;
    else :
        print("wrong!")
print("your score is ", score , "out of 6")
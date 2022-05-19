def make_questions():
    while True:
        question = input("질문을 입력해주세요(종료q) : ")
        if question == 'q':
            break
        total_list.append({"질문" : question, "답변" : ""})

def make_answers():
    for item in total_list:
        print(item['질문'])
        item['답변'] = input(">> 답변을 입력해주세요. : ")

total_list = []
print("이상형이 뭐예요?")
make_questions()
print(total_list)
print("=======================================")
make_answers()
print(total_list)


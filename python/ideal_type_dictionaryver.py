total_dictionary = {}

while True:
    question= input("질문을 입력해주세요 (질문이 없을 시 q 입력):")
    if question=="q":
        break
    else:
        total_dictionary[question]=""

for i in total_dictionary:
    print(i)
    answer= input("답을 입력해주세요:")
    total_dictionary[i]=answer
print(total_dictionary)
from googletrans import Translator

translator = Translator()

# sentence = "안녕하세요. 코드라이언입니다."
sentence = input("번역할 문장을 입력해주세요: ")
while True:
    wanted_destination = input("어떤 언어로 번역을 원하시나요? (한국어,영어,중국어,일본어만 지원 가능): ")
    if wanted_destination == "한국어":
        destination = "ko"
        break
    elif wanted_destination == "영어":
        destination = "en"
        break
    elif wanted_destination == "중국어":
        destination = "zh-cn"
        break
    elif wanted_destination == "일본어":
        destination = "ja"
        break
    else:
        print("지원하지 않는 언어입니다. 다시 입력해주세요.")
    

# line9 ~ line 10 : 언어 감지 관련 강의 내용 코드
# detect 함수는 translator 기능 안에 있다. 그리고 detect 함수는 언어 감지를 원하는 문장을 재료로 필요로 함.
detected = translator.detect(sentence)


# translator.translate(text,dest,src) 세 가지 재료 중 src는 생략 가능.
result = translator.translate(sentence,destination)

print("\n===========출력결과==========")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("=============================")
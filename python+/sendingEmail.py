import smtplib
# SMTP 서버에서는 영어만 알아들을 수 있으므로 한글을 번역하기 위해서는 아래의 MIME가 필요함.
from email.message import EmailMessage
# imghdr은 나중에 확장자가 png에서 jpeg로 바꿔도 유효하도록 알아서 이미지 유형을 판단해줌.
import imghdr
# 이메일 유효성 검사를 위한 모듈 임포트 (regular expression의 줄임말)
import re

SMTP_SERVER = "smtp.gmail.com"
# Gmail을 이용할 때 SMTP_PORT는 무조건 465로 고정. GMAIL에서 지정된 번호이므로 변경 안됨.
SMTP_PORT = 465

# 이메일 유효성 검사 후 유효하면 보내고 아니면 안 보내는 함수
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    # bool은 내장함수로, none이 아니면 true, none이면 false로 처리해줌.
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")

# subject, from, to는 MIME의 header 부분에 속하므로 본문과 달리 아래의 방법으로 지정.
message["Subject"] = "코드라이언 메일 보내기 프로그램 수업 테스트 메일입니다."
message["From"] = "보내는 사람 주소"
message["To"] = "받는 주소 입력"

# image = open("codelion.png","rb")
# 밑의 with ~ as 를 통해 close 문 없이 열었던 파일 사용 뒤 자동으로 닫을 수 있음.
with open("codelion.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('codelion',image_file)
# add_attachment는 텍스트 말고 다른 유형의 파일도 있을 때 사용. 재료로는 image / maintype / subtype 필요.
message.add_attachment(image_file,maintype='image',subtype=image_type)


# SMTP 함수는 우리가 원하는 메일서버에 연결하게 해줌. 재료는 서버주소와 포트번호 2가지가 필요함.
# smtp = smtplib.SMTP 상태로 print(smtp)하면 보안문제로 오류. 따라서 SMTP 뒤에 '_SSL' 추가해야 함.
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)

# print(smtp)

# SMTP 메일서버에 로그인하기
smtp.login("아이디","비밀번호")

sendEmail("받는 사람 주소")

smtp.quit()

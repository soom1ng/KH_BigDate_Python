# 입력 받은 n개의 원소에 대한 평균 구하기
value = list(map(int, input("정수 입력 : ").split()))
print(sum(value) / len(value))


# 정수 n을 입력 받아 n * n 출력하기
# num = int(input("정수를 입력하세요 : "))
# print ( num * num )


# n개에 대한 숫자를 입력 받아 최소값 및 최대값 구하기
numList = list(map(int, input("정수 입력 : ").split()))


# 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
from datetime import datetime

current_year = datetime.today().year # 현재가 몇년인지 확인하기
jumin = input("주민번호를 입력하세요 : ")
# print(jumin[7:8])

age = 2024 - (1900 + int(jumin[0:2]))
# print(age)

if int(jumin[7:8]) == 1 :
    gender = "남자"
elif int(jumin[7:8]) == 2 : 
    gender = "여자"
else : 
    gender = "잘못 입력 하셨습니다."

print("생년월일 : " + jumin[:6])
print("성별 : " + gender)
print(f"나이 : {age}살")


# 알람 설정하기
hour, min = map(int, input("시간 입력 : ").split())
tmp = (hour * 60) + min

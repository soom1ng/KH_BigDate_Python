# 이름 입력
# 나이 입력 : 1 ~ 199 까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# 성별 입력 : 영문자 (남성 : M, m), (여성 : F, f) 으로 입력 받고 잘못 된 값이 오면 재 입력 요청을 한다.
# 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청을 한다.
# 결과는 마지막에 다 함께 출력 한다.

name = input("이름을 입력하세요 : ")

while True:
    age = input("나이를 입력하세요 : ")
    if age.isdigit() : # 입력 받은 문자열이 숫자로 구성되어 있는지 확인 
        age = int(age)
        if 0 < age < 200 : # print("정상 입력입니다.")
            break
    print("나이를 잘 못 입력 하셨습니다.")

        

while True : 
    gender = input("성별을 입력하세요 (m, f) : ")
    if (gender == "f" or "F"):
        gender1 = "여성"
        break
    elif (gender == "m" or "M"):
        gender1 = "남성"
        break
    else:
        print("잘못 입력 하셨습니다.")
        continue

while True :
    jobs = input("""1 : 학생, 2 : 회사원, 3 : 주부, 4 : 무직
직업을 입력하세요 : """)

    if jobs.isdigit() :
        jobs = int(jobs)
        if 0 < jobs < 5 : break
        # if jobs == 1:
        #     job = "학생"
        #     break
        # elif jobs == 2:
        #     job = "회사원"
        #     break
        # elif jobs == 3:
        #     job = "주부"
        #     break
        # elif jobs == 4:
        #     job = "무직"
        #     break
    print("다시 입력하세요.")
    continue

jobs_name = ["", "학생", "회사원", "주부", "무직"]

print(f"""[회원 정보]
이름 : {name}
나이 : {age}
성별 : {gender1}
직업 : {jobs_name[jobs]}
""")

# 조건문 : if ~ else
num = int(input("정수를 입력 하세요 : "))
if num % 2 == 0 : print("짝수 입니다.")
else : print("홀수 입니다.")

n = int(input("정수를 입력 하세요 : "))
if n > 100 :
	print("100보다 커요")
elif n < 100 :
	print("100보다 작아요")
else :
	print("100과 같아요")

print("지금 계절은 ? ", end='');
season = input()
if season == "spring": print("봄이 왔어요.")
elif season == "summer": print("여름이 왔어요.")
elif season == "fall" : print("쓸쓸한 가을 입니다.")
elif season == "winter": print("아직 겨울이네요ㅠㅠ")
else : pass

age = int(input("나이를 입력 하세요 : "))

if(0 < age < 200) :
    print("정상 입력입니다.")
else :
    print("잘못 입력 하셨습니다.")

# 회원 가입을 위한 아이디와 패스워드 입력받기
# String.find(찾을 문자)
# String.find(찾을 문자, 시작 Index)
# String.find(찾을 문자, 시작 Index, 끝 Index)

user = input("아이디 입력 : ") 
if len(user) >= 5 : 
    pw = input("비밀번호 입력 : ")
    if pw.__len__() < 8 or pw.__len__() > 16 :
        print("비밀번호는 8자에서 16자 사이여야 합니다.") 
        pass
    else : 
        print(f"아이디 : {user}")
        print(f"비밀번호 : {pw}")
else : 
    print("아이디는 반드시 5자리 이상이어야 합니다.")
# 영어 소문자와 대문자로 이루어진 단어를 입력 받고 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

result = ""
for e in input() :
    if e.islower() :
        result += e.upper()
    else :
        result += e.lower()
print(result)

# 세개의 자연수를 입력받아서 모두 곱하기
# 결과값에서 나오는 수에서 각 숫자의 출력 횟수를 출력하기
# 출력 
# 17037300 => 0 : 3번, 1 : 1번, 7 : 2번

a, b, c = map(int, input("정수 3개 입력 : ").split())
ls = list(str(a * b * c))
for i in range(10) :
    print(ls.count(str(i))) # 해당 문자의 갯수 반환


# from math import sin, cos, tan, floor, ceil # import math : math 모듈의 전체 함수와 변수를 불러 옴 .
import math as m

print(m.sin(1))
print(m.cos(1))
print(m.tan(1))
print(m.floor(2.5))
print(m.ceil(2.5))

import sys # 시스템 관련 정보를 가지고 있는 모듈, 주로 매개 변수를 받을 때 사용 힘 .
import os 

# 명령줄 인수 출력
print("명령줄 인수 : ", sys.argv)

# 스크립트 실행 경로
print("실행 경로 : ", sys.path[0])

# 프로그램 종료
# sys.exit(0)

# 현재 작업 디렉토리 가져오기
cwd = os.getcwd()
print("현재 작업 디렉토리 : ", cwd)

# 파일 존재 여부 확인
is_file = os.path.isfile('test.py')
print(is_file)

# 시스템 명령어 출력
os.system("ls -l")
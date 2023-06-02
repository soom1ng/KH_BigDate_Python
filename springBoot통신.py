import requests
import json

data = {
    "id" : "우주귀요미",
    "pwd" : "123456"
}

# JSON 데이터를 서버로 전달
url = "http://localhost:8111/login"
header = {"Content-Type" : "application/json"}

response = requests.post(url, data=json.dumps(data), headers=header)

if response.status_code == 200 :
    print("데이터 전송에 성공 했습니다.")
else : 
    print("데이터 전송에 실패 했습니다.")

# Python Object(Ductionary, List, Tuple 등)를 JSON 문자열로 변경하는 것을 JSON Encoding
# 인코딩은 json.dumps() 메소드를 이용해서 JSON 문자열로 변환
# 디코딩은 JSON 문자열을 Python 타입 (Dictonary, List, Tuple 등)으로 변경하는 것 : json.loads()

import json

# customer = {
#     "id" : 123456,
#     "name" :  "우주귀요미",
#     "history" : [
#         {"date" : "2023-05-05", "제품" : "iPhone 12 mini"},
#         {"date" : "2023-06-01", "제품" : "iPhone 13"}
#     ]
# }

# jsonString = json.dumps(customer, ensure_ascii=False)
# print(jsonString)

jsonString = '''{"name" : "siroo", "id" : 123456, "history" : [
    {"date" : "2023-05-05", "item" : "iPhone 12 mini"},
        {"date" : "2023-06-01", "item" : "iPhone 13"}
]}'''

dict = json.loads(jsonString)

print(dict["name"])
for h in dict["history"] :
    print(h["date"], h["item"])
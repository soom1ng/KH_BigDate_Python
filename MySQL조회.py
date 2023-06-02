import pymysql

# 전역변수 선언
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# MySQL 연결
conn = pymysql.connect(host="127.0.0.1", user="root", password="19970817", db="mysqlDB", charset="utf8")

# 커서 생성하기
cur = conn.cursor()
 
cur.execute("SELECT * FROM userTable")

print("ID     이름         이메일                출생연도")
print("-" * 50)

while True :
    row = cur.fetchone()
    if row == None : break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print(f"{data1:7}{data2:10}{data3:20}{data4:6}")
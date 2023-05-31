from abc import *

class NetworkAdapter(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass

class FiveG(NetworkAdapter):
    def __init__ (self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} 5G로 연결 했습니다.")

class WiFi(NetworkAdapter):
    def __init__ (self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} Wi-Fi로 연결 했습니다.")

class LTE(NetworkAdapter):
    def __init__ (self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} LTE로 연결 했습니다.")

net = input("연결할 네트워크를 선택 [1]5G, [2]Wi-Fi, [3]LTE : ")
if net == "1":
    adapter = FiveG("KT Mega Pass")
    adapter.connect()
elif net == "2":
    adapter = WiFi("SK Telecom")
    adapter.connect()
elif net == "3":
    adapter = LTE("SK Telecom")
    adapter.connect()
else: print("연결할 네트워크가 없습니다.")
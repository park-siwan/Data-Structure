from collections import deque


class CustomerComplaint:
    """고객 센터 문의를 나타내는 클래스"""

    def __init__(self, name, email, content):
        self.name = name
        self.email = email
        self.content = content


class CustomerServiceCenter:
    """ 서비스 센터 클래스"""

    def __init__(self):
        self.queue = deque()  # 대기 중인 문의를 저장할 큐 생성

    def process_complaint(self):
        """접수된 고객 센터 문의 내용 처리하는 메소드"""
        # 코드를 쓰세요

    def add_complaint(self, name, email, content):
        """새로운 문의를 큐에 추가 시켜주는 메소드"""
        # 코드를 쓰세요


# 고객 문의 센터 인스턴스 생성
center = CustomerServiceCenter()

# 문의 접수한다
center.add_complaint("박시완", "pswan3168@gmail.com", "음식이 너무 맛이 없어요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()

# 문의 세 개를 더 접수한다
center.add_complaint("이동열", "abcd@gmail.com", "에어컨이 안 들어와요...")
center.add_complaint("배승현", "efgh@gmail.com", "결제가 제대로 안 되는 거 같군요")
center.add_complaint("주도영", "ijklm@gmail.com", "방을 교체해주세요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()
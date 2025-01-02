from locust import HttpUser, task, between

class MyLoadTestUser(HttpUser):
    wait_time = between(1, 5)  # 각 요청 사이의 대기 시간 (1초 ~5초)

    @task
    def index_api(self):
        self.client.get("/")  # 예제: 메인 페이지 요청

    @task
    def movie_api(self):
        self.client.get("/movie")
        #self.client.post("/api/data", json={"key": "value"})  # 예제: 데이터 제출 요청
        
    @task
    def ticket_api(self):
        self.client.post("/ticket")
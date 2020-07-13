from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(5, 9)
    cookies = {}

    @task
    def index_page(self):
        self.client.get("/")

    @task(3)
    def view_organisation(self):
        self.client.get("/organisation/1", cookies=self.cookies)

    def on_start(self):
        files = {
            'username': (None, 'test@gmail.com'),
            'password': (None, 'shh'),
        }
        response = self.client.post("/login/", {"username":"test@gmail.com", "password":"shh"})
        self.cookies = response.cookies

import requests
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class RequestWrapper:
    def __init__(self):
        pass

    @staticmethod
    def get(url: str,
            data: dict = None,
            headers: dict = None,
            params: dict = None):
        log.debug(f"getting {url} with {headers} and {params}")
        try:
            result = requests.get(url=url,
                                  params=params,
                                  headers=headers,
                                  data=data)
            if result.status_code == 200:
                print(result.content)
        except Exception:
            raise Exception(f"Cannot get {url}")

    @staticmethod
    def post(url: str,
             data: dict = None,
             headers: dict = None,
             params: dict = None):
        try:
            result = requests.post(url=url,
                                   params=params,
                                   headers=headers,
                                   data=data)
            if result.status_code == 200:
                print(result.content)
        except Exception:
            raise Exception(f"Cannot post {url}")

    @staticmethod
    def put(url: str,
            data: dict = None,
            headers: dict = None,
            params: dict = None):
        try:
            result = requests.put(url=url,
                                  params=params,
                                  headers=headers,
                                  data=data)
            if result.status_code == 200:
                print(result.content)
        except Exception:
            raise Exception(f"Cannot put {url}")

    @staticmethod
    def delete(url: str,
               data: dict = None,
               headers: dict = None,
               params: dict = None):
        try:
            result = requests.delete(url=url,
                                     params=params,
                                     headers=headers,
                                     data=data)
            if result.status_code == 200:
                print(result.content)
        except Exception:
            raise Exception(f"Cannot delete {url}")


if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    params = {'wd': 'python'}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}

    RequestWrapper.get(url=url,
                       params=params,
                       headers=headers)

    # Homework: could you try to create jira tickets/ update fields/ get all the tickets from your own instance?
    # Reference "https://developer.atlassian.com/cloud/jira/platform/rest/v3/#api-group-Issues"
    # To send requests out from your machine, you can choose Python, Postman(https://www.postman.com/downloads/) or Curl

    # To play with the APIs, let us consider a scenario:
    # You are working for a trading company and your boss asked you to collect all the top Trump related news in the
    # past few months and sort them by popoularity, how would you do it? ref: https://newsapi.org/docs/get-started

    # (Advanced) Let us say you are asked to correlate the sentiment of the news with recent stock price change,
    # how would you do it?
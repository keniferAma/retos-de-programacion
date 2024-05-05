import requests
from typing import Any
import time

HTTP_URL = 'https://httpbin.org'


# By the usual way, we're creating a new connection or session every request we do. 
# while with requests.Session we're reusing the request, because of that by session is faster.

def fetch_get() -> Any:
    r = requests.get(f'{HTTP_URL}/get')
    return r.json()

def fetch_post() -> Any:
    data_to_post = {"key": "value"}
    r = requests.post(f'{HTTP_URL}/post', data=data_to_post)
    return r.json

def fetch_update() -> Any:
    date_to_update = {"key": "value to update"}
    r = requests.put(f'{HTTP_URL}/put', data=date_to_update)
    return r.json


def main() -> None:
    print(fetch_get())
    print(fetch_update())
    print(fetch_post())


init = time.perf_counter()
main()
end = time.perf_counter()
print(end - init)
"""2.2858179000904784"""



"""when we use requests.Session, we're 'reusing' connections and due to that, improves the performance"""

def session_get(session: requests.Session) -> dict:
    r = session.get(f'{HTTP_URL}/get')
    return r.json()

def session_post(session: requests.Session) -> dict:
    data_to_post = {"key": "value"}
    r = session.post(f'{HTTP_URL}/post', data=data_to_post)
    return r.json

def session_update(session: requests.Session) -> dict:
    date_to_update = {"key": "value to update"}
    r = session.put(f'{HTTP_URL}/put', data=date_to_update)
    return r.json


def main_session() -> None:
    client = requests.Session()
    print(session_get(client))
    print(session_update(client))
    print(session_post(client))


init = time.perf_counter()
main_session()
end = time.perf_counter()
print(end - init)
"""1.0269150999374688"""
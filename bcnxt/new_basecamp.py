import requests
MY_URL_NUM = '2361076'

BASE_URL = 'https://basecamp.com/{}/api/v1/'
MY_URL = BASE_URL.format(MY_URL_NUM)

def send_request(url):
    return requests.get(url,auth=AUTH).json()

def get_projects():
    req = BASE_URL + 'projects.json'
    return send_request(req)

def get_me():
    req = BASE_URL + 'people/me.json'
    return send_request(req)

def get_my_todos():
    me = get_me()
    return send_request(me['assigned_todos']['url'])

def get_each_todo(todos=None):
    if todos is None:
        todos = get_my_todos()
    rtn = []
    for t in todos:
        rtn.append(send_request(t['url']))

    return rtn

def get_url(itm):
    return itm['url']

def get_project(project_id):
    url = BASE_URL + 'projects/{}.json'.format(project_id)
    return send_request(url).json()


if __name__ == "__main__":
    print [x  for x in get_projects().json()][0]

from core import make_api_url, send_request, get_auth

# active todos from project
def get_active_project_todo_lists(account_num,project_id):
    return send_request(make_api_url(account_num,'projects',project_id,'todolists'),get_auth())

# complete todos for project
def get_complete_project_todo_lists(account_num,project_id):
    return send_request(make_api_url(account_num,'projects',project_id,'todolists','completed'),get_auth())

# active todos for all projects
def get_all_active_todo_lists(account_num):
    return send_request(make_api_url(account_num,'todolists'),get_auth())

# complete todos for all projects
def get_all_complete_todo_lists(account_num):
    return send_request(make_api_url(account_num,'todolists','completed'),get_auth())

# get todolists assigned to person
def get_todo_lists_for_person(account_num,person_id):
    return send_request(make_api_url(account_num,'people',person_id,'assigned_todos'),get_auth())

# get specific todolist, must specify project and todolist
def get_todo_list(account_num,project_id,todolist_id):
    return send_request(make_api_url(account_num,'projects',project_id,'todolists',todolist_id),get_auth())

def get_todo(account_num,project_id,todo_id):
    return send_request(make_api_url(account_num,'projects',project_id,'todos',todo_id),get_auth())


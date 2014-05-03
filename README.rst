--------------------------------
Python Wrapper for Basecamp Next
--------------------------------


    ++++++++++++++++++++++++++++++++
    api wrapper works for almost all 
    of the new api
    ++++++++++++++++++++++++++++++++
    
    for these functions to work you need to have a file with your
    basecamp user_id and password like this 
    
    user_id
    password
    
    the file needs to be named bcnxt/new_bc/auth.txt
    
    this is how the functions connect to your account

============
get projects
============

    projects = new_bc.projects.get_all_projects(BCACCNT)

=========
get todos
=========

    todos = new_bc.todo_lists.get_all_active_todo_lists(BCACCNT)

==========
get people
==========
    
    person = new_bc.people.get_person(BCACCNT,person_id)

============
get yourself
============
    
    me = new_bc.people.get_me(BCACCNT)



    ++++++++++++++++++++++++++++++++
    or to make any basecamp api call
    ++++++++++++++++++++++++++++++++

    from new_bc.core import send_request,make_api_url,get_auth

    response = send_request(make_api_url(BASECAMP_ACCOUNT_NUM,API_ARGS),get_auth())




Everything below this line is proposed
+++++++++++++++++++++++++++++++++++++++
    ==========================
    to connect to your account
    ==========================

    from bcnxt import BaseCamp
    bc = BaseCamp()
    bc.auth = ('basecamp_id', 'basecamp_pw')
    bc.connect() => if connected returns true

    ========================================
    to get your basecamp account call get_me
    ========================================

    bc.get_me()
    ie: me = bc.get_me()


    =====================
    Then to get your name
    =====================

    print me['name'] => your name


    =================
    to get your todos
    =================

    todos = bc.get_my_todos()

    
    ====================
    to get your messages
    ====================

    messages = bc.get_my_messages()

    
    ====================
    to get your projects
    ====================

    projects = bc.get_my_projects()

    
    
    you see where this is going right?
    -----------------------------------


================================
Python Wrapper for Basecamp Next
================================

    to connect to your account
    --------------------------

    from bcnxt import BaseCamp
    bc = BaseCamp()
    bc.auth = ('basecamp_id', 'basecamp_pw')
    bc.connect() => if connected returns true

    to get your basecamp account call
    ---------------------------------

    bc.get_me()
    ie: me = bc.get_me()

    Then to get your name
    ---------------------

    print me['name'] => your name

    
    to get your todos
    ------------------

    todos = bc.get_my_todos()

    
    to get your messages
    --------------------

    messages = bc.get_my_messages()

    
    to get your projects
    ---------------------

    projects = bc.get_my_projects()

    
    
    you see where this is going right?



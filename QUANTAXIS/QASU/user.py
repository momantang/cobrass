from QUANTAXIS.QAUtil.QALogs import QA_util_log_info


def QA_user_sign_in(name, password, client):
    coll = client.quantaxis.user_list
    cursor = coll.find({'username': name, 'password': password})
    if cursor.count() > 0:
        QA_util_log_info('success login! your username is : %s' % name)
        return cursor
    else:
        QA_util_log_info('Failed to login please check your password')
        return None


def QA_user_sign_up(name, password, client):
    coll = client.quantaxis.user_list
    if coll.find({'username': name}).count() > 0:
        print(name)
        QA_util_log_info('user name is already exist')
        return False
    else:
        coll.insert({'username': name, 'password': password})
        QA_util_log_info('Success sign in! please login in')
        return True

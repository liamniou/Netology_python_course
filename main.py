import requests
import time
import json
import codecs

def contact_api(method, params):
    ACCESS_TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'
    VERSION = '5.73'
    url = 'https://api.vk.com/method/{0}'.format(method)
    params_dict = {
        'access_token': ACCESS_TOKEN,
        'version': VERSION
    }

    params_dict.update(params)
    request = requests.get(url, params=params_dict).json()
    time.sleep(0.35)
    try:
        response = request['response']
        return response
    except KeyError:
        return []

def get_user(username):
    user = contact_api('users.get', {'user_ids': username})[0]
    return user

def get_friends(user_id):
    friends = contact_api('friends.get', {'user_id': user_id})
    return friends

def get_groups(user_id):
    deactivated = None
    try:
        deactivated = get_user(user_id)['deactivated']
    except KeyError:
        pass

    if deactivated:
        return []
    else:
        groups = contact_api('groups.get', {'user_id': user_id})
        return groups

def create_list_of_friends_groups(friends):
    friends_groups = []
    number_of_friends = len(friends)
    for counter, element in enumerate(friends):
        friends_groups += get_groups(element)
        print('Progress: {0}/{1} friends analyzed...'.format(counter+1, number_of_friends))
    return friends_groups

def get_data_about_groups(group_ids):
    groups_data = contact_api('groups.getById', {'group_ids': str(group_ids), 'fields': 'members_count'})
    return groups_data

if __name__ == '__main__':
    target_user = input('Введите ник-нейм или id пользователя: ')
    user_id = str(get_user(target_user)['uid'])
    friends = get_friends(user_id)
    target_user_groups = get_groups(user_id)
    friends_groups = create_list_of_friends_groups(friends)
    only_target_user_groups = set(target_user_groups).difference(set(friends_groups))
    groups_data = get_data_about_groups(only_target_user_groups)
    with codecs.open('groups.json', 'w', encoding='utf-8') as file:
        json.dump(groups_data, file, ensure_ascii=False, indent=4)
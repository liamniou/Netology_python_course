import requests

def get_friends(id):
    url = 'https://api.vk.com/method/friends.get?user_id=' + id + '&v=5.52'
    friends_profile_1 = (requests.get(url).json())['response']['items']
    return friends_profile_1

def find_intersection(id_1, id_2):
    list_1 = get_friends(id_1)
    list_2 = get_friends(id_2)
    intersection = list(set(list_1).intersection(list_2))
    print('Список общих друзей:')
    for item in intersection:
        print('{0}, ссылка на страницу: https://vk.com/id{0}'.format(item))

if __name__ == '__main__':
    find_intersection('74991200', '5699547')
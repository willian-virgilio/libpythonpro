import requests


def buscar_avatar():
    """
    Busca o avatar de ym usuário no Github
    :param usuario: srt com nome do usuario
    :return:str com o link do avatar
    """
    url = f'https://api.github.com/users/willian-virgilio'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar())


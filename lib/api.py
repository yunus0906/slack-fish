import requests

def get_public_holidays(year, country_code):
    """
    API 获取公共节假日
    """
    api = f"https://date.nager.at/api/v3/publicholidays/{year}/{country_code}"
    response = requests.get(api)
    data = response.json()
    return data


def get_daily():
    """
    获取每日一句
    """
    try:
        response = requests.get("https://oiapi.net/API/Daily")
        return {
            'data': response.json()['message'],
        }
    except requests.exceptions.RequestException as e:
        return {
            'data': '她本来就很普通，只不过是你的爱给她镀上了一层光。',
        }

def get_kfc_v_wo50():
    """
    获取疯狂星期四
    """
    try:
        response = requests.get("https://oiapi.net/API/KFC/")
        return {
            'data': response.json()['message'],
        }
    except requests.exceptions.RequestException as e:
        return {
            'data': '她本来就很普通，只不过是你的爱给她镀上了一层光。',
        }

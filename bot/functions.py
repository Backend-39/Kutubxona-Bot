import requests

base_url="http://127.0.0.1:8000/bot/api"

def check_bot_user(telegram_id):
    r=requests.get(
        url=f"{base_url}/bot-users/{telegram_id}/"
    )
    return r.status_code == 200

def add_bot_user(telegram_id,username):
    r=requests.post(
        url=f"{base_url}/bot-users/",
        data={
            "id": telegram_id,
            "username": username
        }
    )
    return r.status_code == 201

def check_registration(telegram_id):
    r=requests.get(
        url=f"{base_url}/bot-users/infos/{telegram_id}/"
    )
    return r.status_code == 200

def register(telegram_id,ism,familiya,otasining_ismi,jinsi,guruh,kurs,tel):
    r=requests.post(
        url=f"{base_url}/bot-users/infos/",
        data={
            "bot_user": telegram_id,
            "ism": ism,
            "familiya": familiya,
            "otasining_ismi": otasining_ismi,
            "jinsi": jinsi,
            "guruh": guruh,
            "kurs": kurs,
            "tel": tel
        }
    )
    return r.status_code == 201

def get_user_info(telegram_id):
    r=requests.get(
        url=f"{base_url}/bot-users/infos/{telegram_id}/"
    )
    if r.status_code == 200:
        return r.json()
    else:
        return None
    
def get_kitoblar():
    r=requests.get(
        url=f"{base_url}/kitoblar/"
    )
    if r.status_code == 200:
        return r.json()
    else:
        return None
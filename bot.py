import requests

TOKEN = '5888802954:AAG1jeTE-CAQD2H7hFRje-CH9Yj_Yd6I7_o'

# get last update data -> update_id, chat_id, text
def last_update_data():
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    if response.status_code == 200:
        data = response.json()
        last_update = data['result'][-1]
        update_id = last_update['update_id']
        chat_id = last_update['message']['from']['id']
        text = last_update['message']['text']

        return update_id, chat_id, text

# send message
def send_message(chat_id, text):
    payload = {
        'chat_id': chat_id,
        'text': text,
    }
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', params=payload)

last_update_id, _, _ = last_update_data()

while True:
    current_update_id, chat_id, text = last_update_data()

    if last_update_id != current_update_id:
        send_message(chat_id, text)
        last_update_id = current_update_id

import requests

TOKEN = '5868643108:AAE5z7rOQZQ1FpTer2IAL7sGaKBpwtnRSxU'

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

last_update_id = -1

while True:
    current_update_id, chat_id, text = last_update_data()
    print(f"update: {last_update_id}, last update: {current_update_id}")
    if last_update_id != current_update_id:
        send_message(chat_id, text)
        last_update_id = current_update_id

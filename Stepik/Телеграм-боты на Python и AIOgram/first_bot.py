import requests
import time


BOT_TOKEN: str = '6181239100:AAGqBfSe-0Y-Y1o_hoFwwBzbsevrz0gj_c4'
API_URL: str = 'https://api.telegram.org/bot'
MAX_COUNTER = 100
OFFSET = -2
SEND_TEXT = 'Ура! Классный апдейт!'


class TelegramBot:
    def __init__(self, token: str, api_url: str, max_counter: int, offset: int) -> None:
        self.token: str = token
        self.api_url: str = api_url
        self.max_counter: int = max_counter
        self.offset: int = offset
        self.counter: int = 0
        self.chat_id: int = 0

    def print_url(self) -> None:
        print(self.api_url)
        print(self.max_counter)
        return None

    def send_message(self, send_text: str) -> None:

        chat_id: int = 0

        while self.counter < self.max_counter:
            print(f'attempt = {self.counter}')
            updates = requests.get(f'{self.api_url}{self.token}/getUpdates?offset={self.offset + 1}').json()
            if updates['result']:
                for result in updates['result']:
                    self.offset = result['update_id']
                    chat_id = result['message']['from']['id']
                requests.get(f'{self.api_url}{self.token}/sendMessage?chat_id={chat_id}&text={send_text}')
            time.sleep(2)
            self.counter += 1
        return None


telegrambot = TelegramBot(BOT_TOKEN, API_URL, MAX_COUNTER, OFFSET)
telegrambot.send_message(SEND_TEXT)
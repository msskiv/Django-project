import requests
from .models import Telesettings


def sendTelegram(customer_name, customer_phone):
    if Telesettings.objects.get(pk=2):
        settings = Telesettings.objects.get(pk=2)
        token = str(settings.tlg_token)
        chat_id = str(settings.tlg_chat)
        text = str(settings.tlg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('<name>') and text.rfind('<phone>'):
            part_1 = text[0:text.find('<name>')]
            part_2 = text[text.find('<name>')+6:text.rfind('<phone>')]
            part_3 = text[text.rfind('<phone>'):-7]
            text_contact = part_1 + customer_name + part_2 + customer_phone + part_3
        else:
            text_contact = text
        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_contact
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки.')
            if req.status_code == 500:
                print('Ошибка 500.')
            else:
                print('Сообщение успешно отправлено.')
    else:
        pass

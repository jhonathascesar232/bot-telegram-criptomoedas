from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from cotacaodecriptomoedasbot.bot import state_manager
from cotacaodecriptomoedasbot.models import TelegramState
from cotacaodecriptomoedasbot.bot import TelegramBot

import logging

logging.basicConfig(
    filename='log.log',
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s: %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)
logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)


def inverte_texto(mensagem):
    '''
    inverte texto
    '''
    return mensagem[::-1]


def dados_da_msn(update):
    from pprint import pprint

    data = {}

    palavras = update.get_message()
    if palavras == None:
        data['palavras'] = False
    else:
        palavras = palavras.get_text().split(" ")
        data['palavras'] = palavras
        data['chat_id'] = update.get_chat().get_id()
        # pprint(data)
        data['comando'] = palavras[0]

        data['mensagem'] = " ".join(
            palavras[1:]) if len(palavras) > 1 else False

        if data['mensagem'] == False:
            return data

    return data


def buscaCep(param):
    from script import cep
    dic = cep.busca_cep(**{"PARM": param})
    return dic


def helloWorld():
    return 'Hello, eu sou um bot!'


@processor(state_manager, from_states=state_types.All)
def hello_world(bot, update: Update, state: TelegramState):
    dados = dados_da_msn(update)

    try:
        comando = dados['comando'].lower()
        chat_id = dados['chat_id']

        if comando == '/start':
            response = '{} {}'.format(
                helloWorld(),
                (update.get_chat().get_username())
            )
        if comando == '/infocep':
            if dados['mensagem']:
                cep = dados['mensagem']
                dic = buscaCep(cep)
                response = 'Cep: {}\n'.format(dic['cep'])
                response += 'Logradouro: {}\n'.format(dic['logradouro'])
                response += 'Bairro: {}\n'.format(dic['bairro'])
                response += 'Cidade: {}'.format(dic['cidade'])
            else:
                response = 'INFO: /infocep (numero do cep)!'
        bot.sendMessage(chat_id, response)
        return
    except Exception as e:
        logging.error(f'Erro: {e}')
        return

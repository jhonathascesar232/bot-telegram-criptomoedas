from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from cotacaodecriptomoedasbot.bot import state_manager
from cotacaodecriptomoedasbot.models import TelegramState
from cotacaodecriptomoedasbot.bot import TelegramBot


def inverte_texto(mensagem):
    '''
    inverte texto
    '''
    return mensagem[::-1]


def dados_da_msn(update):
    data = {}

    palavras = update.get_message().get_text().split(" ")
    chat_id = update.get_chat().get_id()
    comando = palavras[0]
    mensagem = " ".join(palavras[1:]) if len(palavras) > 1 else False

    data = {
        'palavras': palavras,
        'chat_id': chat_id,
        'comando': comando,
        'mensagem': mensagem
    }

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
    comando = dados['comando'].lower()
    chat_id = dados['chat_id']

    if comando == '/start':
        response = helloWorld()
    if comando == '/infocep':
        cep = dados['mensagem']
        dic = buscaCep(cep)

        response = 'Cep: {}\n'.format(dic['cep'])
        response += 'Logradouro: {}\n'.format(dic['logradouro'])
        response += 'Bairro: {}\n'.format(dic['bairro'])
        response += 'Cidade: {}'.format(dic['cidade'])

    bot.sendMessage(chat_id, response)
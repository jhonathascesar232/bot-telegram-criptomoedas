from django_tgbot.decorators import processor
from django_tgbot.state_manager import message_types, update_types, state_types
from django_tgbot.types.update import Update
from .bot import state_manager
from .models import TelegramState
from .bot import TelegramBot


@processor(state_manager, from_states=state_types.All)
def hello_world(bot, update: Update, state: TelegramState):

    chat_id = update.get_chat().get_id()
    comando = update.get_message().get_text().split(" ")[0]
    text = update.get_message().get_text()
    ##
    print(update.get_chat().__str__())
    comandos = bot.getMyCommands()
    print(f'** comandos -> {comandos}')
    ###

    bot.sendMessage(chat_id, f'Texto invertido:\n{text[::-1]}')

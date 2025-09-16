import sys
from pathlib import Path
import telebot

PROJ_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJ_DIR))
from settings import settings

from src.utils.logger import StdLogger
from src.utils.alert import StdAlertManager

from src.orders.service import OrderMapper
from src.orders.service import GetOrderUseCase
from src.orders.service import ConfirmOrderUseCase
from src.orders.service import OrderNotFound

from src.orders.controller import OrderController
from src.orders.repository import InMemoryOrderRepository


logger = StdLogger()
alert = StdAlertManager()

order_repository = InMemoryOrderRepository(logger, alert)
order_mapper = OrderMapper()
get_order_use_case = GetOrderUseCase(
    logger,
    alert,
    order_repository,
    order_mapper,
)
confirm_order_use_case = ConfirmOrderUseCase(
    logger,
    alert,
    order_repository,
    order_mapper,
)
controller = OrderController(
    get_order_use_case,
    confirm_order_use_case,
)


bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=["order"])
def handle_get_order(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Используй: /order <order_id>")
        return
    order_id = args[1]
    try:
        order_dto = controller.get_order_by_id(order_id)
        bot.reply_to(message, str(order_dto.model_dump()))
    except OrderNotFound as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")


@bot.message_handler(commands=["confirm"])
def handle_confirm_order(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Используй: /confirm <order_id>")
        return
    order_id = args[1]
    try:
        controller.confirm_order_by_id(order_id)
        bot.reply_to(message, "Заказ подтверждён!")
    except OrderNotFound as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")


if __name__ == "__main__":
    bot.polling(none_stop=True)

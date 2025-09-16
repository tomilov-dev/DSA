import sys
from pathlib import Path
from flask import Flask
from flask import jsonify

PROJ_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJ_DIR))
from src.utils.logger import StdLogger
from src.utils.alert import StdAlertManager

from src.orders.service import OrderMapper
from src.orders.service import OrderNotFound
from src.orders.service import GetOrderUseCase
from src.orders.service import ConfirmOrderUseCase

from src.orders.controller import OrderController
from src.orders.repository import InMemoryOrderRepository


app = Flask(__name__)

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


@app.errorhandler(OrderNotFound)
def handle_order_not_found(error):
    return jsonify({"error": str(error)}), 404


@app.route("/orders/<order_id>", methods=["GET"])
def get_order(order_id: str):
    order_dto = controller.get_order_by_id(order_id)
    return jsonify(order_dto.model_dump())


@app.route("/orders/<order_id>/confirm", methods=["POST"])
def confirm_order(order_id: str):
    controller.confirm_order_by_id(order_id)
    return jsonify({"status": "confirmed"})


if __name__ == "__main__":
    app.run(debug=True)

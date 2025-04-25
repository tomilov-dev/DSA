from abc import ABC
from abc import abstractmethod


class PaymentServiceInterface(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> dict:
        pass


class OldPaymentService:
    def process_payment(self, amount: float, currency: str) -> bool:
        return True


class OldPaymentServiceAdapter(PaymentServiceInterface):
    def __init__(self, payment_service: OldPaymentService) -> None:
        self.payment_service = payment_service

    def process_payment(self, amount: float, currency: str) -> dict:
        status = self.payment_service.process_payment(amount, currency)
        return {
            "status": "success" if status else "failed",
            "message": "payment successful" if status else "payment failed",
        }


class NewPaymentService:
    def make_payment(self, payment_info: dict) -> dict:
        return {"status": "success", "message": "payment successful"}


class NewPaymentServiceAdapter(PaymentServiceInterface):
    def __init__(self, payment_service: NewPaymentService) -> None:
        self.payment_service = payment_service

    def process_payment(self, amount: float, currency: str) -> dict:
        return self.payment_service.make_payment(
            {"amount": amount, "currency": currency}
        )


class ExternalPaymentService:
    def execute(self, amount: float, currency: str) -> str:
        return "success"


class ExternalPaymentServiceAdapter:
    def __init__(self, payment_service: ExternalPaymentService) -> None:
        self.payment_service = payment_service

    def process_payment(self, amount: float, currency: str) -> dict:
        status = self.payment_service.execute(amount, currency)
        return {
            "status": "success" if status == "success" else "failed",
            "message": (
                "payment successful" if status == "success" else "payment failed"
            ),
        }


def client_code():
    old_service = OldPaymentService()
    new_service = NewPaymentService()
    external_service = ExternalPaymentService()

    adapter_old = OldPaymentServiceAdapter(old_service)
    adapter_new = NewPaymentServiceAdapter(new_service)
    adapter_external = ExternalPaymentServiceAdapter(external_service)

    amount = 100.0
    currency = "USD"
    print(
        f"Payment result (old service): {adapter_old.process_payment(amount, currency)}"
    )
    print(
        f"Payment result (new service): {adapter_new.process_payment(amount, currency)}"
    )
    print(
        f"Payment result (external service): {adapter_external.process_payment(amount, currency)}"
    )


if __name__ == "__main__":
    client_code()

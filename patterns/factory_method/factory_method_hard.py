from abc import ABC
from abc import abstractmethod


class Payment(ABC):
    @abstractmethod
    def authorize(self) -> None:
        pass

    @abstractmethod
    def capture(self) -> None:
        pass

    @abstractmethod
    def refund(self) -> None:
        pass


class PaymentCreator(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        pass

    def process_authorization(self, payment: Payment) -> None:
        payment.authorize()

    def process_capture(self, payment: Payment) -> None:
        payment.capture()

    def process_refund(self, payment: Payment) -> None:
        payment.refund()


class CreditCardPayment(Payment):
    def authorize(self) -> None:
        print("CreditCard payment authorization")

    def capture(self) -> None:
        print("CreditCard payment capture")

    def refund(self) -> None:
        print("CreditCard payment refund")


class PayPalPayment(Payment):
    def authorize(self) -> None:
        print("PayPal payment authorization")

    def capture(self) -> None:
        print("PayPal payment capture")

    def refund(self) -> None:
        print("PayPal payment refund")


class BankTransferPayment(Payment):
    def authorize(self) -> None:
        print("BankTransfer payment authorization")

    def capture(self) -> None:
        print("BankTransfer payment capture")

    def refund(self) -> None:
        print("BankTransfer payment refund")


class CreditCardPaymentCreator(PaymentCreator):
    def create_payment(self) -> CreditCardPayment:
        return CreditCardPayment()


class PayPalPaymentCreator(PaymentCreator):
    def create_payment(self) -> PayPalPayment:
        return PayPalPayment()


class BankTransferPaymentCreator(PaymentCreator):
    def create_payment(self) -> BankTransferPayment:
        return BankTransferPayment()


def client_code(creator: PaymentCreator) -> None:
    payment = creator.create_payment()
    creator.process_authorization(payment)
    creator.process_capture(payment)
    creator.process_refund(payment)


if __name__ == "__main__":
    print("App: Launched with the CreditCardPaymentCreator.")
    client_code(CreditCardPaymentCreator())
    print("\n")

    print("App: Launched with the PayPalPaymentCreator.")
    client_code(PayPalPaymentCreator())
    print("\n")

    print("App: Launched with the BankTransferPaymentCreator.")
    client_code(BankTransferPaymentCreator())

from abc import ABC, abstractmethod


class MessageProcessor(ABC):
    @abstractmethod
    def process(self, message: str) -> str:
        pass


class BaseMessageProcessor(MessageProcessor):
    def process(self, message: str) -> str:
        return message


class MessageProcessorDecorator(MessageProcessor):
    def __init__(self, processor: MessageProcessor) -> None:
        self.processor = processor

    def process(self, message: str) -> str:
        return self.processor.process(message)


class PrefixDecorator(MessageProcessorDecorator):
    def __init__(self, processor: MessageProcessor, prefix: str) -> None:
        super().__init__(processor)
        self.prefix = prefix

    def process(self, message: str) -> str:
        message = self.prefix + message
        return super().process(message)


class SuffixDecorator(MessageProcessorDecorator):
    def __init__(self, processor: MessageProcessor, suffix: str) -> None:
        super().__init__(processor)
        self.suffix = suffix

    def process(self, message: str) -> str:
        message = super().process(message)
        message += self.suffix
        return message


class UppercaseDecorator(MessageProcessorDecorator):
    def process(self, message: str) -> str:
        message = super().process(message)
        return message.upper()


def client_code():
    base_processor = BaseMessageProcessor()

    processor_with_prefix = PrefixDecorator(base_processor, "Hello, ")
    processor_with_suffix = SuffixDecorator(processor_with_prefix, "!")
    processor_with_uppercase = UppercaseDecorator(processor_with_suffix)

    message = "world"
    processed_message = processor_with_uppercase.process(message)
    print(processed_message)  # Ожидаемый вывод: "HELLO, WORLD!"

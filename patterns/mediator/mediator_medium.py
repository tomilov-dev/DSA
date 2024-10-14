from abc import ABC
from abc import abstractmethod


class IParticipant(ABC):
    def __init__(self, mediator: "Mediator") -> None:
        self.mediator = mediator
        self.mediator.register(self)

    @abstractmethod
    def send_event(self, event: str) -> None:
        pass

    @abstractmethod
    def receive_event(self, event: str) -> None:
        pass


class Speaker(IParticipant):
    def __init__(self, mediator: "Mediator") -> None:
        super().__init__(mediator)
        self.speaking = False

    def send_event(self, event: str) -> None:
        self.mediator.notify(self, event)

    def request_to_speak(self) -> None:
        self.send_event("Request to speak")
        self.speaking = True

    def receive_event(self, event: str) -> None:
        if event == "Request to speak":
            self.speaking = False
        elif event == "Session started":
            print("Prepare to speak")
        elif "Question asked" in event and self.speaking:
            print("Answer the question")


class Attendee(IParticipant):
    def send_event(self, event: str) -> None:
        self.mediator.notify(self, event)

    def send_question(self, question: str) -> None:
        self.send_event(f"Question asked: {question}")

    def receive_event(self, event: str) -> None:
        if event == "Session started":
            print("Listen")


class Organizer(IParticipant):
    def notify_session_start(self) -> None:
        self.send_event("Session started")

    def send_event(self, event: str) -> None:
        self.mediator.notify(self, event)

    def receive_event(self, event: str) -> None:
        if event == "Request to speak":
            print("Speaker is speaking")
        elif event == "Session started":
            print("Session has started")


class Mediator(ABC):
    @abstractmethod
    def register(self, participant: IParticipant) -> None:
        pass

    @abstractmethod
    def notify(self, sender: IParticipant, event: str) -> None:
        pass


class ConferenceMediator(Mediator):
    def __init__(self) -> None:
        self.participants: list[IParticipant] = []

    def register(self, participant: IParticipant) -> None:
        self.participants.append(participant)

    def notify(self, sender: IParticipant, event: str) -> None:
        for participant in self.participants:
            if participant != sender:
                participant.receive_event(event)


def client_code():
    mediator = ConferenceMediator()

    speaker = Speaker(mediator)
    attendee = Attendee(mediator)
    organizer = Organizer(mediator)

    speaker.request_to_speak()
    attendee.send_question("What is the future of AI?")
    organizer.notify_session_start()

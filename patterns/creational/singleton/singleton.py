class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not self._initialized:
            self.value = value
            self._initialized = True


def client_code():
    singleton1 = Singleton("First Instance")
    print(singleton1.value)  # Output: First Instance

    singleton2 = Singleton("Second Instance")
    print(singleton2.value)  # Output: First Instance

    print(singleton1 is singleton2)  # Output: True


if __name__ == "__main__":
    client_code()

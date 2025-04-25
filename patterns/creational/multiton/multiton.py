class Multiton:
    _instances = {}
    _initialized = False

    def __new__(cls, key, *args, **kwargs):
        if key not in cls._instances:
            cls._instances[key] = super().__new__(cls)
        return cls._instances[key]

    def __init__(self, key, value):
        if not self._initialized:
            self.key = key
            self.value = value
            self._initialized = True


def client_code():
    multiton1 = Multiton("key1", "First Instance")
    print(multiton1.key, multiton1.value)  # Output: key1 First Instance

    multiton2 = Multiton("key2", "Second Instance")
    print(multiton2.key, multiton2.value)  # Output: key2 Second Instance

    multiton3 = Multiton("key1", "Third Instance")
    print(multiton3.key, multiton3.value)  # Output: key1 First Instance

    print(multiton1 is multiton3)  # Output: True
    print(multiton1 is multiton2)  # Output: False


if __name__ == "__main__":
    client_code()

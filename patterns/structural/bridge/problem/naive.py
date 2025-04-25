"""
Решение задачи управления девайсами (наивный подход)
"""


## Мы имеем два устройства
class TV:
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF")

    def set_volume(self, volume: float):
        print(f"TV volume set to {volume}")


class Radio:
    def turn_on(self):
        print("Radio is now ON")

    def turn_off(self):
        print("Radio is now OFF")

    def set_volume(self, volume: float):
        print(f"Radio volume set to {volume}")


def client_code():
    ## Для управления каждый устройством нам необходимо работать с его классом напрямую
    ## В клиентском коде могут быть видны лишние или опасные детали реализации
    tv = TV()
    tv.turn_on()
    tv.set_volume(15)
    tv.turn_off()

    radio = Radio()
    radio.turn_on()
    radio.set_volume(20)
    radio.turn_off()


if __name__ == "__main__":
    client_code()

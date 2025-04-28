class Lighting:
    def __init__(self) -> None:
        self._light = True
        self._brightness = 100

    def on(self) -> None:
        self._light = True

    def off(self) -> None:
        self._light = False

    def dim(self, brightness: int) -> None:
        self._brightness = brightness

    def get_status(self) -> tuple[bool, int]:
        return self._light, self._brightness


class ClimateControl:
    def __init__(self) -> None:
        self.temperature = 24
        self.conditioner = False
        self.heater = False

    def conditioner_toggle(self) -> None:
        self.conditioner = not self.conditioner

    def heater_toggle(self) -> None:
        self.heater = not self.heater

    def set_temperature(self, temperature: int) -> None:
        self.temperature = temperature

    def get_status(self) -> tuple[int, bool, bool]:
        return self.temperature, self.conditioner, self.heater


class Security:
    def __init__(self) -> None:
        self.alarm = True

    def toggle_alarm(self) -> None:
        self.alarm = not self.alarm

    def status(self) -> bool:
        return self.alarm


class SmartHomeFacade:
    def __init__(
        self,
        lighting: Lighting,
        climate_control: ClimateControl,
        security: Security,
    ) -> None:
        self.lighting = lighting
        self.climate_control = climate_control
        self.security = security

    def light_on(self) -> None:
        self.lighting.on()

    def light_off(self) -> None:
        self.lighting.off()

    def light_dim(self, brightness: int) -> None:
        self.lighting.dim(brightness)

    def conditioner_toggle(self) -> None:
        self.climate_control.conditioner_toggle()

    def heater_toggle(self) -> None:
        self.climate_control.heater_toggle()

    def set_temperature(self, temperature: int) -> None:
        self.climate_control.set_temperature(temperature)

    def toggle_alarm(self) -> None:
        self.security.toggle_alarm()

    def status(self) -> bool:
        return self.security.status()

    def turn_on_all_systems(self) -> None:
        self.light_on()
        self.climate_control.set_temperature(24)
        if not self.climate_control.conditioner:
            self.conditioner_toggle()
        if not self.climate_control.heater:
            self.heater_toggle()
        if not self.security.status():
            self.toggle_alarm()

    def turn_off_all_systems(self) -> None:
        self.light_off()
        if self.climate_control.conditioner:
            self.conditioner_toggle()
        if self.climate_control.heater:
            self.heater_toggle()
        if self.security.status():
            self.toggle_alarm()

    def get_system_status(self) -> dict:
        light_status = self.lighting.get_status()
        climate_status = self.climate_control.get_status()
        security_status = self.security.status()
        return {
            "lighting": light_status,
            "climate_control": climate_status,
            "security": security_status,
        }

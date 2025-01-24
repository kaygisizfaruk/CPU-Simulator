#CPU Simulator
class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0 for i in range(32)]
        self.history_registers = [0 for i in range(10)]
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ""

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

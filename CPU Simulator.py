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
        self.update_display("Welcome to the Ultra Super Calculator")


    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value, 2)
        print(f"Stored {self.number_registers[self.numbers_index]} to register {self.numbers_index}")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value
    
    def store_to_history_register(self, result):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        result = num1 + num2
        self.store_to_history_register(result)
        self.update_display(f"Result: {result}") 
    
    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        result = num1 - num2
        self.store_to_history_register(result)
        self.update_display(f"Result: {result}")
    
    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        result = num1 * num2
        self.store_to_history_register(result)
        self.update_display(f"Result: {result}")
    
    def divide(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        result = 0
        if num2 != 0:
            result = int(num1 / num2)
        else:
            result = "Error: Division by zero"
        return result
    
    def get_last_calculation(self):
        self.temp_history_index -= 1
        last_value = "The last value is: " + int(self.history_registers[self.temp_history_index], 2)
    


your_calculator = UltraSuperCalculator("Ultra Super Calculator")

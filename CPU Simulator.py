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
    
    def binary_reader(self, instruction):
        if len(instruction) != 32:
            self.update_display("Error: Instruction length must be 32 bits")
            return
        opcode = instruction[0:6]
        source_one = instruction[6:11]
        source_two = instruction[11:16]
        store = instruction[16:26]
        function_code = instruction[26:]
        if opcode == "000001":
            self.store_value_to_register(store)
            return
        elif opcode == "100001":
            self.get_last_calculation()
            return
        elif opcode != "000000":
            self.update_display("Error: Invalid opcode")
            return
        result = 0
        if function_code == "100000":
            result = self.add(source_one, source_two)
        elif function_code == "100010":
            result = self.subtract(source_one, source_two)
        elif function_code == "011000":
            result = self.multiply(source_one, source_two)
        elif function_code == "011010":
            result = self.divide(source_one, source_two)
        else:
            self.update_display("Error: Invalid function code")
            return
        self.store_to_history_register(result)
        self.update_display(f"Result: {result}")

your_calculator = UltraSuperCalculator("Ultra Super Calculator")
your_calculator.binary_reader("00000100000000000000000101000000")
your_calculator.binary_reader("00000100000000000000001010000000")
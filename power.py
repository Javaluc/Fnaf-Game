class PowerManagement:
    def __init__(self, max_power=100):
        self.current_power = max_power
        self.max_power = max_power
        self.door_open = False

    def drain_power(self, amount):
        if amount < 0:
            raise ValueError("Power drain amount must be non-negative.")
        self.current_power = max(0, self.current_power - amount)
        print(f"Power drained: {amount}. Current power: {self.current_power}")

    def open_door(self):
        if self.current_power > 0:
            self.door_open = True
            self.drain_power(10)  # Drains 10 units of power every time the door opens
            print("Door opened.")
        else:
            print("Not enough power to open the door.")

    def close_door(self):
        if self.door_open:
            self.door_open = False
            print("Door closed.")
        else:
            print("The door is already closed.")

    def reset_power(self):
        self.current_power = self.max_power
        print("Power has been reset to maximum.")


# Example usage
if __name__ == '__main__':
    power_system = PowerManagement()
    power_system.open_door()
    power_system.close_door()
    power_system.drain_power(20)
    power_system.reset_power()
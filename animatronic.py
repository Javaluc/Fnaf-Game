class Animatronic:
    def __init__(self, name):
        self.name = name
        self.state = 'inactive'
        self.movement_pattern = 'stationary'

    def activate(self):
        self.state = 'active'
        print(f'{self.name} is now active.')

    def deactivate(self):
        self.state = 'inactive'
        print(f'{self.name} is now inactive.')

    def set_movement_pattern(self, pattern):
        self.movement_pattern = pattern
        print(f'{self.name} movement pattern set to {pattern}.')

    def move(self):
        if self.state == 'active':
            print(f'{self.name} is moving in a {self.movement_pattern} pattern.')
        else:
            print(f'{self.name} is inactive and cannot move.')

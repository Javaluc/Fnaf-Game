class Game:
    def __init__(self):
        self.states = []  # List to hold game states
        self.running = True  # Flag to indicate if the game is running

    def add_state(self, state):
        self.states.append(state)

    def change_state(self, state):
        self.states.append(state)

    def game_loop(self):
        while self.running:
            self.handle_events()  # Method to handle events
            self.update()  # Method to update game states
            self.draw()  # Method to draw the current state

    def handle_events(self):
        # Placeholder for event handling logic
        pass

    def update(self):
        # Placeholder for update logic for the current state
        pass

    def draw(self):
        # Placeholder for drawing the current state
        pass

from typing import List, Callable, Any

class Event:
    def __init__(self, point, type, other_data=None):
        self.point = point  # A point (x, y) in 2D space
        self.type = type  # Type of event (e.g., 'start', 'end', 'intersection')
        self.other_data = other_data  # Additional data relevant to the event

class SweepLine:
    def __init__(self, events: List[Event], event_handler: Callable[[Event], Any]):
        self.events = sorted(events, key=lambda event: (event.point[0], event.point[1]))
        self.event_handler = event_handler

    def process_events(self):
        """Processes all events in the sweep line algorithm."""
        for event in self.events:
            self.event_handler(event)

def handle_event(event: Event):
    # Define how to handle each event
    print(f"Processing {event.type} event at point {event.point}, additional data: {event.other_data}")

# Example usage
events = [
    Event((1, 2), 'start', 'data1'),
    Event((2, 3), 'end', 'data2'),
    Event((0, 1), 'intersection')
]

sweep_line = SweepLine(events, handle_event)
sweep_line.process_events()

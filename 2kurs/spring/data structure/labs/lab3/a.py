class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class EmergencyRoom:
    def __init__(self):
        self.queue = Queue()

    def add_patient_to_queue(self, patient):
        print(f"{patient} enters the emergency room queue.")
        self.queue.enqueue(patient)

    def process_patient(self):
        if not self.queue.is_empty():
            patient = self.queue.dequeue()
            print(f"{patient} is being examined.")
        else:
            print("No patients in the queue.")

# Example usage
emergency_room = EmergencyRoom()

# Patients arrive and join the emergency room queue
emergency_room.add_patient_to_queue("John")
emergency_room.add_patient_to_queue("Jane")
emergency_room.add_patient_to_queue("David")

# Process patients
emergency_room.process_patient()  # John is being examined
emergency_room.process_patient()  # Jane is being examined
emergency_room.process_patient()  # David is being examined
emergency_room.process_patient()  # No patients in the queue

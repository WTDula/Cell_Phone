class Cell_Phone:
    def __init__(self, model):
        self.model = model
        self.phone_number = ""
        self.on_vibrate = False
        self.contacts = {"name": "Brad"}
        self.messages = []

    def receive_message(self, text):
        self.messages.append(text)

    def toggle_vibrate(self):
        self.on_vibrate = not(self.on_vibrate)
        print("Vibrate has been toggled")

    def create_text_message(self, contact):
        if(self.contacts["name"] == contact): # check to see if contact parameter is in contacts dictionary
            outgoing_text = input(f"Please enter outgoing text message to {contact}: ")
            print(f"Outgoing text to {contact}: {outgoing_text}")
        else: # if contact not found in contacts dictionary
            print("Contact not found")


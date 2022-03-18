from cell_phone import Cell_Phone

my_cell = Cell_Phone("iPhone 8")

print(my_cell.contacts)

my_cell.receive_message("New phone, who dis?")
my_cell.receive_message("Oh hey! whats up man?")

for text in my_cell.messages:
    print(text)

my_cell.create_text_message("Brad")
my_cell.create_text_message("Scorpion")

my_cell.toggle_vibrate()

if(my_cell.on_vibrate):
    print("Cell phone is on vibrate.")
else:
    print("Cell phone is NOT on vibrate.")
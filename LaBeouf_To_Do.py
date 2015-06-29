from tkinter import *
from tkinter import ttk, simpledialog, messagebox
import random

# Motivational slogans
LaBeouf = ["Do it! Just do it!", "Don't let your dreams be dreams.",
 "Yesterday you said tomorrow., So just do it!", "Make your dreams come true. Just do it!",
  "If you're tired of starting over, stop giving up.", "YES YOU CAN! JUST DO IT! ",
   "Nothing is impossible...", "DO IT! JUST DO IT!", "What are you waiting for?!", 
   "Some people dream of success, while you’re going to wake up and work hard at it."]

root = Tk() # Make a root GUI window
root.title("THINGS TO JUST DO!")
entries = []

# I am not sure why this works as well as it does, but hey....it's great.
def add_new_item():
	"""This adds an item to the list."""
	
	x = simpledialog.askstring((random.choice(LaBeouf)), 'What are your dreams?')
	if 'entry1' not in globals():
		entry1 = ttk.Entry(default_to_do, width = 30)
		entry1.pack()
		entry1.insert(0, x)
		entries.append(entry1)
	else:
		messagebox.showwarning('Hmmm....something went wrong.'.format(random.choice(LaBeouf)))

def delete_item():
	"""Delete an item from the list and remove the entry placeholder."""

	item_to_delete = simpledialog.askstring((random.choice(LaBeouf)),
	 'What did you do?')
	for entry in entries:
		if entry.get() == item_to_delete:
			print('found it')
			entries.remove(entry)
			entry.forget()
			messagebox.showwarning('YOU DID IT!',
			 'I KNEW YOU COULD {0}!'.format(item_to_delete.upper()))

def print_all():
	"""Print all the things."""

	for number, entry in enumerate(entries, start = 1):
		if (len(entry.get()) > 0):
			messagebox.showwarning('DO IT! JUST DO IT!', '{0}){1}\n\n\t{2}'.format(number,
			 entry.get(), (random.choice(LaBeouf))))


######## Set up controls section #######
controls = ttk.Frame(root, height = 300, width = 400, relief = RAISED) # Make the side Frame
controls.pack()

###### Controls Buttons ######
# Add item button #
add_item_button = ttk.Button(controls, text = "DO WHAT?", command = add_new_item)
add_item_button.grid(column = 0, row = 0, stick = 'nw')
# Print Button #
print_button = ttk.Button(controls, text = 'PRINT THEM ALL!', command = print_all)
print_button.grid(column = 1, row = 0)
# Delete item button #
delete_item_button = ttk.Button(controls, text = "WHAT DID YOU DO?", command = delete_item)
delete_item_button.grid(column = 3, row = 0, stick = 'nw')

###### Main list frame #####
default_to_do = ttk.Frame(root, height = 300, width = 400, relief = SUNKEN) # Make the main body frame
default_to_do.pack()

###### Background image for main list ######
background_image = PhotoImage(file = 'LaBeouf_image.jpg')
background_label = Label(default_to_do, image = background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()

#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

FS = FileStorage()

# All States present
all_states = FS.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a State
new_state = State()
new_state.name = "California"
FS.new(new_state)
FS.save()
print("New State: {}".format(new_state))

# All States displayed
all_states = FS.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
FS.new(another_state)
FS.save()
print("Another State: {}".format(another_state))

# All States
all_states = FS.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Delete the new State from the database
FS.delete(new_state)

# Check for the results 
all_states = FS.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

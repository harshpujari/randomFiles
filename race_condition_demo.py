import threading
# Shared variable
counter = 0

# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(1000000):
        counter += 1

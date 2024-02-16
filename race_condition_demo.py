import threading
# Shared variable.
counter = 0

# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(1000000):
        counter += 1

# Create two threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of the counter
print("Final Counter Value:", counter)

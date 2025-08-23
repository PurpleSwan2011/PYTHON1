import time

# Start the timer
start_time = time.time()

# Loop example
for i in range(1000000):
    _ = i * 2  # Simulate some work

# End the timer
end_time = time.time()

# Calculate and display the duration
duration = end_time - start_time
print(f"Loop executed in {duration:.4f} seconds")

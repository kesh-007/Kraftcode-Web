import psutil

# Get memory usage
memory = psutil.virtual_memory()

print("Memory Usage:")
print(f"Total: {memory.total / (1024 ** 3):.2f} GB")
print(f"Available: {memory.available / (1024 ** 3):.2f} GB")
print(f"Used: {memory.used / (1024 ** 3):.2f} GB")
print(f"Percentage Used: {memory.percent:.2f}%")

# Get CPU information
cpu_info = psutil.cpu_percent(interval=1, percpu=True)

print("\nCPU Usage:")
for i, percent in enumerate(cpu_info):
    print(f"Core {i + 1}: {percent}%")

# Get disk usage
disk = psutil.disk_usage('/')

print("\nDisk Usage:")
print(f"Total: {disk.total / (1024 ** 3):.2f} GB")
print(f"Used: {disk.used / (1024 ** 3):.2f} GB")
print(f"Free: {disk.free / (1024 ** 3):.2f} GB")
print(f"Percentage Used: {disk.percent:.2f}%")

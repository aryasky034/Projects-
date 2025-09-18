import platform
import psutil

def get_system_info():
    # Get basic system information
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM": round(psutil.virtual_memory().total / (1024 ** 3), 2)  # Convert bytes to GB
    }
    
    return system_info

def display_info(info):
    print("Hardware Information:")
    print("----------------------")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    hardware_info = get_system_info()
    display_info(hardware_info)

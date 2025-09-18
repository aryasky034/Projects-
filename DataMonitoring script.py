import os
import time
import psutil
import matplotlib.pyplot as plt
from fpdf import FPDF
from getpass import getpass

# Constants
USERNAME = "admin"
PASSWORD = "password"
OUTPUT_PDF_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "activity_report.pdf")

# Function to authenticate user
def authenticate():
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    return username == USERNAME and password == PASSWORD

# Function to monitor system activity
def monitor_activity(duration):
    cpu_usage = []
    memory_usage = []
    disk_usage = []
    start_time = time.time()

    while time.time() - start_time < duration:
        cpu_usage.append(psutil.cpu_percent(interval=1))
        memory_usage.append(psutil.virtual_memory().percent)
        disk_usage.append(psutil.disk_usage('/').percent)       
        
    return cpu_usage, memory_usage, disk_usage

# Function to create a PDF report
def create_pdf(cpu_usage, memory_usage, disk_usage):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="User  Activity Report", ln=True, align='C')

    pdf.cell(200, 10, txt="CPU Usage (%)", ln=True)
    pdf.cell(200, 10, txt=str(cpu_usage), ln=True)

    pdf.cell(200, 10, txt="Memory Usage (%)", ln=True)
    pdf.cell(200, 10, txt=str(memory_usage), ln=True)

    pdf.cell(200, 10, txt="Disk Usage (%)", ln=True)
    pdf.cell(200, 10, txt=str(disk_usage), ln=True)

    pdf.output(OUTPUT_PDF_PATH)
    print(f"PDF report created at: {OUTPUT_PDF_PATH}")

# Function to visualize data
def visualize_data(cpu_usage, memory_usage, disk_usage):
    plt.figure(figsize=(10, 6))
    #print("cpu usage:",cpu_usage)
    plt.subplot(3, 1, 1)
    plt.plot(cpu_usage, label='CPU Usage (%)', color='blue')
    plt.title('CPU Usage Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('CPU Usage (%)')
    plt.legend()
    #print("memory usage:",memory_usage)
    plt.subplot(3, 1, 2)
    plt.plot(memory_usage, label='Memory Usage (%)', color='green')
    plt.title('Memory Usage Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Memory Usage (%)')
    plt.legend()
    #print("disk usage:",disk_usage)
    plt.subplot(3, 1, 3)
    plt.plot(disk_usage, label='Disk Usage (%)', color='red')
    plt.title('Disk Usage Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Disk Usage (%)')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Main function
def main():
    if authenticate():
        print("Authentication successful. Monitoring activity...")
        number=input("please enter duration to monitor in minutes: ")
        user_input=int(number)
        cpu_usage, memory_usage, disk_usage = monitor_activity(duration=user_input*60)
        visualize_data(cpu_usage, memory_usage, disk_usage)
        create_pdf(cpu_usage, memory_usage, disk_usage)
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
   
        

import os
from pathlib import Path

import meraki
from dotenv import load_dotenv

# Load values from the .env file in this same folder.
load_dotenv(Path(__file__).parent / ".env")

API_KEY = os.getenv("MERAKI_API_KEY")
DEVICE_SN = os.getenv("DEVICE_SN")

if not API_KEY:
    raise Exception("Missing MERAKI_API_KEY in .env file")

if not DEVICE_SN:
    raise Exception("Missing DEVICE_SN in .env file")

dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

print("Meraki Access Point Reboot Demo")
print("------------------------------")
print(f"Target AP Serial: {DEVICE_SN}")

confirm = input("Type YES to send reboot command: ")

if confirm == "YES":
    response = dashboard.devices.rebootDevice(DEVICE_SN)
    print("Reboot command sent successfully.")
    print(response)
else:
    print("Cancelled.")

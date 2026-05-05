import os
import meraki

API_KEY = os.getenv("ENTERV MERAKI API KEY HERE")

if not API_KEY:
    raise Exception("Missing MERAKI_DASHBOARD_API_KEY environment variable")

dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

serial = "ENTER ACCESS POINT SERIAL NUMBER HERE"

print("Meraki Access Point Reboot Demo")
print("-----------------------")
print(f"Target AP Serial: {serial}")

confirm = input("Type YES to send reboot command: ")

if confirm == "YES":
    response = dashboard.devices.rebootDevice(serial)
    print("Reboot command sent successfully.")
    print(response)
else:
    print("Cancelled.")
#!/usr/bin/env python3
"""Meraki access point reboot script with beginner-friendly status polling."""

import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv


BASE_URL = "https://api.meraki.com/api/v1"
POLL_SECONDS = 15
MAX_POLLS = 40


# Load values from the .env file in this same folder.
load_dotenv(Path(__file__).parent / ".env")

API_KEY = os.getenv("MERAKI_API_KEY")
ORG_ID = os.getenv("MERAKI_ORG_ID")
DEVICE_SN = os.getenv("DEVICE_SN")

if not API_KEY:
    raise Exception("Missing MERAKI_API_KEY in .env file")

if not ORG_ID:
    raise Exception("Missing MERAKI_ORG_ID in .env file")

if not DEVICE_SN:
    raise Exception("Missing DEVICE_SN in .env file")

headers = {
    "X-Cisco-Meraki-API-Key": API_KEY,
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_device_status():
    # Ask Meraki for the current status of one device by serial number.
    url = f"{BASE_URL}/organizations/{ORG_ID}/devices/statuses"
    params = {"serials[]": DEVICE_SN}

    response = requests.get(url, headers=headers, params=params, timeout=30)
    response.raise_for_status()

    devices = response.json()
    if not devices:
        return "unknown"

    return devices[0].get("status", "unknown").lower()


print("Meraki Access Point Reboot Demo")
print("-------------------------------")
print(f"Target Org ID: {ORG_ID}")
print(f"Target AP Serial: {DEVICE_SN}")

confirm = input("Type YES to send reboot command: ")

if confirm == "YES":
    # Send the reboot command to the Meraki Dashboard API.
    url = f"{BASE_URL}/devices/{DEVICE_SN}/reboot"
    response = requests.post(url, headers=headers, timeout=30)
    response.raise_for_status()

    print("Reboot command sent successfully.")
    print(response.json())

    print("\nWatching device status...")
    saw_device_go_offline = False

    for poll_number in range(1, MAX_POLLS + 1):
        status = get_device_status()
        print(f"Check {poll_number}: device status is {status}")

        # A reboot is complete after the device leaves online and then comes back online.
        if status != "online":
            saw_device_go_offline = True

        if saw_device_go_offline and status == "online":
            print("Reboot appears complete. Device is back online.")
            break

        time.sleep(POLL_SECONDS)
    else:
        print("Stopped checking before the reboot completion was confirmed.")
else:
    print("Cancelled.")

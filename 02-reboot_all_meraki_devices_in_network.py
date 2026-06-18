import os
import time
import meraki

# -----------------------------
# Demo Settings
# -----------------------------
NETWORK_NAME = "enter newtork name here"
DELAY_SECONDS = 5

# -----------------------------
# API Key
# For demo only: hardcoded key
# After demo, remove this and use environment variable instead
# -----------------------------
API_KEY = "ENTER YOUR PERSONAL API KEY HERE 123123"

# -----------------------------
# Connect to Meraki Dashboard API
# -----------------------------
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

print("\nMeraki Auto-Reboot All APs in Network")
print("-------------------------------------")
print(f"Target Network Name: {NETWORK_NAME}")

# -----------------------------
# Get organizations
# -----------------------------
organizations = dashboard.organizations.getOrganizations()

if not organizations:
    raise Exception("No organizations found for this API key")

print("\nOrganizations found:")
for org in organizations:
    print(f"- {org['name']}")

# -----------------------------
# Find the network by name
# -----------------------------
target_network = None
target_org = None

for org in organizations:
    org_id = org["id"]
    networks = dashboard.organizations.getOrganizationNetworks(org_id)

    for network in networks:
        if network["name"].lower() == NETWORK_NAME.lower():
            target_network = network
            target_org = org
            break

    if target_network:
        break

if not target_network:
    raise Exception(f"Network named '{NETWORK_NAME}' was not found")

network_id = target_network["id"]

print(f"\nFound network: {target_network['name']}")
print(f"Organization: {target_org['name']}")
print(f"Network ID: {network_id}")

# -----------------------------
# Get all devices in the network
# -----------------------------
devices = dashboard.networks.getNetworkDevices(network_id)

print("\nAll devices found in this network:")
for device in devices:
    name = device.get("name") or "No name"
    model = device.get("model") or "No model"
    serial = device.get("serial") or "No serial"
    print(f"- {name} | {model} | {serial}")

# -----------------------------
# Keep only Meraki Wireless APs
# MR = Meraki AP
# CW = Cisco Wi-Fi 6/6E APs managed in Meraki Dashboard
# -----------------------------
access_points = [
    device for device in devices
    if device.get("model", "").startswith(("MR", "CW"))
]

if not access_points:
    raise Exception("No Meraki wireless access points found in this network")

print("\nAccess Points selected for reboot:")
for ap in access_points:
    name = ap.get("name") or "No name"
    model = ap.get("model") or "No model"
    serial = ap.get("serial") or "No serial"
    print(f"- {name} | {model} | {serial}")

print(f"\nTotal APs to reboot: {len(access_points)}")

# -----------------------------
# Safety confirmation
# -----------------------------
confirm = input("\nType YES to reboot ALL APs listed above: ")

if confirm != "YES":
    print("Operation cancelled.\n")
    exit()

# -----------------------------
# Reboot APs one by one
# -----------------------------
print("\nStarting AP reboot process...\n")

for index, ap in enumerate(access_points, start=1):
    name = ap.get("name") or "No name"
    model = ap.get("model") or "No model"
    serial = ap.get("serial")

    try:
        print(f"[{index}/{len(access_points)}] Rebooting {name} | {model} | {serial}")

        response = dashboard.devices.rebootDevice(serial)

        print(f"Success: reboot command sent to {name}")
        print(response)
        print(f"Waiting {DELAY_SECONDS} seconds before next AP...\n")

        time.sleep(DELAY_SECONDS)

    except Exception as e:
        print(f"Error rebooting {name} | {serial}")
        print(e)
        print("Continuing to next AP...\n")

print("Done. All reboot commands have been processed.\n")
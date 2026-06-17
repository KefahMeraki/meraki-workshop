# Lab 02: Reboot All Devices in a Meraki Network

In this lab, you will use the Cisco Meraki Dashboard API and a Python script to reboot all Meraki devices inside one specific Meraki Dashboard network.

This exercise will walk you through confirming your API key, setting the target network name, running the script, reviewing the devices found, confirming the reboot action, and verifying the results in the Meraki Dashboard.

[!WARNING]
This lab may reboot all Meraki-managed devices inside the selected network, including access points, switches, cameras, security appliances, and other supported devices. Run this only in a demo or approved lab network.

1. Confirm the Meraki Python Library is Installed

If you already completed Lab 01, the Meraki Python library should already be installed.

To confirm or install it again, open Windows PowerShell and run:

```powershell
pip install meraki
```



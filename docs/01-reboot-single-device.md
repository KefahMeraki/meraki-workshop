Steps for Rebooting Single Device using a Python script:

Logon to [KefahMeraki/meraki-workshop: Welcome to the Cisco Meraki Workshop repo. Explore automation scripts, lab exercises, and real-world demos to get hands-on with Meraki solutions.](https://github.com/KefahMeraki/meraki-workshop/tree/main)

1)	Install Python library
Enter MS power shell 
Use command:
```powershell
 pip install meraki
```
 

3)	Generate/Prepare an API Key:
Create an API Key if one isn't provided. API keys are per user and Max of 2 Keys can be generated.
1.	Click on the Organization Menu
2.	Under Configuration, select API & Webhooks
3.	At the top, select the section called API keys and access
4.	Click on the blue Generate API Key button

 

 

Copy the API key and save it to a text file in a safe place. You will need this Key.
Check the box stating you've safely stored your API key and click the Done button – If you do not save the key, you will need to revoke the key and generate new one if not saved since it will not be visible again.

 

Create the reboot script
Using your windows shell or Visual Studio
PS C:\Users\kefadda> notepad reboot_single_device.py
 
Note: For this Lab, you will need to prepare the generated key that was generated as well as the Serial Number – have them ready on a text file.
 

Here is the script in blue:
enter the serial number for the desired device to be rebooted inside this line 
serial = “enter serial here”

```python
import os
import meraki

API_KEY = os.getenv("MERAKI_DASHBOARD_API_KEY")

if not API_KEY:
    raise Exception("Missing MERAKI_DASHBOARD_API_KEY environment variable")

dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

serial = "ENTER SERIAL NUMBER HERE"

print("Meraki Reboot Demo")
print("-----------------------")
print(f"Target AP Serial: {serial}")

confirm = input("Type YES to send reboot command: ")

if confirm == "YES":
    response = dashboard.devices.rebootDevice(serial)
    print("Reboot command sent successfully.")
    print(response)
else:
    print("Cancelled.")
```

If using Power shell, set the environment variable for the first time only by typing the following command:
```powershell
$env:MERAKI_DASHBOARD_API_KEY”12345 your generated Key Here 12345”
```
 

Run the script using Python:
```powershell
Python reboot_single_device.py
```
 
You can observe the Device before you execute to see if it is online first.
Then, hit enter and monitor the device rebooting by going to the device and Event Log
 

 
 

 

END OF SECTION

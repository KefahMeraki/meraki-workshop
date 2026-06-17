# Lab 02: Reboot All Devices in a Meraki Network

In this lab, you will use the Cisco Meraki Dashboard API and a Python script to reboot all Meraki devices inside one specific Meraki Dashboard network.

This exercise will walk you through confirming your API key, setting the target network name, running the script, reviewing the devices found, confirming the reboot action, and verifying the results in the Meraki Dashboard.

### [!WARNING]
"This lab may reboot all Meraki-managed devices inside the selected network, including access points, switches, cameras, security appliances, and other supported devices. Run this only in a demo or approved lab network."

### 1. Confirm the Meraki Python Library is Installed

Before running the script, confirm that the Meraki Python library is installed on your computer.

Open Windows PowerShell and run the following command:

```powershell
python -m pip install meraki
```

If the library is already installed, you may see a message similar to:

Requirement already satisfied

This means the Meraki library is already available and you can continue with the lab.

### [!NOTE]
*On some Windows computers, the command pip install meraki may not work because pip is not recognized directly. Using python -m pip install meraki is more reliable because it runs pip through your installed Python version.*


![Windows Power Shell](images/already-satisfied.png)



### 2. Confirm Your API Key is Active in PowerShell

Before running the script, confirm that your Meraki Dashboard API key is available as an environment variable.

Run the following command:

```powershell
echo $env:MERAKI_DASHBOARD_API_KEY
```

![Windows Power Shell](images/echo.png)

If the API key appears, you can continue to the next step.

If it is blank, set the environment variable again:

```python
$env:MERAKI_DASHBOARD_API_KEY="PASTE_YOUR_API_KEY_HERE"
```

### [!IMPORTANT]
*Do not upload API keys to GitHub. API keys should be stored securely and used only as environment variables during the lab.*

### 3. Create the Reboot Script

Using Windows PowerShell, Notepad, or Visual Studio Code, create a new Python file named:

```python
notepad reboot_all_devices_in_network.py
```

Copy the script below into the file.

Update this line with the name of your demo network:

```
NETWORK_NAME = "ENTER NETWORK NAME HERE"
```




  





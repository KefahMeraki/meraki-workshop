
# *UNDER CONSTRUCTION - WORKING ON IT NOW*
# Lab 03: Meraki Workflow Automation

In this lab, you will explore **Cisco Workflows** inside the Meraki Dashboard and use a pre-built workflow from the **Cisco Workflow Exchange**.

For this exercise, we will use the **Create Wireless SSID with PSK Authentication workflow**. This workflow demonstrates how automation can simplify common Meraki Dashboard tasks, such as creating a wireless SSID with WPA2-PSK authentication.



> [!NOTE]
> *This lab is designed to demonstrate workflow automation using the Meraki Dashboard and Cisco Workflows. No Python scripting is required for this lab.*



## Learning Objectives



By the end of this lab, you will be able to:

- [Generate or prepare a Meraki Dashboard API key](#1-generate-or-prepare-a-meraki-dashboard-api-key)
- [Access Cisco Workflows from the Meraki Dashboard](#2-access-cisco-workflows-from-the-meraki-dashboard)
- [Connect Cisco Workflows to Meraki using Targets](#3-connect-cisco-workflows-to-meraki-using-targets)
- [Explore the Cisco Workflow Exchange](#4-explore-the-cisco-workflow-exchange)
- [Install a pre-built Meraki workflow](#5-install-a-pre-built-meraki-workflow)
- [Run the workflow to create a wireless SSID](#6-run-the-workflow-to-create-a-wireless-ssid)
- [Verify the SSID in the Meraki Dashboard](#7-verify-the-ssid-in-the-meraki-dashboard)

 ## 1. Generate or Prepare a Meraki Dashboard API Key
 Before connecting Cisco Workflows to Meraki, you will need a Meraki Dashboard API key.

If you already generated an API key prevoiusly, you may use the same API key for this lab.

If you do not have an API key, generate one from the Meraki Dashboard.

#### Steps to Generate an API Key
- Log in to the Meraki Dashboard.
- Click the **Organization** menu.
- Under **Configuration**, select **API & Webhooks**.
- Select **API keys and access**.
- Click **Generate API Key**.
- Copy the API key and save it in a secure location.

  ![Windows Power Shell](images/API&Webhooks.png)
  
  ![Windows Power Shell](images/generate-key.png)

  ![Windows Power Shell](images/store-personal-API-key.png)
  
  

> [!IMPORTANT]
> *The API key is shown only once. If you lose it, you will need to revoke it and generate a new one.*

*Do not upload API keys to GitHub or share them in screenshots.*

## 2. Access Cisco Workflows from the Meraki Dashboard
Open a browser and log in to the [Meraki Dashboard](https://dashboard.meraki.com).
> [!TIP]
> *To keep this lab guide open, right-click the link and select **Open link in new tab**, or hold **Ctrl** while clicking the link.*


After logging in, select the correct organization and network for your lab environment.

From the left navigation menu, go to **Automation**


Cisco Workflows is available from the Automation section of the Meraki Dashboard.
![Windows Power Shell](images/lab03-automation-dashboard.png)


## 3. Connect Cisco Workflows to Meraki Using Targets
Before running a Meraki workflow, Cisco Workflows needs a connection to the Meraki Dashboard API. This connection is configured using **Targets**.

A **Target** is the system or resource that Cisco Workflows will communicate with when the workflow runs. Targets can be different types depending on what the workflow needs to connect to.

For this lab, the workflow will connect to Meraki, so the Target Type must be:

Meraki Endpoint

> [!NOTE]
> Cisco Workflows can use different Target Types depending on the automation use case. For this lab, we are using a **Meraki Endpoint** because the workflow needs to communicate with the Meraki Dashboard API.

### Create a New Meraki Target

In the Meraki Dashboard, navigate to: **Automation > Targets**

Follow these steps:

Click **Automation** from the left menu.
Under **Workflows**, select **Targets**.
Click + **New target**.
Select the Target Type:
**Meraki Endpoint**
Enter a name for the Target.

Example:
```
DEMO- Meraki Dashboard Target
```
> [!NOTE]
> *If a **Meraki Endpoinbt** Target already exists in your lab environment, you may be able to use the existing Target instead of creating a new one.*

![Windows Power Shell](images/lab03-new-target.png)


### Create a new account key using the following information:

Display Name: ```text 
DEMO-Meraki API```

Account Key Type: ```Meraki Credentials```

Meraki API Key: ```Paste your Meraki Dashboard API key```

Click **Save**

### Validate the Target

After saving, confirm that the Target status is **blue** and shows as **valid**.
































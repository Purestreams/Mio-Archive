# Create VM template in Proxmox VE

This guide will walk you through the steps to create a VM template in Proxmox VE (PVE). A VM template allows you to quickly deploy new virtual machines with pre-configured settings and software. Debian 13 will be used as an example OS for the VM template.

## Prerequisites

Download the Debian 13 Cloud ISO from the official Debian website: [Debian 13 Cloud ISO](https://cloud.debian.org/images/cloud/trixie/)

In this guide, we will use the following specifications for the VM template [https://cloud.debian.org/images/cloud/trixie/20250814-2204/debian-13-genericcloud-amd64-20250814-2204.qcow2](https://cloud.debian.org/images/cloud/trixie/20250814-2204/debian-13-genericcloud-amd64-20250814-2204.qcow2)


## Download the Debian 13 Cloud ISO to the PVE server

1. Log in to your Proxmox VE web interface.
2. Open a terminal on your PVE server or use the web-based shell.

```bash
cd /var/lib/vz/template/
# Create a directory for the ISO if it doesn't exist
mkdir -p qcow2
cd qcow2
# Download the Debian 13 Cloud ISO
wget https://cloud.debian.org/images/cloud/trixie/20250814-2204/debian-13-genericcloud-amd64-20250814-2204.qcow2
``` 

## Create a new VM in Proxmox VE

1. In the Proxmox VE web interface, click on "Create VM" in the top right corner.
2. In the "General" tab, enter a name for your VM (e.g., "Debian13-Template").
3. In the "OS" tab, select "Do not use any media" since we will be using a cloud image.
4. In the "System" tab, you can leave the default settings or adjust them as needed.
5. In the "Hard Disk" tab, do not add a disk here; we will attach the downloaded QCOW2 image later.
6. In the "CPU" tab, allocate the desired number of cores (e.g., 2 cores).
7. In the "Memory" tab, allocate the desired amount of RAM (e.g., 2048 MB).
8. In the "Network" tab, configure the network settings as needed (e.g., bridge mode).
9. Click "Finish" to create the VM.

## Attach the downloaded QCOW2 image to the VM

1. Open a terminal on your PVE server or use the web-based shell.

```bash
qm importdisk 101 /var/lib/vz/template/debian-13-genericcloud-amd64-20250814-2204.qcow2 local --format=qcow2
```

Breakdown of the command:
- `qm importdisk`: Proxmox command to import a disk image to a VM.
- Replace `101` with the VM ID of the VM you just created.
- `/var/lib/vz/template/debian-13-genericcloud-amd64-20250814-2204.qcow2`: Path to the downloaded QCOW2 image.
- `local`: The storage location where the disk will be imported (adjust if necessary).
- `--format=qcow2`: Specifies the format of the disk image.

2. After importing the disk, go back to the Proxmox VE web interface.
3. Select the VM you created (e.g., "Debian13-Template").
4. Go to the "Hardware" tab.
5. There is a unused disk listed. Select it and click "Edit", and enable the disk.
6. Go to the "Options" tab, select "Boot Order", and set the imported disk as the first boot device.


## Set username and password for the VM

1. Go to the Cloud-Init tab of the VM.
2. Set username to `root`.
3. Set a secure password for the root user.
4. Optionally, configure other settings such as SSH keys, network configuration, etc.

## Convert the VM to a template

1. Once you have configured the VM and are satisfied with the settings, right-click on the VM in the Proxmox VE web interface.
2. Select "Convert to Template" from the context menu.
3. Confirm the action when prompted.

## Deploy new VMs from the template

1. To deploy a new VM from the template, right-click on the template in the Proxmox VE web interface.
2. Select "Clone" from the context menu.
3. In the "Clone" dialog, enter a name for the new VM and choose whether to make a full clone or a linked clone.
4. Click "Clone" to create the new VM.
5. You can still change the username and password in the Cloud-Init tab of the new VM if needed.
6. Start the new VM and it will boot with the pre-configured settings from the template.
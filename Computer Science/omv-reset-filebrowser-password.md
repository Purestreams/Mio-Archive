# OpenMediaVault Reset File Browser Password

When you need to reset the password for the file browser in OpenMediaVault, follow these steps:

1. **Access the Command Line:**
   - Log in to your OpenMediaVault server via SSH or directly on the console.

2. **Find the Configuration File:**
   - The file browser configuration is stored in a folder typically located at:
     ```
     /var/lib/filebrowser
     ```

3. **Delete all the file inside the configuration folder:**
   - Use the following command to remove all files in the file browser configuration directory:
     ```sh
     rm -rf /var/lib/filebrowser/*
     ```

4. **Reinstall File Browser:**
    - Reinstall the file browser through the OpenMediaVault web interface (remove the plugin and then install it again)
    - The password will be reset to the default value, which is usually `admin`. (username: `admin`, password: `admin`



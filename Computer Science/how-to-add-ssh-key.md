# How to Add an SSH Key

When the cloud platform provide you only the SSH private key file, you can follow these steps to add it to your SSH configuration.

### 1. Copy the SSH Private Key File

If you already have an SSH private key file (for example, `id_rsa`), copy it to your SSH directory:

```bash
cp /path/to/your/existing/id_rsa ~/.ssh/
```

Replace `/path/to/your/existing/id_rsa` with the actual path to your private key file.

### 2. Set Proper Permissions

SSH requires your private key file to have strict permissions:

```bash
chmod 600 ~/.ssh/id_rsa
```

### 3. (Optional) Add the Public Key

If you also have the corresponding public key (`id_rsa.pub`), copy it as well:

```bash
cp /path/to/your/existing/id_rsa.pub ~/.ssh/
chmod 644 ~/.ssh/id_rsa.pub
```

### 4. Add the Key to the SSH Agent

Start the SSH agent and add your key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

### 5. Test the SSH Key

Test your SSH key by connecting to a server (replace `user@hostname` with actual values):

```bash
ssh -i ~/.ssh/id_rsa user@hostname
```

---

**Summary:**  
Copy your private key to `~/.ssh/`, set permissions, add it to the SSH agent, and you’re done.

Let me know if you need help with a specific key file or SSH configuration!
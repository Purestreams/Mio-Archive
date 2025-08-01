# Create a User for Root to Run a Program (No Login Shell, No Password)

To create a user in Debian that is only meant to be used by root to run a specific program, and cannot be used to sign in (i.e., login shell disabled and no password), follow these steps as root:

1. **Create the user without a password and with a locked shell:**
```sh
adduser --system --no-create-home --shell /usr/sbin/nologin myserviceuser
```
- `--system` creates a system user.
- `--no-create-home` does not create a home directory.
- `--shell /usr/sbin/nologin` disables shell access.

2. **Alternatively, with `useradd`:**
```sh
useradd --system --no-create-home --shell /usr/sbin/nologin myserviceuser
```

3. **Do not set a password:**
- By default, system users created this way do not have a password. If you want to ensure the account is locked (cannot be logged into by any means), you can explicitly lock it:
```sh
usermod -L myserviceuser
```

4. **Usage:**
- Now, only root (or processes running as root) can use `su -s` or `runuser` to run a program as this user:
```sh
sudo -u myserviceuser /path/to/program
```
or
```sh
runuser -u myserviceuser -- /path/to/program
```

**Summary:**  
This user cannot be used to login (no password, nologin shell), and is suitable for root to run a service or process as a non-privileged user.
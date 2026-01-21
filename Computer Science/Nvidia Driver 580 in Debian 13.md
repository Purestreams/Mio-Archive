# Install NVIDIA Driver 580 on Debian 13

Pins the NVIDIA driver stack to the **580.x** branch while keeping Debian as the default source for everything else.

## 1) (Optional) Enable the NVIDIA CUDA repo via `extrepo`

Only do this if you want packages from NVIDIA's repo.

```bash
sudo apt install extrepo
sudo extrepo enable nvidia-cuda
sudo apt update
```

## 2) Pin the NVIDIA stack to a known-good branch (580.*)

Also de-prioritize the NVIDIA repo in general, so Debian wins by default.

Create the pin file:

```bash
sudo vim.tiny /etc/apt/preferences.d/90-nvidia-pin
```

Add:

```plaintext
# De-prioritize the NVIDIA CUDA repo in general
Package: *
Pin: origin "developer.download.nvidia.com"
Pin-Priority: 100

# Prefer Debian by default
Package: *
Pin: release o=Debian
Pin-Priority: 500

# But force NVIDIA driver stack to 580.*
Package: nvidia-* libnvidia-* libcuda* firmware-nvidia-* xserver-xorg-video-nvidia \
         nvidia-settings libxnvctrl0 libnvcuvid* \
         libegl-nvidia* libglx-nvidia* libgles-nvidia*
Pin: version 580.*
Pin-Priority: 1001
```

Refresh package metadata:

```bash
sudo apt update
```

## 3) Install the driver

Uses DKMS and works with the stock Debian kernel.

```bash
sudo apt install nvidia-driver nvidia-kernel-open-dkms
```
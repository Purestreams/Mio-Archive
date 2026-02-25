# PVE Source List

## Debian 12

### non-China

/etc/apt/sources.list.d/pve-no-subscription.list
```
deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription
```

/etc/apt/sources.list.d/ceph.list
```
deb http://download.proxmox.com/debian/ceph-quincy bookworm no-subscription
```

### China

/etc/apt/sources.list
```
deb http://mirrors.ustc.edu.cn/debian bookworm main contrib non-free non-free-firmware
# deb-src http://mirrors.ustc.edu.cn/debian bookworm main contrib non-free non-free-firmware
deb http://mirrors.ustc.edu.cn/debian bookworm-updates main contrib non-free non-free-firmware
# deb-src http://mirrors.ustc.edu.cn/debian bookworm-updates main contrib non-free non-free-firmware

# backports
# deb http://mirrors.ustc.edu.cn/debian bookworm-backports main contrib non-free non-free-firmware
# deb-src http://mirrors.ustc.edu.cn/debian bookworm-backports main contrib non-free non-free-firmware

deb http://mirrors.ustc.edu.cn/debian-security/ bookworm-security main contrib non-free non-free-firmware
# deb-src http://mirrors.ustc.edu.cn/debian-security/ bookworm-security main contrib non-free non-free-firmware
```

/etc/apt/sources.list.d/pve-no-subscription.list
```
deb http://mirrors.ustc.edu.cn/proxmox/debian/pve bookworm pve-no-subscription
```

/etc/apt/sources.list.d/ceph.list
```
deb http://mirrors.ustc.edu.cn/proxmox/debian/ceph-quincy bookworm no-subscription
```
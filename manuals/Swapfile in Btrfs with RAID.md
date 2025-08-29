# Swapfile Problems in Btrfs with RAID

When using a swapfile on a Btrfs filesystem configured with RAID (such as RAID 1, RAID 10, etc.), you will encounter issues due to the way Btrfs handles file storage and allocation. 



## Disk Configuration

```
root@pve:~# btrfs fi show /
Label: none  uuid: 29ed99c6-95ef-4154-a8f0-e5212a641de3
        Total devices 2 FS bytes used 625.02GiB
        devid    1 size 3.49TiB used 641.01GiB path /dev/nvme0n1p3
        devid    2 size 3.49TiB used 641.01GiB path /dev/nvme1n1p3

root@pve:~# btrfs filesystem df /
Data, RAID1: total=638.00GiB, used=623.59GiB
System, RAID1: total=8.00MiB, used=112.00KiB
Metadata, RAID1: total=3.00GiB, used=1.43GiB
GlobalReserve, single: total=512.00MiB, used=0.00B
```

## Problem when creating a swapfile

When you try to create a swapfile on a Btrfs filesystem with RAID, you might see an error like this:

```
root@pve:~# mkdir -p /swap
root@pve:~# chattr +C /swap
root@pve:~# lsattr -d /swap
---------------C------ /swap
root@pve:~# dd if=/dev/zero of=/swap/swapfile bs=1M count=32768 status=progress
33468448768 bytes (33 GB, 31 GiB) copied, 16 s, 2.1 GB/s
32768+0 records in
32768+0 records out
34359738368 bytes (34 GB, 32 GiB) copied, 16.4936 s, 2.1 GB/s
root@pve:~# chmod 600 /swap/swapfile
root@pve:~# btrfs inspect-internal map-swapfile -r /swap/swapfile
ERROR: unsupported block group profile: 16
```


`ERROR: unsupported block group profile: 16` That error means your Btrfs data block groups aren’t SINGLE (they’re using a RAID profile, likely RAID10/RAID1). Btrfs swapfiles only work on a single‑device/SINGLE data profile. On multi‑device/RAID Btrfs, swapfiles are not supported.

## Solution

We do not recommend using swapfiles on Btrfs filesystems with RAID configurations. If you want to do it, you need to reconfigure your Btrfs filesystem, this will lead to a potential data loss if not done carefully.

If you really need swap space, add a dedicated swap partition on a separate disk or use a non-RAID Btrfs filesystem for swapfile usage.


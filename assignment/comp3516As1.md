---
title: "COMP3516 Assignment 1"
author: "Zhu Yecheng 3036061373"
date: "2026-04-29"
geometry: margin=2cm
---

## Q1

### (a)

**False.** Nearby Access Points can still cause Adjacent Channel Interference (ACI) due to out-of-band emissions, even if they are on different, non-overlapping channels. If the channels are different but overlapping, such as channels 1 and 2 in the 2.4 GHz band, they will cause severe interference.

### (b)

**False.** The distance formula for FMCW radar is

$$d = \frac{c \cdot \tau}{2}$$

so the change in distance is

$$\Delta d = \frac{c \cdot \Delta \tau}{2}$$

Given $\Delta \tau = 0.01\mu s = 10^{-8} \text{ s}$ and $c = 3 \times 10^8 \text{ m/s}$,

$$\Delta d = \frac{3 \times 10^8 \times 10^{-8}}{2} = \frac{3}{2} = 1.5 \text{ meters}$$

so the correct answer is $1.5$ meters, not $0.75$ meters.

### (c)

**False.** Range resolution is determined by

$$\Delta R = \frac{c}{2B}$$

and depends only on the bandwidth $B$, not the number of antennas. Antennas improve angular resolution rather than range resolution. Upgrading from 40 MHz to 160 MHz is a $4\times$ increase in bandwidth, so range resolution improves by $4\times$, not $16\times$.

### (d)

**False.** In an Autocorrelation Function (ACF), the period of the signal is indicated by the time delay of the first peak, namely its x-axis position. The absolute peak height on the y-axis reflects signal energy or variance rather than the breathing frequency or speed.

### (e)

**False.** The principle is the opposite. When the device is static, the accelerometer measures the gravity vector reliably, so it gives good pitch and roll information. When the device is moving, linear acceleration corrupts that measurement, so the gyroscope becomes more reliable for tracking orientation.

### (f)

**3430 Hz** or $3.43 \text{ kHz}$.

Using

$$\Delta R = \frac{c}{2B}$$

we have

$$0.05 = \frac{343}{2B}$$

so

$$B = \frac{343}{0.1} = 3430 \text{ Hz}$$

### (g)

Blank 1: **4**

Nyquist theorem requires the sampling rate to be at least twice the maximum frequency of $2 \text{ Hz}$.

Blank 2: **5**

A precision error of 2 steps per 10 seconds is $0.2 \text{ Hz}$. Since frequency resolution is

$$\Delta f = \frac{1}{T}$$

we need

$$T = \frac{1}{0.2} = 5 \text{ seconds}$$

Blank 3: **frequency**

Blank 4: **latency**

## Q2

### (a)

He should stick with **100 Hz**.

Frequency resolution depends on the duration of the time window, where

$$\Delta f = \frac{1}{T}$$

If Harry increases the sampling rate to 1000 Hz while keeping the window at 1000 samples, the window duration shrinks from 10 seconds to 1 second. That worsens the frequency resolution from $0.1 \text{ Hz}$ to $1 \text{ Hz}$. Also, 100 Hz is already well above the Nyquist rate required for a breathing signal around $0.2$ to $0.5 \text{ Hz}$.

### (b)

**No, this is not a good idea.**

Shortening the window to 5 seconds worsens the frequency resolution to

$$\Delta f = \frac{1}{5} = 0.2 \text{ Hz}$$

Because breathing is a very low-frequency physiological signal, a coarse resolution of $0.2 \text{ Hz}$ is not precise enough to estimate a specific breathing rate accurately.

### (c)

**5 GHz band**.

The 5 GHz band has a shorter wavelength than 2.4 GHz, so its phase is more sensitive to tiny chest movements during breathing. It also generally experiences less interference from common household devices such as Bluetooth devices, microwaves, and older IoT devices.

### (d)

The most likely cause is that Harry is sitting in a sensing blind spot, or that the line-of-sight signal is overwhelmingly dominant. The multipath reflections from his chest may be too weak, or they may cancel out destructively at the receiver, so his chest displacement does not create a measurable change in the CSI compared with the strong static direct path from the ceiling AP to the desk.

### (e)

There are two main problems with relying on regular WiFi traffic.

1. **Irregular sampling rate:** Regular WiFi traffic is bursty and packet intervals are uneven. FFT requires a uniformly sampled time series, so irregular timing breaks the frequency-domain analysis.
2. **Low packet rate:** If the network is idle, the packet transmission rate may fall below the Nyquist rate needed to capture the breathing waveform continuously.
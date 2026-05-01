---
title: "COMP3516 Assignment 1"
author: "Zhu Yecheng 3036061373"
date: "2026-04-29"
geometry: margin=2cm
---

## Q1

### (a)

False. 

Adjacent Channel Interference (ACI) due to out-of-band emissions

### (b)

False. 

$$\Delta d = \frac{3 \times 10^8 \times 10^{-8}}{2} = \frac{3}{2} = 1.5 \text{ meters}$$

not $0.75$ meters.

### (c)

False.

$$\Delta R = \frac{c}{2B}$$

and depends only on the bandwidth $B$, not the number of antennas. Antennas improve angular resolution rather than range resolution. Upgrading from 40 MHz to 160 MHz is a $4\times$ increase in bandwidth, so range resolution improves by $4\times$.

### (d)

False.  

The absolute peak height on the y-axis reflects signal energy or variance rather than the breathing frequency or speed.

### (e)

False. 

When the device is static, the accelerometer measures the gravity vector reliably, so it gives good pitch and roll information. When the device is moving, linear acceleration corrupts that measurement, so the gyroscope becomes more reliable for tracking orientation.

### (f)

3430 Hz

$$B = \frac{343}{0.1} = 3430 \text{ Hz}$$

### (g)

Blank 1: 4

Nyquist theorem requires the sampling rate to be at least twice the maximum frequency of $2 \text{ Hz}$.

Blank 2: 5

A precision error of 2 steps per 10 seconds is $0.2 \text{ Hz}$. Since frequency resolution is

$$T = \frac{1}{0.2} = 5 \text{ seconds}$$

Blank 3: frequency

Blank 4: latency

## Q2

### (a)

Keep 100 Hz.

Frequency resolution depends on the duration of the time window, where

$$\Delta f = \frac{1}{T}$$

If Harry increases the sampling rate to 1000 Hz while keeping the window at 1000 samples, the window duration shrinks from 10 seconds to 1 second. That worsens the frequency resolution from $0.1 \text{ Hz}$ to $1 \text{ Hz}$. Also, 100 Hz is already well above the Nyquist rate required for a breathing signal around $0.2$ to $0.5 \text{ Hz}$.

### (b)

not a good idea.

Shortening the window to 5 seconds worsens the frequency resolution to

$$\Delta f = \frac{1}{5} = 0.2 \text{ Hz}$$

Because breathing is a very low-frequency physiological signal, a coarse resolution of $0.2 \text{ Hz}$ is not precise enough to estimate a specific breathing rate accurately.

### (c)

5 GHz.

The 5 GHz band has a shorter wavelength than 2.4 GHz, so its phase is more sensitive to tiny chest movements during breathing. It also generally experiences less interference from common household devices such as Bluetooth devices, microwaves, and older IoT devices.

### (d)

- The macro-movements of other people in the library ,eg. walking, shifting in chairs, create massive fluctuations in the CSI data that easily drown out the tiny, millimeter-scale micro-movements of his breathing.

- Because the AP is on the ceiling and the ESP32 is on the desk, the direct signal between them is overwhelmingly strong, making it extremely difficult to isolate the much weaker signal reflecting off his chest.

### (e)

There are two main problems with relying on regular WiFi traffic.

- Irregular sampling rate: Regular WiFi traffic is bursty and packet intervals are uneven. FFT requires a uniformly sampled time series, so irregular timing breaks the frequency-domain analysis.

- Low packet rate: If the network is idle, the packet transmission rate may fall below the Nyquist rate needed to capture the breathing waveform continuously.
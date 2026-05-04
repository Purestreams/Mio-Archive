---
geometry: margin=1.5cm
---

# COMP3516 Data Analytics for IoT

## Revision Guide: Core Concepts, Formulas, and Practice Questions

This guide is organized to help you scan the key ideas quickly, then review the formulas and sample calculations in one place.

---

## **Part 1: Course Revision Notes**

#### **1. Wireless IoT & Connectivity (Lecture 2)**

*   **Evolution of Networks:** Computing progressed from high-performance machines to the internet, and now to **AIoT** (Artificial Intelligence of Things), where connectivity and sensing are omnipresent.
*   **Cellular Generations:** Each generation optimizes cost while enabling new use cases (e.g., 2G for digital voice, 4G for broadband data/LTE, 5G for industrial IoT and extreme data rates).
*   **IoT Wireless Protocols:**
    *   **Bluetooth & BLE:** Short-range Personal Area Networks (PANs). BLE is heavily optimized for low power.
    *   **Wi-Fi:** High data rate, ubiquitous 802.11 standard.
    *   **Zigbee:** IEEE 802.15.4 standard; optimized for low power, low data rates, and mesh networking.
    *   **LPWAN (LoRa):** Low Power Wide Area Networks provide extremely long-range and low-bandwidth communication. LoRa uses Chirp Spread Spectrum (CSS) modulation, which makes it highly resilient to interference.

#### **2. Signals & Sensing Basics (Lectures 3 & 4)**

*   **Analog vs. Digital:** Analog signals are continuous, while digital signals are discrete. The conversion process (ADC) involves **sampling** (time domain) and **quantization** (amplitude domain).
*   **Complex Signals & FFT:** Complex signals combine sine and cosine components via the complex plane. The Fast Fourier Transform (FFT) converts time-domain signals into the frequency domain, which is essential for identifying patterns like pathological tremors.
*   **FMCW Radar (mmWave):** Frequency Modulated Continuous Wave radar operates using linear chirps (frequency increases linearly over time).
    *   **Range:** Extracted using a Range-FFT on the Intermediate Frequency (IF) signal.
    *   **Velocity (Doppler):** Measured via small phase shifts across consecutive chirps (Doppler-FFT).
    *   **Angle of Arrival (AoA):** Calculated by measuring phase differences across an array of multiple receiving antennas.

#### **3. WiFi Sensing & Channel State Information (Lectures 5.1 & 5.2)**

*   **RSSI vs. CSI:** Received Signal Strength Indicator (RSSI) is a single, unstable scalar value representing total power. Channel State Information (CSI) provides fine-grained, stable amplitude and phase data for every OFDM subcarrier.
*   **Multipath Effect:** Wireless signals bounce off walls and objects, arriving at the receiver via multiple paths (Line-of-Sight and Non-Line-of-Sight).
*   **Sensing Approaches:**
    *   **Geometric:** Uses Time of Flight (ToF), Angle of Arrival (AoA), and Doppler Frequency Shift (DFS).
    *   **Statistical:** Relies on the Autocorrelation Function (ACF) to extract speed and periodic motions (e.g., breathing) independently of user location or direction.

#### **4. Systems Design & Mobile Sensing (Lectures 6 & 7)**

*   **System Pipeline:** Data flows from Hardware/Sensors -> Data Acquisition (via protocols like **MQTT**) -> Preprocessing (Windowing/Filtering) -> Core Algorithms -> User Interface.
*   **Target Detection:** Uses techniques like Constant False Alarm Rate (CFAR) to evaluate test cells against background noise.
*   **Mobile Sensing (IMUs):** Smartphones use accelerometers, gyroscopes, and magnetometers to track motion. Standard tasks like step counting use Finite State Machines (FSM) to detect peaks and valleys in the acceleration signal.
*   **Human Activity Recognition (HAR):** Traditional pipelines involve data collection, feature extraction (mean, variance, peaks), and classical machine learning (SVM, K-NN). Modern approaches increasingly use Large Language Models (LLMs) to synthesize training data.

#### **5. Indoor Localization (Lecture 8)**

*   **The Problem:** GPS fails indoors due to structural blocking and severe multipath interference.
*   **Mainstream Approaches:**
    *   **Trilateration:** Uses geometric intersection of ranges (Time-of-Flight or RSSI) from known anchors.
    *   **Fingerprinting:** Matches live radio/magnetic signatures against a pre-surveyed reference map. Very accurate but requires heavy maintenance.
    *   **Pedestrian Dead-Reckoning (PDR):** Uses IMUs to integrate step counts and heading over time. It suffers from unbounded accumulative error.

#### **6. Deep Wireless Sensing & Evaluation (Lectures 9 & 10)**

*   **Deep Learning Challenges:** CSI data is non-visual, complex-valued, and highly sensitive to environmental domain shifts. 
*   **Data Augmentation & Synthesis:** Frameworks like RFBoost use physical data augmentation (time/frequency shifts), while RF-Diffusion uses generative AI to synthesize authentic training data.
*   **System Evaluation:** It is critical to choose the right metrics based on the application's real-world cost of errors.
    *   **Classification:** Accuracy, Precision, Recall, F1-Score, and ROC Curves (plotting True Positive Rate against False Positive Rate).
    *   **Regression:** Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Cumulative Distribution Functions (CDF).

---

## **Part 2: Core Mathematical Formulas**


### **1. Nyquist Sampling Theorem**
$$f_s > 2f_{\text{max}}$$

**The Variables:**

*   **$f_s$**: The sampling frequency (how many times per second you record a measurement, in Hz).
*   **$f_{\text{max}}$**: The highest frequency component present in the original analog signal (in Hz).

**The Explanation:**
When you convert an analog signal (like a sound wave or a vibration) into digital data, you are essentially taking rapid "snapshots" of it. If you take snapshots too slowly, you lose the true shape of the wave—a problem called **aliasing**. (Think of how car wheels sometimes look like they are spinning backward on video; that's visual aliasing because the camera's frame rate is too slow). 

This theorem states a hard physical law: to perfectly capture a signal without distorting it, your sampling rate must be strictly greater than twice the highest frequency in that signal.

---

### **2. Shannon-Hartley Theorem**
$$C = B \cdot \log_2\left(1 + \frac{S}{N}\right)$$

**The Variables:**

*   **$C$**: Channel capacity (the absolute maximum data rate achievable, in bits per second).
*   **$B$**: Bandwidth (the width of the frequency band allocated to you, in Hz).
*   **$S$**: Average received signal power (Watts).
*   **$N$**: Average noise or interference power (Watts). 
*   **$S/N$**: The Signal-to-Noise Ratio (SNR).

**The Explanation:**
This is the foundational equation of modern telecommunications. It tells you the absolute "speed limit" for sending data over any wireless channel. If you want to send data faster (increase $C$), you only have two choices:
1.  **Increase Bandwidth ($B$)**: Buy a wider "pipe" (this is why 5G uses wider frequency bands than 4G).
2.  **Increase SNR ($S/N$)**: Shout louder (increase transmit power) or reduce the background noise.

---

### **3. FMCW Radar: Range Estimation**
$$d = \frac{c f_\tau}{2S}$$

**The Variables:**

*   **$d$**: Distance to the target (meters).
*   **$c$**: The speed of light (roughly $3 \times 10^8$ m/s).
*   **$f_\tau$**: The Intermediate Frequency (IF), also called the beat frequency (Hz).
*   **$S$**: The chirp slope (how fast the frequency of the radar pulse increases over time, in Hz/s).

**The Explanation:**
An FMCW (Frequency Modulated Continuous Wave) radar doesn't just send a blip and wait for it to bounce back. It sends a "chirp"—a continuous wave whose frequency rises steadily. When the echo bounces off a target and comes back, the radar is already transmitting at a *new*, higher frequency. 

By mixing the current transmitting frequency with the delayed echo frequency, the radar gets an Intermediate Frequency ($f_\tau$). Because the frequency increases at a known slope ($S$), this frequency difference is directly proportional to how long the signal was in the air. The $2$ in the denominator accounts for the round-trip travel (there and back).

---

### **4. FMCW Radar: Range Resolution**
$$d_{res} = \frac{c}{2B}$$

**The Variables:**

*   **$d_{res}$**: Range resolution (the minimum distance required between two objects for the radar to see them as two separate things, rather than one big blob).
*   **$c$**: The speed of light.
*   **$B$**: Total bandwidth of the radar's chirp (Hz).

**The Explanation:**
This formula reveals a crucial radar design secret: **resolution depends *only* on bandwidth.** If you want a sharper, more precise radar that can distinguish a person's chest moving from their arm moving, you cannot just turn up the power; you *must* increase the bandwidth. (For example, a radar with 4 GHz of bandwidth can resolve objects 3.75 cm apart, while standard 20 MHz Wi-Fi can only resolve objects 7.5 meters apart).

---

### **5. FMCW Radar: Velocity Estimation & Resolution**

**Velocity:** $$v = \frac{\lambda \Delta\phi}{4\pi T_c}$$
**Resolution:** $$v_{res} = \frac{\lambda}{2 T_f}$$

**The Variables:**

*   **$v$**: Velocity of the moving object (m/s).
*   **$\lambda$**: Wavelength of the radar signal (meters).
*   **$\Delta\phi$**: The phase shift measured between two consecutive radar chirps (radians).
*   **$T_c$**: The time duration of a single chirp (seconds).
*   **$T_f$**: Total frame time (the total time spent observing a sequence of chirps).

**The Explanation:**
To measure speed, radar relies on the Doppler effect. But instead of trying to measure incredibly tiny frequency shifts, modern mmWave radar measures **phase shifts**. If an object moves even a fraction of a millimeter between two rapid chirps ($T_c$), the returning wave hits the antenna at a slightly different point in its cycle (phase shift, $\Delta\phi$). 

The resolution formula ($v_{res}$) shows that if you want to detect finer differences in speed (like distinguishing a slow walk from a very slow walk), you need to observe the target for a longer continuous period ($T_f$).

---

### **6. FMCW Radar: Angle of Arrival (AoA)**
$$\theta = \sin^{-1}\left( \frac{\lambda \Delta \phi}{2 \pi s} \right)$$

**The Variables:**

*   **$\theta$**: The angle at which the signal is hitting the radar (relative to straight ahead).
*   **$\lambda$**: Wavelength of the signal.
*   **$\Delta\phi$**: The phase difference of the arriving signal measured across *two different receiving antennas*.
*   **$s$**: The physical physical distance separating the two antennas on the radar board.

**The Explanation:**
You can't determine direction with just one ear, and a radar can't determine angle with just one antenna. If a wave arrives from an angle, it will physically strike one receiving antenna slightly before it strikes the antenna next to it. This tiny time delay creates a phase difference ($\Delta\phi$). By measuring this difference and knowing exactly how far apart the antennas are ($s$), the radar can use basic trigonometry (the arcsine function) to pinpoint exactly what angle the reflection came from.

---

### **7. Classification Evaluation Metrics**
These are the statistical formulas used to evaluate how well an IoT AI/Machine Learning model is actually performing.

**Precision:** $$\frac{\text{TP}}{\text{TP} + \text{FP}}$$
*   **The Concept:** "Out of all the times the system *cried wolf*, how many times was there actually a wolf?"
*   **Why it matters:** Use this when False Positives (FP) are expensive. If a smart home security system sends you a panic alert every time a shadow moves, it has terrible precision, and you will eventually ignore it.

**Recall (Detection Rate):** $$\frac{\text{TP}}{\text{TP} + \text{FN}}$$
*   **The Concept:** "Out of all the actual wolves that attacked, how many did the system catch?"
*   **Why it matters:** Use this when False Negatives (FN) are dangerous. If a wearable IoT fall-detection system misses a real fall, the consequences are severe. You want incredibly high recall, even if it means a few false alarms.

**F1-Score:** $$\frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$
*   **The Concept:** The harmonic mean of Precision and Recall. 
*   **Why it matters:** Often, improving Recall destroys Precision, and vice-versa. The F1-score gives you a single, balanced grade for your model when you care about catching real events but also don't want to be overwhelmed by false alarms.

---

## MCQ

Here are 35 additional multiple-choice questions, complete with answers and explanations, to extend your practice set to a full 50 questions. These cover the breadth of the COMP3516 Data Analytics for IoT syllabus, from wireless fundamentals to deep learning evaluation.

---

### **Lecture 2: Wireless for IoT**

**16. Which of the following Low Power Wide Area Network (LPWAN) technologies operates on a licensed radio spectrum?**

*   A. LoRa
*   B. Sigfox
*   C. NB-IoT
*   D. Helium
**Answer: C**

**Explanation:** NB-IoT (Narrowband IoT) and LTE-M are cellular-based LPWAN technologies that operate on regulated, licensed spectrums controlled by telecommunications operators. LoRa and Sigfox operate on public, unlicensed spectrums.

**17. What is the primary modulation technique used by the physical layer of LoRa communication?**

*   A. Orthogonal Frequency-Division Multiplexing (OFDM)
*   B. Chirp Spread Spectrum (CSS)
*   C. Direct-Sequence Spread Spectrum (DSSS)
*   D. Frequency-Shift Keying (FSK)
**Answer: B**

**Explanation:** LoRa uses Chirp Spread Spectrum (CSS) modulation, encoding data by adjusting the starting time phase of a linear frequency-swept chirp. This makes it highly resilient to noise and interference.

**18. According to the Shannon-Hartley Theorem, $C = B \cdot \log_2(1 + S/N)$, how can you increase the maximum error-free capacity of a wireless channel?**

*   A. Decrease the channel bandwidth.
*   B. Increase the background noise power.
*   C. Increase the transmit signal power or increase the bandwidth.
*   D. Decrease the Signal-to-Noise Ratio (SNR).
**Answer: C**

**Explanation:** Channel capacity ($C$) scales linearly with bandwidth ($B$) and logarithmically with the Signal-to-Noise ratio ($S/N$). Therefore, increasing the signal power ($S$) or the bandwidth ($B$) increases overall capacity.

---

### **Lecture 3: Signals**

**19. You are sampling an analog signal that has a maximum frequency component of 2.5 kHz. To uniquely and correctly represent this signal without aliasing, what is the absolute minimum Nyquist sampling rate required?**

*   A. 1.25 kHz
*   B. 2.5 kHz
*   C. 5.0 kHz
*   D. Strictly greater than 5.0 kHz
**Answer: D**

**Explanation:** The Nyquist Sampling Theorem requires the sampling rate to be strictly greater than twice the highest frequency component ($f_s > 2f_{\text{max}}$). Therefore, it must be $> 5.0$ kHz.

**20. What does the Fast Fourier Transform (FFT) algorithm actually compute for a given time-series signal?**

*   A. The physical location of the signal source.
*   B. The phase shift of the signal relative to the speed of light.
*   C. The power spectrum, decomposing the signal into its constituent sinusoidal frequency components.
*   D. The total amplitude of the signal over time.
**Answer: C**

**Explanation:** FFT converts a time-domain signal into the frequency domain, showing the amplitude and phase of the individual frequency bins that make up the complex signal.

---

### **Lecture 4: mmWave Sensing**

**21. In an FMCW radar system, how is the range of a single stationary target calculated?**

*   A. By measuring the absolute time of flight using a synchronized atomic clock.
*   B. By measuring the frequency difference (Intermediate Frequency) between the transmitted chirp and the received echo.
*   C. By measuring the phase shift across multiple antennas.
*   D. By calculating the Doppler shift of the target.

**Answer: B**

**Explanation:** FMCW radar measures distance by mixing the Transmit (Tx) and Receive (Rx) signals to produce an Intermediate Frequency (IF). The IF frequency is directly proportional to the distance of the object.

**22. If two stationary objects are perfectly equidistant from an FMCW radar, how will they appear in the Range-FFT output?**

*   A. As two distinct peaks, separated by their angular difference.
*   B. As no peaks, because their signals will destructively interfere.
*   C. As a single combined peak at that specific distance.
*   D. As two peaks, separated by their velocity difference.

**Answer: C**

**Explanation:** The Range-FFT only resolves targets based on their radial distance. Equidistant targets produce the exact same Intermediate Frequency and will merge into one single peak in the Range-FFT. 

**23. Why is phase shift, rather than frequency shift, used to measure the micro-velocity (Doppler effect) of a target in mmWave radar?**

*   A. Phase shifts are immune to multipath interference.
*   B. Frequency changes for sub-wavelength movements are too small to measure reliably, while phase changes are extremely sensitive to tiny movements.
*   C. The Range-FFT cannot process frequency shifts.
*   D. Antennas cannot detect frequency changes in moving targets.

**Answer: B**

**Explanation:** For small movements (like a few millimeters), the change in the IF frequency is negligible (e.g., ~333 Hz), but the phase change is massive (e.g., 180 degrees), making phase the only reliable metric for micro-motion.

**24. The Angle of Arrival (AoA) resolution of a radar system degrades (gets worse) under which condition?**

*   A. When the target moves closer to the radar.
*   B. When the target's look angle ($\theta$) moves further away from the boresight (the center, $\theta=0$).
*   C. When the number of receiving antennas ($M$) increases.
*   D. When the radar bandwidth ($B$) increases.

**Answer: B**

**Explanation:** The AoA resolution formula contains a $1/\cos(\theta)$ term. Resolution is optimal at the boresight ($\theta=0$ where $\cos(0)=1$) and worsens as the angle increases toward the periphery of the Field of View.

---

### **Lecture 5: Channel State Information & WiFi Sensing**

**25. Which of the following is a fundamental reason why RSSI (Received Signal Strength Indicator) is unreliable for fine-grained indoor sensing?**

*   A. It operates at too high of a frequency to penetrate walls.
*   B. It only measures the Line-of-Sight path and ignores reflections.
*   C. It is a single scalar value that aggregates all multipath signals, meaning an obstacle could actually cause RSSI to increase due to constructive interference.
*   D. It requires massive multi-antenna arrays to be calculated.
**Answer: C**

**Explanation:** Because of multipath fading, a human blocking the direct path might alter the phase of the signals such that the remaining reflected paths combine constructively, unexpectedly raising the total RSSI.

**26. In the context of WiFi CSI dynamics, human motion alters which component of the Channel Frequency Response (CFR)?**

*   A. The static component only.
*   B. Both the static and the dynamic components equally.
*   C. The dynamic component only.
*   D. Neither; human motion only affects the MAC layer.
**Answer: C**

**Explanation:** The total channel response is $H = H_{\text{static}} + H_{\text{dynamic}}$. Stationary objects (walls, furniture) make up the static part, while moving bodies generate the time-varying dynamic component.

**27. What is the primary advantage of the Statistical Electromagnetic Approach (using the Autocorrelation Function) over the traditional Doppler Frequency Shift (DFS) approach in WiFi sensing?**

*   A. It extracts the absolute absolute speed of the target independent of their position and movement direction relative to the WiFi link.
*   B. It completely eliminates the static components of the environment.
*   C. It requires only a single frequency subcarrier to operate.
*   D. It can directly render 3D point clouds of the target.
**Answer: A**

**Explanation:** Standard DFS only measures the *radial* projection of velocity (how fast the target moves directly toward/away from the antennas). The ACF method uses the 0th-order Bessel function to estimate absolute speed regardless of trajectory.

---

### **Lecture 6: IoT System Design**

**28. In the MQTT protocol, a subscriber subscribes to the topic `home/groundfloor/+/temperature`. Which of the following published topics will this client successfully receive?**

*   A. `home/groundfloor/kitchen/brightness`
*   B. `home/firstfloor/kitchen/temperature`
*   C. `home/groundfloor/livingroom/temperature`
*   D. `home/groundfloor/kitchen/oven/temperature`
**Answer: C**

**Explanation:** The `+` is a single-level wildcard. It matches exactly one level in the hierarchy. Option C matches perfectly. Option D has too many levels, and Option A ends in `brightness` instead of `temperature`.

**29. What is the primary function of a Hampel Filter in an IoT data pipeline?**

*   A. To completely block high-frequency signals above a cutoff threshold.
*   B. To act as a robust statistical filter for outlier detection and removal in time-series data.
*   C. To perform a Fast Fourier Transform on incoming data streams.
*   D. To convert analog signals to digital signals.
**Answer: B**

**Explanation:** The Hampel filter uses a sliding window to calculate the local median and Median Absolute Deviation (MAD) to identify and remove extreme outliers in time-series data.

---

### **Lecture 7: Mobile Sensing**

**30. Which mobile smartphone sensor provides the most reliable data for detecting when a user walks up a flight of stairs or takes an elevator?**

*   A. Magnetometer
*   B. Proximity Sensor
*   C. Gyroscope
*   D. Barometer
**Answer: D**

**Explanation:** Barometers measure atmospheric pressure, which decreases linearly and reliably as elevation increases (ascending floors), making it the perfect sensor for vertical floor transitions.

**31. What is the most significant practical challenge when using a smartphone's accelerometer for step counting?**

*   A. Accelerometers cannot measure gravity.
*   B. Accelerometers sample at too low of a frequency (e.g., 1 Hz).
*   C. Massive signal variability depending on where the user places the device (e.g., pocket, backpack, hand) and individual walking styles.
*   D. Accelerometers only measure motion in two dimensions.
**Answer: C**

**Explanation:** The signal shape changes dramatically based on device placement and user demographics, making it difficult to write a universal threshold or algorithm for step detection.

**32. In the Human Activity Recognition (HAR) preprocessing pipeline, why is "coordinate transformation" (calculating the vector magnitude $m = \sqrt{x^2+y^2+z^2}$) commonly performed on raw accelerometer data?**

*   A. To filter out high-frequency noise.
*   B. To isolate the Earth's gravitational pull.
*   C. To reduce the 3-axis data into a single time series that is independent of how the device is physically oriented.
*   D. To convert the data from the time domain to the frequency domain.
**Answer: C**

**Explanation:** Taking the vector magnitude collapses the $x,y,z$ axes into one scalar value, making the data orientation-invariant (it doesn't matter if the phone is upside down or tilted in the user's pocket).

---

### **Lecture 8: Indoor Localization**

**33. Why does standard trilateration fail to provide accurate localization using WiFi RSSI indoors?**

*   A. WiFi signals travel faster than the speed of light indoors.
*   B. The variance in RSSI at a fixed distance is extremely high due to severe multipath fading, making the inverse mapping of RSSI-to-distance mathematically ill-posed.
*   C. Most smartphones do not have WiFi chips.
*   D. RSSI cannot be measured below 5 GHz.
**Answer: B**

**Explanation:** RSSI is wildly inconsistent indoors because of reflections and obstacles (shadowing). You cannot reliably convert a fluctuating RSSI value into a precise physical distance (ranging), which trilateration requires.

**34. In the context of WiFi Fingerprinting localization, what is the primary drawback of the "Offline Phase"?**

*   A. It requires the deployment of thousands of custom Bluetooth beacons.
*   B. It is extremely time-consuming and labor-intensive to manually survey and build the radio map for an entire building.
*   C. It relies on GPS satellites, which are blocked indoors.
*   D. It drains the user's smartphone battery instantaneously.
**Answer: B**

**Explanation:** Fingerprinting requires a pre-surveyed radio map. Sending humans to record WiFi signatures at every square meter of a building is heavily labor-intensive and costly.

**35. What is the primary failure mode of Pedestrian Dead-Reckoning (PDR) using an IMU?**

*   A. It requires line-of-sight to WiFi Access Points.
*   B. Step counting algorithms cannot detect running.
*   C. It suffers from unbounded, accumulative tracking error over time due to sensor drift.
*   D. It only works if the user holds the phone perfectly flat.
**Answer: C**

**Explanation:** Dead-reckoning integrates relative motion from a starting point. Any tiny error in heading or step length accumulates indefinitely with every single step, eventually leading to massive location drift.

**36. How do Particle Filters integrated with floor maps improve indoor inertial tracking?**

*   A. They act as physical anchors on the walls that emit ultrasonic beeps.
*   B. They eliminate impossible location hypotheses by assigning zero weight to particles that attempt to pass through solid walls on the map.
*   C. They convert RSSI signals into precise time-of-flight measurements.
*   D. They boost the sampling rate of the smartphone's IMU.
**Answer: B**

**Explanation:** Particle filters simulate thousands of possible user trajectories. The floor plan acts as a physical constraint; if a particle's trajectory walks through a mapped wall, that particle is killed (assigned zero weight), automatically correcting sensor drift.

---

### **Lecture 9: Deep Wireless Sensing**

**37. When curating a large-scale CSI dataset for Deep Learning, what makes it uniquely difficult compared to curating an image dataset (like ImageNet)?**

*   A. CSI files are significantly smaller and harder to store.
*   B. CSI contains no interpretable visual semantic information, meaning all ground-truth labels must be recorded synchronously at the exact moment of data capture; they cannot be labeled offline later.
*   C. Deep learning models cannot process complex numbers.
*   D. There are no privacy concerns with CSI data, making it too easy to over-collect.
**Answer: B**

**Explanation:** You can look at a photo later and label it "dog". You cannot look at a raw CSI heatmap later and reliably label it "user drinking water." The label must be locked in during the physical experiment.

**38. The RFBoost framework introduces "Physical Data Augmentation." Why is this preferred over applying standard image augmentation (like flipping or rotating) to a CSI spectrogram?**

*   A. Image augmentations take too much CPU power to compute.
*   B. Physical data augmentation is the only way to convert WiFi to mmWave.
*   C. Standard image transforms destroy the physical meaning of the RF data (e.g., flipping the time axis reverses motion semantics), whereas physical augmentation preserves valid RF properties.
*   D. RFBoost uses Large Language Models to write new CSI data from scratch.
**Answer: C**

**Explanation:** RF signals are governed by physics. Flipping a spectrogram vertically inverses the frequency shifts, turning a "push" into a "pull". RFBoost uses mathematically valid transformations like time-shifting or selecting subset antennas.

**39. In the Widar3.0 dataset, the Body-coordinate Velocity Profile (BVP) is used as the data representation instead of raw CSI. What is the primary benefit of BVP?**

*   A. It requires less computational overhead than raw CSI.
*   B. It removes environmental and positional domain bias, retaining a clean physical motion signature that generalizes across different rooms and orientations.
*   C. It requires only a single WiFi receiver to operate.
*   D. It allows the neural network to visualize the user's face.
**Answer: B**

**Explanation:** BVP is a theoretically domain-independent representation. It strips away the reflections of the specific room and the user's orientation, leaving only the pure physical motion profile, solving the cross-domain generalizability problem.

**40. The RF-Diffusion model uses "Time-Frequency Diffusion" to synthesize fake RF data. What two critical physical properties does this model explicitly prioritize?**

*   A. MAC layer headers and IP addresses.
*   B. Time-domain amplitude accuracy and frequency-domain continuity.
*   C. Bounding box coordinates and pixel density.
*   D. Antenna length and power consumption.
**Answer: B**

**Explanation:** RF-Diffusion operates in both domains simultaneously, prioritizing precise amplitude in the time domain and continuous, un-broken spectral structures in the frequency domain to ensure the generated signals obey RF physics.

**41. The SLNet architecture features a "Spectrogram Enhancement Network (SEN)." What is its specific purpose?**

*   A. To encrypt the CSI data before passing it to the cloud.
*   B. To upscale the resolution of cameras monitoring the environment.
*   C. To correct and remove spectral leakage and artifacts natively produced by the Short-Time Fourier Transform (STFT).
*   D. To convert human speech into text.
**Answer: C**

**Explanation:** STFT inherently suffers from spectral leakage, which blurs the spectrogram. The SEN cleans these artifacts to produce sharp, ideal frequency responses prior to feature extraction.

---

### **Lecture 10: Systems Evaluation**

**42. You evaluate an IoT intrusion detection model. It has a Precision of 95% but a Recall of 30%. What does this indicate about the system's real-world behavior?**

*   A. It catches almost all intruders, but also triggers many false alarms.
*   B. When it triggers an alarm, it is almost certainly a real intruder, but it completely misses the vast majority of actual intruders.
*   C. It is a perfectly balanced system.
*   D. The system is misconfigured and classifying everything as an intruder.
**Answer: B**

**Explanation:** High precision (95%) means its positive predictions are highly reliable (few false alarms). Low recall (30%) means it only caught 30% of the actual positive cases, missing 70% of them (many false negatives).

**43. Which evaluation metric should you prioritize for a medical wearable device where missing a cardiac event (False Negative) is fatal, but occasional false alarms (False Positives) are acceptable?**

*   A. Precision
*   B. Accuracy
*   C. Recall
*   D. Mean Squared Error
**Answer: C**

**Explanation:** Recall measures the ability to find *all* relevant positive instances ($\frac{TP}{TP + FN}$). Minimizing False Negatives maximizes Recall, making it the critical metric for life-safety systems.

**44. Why is general "Accuracy" a poor metric for evaluating a fall detection dataset containing 990 hours of normal walking and only 10 actual falls?**

*   A. Accuracy cannot handle time-series data.
*   B. The dataset is imbalanced; a broken model that simply guesses "No Fall" 100% of the time will score 99% accuracy while failing its actual task.
*   C. Falls can only be evaluated using the F1-Score.
*   D. Accuracy requires a complex-valued neural network to compute.
**Answer: B**

**Explanation:** Accuracy fails on heavily imbalanced datasets because the overwhelming majority class masks the model's inability to detect the minority class.

**45. When reading an ROC (Receiver Operating Characteristic) curve, what represents the "perfect" classifier?**

*   A. A diagonal line from the bottom-left to top-right.
*   B. A curve with an Area Under Curve (AUC) of 0.5.
*   C. A curve that hugs the bottom right corner.
*   D. A curve that reaches the absolute top-left corner, with an AUC of 1.0.
**Answer: D**

**Explanation:** The top left corner represents 100% True Positive Rate and 0% False Positive Rate. An Area Under the Curve (AUC) of 1.0 indicates perfect classification.

**46. For evaluating a continuous regression task like indoor spatial localization (predicting X, Y coordinates), which visualization is considered the standard default for reporting performance?**

*   A. Confusion Matrix
*   B. Cumulative Distribution Function (CDF) plot
*   C. ROC Curve
*   D. Venn Diagram
**Answer: B**

**Explanation:** A CDF plots the full distribution of the localization error across all samples. It allows readers to instantly see percentile performance (e.g., "80% of estimates had an error of less than 1.2 meters").

---

### **Mixed Integration Questions**

**47. A smart home system uses WiFi sensing to detect if a user is standing or sitting, and uses a smartphone's barometer to detect which floor they are on. This system is relying on:**

*   A. Exclusively device-free sensing.
*   B. Exclusively device-based sensing.
*   C. A fusion of device-free sensing (WiFi) and device-based sensing (barometer).
*   D. Acoustic ranging and trilateration.
**Answer: C**

**Explanation:** WiFi sensing analyzes ambient signal disruptions without the user wearing a device (device-free), while the barometer requires the user to physically carry the smartphone (device-based mobile sensing).

**48. Why would a deep learning engineer choose to use a CNN over standard classical machine learning (like an SVM) for classifying Human Activity from IMU data?**

*   A. CNNs require significantly less training data than SVMs.
*   B. CNNs automatically learn and extract high-dimensional hidden features from the raw segments, avoiding manual feature engineering.
*   C. CNNs use less battery power on the mobile device during training.
*   D. CNNs guarantee 100% cross-domain generalizability.
**Answer: B**

**Explanation:** Traditional ML requires manual feature engineering (e.g., calculating mean, variance, peaks). Deep learning architectures (like CNNs) automatically compute deep feature representations directly from the raw data.

**49. An acoustic ranging system sends an ultrasonic pulse. The echo is received exactly 0.02 seconds later. Assuming the speed of sound is $340 \text{ m/s}$, how far away is the reflecting wall?**

*   A. 3.4 meters
*   B. 6.8 meters
*   C. 1.7 meters
*   D. 17 meters
**Answer: A**

**Explanation:** The total distance the sound traveled (there and back) is $d_{total} = v \cdot t = 340 \cdot 0.02 = 6.8$ meters. Because the wall is half the total travel distance, $d = 6.8 / 2 =$ 3.4 meters.

**50. You are tasked with evaluating a new WiFi-based breathing monitoring system against an existing medical ECG machine. You decide to plot the absolute error of the breathing rate (in BPM) using a visualization that displays the median, quartiles, and the full continuous shape of the error distribution. What plot should you use?**

*   A. A Boxplot
*   B. A Violin Plot
*   C. A Scatter Plot
*   D. An ROC Curve
**Answer: B**

**Explanation:** While a boxplot shows the median and quartiles, a Violin plot extends the boxplot by also displaying the full continuous density/shape of the underlying data distribution.

---


## **Part 3: Sample Calculation Questions**

Here is a set of brand-new sample questions modeled directly on the format, difficulty, and topics of the COMP3516 past paper. 

Per your request, I have included **full, step-by-step physical explanations** for the formulas in the calculation section to help you understand *why* the math works, rather than just plugging in numbers.

---

# COMP3516 Data Analytics for IoT: Practice Paper

## Part A: Multiple Choice Questions

### Section 1: Exactly ONE correct answer per question (1 mark each)

**1. You are designing a smart-home security system using FMCW mmWave radar. You need the radar to be able to distinguish between a person's moving chest (breathing) and their stationary arm, which are 5 cm apart. What is the absolute *minimum* chirp bandwidth required for this radar?**

- A. 2 GHz
- B. 3 GHz
- C. 4 GHz
- D. 5 GHz
> **Answer: B.** Range resolution $d_{res} = \frac{c}{2B}$. Rearranging for bandwidth: $B = \frac{c}{2d_{res}} = \frac{3 \times 10^8}{2 \times 0.05} = 3 \times 10^9 \text{ Hz} = 3 \text{ GHz}$. 

**2. When tracking a pedestrian using an IMU (Pedestrian Dead-Reckoning), which method is used to estimate travel distance?**

- A. Double integration of the accelerometer's linear acceleration over time.
- B. Integrating the gyroscope's angular velocity to find the linear path.
- C. Detecting steps using acceleration peaks/valleys and multiplying by stride length.
- D. Measuring the Doppler frequency shift of the Earth's magnetic field.
> **Answer: C.** Double integration (A) causes unbounded error/drift. Step counting (C) is the standard PDR approach.

**3. In deep learning for wireless sensing (Deep Wireless Sensing), what is the primary reason standard Computer Vision (CV) data augmentation techniques like "random image flipping" or "rotation" often fail when applied to CSI time-frequency spectrograms?**

- A. CSI spectrograms are always real-valued, whereas CV models expect complex values.
- B. Flipping or rotating a spectrogram fundamentally destroys or reverses the physical laws of motion and time-frequency semantics.
- C. Spectrograms are 1D arrays, making 2D image transforms mathematically impossible.
- D. Deep learning models cannot process the high signal-to-noise ratio of raw CSI data.
> **Answer: B.** Time and frequency are strictly directional physical properties. Flipping the time axis reverses the motion; flipping the frequency axis changes the physical speed/direction.

### Section 2: One OR MORE correct answers per question (2 marks each)

**4. The BeepBeep acoustic ranging protocol solves the issue of clock synchronization between two smartphones. Which of the following statements about BeepBeep are true?**

- A. It requires the two devices to be perfectly time-synchronized before sending the first beep.
- B. It uses a symmetric two-way beep exchange, where both devices record their own beeps and the other's beeps.
- C. It relies on the difference between Local Effective Time of Arrival (ETOA) at both devices to cancel out hardware processing delays.
- D. It relies on measuring the phase shift of an ultrasonic continuous wave.
> **Answer: B, C.** 

**5. Which of the following are valid reasons why raw CSI (Channel State Information) is superior to RSSI (Received Signal Strength Indicator) for indoor sensing tasks like breathing detection?**

- A. CSI provides fine-grained amplitude and phase data across multiple orthogonal subcarriers, rather than just one aggregate power value.
- B. CSI completely eliminates the multipath effect, making signals travel in a perfect straight line.
- C. CSI is a PHY-layer measurement, allowing us to observe how the environment affects specific frequencies.
- D. RSSI is highly susceptible to constructive and destructive interference, making it fluctuate unpredictably even when the target is stationary.
> **Answer: A, C, D.** 

---

## Part B: Essay and Calculation Questions

### Question 1: Radar Sensing & Formula Explanations (15 Points)
You are using a **77 GHz FMCW radar** to track a moving robot in an indoor warehouse. 

*   The speed of light $c = 3 \times 10^8 \text{ m/s}$.
*   The radar chirp slope $S = 60\,\text{MHz}/\mu\text{s}$.
*   The chirp duration $T_c = 50\,\mu\text{s}$.

**Part A (7 Points)**
The radar receives a reflected signal from the robot. After mixing the transmitted and received signals, the resulting Intermediate Frequency (IF) tone is exactly $f_\tau = 2 \text{ MHz}$. 
Calculate the physical distance to the robot. **Provide a full explanation of the underlying physics and the formula used.**

> **Answer:**
> **1. The Calculation:**
> First, ensure all units match (convert to standard SI units: Hz and seconds):
> $S = 60\,\text{MHz}/\mu\text{s} = 60 \times 10^{12}\,\text{Hz/s}$
> $f_\tau = 2 \text{ MHz} = 2 \times 10^6 \text{ Hz}$
> 
> $d = \frac{c \cdot f_\tau}{2S}$
> $d = \frac{(3 \times 10^8) \times (2 \times 10^6)}{2 \times (60 \times 10^{12})}$
> $d = \frac{6 \times 10^{14}}{120 \times 10^{12}} = \frac{600}{120} = \mathbf{5 \text{ meters}}$.
> 
> **2. The Formula Explanation:**
> An FMCW radar determines distance by measuring *frequency differences*. It transmits a chirp whose frequency rises linearly over time at a rate of $S$ (the slope). 
> 
> When the signal bounces off the robot and returns, it has been delayed by the time-of-flight ($\tau$). Because the transmitted frequency is constantly rising, by the time the echo returns, the radar is already transmitting at a higher frequency. 

> *   The round-trip time of flight is $\tau = \frac{2d}{c}$ (distance there and back, divided by the speed of light).
> *   The frequency difference (Intermediate Frequency, $f_\tau$) between the current transmission and the delayed echo is simply the slope multiplied by the time delay: $f_\tau = S \cdot \tau$.
> *   Substituting $\tau$ gives: $f_\tau = S \cdot \frac{2d}{c}$. Rearranging this to solve for distance gives the final formula: $d = \frac{c \cdot f_\tau}{2S}$.

**Part B (8 Points)**
The robot begins moving. By observing the range-FFT peaks over two consecutive chirps, you notice the IF signal peak has not changed its frequency, but its **phase** has shifted by $\Delta\phi = \pi/2$ radians. 
Calculate the radial velocity of the robot. **Provide a full explanation of the underlying physics and the formula used.**

> **Answer:**
> **1. The Calculation:**
> First, find the wavelength ($\lambda$) of the 77 GHz signal:
> $\lambda = \frac{c}{f} = \frac{3 \times 10^8}{77 \times 10^9} \approx 0.0039 \text{ meters (3.9 mm)}$.
> 
> $v = \frac{\lambda \cdot \Delta\phi}{4\pi \cdot T_c}$
> $v = \frac{0.0039 \times (\pi/2)}{4\pi \times (50 \times 10^{-6})}$
> $v = \frac{0.0039 \times 0.5}{4 \times 0.00005} = \frac{0.00195}{0.0002} = \mathbf{9.75 \text{ m/s}}$.
> 
> **2. The Formula Explanation:**
> While frequency shifts are used to measure large distances, *phase shifts* are incredibly sensitive to micro-movements (the Doppler effect). 
> 
> A full phase cycle is $2\pi$ radians, which corresponds to the wave traveling exactly one wavelength ($\lambda$). Because the radar signal has to travel to the target *and* back, the total distance the wave travels changes by $2 \cdot \Delta d$. 

> *   Therefore, the phase shift is the fraction of the wavelength the object moved, times $2\pi$, multiplied by 2 for the round trip: $\Delta\phi = \frac{2 \cdot \Delta d}{\lambda} \cdot 2\pi = \frac{4\pi \cdot \Delta d}{\lambda}$.
> *   Rearranging to find the tiny distance moved between chirps: $\Delta d = \frac{\lambda \cdot \Delta\phi}{4\pi}$.
> *   Velocity is simply distance divided by time. Since this distance was covered in the time between two chirps ($T_c$), we divide by $T_c$ to get the final formula: $v = \frac{\lambda \cdot \Delta\phi}{4\pi \cdot T_c}$.

---

### Question 2: Acoustic Ranging & Timestamps (10 Points)
You are implementing the BeepBeep protocol using two smartphones, Phone A and Phone B. The speed of sound is $340 \text{ m/s}$. 

*   Phone A emits a beep. It records the end of its own beep transmission at $t_{A1}$.
*   Phone B records the arrival of A's beep at $t_{B1}$.
*   Phone B emits a reply beep. It records the end of its own transmission at $t_{B3}$.
*   Phone A records the arrival of B's beep at $t_{A3}$.

Through WiFi, Phone A and B exchange their Local Effective Time of Arrival (ETOA). 

*   Phone A calculates: $\text{ETOA}_A = t_{A3} - t_{A1} = 150 \text{ ms}$.
*   Phone B calculates: $\text{ETOA}_B = t_{B3} - t_{B1} = 50 \text{ ms}$.

**Part A (6 Points)**
Calculate the physical distance between Phone A and Phone B.

> **Answer:**
> One-way propagation delay $P = \frac{|\text{ETOA}_A - \text{ETOA}_B|}{2}$
> $P = \frac{|150 \text{ ms} - 50 \text{ ms}|}{2} = \frac{100 \text{ ms}}{2} = 50 \text{ ms} = 0.05 \text{ seconds}$.
> 
> Distance $D = c \cdot P = 340 \text{ m/s} \times 0.05 \text{ s} = \mathbf{17 \text{ meters}}$.

**Part B (4 Points)**
Why do we take the *difference* between the two ETOA values and divide by 2? Explain how this mathematically removes the unknown clock offset between Phone A and Phone B.

> **Answer:**
> Because Phone A and Phone B are independent devices, their internal clocks are not synchronized. Let's say Phone B's clock is running $\Delta_{clock}$ seconds ahead of Phone A. 

> *   If we try to calculate one-way time of flight directly ($t_{B1} - t_{A1}$), the result will be ruined by $\Delta_{clock}$.
> *   However, $\text{ETOA}_A$ is measured entirely on Phone A's clock. $\text{ETOA}_B$ is measured entirely on Phone B's clock. 
> *   By subtracting $\text{ETOA}_B$ from $\text{ETOA}_A$, the delay caused by Phone B waiting to send its reply ($t_{B3} - t_{B1}$) is cleanly subtracted from the total time Phone A waited ($t_{A3} - t_{A1}$). 
> *   What remains is *only* the acoustic travel time from A to B, plus the travel time from B to A. Since the sound traveled the same distance twice, we divide by 2 to get the one-way propagation time, completely avoiding the need to align the two clocks.

---

### Question 3: Signal Analytics & Autocorrelation (10 Points)
You are monitoring an elderly patient using a completely device-free, statistical WiFi sensing approach based on the Autocorrelation Function (ACF) of the Channel State Information (CSI).

You plot the ACF of the CSI amplitude over a 60-second time window. The resulting plot shows a smooth, periodic waveform (like a sine wave) that does *not* decay to zero. You count exactly 18 distinct peaks in the ACF plot within this 60-second window.

**Part A (4 Points)**
What physical human activity is this system currently observing? Justify your answer based on the shape of the ACF plot.

> **Answer:**
> The system is observing **human breathing (respiration)**. 
> *Justification:* Random motion (like walking or waving) would cause the ACF to decay rapidly to zero, as the signal is not correlated with itself over long time lags. A smooth, non-decaying periodic oscillation in the ACF is the hallmark signature of minute, repeating physiological motions (chest rise and fall).

**Part B (4 Points)**
Estimate the value of this activity (include the correct units). 

> **Answer:**
> 18 peaks in a 60-second window means the periodic motion repeats 18 times per minute. 
> Therefore, the breathing rate is **18 Breaths Per Minute (BPM)**.

**Part C (2 Points)**
If the patient suddenly stands up and starts walking around the room, how will the ACF plot change visually?

> **Answer:**
> The smooth periodic peaks will instantly disappear. The ACF curve will spike near a time lag of 0 (perfect correlation with itself), and then **rapidly decay toward zero** at larger time lags, reflecting the unpredictable, dynamic nature of walking.
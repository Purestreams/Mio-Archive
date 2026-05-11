Wireless IoT and Connectivity: AIoT combines connectivity, sensing, and analytics./ 2G mainly enabled digital voice, 4G enabled LTE broadband, and 5G targets industrial IoT with extreme data rates and low latency./ BLE is short-range and ultra-low-power for PAN use./ WiFi offers high-rate ubiquitous 802.11 connectivity./ Zigbee is IEEE 802.15.4 for low-power low-rate mesh networks./ LoRa is LPWAN and uses Chirp Spread Spectrum for long-range low-bandwidth communication./ NB-IoT and LTE-M are licensed cellular LPWAN options.

Signal Processing Laws: Nyquist Sampling Theorem requires $f_s > 2f_{max}$ to prevent aliasing./ Shannon-Hartley Theorem gives $C = B \cdot \log_2(1 + S/N)$ as channel capacity from bandwidth and signal-to-noise ratio.

Analog Digital and FFT Basics: Analog signals are continuous and digital signals are discrete./ ADC consists of time-domain sampling and amplitude quantization./ Complex signals combine sine and cosine components in the complex plane./ FFT converts time-domain signals to frequency-domain spectra and is used to expose dominant frequencies such as tremor, breathing, or IF tones.

Radar Sensing and FMCW Fundamentals: FMCW transmits a linear chirp whose frequency changes over time and receives an echo delayed by $\tau = 2d/c$ from the target./ Mixing the received echo with the current transmit chirp produces a beat signal whose frequency is proportional to delay, with $f_\tau = S\tau$./ Range estimation uses $d = c f_\tau / 2S$ with beat frequency and chirp slope./ Range resolution uses $d_{res} = c / 2B$, so bandwidth alone determines theoretical resolution./ Velocity estimation uses $v = \lambda \Delta \phi / 4 \pi T_c$ from inter-chirp phase shifts across multiple chirps./ Velocity resolution uses $v_{res} = \lambda / 2 T_f$ and depends on total frame time./ Angle of arrival uses $\theta = \sin^{-1}(\lambda \Delta \phi / 2 \pi s)$ from antenna phase differences./ In practice, FMCW gets range from beat frequency within a chirp, velocity from change across chirps, and angle from difference across antennas./ Phase sensitivity follows $\Delta \phi = 4 \pi \Delta d / \lambda$, so small distance changes create large phase changes./ Wavelength follows $\lambda = c/f$, with 60 GHz giving about 5 mm in air./ IF frequency shift follows $\Delta f = S \cdot 2 \Delta d / c$, where $S$ is the chirp slope./ Chirp slope controls frequency sensitivity to range changes./ With $\lambda = 4$ mm, a 1 mm distance change gives a $\pi$ phase change; if $S = 50\,\text{MHz}/\mu\text{s}$, the frequency shift is $1000/3$ Hz.

Radar Processing Insights: Range-FFT resolves targets only by radial distance, so equidistant targets merge into one peak./ Doppler-FFT or inter-chirp phase tracks motion across chirps./ Phase shift is much more sensitive than frequency shift for sub-wavelength micro-motion./ AoA resolution is best at boresight and worsens away from $\theta = 0$ because of a $1/\cos(\theta)$ effect.

Evaluation Statistics: Precision is $TP / (TP + FP)$ and measures the cost of false alarms./ Recall is $TP / (TP + FN)$ and measures the ability to capture true positives./ F1-score is $2 \cdot P \cdot R / (P + R)$ and balances precision with recall.

Evaluation Metrics and Plots: Accuracy can be misleading on heavily imbalanced data./ Recall is the priority when false negatives are costly, while precision matters when false positives are costly./ ROC curves plot TPR against FPR and the ideal classifier sits at the top-left with AUC 1./ Regression tasks often report MSE, RMSE, and CDF rather than classification scores.

Mobile Sensing Hardware and Capabilities: Accelerometers measure proper or linear acceleration for step counting, motion detection, linear motion tracking, and dead reckoning./ Gyroscopes measure angular velocity and, together with magnetometers, support rotation tracking, direction change estimation, and absolute heading./ Magnetometers measure the Earth's magnetic field and support compass heading and landmark-based localization./ Barometers measure atmospheric pressure for relative elevation change, absolute altitude estimation, floor change detection, and elevator sensing./ GPS provides absolute outdoor location, but accuracy degrades indoors and in urban canyons; inertial tracking can bridge missing readings./ Landmark correction uses pressure changes in elevators, magnetic distortions, and occasional GPS near windows to correct accumulated inertial errors./ Event detection includes elevator detection by barometer, door-entry detection by occasional GPS, and magnetic anomalies as spatial landmarks./ Proximity sensors detect nearby objects for call-screen control and simple context awareness./ Ambient light sensors measure illumination for brightness adaptation and coarse environment sensing./ Microphones and cameras can also be used for audio-visual sensing, but they usually consume more power and raise stronger privacy concerns.

IoT System Pipeline and Detection: A typical pipeline is hardware or sensors to acquisition to preprocessing to core algorithms to user interface./ MQTT uses hierarchical topics for data acquisition, where + matches one level and # matches remaining levels./ CFAR compares a test cell against surrounding background noise for target detection./ Hampel filtering removes outliers using local median and MAD.

Human Activity Recognition and IMU Preprocessing: Step counting commonly uses FSM peak-and-valley detection on acceleration./ Coordinate transformation uses vector magnitude to reduce orientation sensitivity./ Traditional HAR uses handcrafted features such as mean, variance, and peaks with classifiers such as SVM or K-NN./ Deep models can learn features directly from raw segments.

WiFi CSI Processing and Mathematics: CSI measures complex channel gains./ CSI amplitude is $\sqrt{a^2 + b^2}$ or $\sqrt{\text{real}^2 + \text{imag}^2}$, and CSI phase is $\arctan(b/a)$ or $\arctan(\text{imag}/\text{real})$./ Superimposing static $-5 + 19j$ and dynamic $20 - 23j$ gives $15 - 4j$./ SNR improves through frequency diversity across subcarriers and space diversity across antennas./ Common input representations include raw time series, time-frequency spectrograms, and antenna-carrier spatial matrices./ FFT window length sets frequency resolution $\Delta f = 1/T$, while longer ACF windows improve single-user estimation robustness.

RSSI vs CSI and Sensing Approaches: RSSI is a single unstable total-power scalar and can even rise under constructive interference./ Total CFR can be viewed as $H = H_{static} + H_{dynamic}$, with motion mainly altering the dynamic component./ Geometric sensing uses ToF, AoA, and DFS./ Statistical sensing uses ACF to estimate absolute speed and periodic motion more independently of user location and direction.

OFDM and Features: Orthogonal Frequency Division Multiplexing splits one wideband channel into many orthogonal narrowband subcarriers that transmit data in parallel./ Orthogonality allows subcarriers to overlap in frequency without mutual interference under ideal synchronization, which improves spectral efficiency./ OFDM is robust to multipath and frequency-selective fading because each subcarrier experiences an approximately flat channel and can be equalized with low complexity./ A cyclic prefix reduces inter-symbol interference when the channel delay spread stays within the guard interval./ OFDM is efficiently implemented with IFFT and FFT and works well with MIMO and modern wireless systems such as WiFi./ OFDM also has drawbacks including high peak-to-average power ratio and sensitivity to timing offset and carrier-frequency offset.

CSI Representation Tradeoffs: Raw time-series preserves physical phase information and needs minimal preprocessing for low latency, but suffers heavy noise from hardware offsets and requires massive training data./ Spectrograms visualize rhythmic cycles such as breathing and can leverage pre-trained vision models, but STFT introduces high computational overhead and loses transient temporal resolution./ Spatial matrices capture MIMO diversity and frequency correlations, but they have high risk of environment overfitting and poor cross-room generalizability.

Indoor Localization and Metrics: RSSI fingerprinting compares vectors using Euclidean distance $d(A, B) = \sqrt{\sum (p_i - q_i)^2}$./ RSSI confidence is reduced by path loss, shadowing, multipath effect, Non-line-of-sight propagation, environmental change, and hardware and OS latency./ Trilateration can be solved from circles or ellipses when geometric constraints are known./ TRRS measures multipath similarity rather than physical distance because spatial decorrelation happens within a few centimeters./ RTT methods such as BeepBeep can be accurate but are unsuitable for low-power tags because of recording power, hardware complexity, and processing cost./ 160 MHz bandwidth gives 1.875 m resolution, while 80 MHz gives 3.75 m resolution.

Indoor Localization Approaches and PDR: Fingerprinting matches live radio or magnetic signatures to a surveyed map and is accurate but labor-intensive to maintain./ PDR uses IMUs, step counts, and heading, but drift accumulates without bound over time./ Particle filters with floor maps remove impossible trajectories by assigning zero weight to particles that cross walls.

Signal Propagation and Physics: Spatial resolution follows $\Delta d = c/B$ and determines whether separate paths can be resolved in the channel impulse response./ With 80 MHz WiFi, the resolution is 3.75 m, so paths separated by less than this merge into one CIR peak./ Penetration loss can be modeled as 0.5, and each reflection can attenuate by about 0.6./ A direct path can be weaker than a reflected path under Non-Line-of-Sight blockage./ Paths at 1 m and 3 m can merge into one peak when the resolution is too coarse.

Sensing Estimation Theory: Nyquist requires $f_s > 2 f_{max}$ for reliable sensing./ A 30 BPM breathing signal corresponds to 0.5 Hz and therefore needs at least 1 Hz sampling./ Oversampling improves SNR by spreading quantization noise./ Maximal Ratio Combining maximizes static SNR but suppresses dynamic motion signals.

Reasons For and Against Deep Learning in Wireless Sensing: Reasons to use deep learning include automated feature extraction, because it can learn complex non-linear relationships in multipath signals without hand-crafted geometric or physical models such as the Fresnel Zone model./ Reasons to use deep learning also include superior handling of high-dimensional CSI data across multiple antennas, subcarriers, and time, allowing the model to capture correlations that simple threshold-based algorithms miss./ Reasons not to use deep learning include weak cross-domain generalizability, because a model may learn environment-related features rather than activity-related features and then fail in new environments without extensive retraining./ Reasons not to use deep learning also include interpretability and black-box issues, which make alarms harder to debug or trust in critical applications such as elderly fall detection.

Deep Wireless Sensing Models and Pitfalls: RFBoost uses physically valid augmentation such as time or frequency shifts instead of generic image flips./ Widar3.0 uses Body-coordinate Velocity Profile (BVP) to reduce environment and orientation bias./ RF-Diffusion preserves time-domain amplitude accuracy and frequency-domain continuity when synthesizing RF data./ SLNet uses SEN to reduce STFT spectral leakage./ Raw CSI is not visually interpretable, so labels usually must be recorded synchronously during data collection rather than offline afterward.

System Comparison: mmWave radar operates around 60-80 GHz and gives smaller wavelength, stronger phase sensitivity, better angle resolution, and stronger interference robustness./ ISM-band FMCW radar offers high resolution with better penetration than mmWave and therefore acts as a middle ground./ WiFi sensing has the lowest cost and best wall penetration, but lower resolution and higher phase errors due to unsynchronized clocks./ Systems with the same bandwidth have the same theoretical range resolution regardless of carrier frequency./ ISM and WiFi usually offer wider coverage and better penetration, commodity WiFi is usually cheapest, and custom ISM radars cost more.

Sleep and Motion Analysis: Awake state shows frequent macro-motion and intensive movement./ NREM sleep shows stable rhythmic breathing with lower variability./ REM sleep shows higher breathing-rate variability than NREM./ CSI can separate sleep stages through macro-motion and micro-breathing patterns./ In ACF, high-frequency cycles indicate speed, low-frequency cycles indicate breathing, and high-amplitude random fluctuations indicate irregular motion./ MRC is useful for speed estimation but should be avoided for motion statistics because it suppresses dynamic multipath fluctuations./ Irregular motion creates high-amplitude random ACF noise, while an empty room produces low-amplitude random ACF noise./ A normalized ACF must equal 1 at $\tau = 0$.

ACF Numerical Estimation: Constant speed follows $v = (f_d \cdot \lambda)/2$ from high-frequency ACF oscillation./ A worked example gives $v = 0.2$ m/s for 10 cycles in 1.5 s when $\lambda = 6$ cm./ Breathing rate follows $\text{BPM} = 60/T$, so a 3 s cycle corresponds to 20 BPM./ Incorrect ACF plots often show offsets or physically impossible values.

Robot Inertial Tracking: Dead reckoning obtains location by integrating local $v_x(t)$ and $v_y(t)$ over time./ Global projection converts motion to the East-North frame using rotation angle $\theta$./ Constant velocity gives zero accelerometer reading./ Linearly changing velocity gives constant accelerometer amplitude./ Flat 2D motion gives zero gyroscope readings on the x and y axes.

Tracking Tag Design: General resolution follows $\Delta d = v / 2B$, where $v$ is the speed of light or sound depending on the medium./ WiFi needs about 150 MHz bandwidth for 1 m accuracy./ Acoustic sensing needs only 171.5 Hz bandwidth for 1 m accuracy./ Pseudo-ultrasound in the 20-24 kHz band gives about 4.29 cm resolution without being intrusive.

Acoustic Ranging and BeepBeep: BeepBeep uses symmetric two-way beeps and local ETOA values to cancel clock offset between phones./ One-way propagation delay is half the absolute difference between the two ETOA values./ Distance equals sound speed times one-way propagation delay./ It can be accurate but is usually too power-hungry for low-power tags.

Appendix:

Nyquist sampling:
$$
f_s > 2f_{\max}
$$
do not sample below the boundary; wording can be "at least" or slightly above.

Shannon-Hartley theorem:
$$
C = B \cdot \log_2\left(1 + \frac{S}{N}\right)
$$
use linear $S/N$, not dB; log base is 2.

Radar:

FMCW round-trip delay:
$$
t_{delay} = \frac{2d}{c}
$$
round trip, so factor 2.

Beat frequency:
$$
f_{\tau} = S \cdot t_{delay}
$$
$S \neq B$.

FMCW range:
$$
d = \frac{c f_{\tau}}{2S}
$$
keep the 2; use chirp slope, not carrier frequency.

Radar range resolution:
$$
d_{res} = \frac{c}{2B}
$$
resolution depends on bandwidth, not carrier frequency alone.

Velocity from inter-chirp phase:
$$
v = \frac{\lambda \Delta \phi}{4 \pi T_c}
$$
use $T_c$, not $T_f$.

Velocity resolution:
$$
v_{res} = \frac{\lambda}{2T_f}
$$
use $T_f$, not $T_c$.

Angle of arrival:
$$
AoA = \sin^{-1}\left(\frac{\lambda \Delta \phi}{2 \pi s}\right)
$$
antenna phase difference, and keep the inverse sine.

Phase sensitivity:
$$
\Delta \phi = \frac{4 \pi \Delta d}{\lambda}
$$
smaller $\lambda$ means larger phase sensitivity.

Wavelength:
$$
\lambda = \frac{c}{f}
$$
$c$ is propagation speed.

IF frequency shift from distance change:
$$
\Delta f = S \cdot \frac{2 \Delta d}{c}
$$
do not mix with FFT resolution.

Sanity check:
$$
\lambda = 4\text{ mm}, \quad \Delta d = 1\text{ mm} \Rightarrow \Delta \phi = \pi
$$
if far from $\pi$, check units.

Wireless and Localization:

CSI amplitude:
$$
|CSI| = \sqrt{a^2 + b^2} = \sqrt{\text{real}^2 + \text{imag}^2}
$$
take magnitude, do not add real and imag directly.

CSI phase:
$$
\phi = \arctan\left(\frac{b}{a}\right) = \arctan\left(\frac{\text{imag}}{\text{real}}\right)
$$

FFT frequency resolution:
$$
\Delta f = \frac{1}{T}
$$
longer observation time improves resolution.

RSSI fingerprinting Euclidean distance:
$$
d(A, B) = \sqrt{\sum (p_i - q_i)^2}
$$

WiFi CIR spatial resolution:
$$
\Delta d = \frac{c}{B}
$$
WiFi uses $\frac{c}{B}$, radar uses $\frac{c}{2B}$.

Sanity check:
$$
160\text{ MHz} \Rightarrow 1.875\text{ m}, \quad 80\text{ MHz} \Rightarrow 3.75\text{ m}
$$
larger bandwidth means finer resolution.

Evaluation and Motion:

Precision:
$$
P = \frac{TP}{TP + FP}
$$

Recall:
$$
R = \frac{TP}{TP + FN}
$$
denominator uses $FN$.

Accuracy:
$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$
can mislead on imbalanced data.

False positive rate:
$$
FPR = \frac{FP}{FP + TN}
$$
ROC uses TPR vs FPR.

F1-score:
$$
F1 = \frac{2PR}{P + R}
$$
not the arithmetic mean.

Mean squared error:
$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2
$$
squared unit.

Root mean squared error:
$$
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2}
$$
back to original unit.

Doppler speed:
$$
v = \frac{f_d \cdot \lambda}{2}
$$
different from FMCW phase-based velocity.

Breathing rate:
$$
BPM = \frac{60}{T}
$$
$T$ in seconds.

Normalized ACF:
$$
R(0) = 1
$$
normalized ACF must start at 1.

Mobile Sensing:

Coordinate transform magnitude:
$$
m = \sqrt{x^2 + y^2 + z^2}
$$

Acoustic and Tag:

General resolution:
$$
\Delta d = \frac{v}{2B}
$$
$v$ is propagation speed, not target speed.

BeepBeep one-way propagation delay:
$$
P = \frac{|\text{ETOA}_A - \text{ETOA}_B|}{2}
$$

BeepBeep distance:
$$
D = v_{sound} \cdot P
$$
use sound speed, not light speed.

WiFi 1 m resolution target:
$$
B \approx 150\text{ MHz}
$$
this uses light speed.

Acoustic 1 m resolution target:
$$
B \approx 171.5\text{ Hz}
$$

Pseudo-ultrasound example:
$$
20\text{ kHz} \text{ to } 24\text{ kHz} \Rightarrow B = 4\text{ kHz} \Rightarrow \Delta d \approx 4.29\text{ cm}
$$
use bandwidth, not center frequency.
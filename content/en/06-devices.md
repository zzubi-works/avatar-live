# 6. Devices

On the **Devices** page you choose what moves your avatar. The devices you set here are shared by all avatars.

![Devices page](img/devices.png)

## Webcam

| Item | What it does |
|---|---|
| **Webcam** switch | Turn webcam tracking on / off |
| Camera list | Choose the camera to use |
| **Recenter** | Make your current face direction the front |
| **Tracking quality** | **Smooth** / **Balanced** / **Eco** — use Balanced or Eco alongside a game |

If there is a problem with the camera, the reason is shown on this card (not connected, image too dark, in use by another app, and so on).

## Microphone

| Item | What it does |
|---|---|
| **Microphone** switch | Turn the microphone (lip sync) on / off |
| Microphone list | Choose the microphone to use |
| **Input** meter | The sound level coming in now |
| **Noise gate** | Keep background noise from moving the mouth |
| **Detect background noise** | Measures the noise while you stay quiet and sets the gate automatically |
| **Noise gate details** | **Auto / Manual**, open and close levels, response time |

## Tracking sources

Choose what moves each body part.

| Item | Options |
|---|---|
| **Face engine** | Auto / MediaPipe / OpenSeeFace |
| **Arms · Hands · Fingers** | MediaPipe / Ultraleap / Off |
| **Mouth** | Face + mic / Face / Mic / Off |
| **Advanced** › Face · Head · Eyes | Face / Off |

### OpenSeeFace

Another engine that tracks the face only. It is not included with Avatar Live, so download it yourself, place it **outside the installation folder**, and choose it under **OpenSeeFace folder**.

### Face app (VMC · iFacialMocap)

Receives the face from another app or an iPhone instead of the webcam.

| Item | What it does |
|---|---|
| **Source** | None / VMC / iFacialMocap |
| Switch | Start receiving |
| **Port** / **iPhone address** | Connection details |
| **Allow devices on my network** | Receive from phones and PCs on the same network |
| **This PC's addresses** · **Copy** | The address to enter in the iFacialMocap app |
| **Recenter** | Make your current head direction the front |

## Ultraleap hand tracking

Tracks arms, hands and fingers with a Leap Motion / Ultraleap device. Install the Ultraleap software, connect the device, then choose **Ultraleap** in the tracking sources.

| Item | What it does |
|---|---|
| Switch · status | Turn it on; whether the device and hands are visible |
| **Calibration (where the device is)** | Device position and direction, hand size, smoothing |
| **Calibrate** | Put your hands on the keyboard and click it to set that spot as the keyboard position |

## External tracking (OSC · VMC)

Connects with other apps on this PC. Off by default.

| Item | What it does |
|---|---|
| **OSC input (avatar parameters)** | Change avatar parameters with OSC tools made for VRChat |
| **VMC input (body and bones from another app)** | Receive the body from another motion app, and choose which **Parts** to receive |
| **Write the sender's shapes onto the avatar** | Apply the received expressions as they are |

> **Ultraleap, iFacialMocap and OSC / VMC** are expected to work, but they are **experimental features**: the devices and apps involved have not yet been tested in the developer's environment.

VMC **output** is in [Chapter 9](09-output.md#external-output-vmc).

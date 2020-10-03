## Introduction
This repository contains the [Unity](https://unity.com/) project and scenes, and the Python3 scripts for experiments described in the article:

**“Neural interface instrumented virtual reality headsets: Toward next-generation immersive applications,” IEEE Systems, Man, and Cybernetics Magazine, vol. 6, no. 3, pp. 20–28, 2020.** [Link](https://ieeexplore.ieee.org/document/9142156)

The article describes the development of system that combines an open-source, wireless, and multimodal (BMI) with an off-the-shelf head-mounted display (HMD) for VR/AR application. The proposed system is capable of measuring electroencephalography (EEG), electrooculography (EOG), electrocardiography (ECG) and facial electromyography (EMG) signals in a portable, wireless and non-invasive way.

## BMI-HMD system
The BMI-HMD system (Figure 3) is comprised of three main parts:
1. The biopotential amplifier module, based on the [OpenBCI Cyton board](https://shop.openbci.com/products/cyton-biosensing-board-8-channel) (Figure 1a and 1b)
2. The HMD used was the [Oculus Development Kit 2](https://en.wikipedia.org/wiki/Oculus_Rift#Development_Kit_2) (Figure 2)
3. Dry electrodes (Figure 1c and 1d)

| [<img src="https://user-images.githubusercontent.com/8238803/94977768-461a8900-04e8-11eb-8068-e918b30ef536.png" width="450"/>](https://user-images.githubusercontent.com/8238803/94977768-461a8900-04e8-11eb-8068-e918b30ef536.png)| <img src="https://user-images.githubusercontent.com/8238803/94977776-47e44c80-04e8-11eb-9166-4d54d69f07ca.png" width="450"/> |

[<img src="https://user-images.githubusercontent.com/8238803/94977779-49ae1000-04e8-11eb-87c5-d014b4a4e7e9.png" width="800"/>](https://user-images.githubusercontent.com/8238803/94977779-49ae1000-04e8-11eb-87c5-d014b4a4e7e9.png)

## Validation scenarios
Three validation scenarios were developed to acquire EEG, EOG and facial EMG signals.
Moreover, in each of these three scenarios ECG is recorded.

### 1. EEG scenario
It is comprised of three 30-second stages where the user performs:
  1. resting with open eyes
  2. staring at a blinking sphere (12.5 Hz) to evoke [SSVEP](https://en.wikipedia.org/wiki/Steady_state_visually_evoked_potential)
  3. resting with closed eyes
  <p align="center">
  <img src="https://user-images.githubusercontent.com/8238803/71700591-e3e2fb00-2d92-11ea-8717-08c116199da0.gif" width="300" /> 
  </p>

### 3. EOG scenario
The user is asked to follow a target for approximately 5 minutes. The target moved from the center of the field-of-view to one of eight positions: right, right-up, up, left-up, left, left-down, down, and right-down.
  <p align="center">
  <img src="https://user-images.githubusercontent.com/8238803/71700593-e80f1880-2d92-11ea-8aa1-8f699cf1646c.gif" width="300" /> 
  </p>
  
### 4. Facial EMG scenario
Facial EMG signals can be used to detect different facial expressions. During 5 minutes, the user is presented with one of four cues that indicate what facial expression to perform.
  <p align="center">
  <img src="https://user-images.githubusercontent.com/8238803/71700595-e9404580-2d92-11ea-9a9b-3723da0aa58e.gif" width="300" /> 
  </p>
  
## Requirements
Besides Unity and Python3, the experiments require [MuLES](https://github.com/MuSAELab/MuLES/releases) for the acquisition and synchronization of physiological signals.

## Execution
1. Execute MuLES, select the device to stream and port 30000.
2. Click on Play on the Unity scene under evaluation
3. Run the Python3 that corresponds to the evaluation scenario.

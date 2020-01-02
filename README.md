## Introduction
This repository contains the [Unity](https://unity.com/) project and scenes, and the Python3 scripts for experiments described in the article "Combining a Body/Brain-Machine Interface with an Off-the-Shelf Virtual Reality Headset for Next-Generation Immersive Applications" in the IEEE Systems, Man, and Cybernetics Magazine, Year: X | Volume: Y, Issue Z.

The article describes the development of system that combines an open-source, wireless, and multimodal (BMI) with an off-the-shelf head-mounted display (HMD) for VR/AR application. The proposed system is capable of measuring electroencephalography (EEG), electrooculography (EOG), electrocardiography (ECG) and facial electromyography (EMG) signals in a portable, wireless and non-invasive way.

## BMI-HMD system
The BMI-HMD system is comprised of three main parts:
1. The biopotential amplifier module, based on the [OpenBCI Cyton board](https://shop.openbci.com/products/cyton-biosensing-board-8-channel)
2. The HMD used was the [Oculus Development Kit 2](https://en.wikipedia.org/wiki/Oculus_Rift#Development_Kit_2)
3. Dry electrodes

## Validation scenarios
Three validation scenarios were developed to acquire EEG, EOG and facial EMG signals.
Moreover, in each of these three scenarios ECG is recorded.

### 1. EEG scenario
It is comprised of three 30-second stages where the user performs:
  1. resting with open eyes
  2. staring at a blinking sphere (12.5 Hz) to evoke [SSVEP](https://en.wikipedia.org/wiki/Steady_state_visually_evoked_potential)
  3. resting with closed eyes

### 3. EOG scenarios
The user is asked to follow a target for approximately 5 minutes. The target moved from the center of the field-of-view to one of eight positions: right, right-up, up, left-up, left, left-down, down, and right-down.

### 4. Facial EMG scenarios
Facial EMG signals can be used to detect different facial expressions. During 5 minutes, the user is presented with one of four cues that indicate what facial expression to perform.

## Requirements
Besides Unity and Python3, the experiments require [MuLES](https://github.com/MuSAELab/MuLES/releases) for the acquisition and synchronization of physiological signals.

## Execution
1. Execute MuLES, select the device to stream and port 30000.
2. Click on Play on the Unity scene under evaluation
3. Run the Python3 that corresponds to the evaluation scenario.

# -*- coding: utf-8 -*-
"""
Automates the emotion experiment
"""

from mules import MulesClient
from experiment import *
import subprocess
from playsound import playsound
import numpy as np

if __name__ == "__main__":
    
    ###################    
    ## Instructions 
    ###################
    # 1. Run MuLES with the Saving and Streaming setings
    # 2. Run the emg_scene in the Unity3D proyect
    # 3. Run this Python script

    
    ###################    
    ## Parameters
    ###################
    time_stimulus = 2
    time_trial = 2
    n_trials = 2
    
    neutral = 10
    angry = 12
    astonichment = 14
    happy = 16
    
    np.random.seed(42)
    stimuli = np.array([neutral,angry,astonichment,happy])

    ###################    
    ## TCP/IP clients
    ###################
    # TCP Client for MuLES
    mules_eeg = MulesClient('localhost', 30000)
    pause(10)

    # TCP Client for Unity
    unity = TcpClient('localhost', 40000) 
    unity.connect()
    pause(3)

    ###################    
    ## Experiment
    ###################
    
    for i_trial in range(n_trials):     
        # Tone start
        tone(500, 500)
        pause(1)
        
        for stimulus in stimuli:     
            # Send trigger to MuLES
            mules_eeg.sendtrigger(stimulus)
#            mules_ecg.sendtrigger(trigger)        
            # Send command to Unity
            unity.writeInt32(stimulus)
            # Time on Stimulus
            pause(time_stimulus)
            # Send command to Unity
            unity.writeInt32(770)
            # Send trigger to MuLES
#            mules_ecg.sendtrigger(trigger)        
            pause(time_stimulus)
            pause(time_stimulus)

            mules_eeg.sendtrigger(stimulus)

            pause(time_stimulus)
                
        # Shuffles the stimuli
        stimuli = np.random.permutation(stimuli)
        # Pause between trials
        pause(time_trial)
    
    ###################    
    ## End Experiment
    ################### 
    mules_eeg.kill()
#    mules_ecg.kill()
    unity.writeInt32(660)
    unity.close()
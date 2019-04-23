# -*- coding: utf-8 -*-
"""
Automates the Eye-Gaze experiment
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
    # 2. Run the eog_scene in the Unity3D proyect
    # 3. Run this Python script


    ###################    
    ## Parameters
    ###################
    time_stimulus = 2
    time_trial = 2
    n_trials = 2

    nn =  90
    nw = 135
    ww = 180
    sw = 225
    ss = 270
    se = 315
    ee =   0
    ne =  45
    cc = 777
    
    np.random.seed(42)
    stimuli = np.array([ee,ne,nn,nw,ww,sw,ss,se])


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
            # Trigger
            trigger = int(np.round((stimulus / 45) + 10 ) )            
            # Send trigger to MuLES
            mules_eeg.sendtrigger(trigger)
#            mules_ecg.sendtrigger(trigger)        
            # Send command to Unity
            unity.writeInt32(stimulus)
            # Time on Stimulus
            pause(time_stimulus)
            # Send command to Unity
            unity.writeInt32(cc)
            # Send trigger to MuLES
            mules_eeg.sendtrigger(trigger)
#            mules_ecg.sendtrigger(trigger)        
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
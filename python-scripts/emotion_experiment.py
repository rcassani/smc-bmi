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
    ## Parameters
    ###################
    time_stimulus = 2
    time_trial = 0
    n_trials = 10
    
    neutral = 10
    angry = 12
    astonichment = 14
    happy = 16
    
    np.random.seed(42)
    stimuli = np.array([neutral,angry,astonichment,happy])

    mules_path = r'C:\Program Files (x86)\MuSAE_Lab\MuLES\mules.exe'
#    eog_path = r'D:\Users\cassani\Documents\GitHub\oculus-eeg\eog_server.exe'
    
    eog_path = r'C:\Users\student\Documents\GitHub\oculus-eeg\unity-app\emotion_server.exe'

    # Number of DEVICE in MuLES config.ini file
    mules_eeg_device = 'DEVICE07'
#    mules_ecg_device = "DEVICE07"

    ###################    
    ## Execute other software
    ###################
    # Execute MuLES
    subprocess.Popen(mules_path + ' -- "' + mules_eeg_device + '"' + ' PORT=30000 LOG=T TCP=T')
#    pause(5)
    # Execute MuLES
#    subprocess.Popen(mules_path + ' -- "' + mules_ecg_device + '"' + ' PORT=31000 LOG=T TCP=T') 
    # Pause for the Experimenter to confirm the quality of the Epoc electrodes
    pause(15)

    # Execute Unity App
    #subprocess.Popen(eog_path)

    ###################    
    ## TCP/IP clients
    ###################
    # TCP Client for MuLES
    mules_eeg = MulesClient('localhost', 30000)
    pause(2)
#    mules_ecg = MulesClient('localhost', 31000)
    #pause(10)
    # TCP Client for Unity
    unity = TcpClient('localhost', 40000) 
    unity.connect()

    # Wait for Unity App
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
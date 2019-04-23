# -*- coding: utf-8 -*-
"""
EEG SSVEP experiment
"""

from mules import MulesClient
from experiment import *
import subprocess
from playsound import playsound

if __name__ == "__main__":

    ###################    
    ## Instructions 
    ###################
    # 1. Run MuLES with the Saving and Streaming setings
    # 2. Run the eeg_scene in the Unity3D proyect
    # 3. Run this Python script

    ###################    
    ## Parameters
    ###################
    time_open   = 30
    time_blink  = 30
    time_closed = 30
    
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
    ## Phase 1, Open Eyes
    ################### 
    command = 10
    # Send audio command
    playsound('./support/open.mp3')
    tone(500,500)

    # Send command to Unity
    unity.writeInt32(command)
    pause(5)

    # Send trigger to MuLES
    mules_eeg.sendtrigger(command)
#    mules_ecg.sendtrigger(command)
    
    # Wait X seconds
    pause(time_open)

    # Send trigger to MuLES
    mules_eeg.sendtrigger(command)
#    mules_ecg.sendtrigger(command)
    
    ###################    
    ## Phase 2, Blinking SSVEP
    ################### 
    command = 20
    # Send audio command
    playsound('./support/blink.mp3')
    tone(500,500)

    # Send command to Unity
    unity.writeInt32(command)
    pause(5)

    # Send trigger to MuLES
    mules_eeg.sendtrigger(command)
#    mules_ecg.sendtrigger(command)
    
    # Wait X seconds
    pause(time_blink)

    # Send trigger to MuLES
    mules_eeg.sendtrigger(command)
#    mules_ecg.sendtrigger(command)
    
    ###################    
    ## Phase 3, Close Eyes
    ################### 
    command = 30
    # Send audio command
    playsound('./support/closed.mp3')
    tone(500,500)

    # Send command to Unity
    unity.writeInt32(command)
    pause(5)

    # Send trigger to MuLES
    mules_eeg.sendtrigger(command)
#    mules_ecg.sendtrigger(command)
    
    # Wait X seconds
    pause(time_closed)

    # Send trigger to MuLES
    mules_eeg.sendtrigger(command)
#    mules_ecg.sendtrigger(command)
    
    ###################    
    ## End Experiment
    ###################
    mules_eeg.kill()
#    mules_ecg.kill()
    unity.writeInt32(66)
    unity.close()
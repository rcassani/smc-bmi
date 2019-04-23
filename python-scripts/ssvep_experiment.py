# -*- coding: utf-8 -*-
"""
Automates the SSVEP experiment
"""

from mules import MulesClient
from experiment import *
import subprocess
from playsound import playsound

if __name__ == "__main__":
    ###################    
    ## Parameters
    ###################
    time_open   = 30
    time_blink  = 30
    time_closed = 30
    
    mules_path = 'C:\Program Files (x86)\MuSAE_Lab\MuLES\mules.exe'
#    ssvep_path = r'C:\Users\student\Documents\GitHub\oculus-eeg\unity-app\Builds\ssvep\ssvep_server.exe'

    # Number of DEVICE in MuLES config.ini file
    mules_eeg_device = 'DEVICE06'
#    mules_ecg_device = "DEVICE08"

    ###################    
    ## Execute other software
    ###################
    # Execute MuLES
    subprocess.Popen(mules_path + ' -- "' + mules_eeg_device + '"' + ' PORT=30000 LOG=T TCP=T')
    pause(5)
    # Execute MuLES
#    subprocess.Popen(mules_path + ' -- "' + mules_ecg_device + '"' + ' PORT=31000 LOG=T TCP=T') 
    # Pause for the Experimenter to confirm the quality of the Epoc electrodes
    pause(20)
    
    # Execute Unity App
#    subprocess.Popen(ssvep_path)

    ###################    
    ## TCP/IP clients
    ###################
    # TCP Client for MuLES
    mules_eeg = MulesClient('localhost', 30000)
#    pause(2)
#    mules_ecg = MulesClient('localhost', 31000)
    
    pause(10)
    
    # TCP Client for Unity
    unity = TcpClient('localhost', 40000) 
    unity.connect()

    # Wait for Unity App
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
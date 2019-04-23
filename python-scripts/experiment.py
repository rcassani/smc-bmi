# -*- coding: utf-8 -*-
"""
Functions for experiments
"""

import winsound
import time    
import socket
import array
import struct


def tone(f=500, d=500):
    """
    Uses the Sound-playing interface for Windows to play a beep
        
    Arguments
    f: Frequency of the beep in Hz
    d: Duration of the beep in ms
    """
    winsound.Beep(f,d)
    
def pause(seconds):
    """
    Pauses the execution for s seconds
    
    Arguments
    s: Number of seconds to wait
    """
    time.sleep(seconds)

class TcpClient():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    def connect(self):
        """
        Connects to a TCP/IP server 
        """
        print('Attempting connection')
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.ip, self.port))
            print('Connection successful')
        except:
            self.client = None
            print('Connection attempt unsuccessful')
            raise
            
    def writeInt32(self, integer32):
        """
        Writes one Int32
        """
        bytes_4B = struct.pack('i', integer32)
        bytes_4B = bytes_4B[::-1]
        self.client.send(bytes_4B)
        return
		
    def writeArray(self, array):
        bytes = struct.pack('=%sf' % array.shape[0], *array)
        bytes = bytes[::-1] # reverse order
        self.client.send(bytes)
        return
    
    def readInt32(self):
        """
        Reads one Int32
        """
        n_bytes_4B = array.array('B',self.client.recv(4) )
        integer32 = struct.unpack('i',n_bytes_4B[::-1])[0] 
        return integer32
    
    def close(self):
        """
        Closes the communication with the Server
        """
        self.client.close()
        self.client = None
        return

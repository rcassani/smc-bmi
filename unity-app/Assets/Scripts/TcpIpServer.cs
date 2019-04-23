using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;
using System.Net.Sockets;
using System.Net;

public class TcpIpServer {
    TcpListener server;
    TcpClient client;
    NetworkStream stream; 

    // Constructor
    public TcpIpServer(string server_ip, int server_port)
    {   
        // Create TCP Server
        IPAddress localAddr = IPAddress.Parse(server_ip);
        this.server = new TcpListener(localAddr, server_port);
        // Start listening for client
        server.Start();
        // Accept client request, block until Client connects
        this.client = server.AcceptTcpClient();
        this.stream = this.client.GetStream();
    }


    // Get 1 Byte data
    public int ReadCommand() {
        // Read 4 bytes from Steam
        byte[] read_data = new byte[4];
        stream.Read(read_data, 0, 4);
        // Cast 4bytes as Int32
        Array.Reverse(read_data);
        int command = BitConverter.ToInt32(read_data, 0);
        return command;
    }

    public bool IsDataAvailable()
    {   
        // Check if there is avialable data in steam
        return this.stream.DataAvailable;
    }

    public void WriteInt32(int to_send)
    {
        byte[] to_send_array = BitConverter.GetBytes(to_send);
        Array.Reverse(to_send_array);
        stream.Write(to_send_array, 0, 4);
        return;
    }

}

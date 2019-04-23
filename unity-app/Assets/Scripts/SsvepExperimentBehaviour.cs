using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SsvepExperimentBehaviour : MonoBehaviour {
    public int ServerPort = 40000;
    public GameObject blinkingTarget;
    public GameObject fixationTarget;
    private TcpIpServer tcp_server; 

    // Use this for initialization
	void Start () {
        // Create TCP Server and Block until Client is connected
        tcp_server = new TcpIpServer("0.0.0.0", ServerPort);
	}
	
	// Update is called once per frame
	void Update () {
        if(this.tcp_server.IsDataAvailable())
        {
            int command = this.tcp_server.ReadCommand();
            Debug.Log("Command: " + command.ToString());
            switch (command)
            {
                case 10:
                    print("Open eyes section");
                    blinkingTarget.SetActive(false);
                    fixationTarget.SetActive(true);
                    break;

                case 30:
                    print("Closed eyes section");
                    blinkingTarget.SetActive(false);
                    fixationTarget.SetActive(false);
                    break;

                case 20:
                    print("SSVEP section");
                    blinkingTarget.SetActive(true);
                    fixationTarget.SetActive(false);
                    break;

                case 66:
                    Application.Quit();
                    break;
                
            }
        }
    }
}

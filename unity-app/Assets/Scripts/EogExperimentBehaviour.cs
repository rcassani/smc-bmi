using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EogExperimentBehaviour : MonoBehaviour {
    public int ServerPort = 40000;
    public int Radious = 10;
    public GameObject gazeTarget;
    private TcpIpServer tcp_server;
    private RectTransform guiRectTransform;

    // Use this for initialization
    void Start () {
        // Create TCP Server and Block until Client is connected
        tcp_server = new TcpIpServer("0.0.0.0", ServerPort);
         this.guiRectTransform = gazeTarget.GetComponent<RectTransform>();
	}
	
	// Update is called once per frame
	void Update () {
        if(this.tcp_server.IsDataAvailable())
        {
            float x_gui = 0f;
            float y_gui = 0f;

            int angle = this.tcp_server.ReadCommand();
            Debug.Log("Angle: " + angle.ToString() + "degrees");

            switch(angle)
            {
                case 777:
                    x_gui = 0f;
                    y_gui = 0f;
                    break;
                case 660:
                    Application.Quit();
                    break;
                default:
                    float angle_radians = angle * Mathf.PI / 180.0f;
                    x_gui = Radious * Mathf.Cos(angle_radians);
                    y_gui = Radious * Mathf.Sin(angle_radians);
                    break;
            }

            guiRectTransform.localPosition = new Vector3(x_gui, y_gui, 0);
                        
        }
    }
}

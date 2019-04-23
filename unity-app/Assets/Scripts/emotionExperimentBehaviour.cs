using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class emotionExperimentBehaviour : MonoBehaviour {
    private TcpIpServer tcp_server;
    public int ServerPort = 40000;
    public GameObject Neutral;
    public GameObject Happy;
    public GameObject Astonichment;
    public GameObject Angry;

    /*private RectTransform guiRectTransformNeutral;
    private RectTransform guiRectTransformAngry;
    private RectTransform guiRectTransformAstonichment;
    private RectTransform guiRectTransformHappy;*/

    // Use this for initialization
    void Start () {
        tcp_server = new TcpIpServer("0.0.0.0", ServerPort);
        /*this.guiRectTransformNeutral = Neutral.GetComponent<RectTransform>();
        this.guiRectTransformAngry = Angry.GetComponent<RectTransform>();
        this.guiRectTransformAstonichment = Astonichment.GetComponent<RectT*/
	}
	
	// Update is called once per frame
	void Update () {
        if(this.tcp_server.IsDataAvailable())
        {
            int command = this.tcp_server.ReadCommand();
            Debug.Log("Face: " + command.ToString());
            
            switch(command)
            {
                case 10:
                    print("Neutral Image");
                    Neutral.SetActive(true);
                    Angry.SetActive(false);
                    Astonichment.SetActive(false);
                    Happy.SetActive(false);
                    //guiRectTransformNeutral.localPosition = new Vector3(0f, 0f, 0);
                    break;

                case 12:
                    print("Angry Image");
                    Neutral.SetActive(false);
                    Angry.SetActive(true);
                    Astonichment.SetActive(false);
                    Happy.SetActive(false);
                    //guiRectTransformAngry.localPosition = new Vector3(0f, 0f, 0);
                    break;

                case 14:
                    print("Astonichment Image");
                    Neutral.SetActive(false);
                    Angry.SetActive(false);
                    Astonichment.SetActive(true);
                    Happy.SetActive(false);
                    //guiRectTransformAstonichment.localPosition = new Vector3(0f, 0f, 0);
                    break;

                case 16:
                    print("Happy Image");
                    Neutral.SetActive(false);
                    Angry.SetActive(false);
                    Astonichment.SetActive(false);
                    Happy.SetActive(true);
                //guiRectTransformHappy.localPosition = new Vector3(0f, 0f, 0);
                break;
                
                case 660:
                Application.Quit();
                break;

                case 770:
                print("No Image");
                Neutral.SetActive(false);
                Angry.SetActive(false);
                Astonichment.SetActive(false);
                Happy.SetActive(false);
                break;
            }
        }
    }
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour {
    public int speed = 0;
	// Use this for initialization
	void Start () {
        //camera.transform.eulerAngles = new Vector3(0, 0, 0);

    }

    // Update is called once per frame
    void Update () {
        // get Camera sibiling object
        Transform camera = transform.GetChild(0);
        Transform body = transform.GetChild(1);

        Vector3 eulerBody = body.eulerAngles;
        
        // rotate body Y acording to camera
        body.eulerAngles = new Vector3(0, camera.eulerAngles.y, 0);

        // get input data from keyboard or controller
        float moveVertical = Input.GetAxis("Vertical");

        // use Vertical input to move forward Player
        transform.position = body.position + body.forward * speed * Time.deltaTime * moveVertical;
        body.position = transform.position;

    }
}

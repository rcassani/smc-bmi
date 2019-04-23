using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Blinking : MonoBehaviour {
    [Tooltip("VR headset frequency rate (Hz)")]
    public float frameRate = 75.0f;
    [Tooltip("Frequency desired for stimulus (Hz)")]
    public float stimulusDesireFrequency = 1.0f;
    [Tooltip("Frequency real for stimulus (Hz)")]
    public float stimulusAproxFrequency = 0.0f;
    [Tooltip("Frequency real for stimulus (Hz)")]
    public float stimulusRealFrequency = 0.0f;


    private bool[] vFrames;
    private int ixFrame = 0;
    private Renderer rend;
    private float timeKeeper = 0f;
 
    // Use this for initialization
    void Start () {
        timeKeeper = Time.realtimeSinceStartup;
        // Get Mesh Rendered
        rend = GetComponent<Renderer>();
        // Calculate the number of ON and OFF frames
        float stimulusPeriod = 1 / stimulusDesireFrequency;
        int nFrames = Mathf.RoundToInt(stimulusPeriod / Time.fixedDeltaTime);
        int nWhiteFrames = Mathf.CeilToInt((float)nFrames / 2f);
        int nBlackFrames = nFrames - nWhiteFrames;
        // Array with black frames (false)    
        bool[] bFrames = new bool[nBlackFrames];
        // Array with white frames (true)
        bool[] wFrames = new bool[nWhiteFrames];
        for(int i = 0; i<wFrames.Length; i++) {wFrames[i] = true;}
        // Concatenate arrays
        vFrames = new bool[wFrames.Length + bFrames.Length];
        wFrames.CopyTo(vFrames, 0);
        bFrames.CopyTo(vFrames, wFrames.Length);
        // Calculate real stimulus frequency
        stimulusAproxFrequency = 1 / (vFrames.Length * Time.fixedDeltaTime);
	}
	
    //void FixedUpdate()
    void Update()
    {
        rend.enabled = vFrames[ixFrame];
        ixFrame = ixFrame + 1;
        if(ixFrame >= vFrames.Length)
            {           
            ixFrame = 0;
            stimulusRealFrequency = 1 / (Time.realtimeSinceStartup - timeKeeper);
            timeKeeper = Time.realtimeSinceStartup;
            }
    }


}

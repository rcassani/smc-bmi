using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FrameRateCalculator : MonoBehaviour {
    public float calculationPeriod = 1f;
    public float frameRate = 0f;
    private float timeKeeper = 0f;
    private float frameDelta = 0f;

    // Use this for initialization
    void Start () {
        timeKeeper = Time.realtimeSinceStartup;
        InvokeRepeating("FpsCalculator", time: 0.0f, repeatRate: calculationPeriod);
    }

    void FpsCalculator()
    {
        frameDelta = Time.frameCount - frameDelta;
        frameRate = frameDelta / (Time.realtimeSinceStartup - timeKeeper);
        //print(frameRate.ToString("F4"));
        timeKeeper = Time.realtimeSinceStartup;
        frameDelta = Time.frameCount;

    }

}

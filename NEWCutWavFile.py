

import wave
import numpy as np
import os

CutTimeDef = 58000
CutFrameNum =0


FileName = ".\Music\\"+ ".wav"


def SetFileName(WavFileName):
    global  FileName
    print("SetFileName File Name is ", FileName)
    FileName = WavFileName;
def CutFile():
    global  FileName
    print("CutFile File Name is ",FileName)
    f = wave.open(r"" + FileName, "rb")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    CutFrameNum = framerate * CutTimeDef / 1000
    print("CutFrameNum=%d" % (CutFrameNum))

    print("nchannels=%d" % (nchannels))
    print("sampwidth=%d" % (sampwidth))
    print("framerate=%d" % (framerate))
    print("nframes=%d" % (nframes))
    str_data = f.readframes(nframes)
    f.close()
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data.shape = -1, 2
    wave_data = wave_data.T
    temp_data = wave_data.T
    # StepNum = int(nframes/200)
    StepNum = int(CutFrameNum);
    StepTotalNum = 0;
    haha = 0

    tempPath = os.path.dirname(__file__)
    tempPath = tempPath + '/MusicResult'
    os.mkdir(tempPath)

    while StepTotalNum < nframes:
        print("Stemp=%d" % (haha))
        if(haha<10):
            FileName = ".\MusicResult\\00" + str(haha) + ".wav"
        elif(haha<100):
            FileName = ".\MusicResult\\0" + str(haha) + ".wav"
        else:
            FileName = ".\MusicResult\\0" + str(haha) + ".wav"
        print(FileName)
        temp_dataTemp = temp_data[StepNum * (haha):StepNum * (haha + 1)]
        haha = haha + 1;
        StepTotalNum = haha * StepNum;
        temp_dataTemp.shape = 1, -1
        temp_dataTemp = temp_dataTemp.astype(np.short)
        f = wave.open(r"" + FileName, "wb")
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        f.writeframes(temp_dataTemp.tostring())
        f.close()

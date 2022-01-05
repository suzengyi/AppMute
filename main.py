from pycaw.pycaw import AudioUtilities
import sys

def mute():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process is None :
            continue
        name=session.Process.name()
        for arg in sys.argv:
            if arg.lower() in name.lower():
                volume = session.SimpleAudioVolume
                volume.SetMute(volume.GetMute()^1,None)

if __name__=='__main__':
    mute()
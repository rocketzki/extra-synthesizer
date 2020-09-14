from defaults import ROOT_DIR
import soundfile as sf


def samples_to_wav(data):
    path = ROOT_DIR + "/static/temp/out.wav"
    sf.write(path, data, 22050, subtype='PCM_16')
    return path

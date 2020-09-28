import base64
import os
import tempfile
from wsgiref.util import FileWrapper

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from defaults import ROOT_DIR
from extra_synthesizer.synthesize.interpret import interpret
import soundfile as sf

TEMP_FILE_NAME = ROOT_DIR + "\\resources\\temp\\speech.wav"

TARGET_FOLDER = ROOT_DIR + "\\resources\\target\\"
SHOULD_SAVE_LOCALLY = True


@csrf_exempt
def index(request):
    return render(request, 'templates/index.html')


@csrf_exempt
def synthesize(request):
    req_data = request.POST

    text = req_data.get("text")
    enhanced = req_data.get("enhanced")
    ssml = req_data.get("ssml")

    audio_samples = interpret(text, ssml=string_to_bool(ssml), enhanced=string_to_bool(enhanced))
    sf.write(TEMP_FILE_NAME, audio_samples, 22050, subtype='PCM_16', format='WAV')

    if SHOULD_SAVE_LOCALLY:
        sf.write(TARGET_FOLDER + str(text).replace("?", "_pytanie_popr").replace("!", "wykrz_popr") + ".wav",
                 audio_samples, 22050, subtype='PCM_16', format='WAV')

    att = open(TEMP_FILE_NAME, 'rb').read()
    enc = base64.b64encode(att)

    response = FileResponse(str(enc, 'ascii', 'ignore'), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="speech.json"'
    response['Access-Control-Allow-Origin'] = '*'

    os.unlink(TEMP_FILE_NAME)

    return response


def string_to_bool(val):
    if val == 'true':
        return True
    elif 'false':
        return False
    else:
        raise AttributeError("Val has to be either 'false' or 'true'")


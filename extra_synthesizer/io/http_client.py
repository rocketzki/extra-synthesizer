import requests
import base64 as b

from defaults import ROOT_DIR
from extra_synthesizer.settings import KEY

G_API_SYNTH_ADDRESS = "https://texttospeech.googleapis.com/v1/text:synthesize"


# save flag for debug purposes
def shoot_synth_api(payload, save=False):
    if KEY == "":
        raise AttributeError("You need to set google api syntesizer key in order to run the service.")
    print("[LOG INFO] Calling Google Text-To-Speech Api with payload: " + str(payload))
    r = requests.post(G_API_SYNTH_ADDRESS, json=payload,
                      headers={"Content-Type": "application/json; charset=utf-8", "X-Goog-Api-Key": KEY})
    res_data = b.urlsafe_b64decode(r.json()["audioContent"])
    if save:
        with open(ROOT_DIR + "\\resources\\samples\\out.wav", "wb") as file:
            file.write(res_data)

    return res_data

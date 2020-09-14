import requests
import base64 as b

key = ""
address = "https://texttospeech.googleapis.com/v1/text:synthesize"


def shoot_synth_api(payload, save=False):
    print("[LOG INFO] Calling Google Text-To-Speech Api with payload: " + str(payload))
    r = requests.post(address, json=payload,
                      headers={"Content-Type": "application/json; charset=utf-8", "X-Goog-Api-Key": key})
    res_data = b.urlsafe_b64decode(r.json()["audioContent"])
    if save:
        with open("D:\workspace\code\python\extra_synthesizer\\resources\\samples\out.wav", "wb") as file:
            file.write(res_data)

    return res_data

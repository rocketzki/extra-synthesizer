from extra_synthesizer.io.http_client import shoot_synth_api


def synthesize(ssml_body, ssml_gender='FEMALE'):
    return shoot_synth_api({'input': {'ssml': build_ssml(ssml_body)},
            'voice': {'languageCode': 'pl-pl', 'name': 'pl-PL-Wavenet-A', 'ssmlGender': ssml_gender},
            'audioConfig': {'audioEncoding': 'LINEAR16', 'sampleRateHertz': '44100'}})


def build_ssml(text):
    return "<speak>{}</speak>".format(text)


def ssml_word_verbatim(text):
    return "<say-as interpret-as='verbatim'>{}</say-as>".format(text)


def ssml_paragraph(text):
    return "<p>{}</p>".format(text)


def ssml_sentences(text):
    sentence_tag = "<s>{}</s>"

    if not isinstance(text, list):
        return ssml_paragraph(sentence_tag.format(text))
    else:
        return ssml_paragraph("".join([sentence_tag.format(sentence) for sentence in text]))

import os
import numpy as np
import librosa
import tempfile

from defaults import ROOT_DIR
from extra_synthesizer.audio.transformer import transform
from extra_synthesizer.dict.dict_check import to_sentences, dict_lookup
from extra_synthesizer.synthesize.ssml import *


def interpret(text, ssml=False, enhanced=False):
    sentences = to_sentences(text)
    synthesized_text = []

    for sentence in sentences:

        if ssml:
            to_process = __process_sentence(sentence, enhanced)
        else:
            to_process = __process_sentence_ssml(sentence, enhanced)

        synthesized_sentence = wav_byte_arr_to_amplitudes(synthesize(to_process))

        if str(sentence).endswith("?") and enhanced:
            synthesized_sentence = transform(synthesized_sentence, mode="question")
        elif str(sentence).endswith("!") and enhanced:
            synthesized_sentence = transform(synthesized_sentence, mode='exclamation')

        synthesized_text.append(synthesized_sentence)

    return concat_samples(synthesized_text)


def __process_sentence(sentence, enhanced):
    if enhanced:
        for checked_word in dict_lookup(sentence):
            word = checked_word["word"]

            if not bool(checked_word["result"]):
                sentence = str(sentence).replace(word, ssml_word_verbatim(word))

    return sentence


def __process_sentence_ssml(sentence, enhanced):
    return ssml_sentences(__process_sentence(sentence, enhanced))


def concat_samples(samples):
    return np.concatenate([sample for sample in samples])


def wav_byte_arr_to_amplitudes(wav_byte_arr):
    temp_wave_file = tempfile.NamedTemporaryFile(suffix=".wav", dir=ROOT_DIR + "/resources/temp", delete=False)
    temp_wave_file.write(wav_byte_arr)
    temp_wave_file.seek(0)
    data, sr = librosa.load(temp_wave_file.name)
    temp_wave_file.close()
    os.unlink(temp_wave_file.name)

    return data

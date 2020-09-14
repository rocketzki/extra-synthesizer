import librosa.display
import numpy as np
import os

from defaults import ROOT_DIR
from extra_synthesizer.audio.common import _get_bin_nr, sr, n_fft, hop_length

__question_pattern = np.poly1d([24.95975232, -2.89615583, 0.23232714])
__exclamation_pattern = np.poly1d([35.56182947, 2.58020149, -0.15004904])


def calculate_pattern_poly_coeff(file_name):
    y_source, sr_source = librosa.load(os.path.join(ROOT_DIR, file_name), sr=sr)
    f0_source, voiced_flag, voiced_probs = librosa.pyin(y_source, fmin=librosa.note_to_hz('C2'),
                                                        fmax=librosa.note_to_hz('C7'), pad_mode='constant',
                                                        center=True, frame_length=4096, hop_length=512, sr=sr_source)
    all_freq_bins = librosa.core.fft_frequencies(sr=sr, n_fft=n_fft)
    f0_freq_bins = list(filter(lambda x: np.isfinite(x), map(lambda val: _get_bin_nr(val, all_freq_bins), f0_source)))

    return np.polynomial.polynomial.polyfit(np.arange(0, len(f0_freq_bins), 1), f0_freq_bins, 3)


def calculate_pattern_poly_func(coefficients):
    return np.poly1d(coefficients)


def question_pattern():
    return __question_pattern


def exclamation_pattern():
    return __exclamation_pattern

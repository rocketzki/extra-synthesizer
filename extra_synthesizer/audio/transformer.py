import librosa.display
import numpy as np
from extra_synthesizer.audio.common import hop_length, n_fft, _show_spectrogram_with_f0_plot, sr
from extra_synthesizer.audio.pattern import _question_pattern, _exclamation_pattern


def transform(sentence_audio_sample, mode=None, show_spectrograms=False, frames_from_end_to_transform=12):
    # cutting out silence
    y_trimmed, idx = librosa.effects.trim(sentence_audio_sample, top_db=60, frame_length=256, hop_length=64)

    stft_original = librosa.stft(y_trimmed, hop_length=hop_length, pad_mode='constant', center=True)

    stft_original_roll = stft_original.copy()
    rolled = stft_original_roll.copy()

    source_frames_count = np.shape(stft_original_roll)[1]
    sentence_ending_first_frame = source_frames_count - frames_from_end_to_transform
    sentence_len = np.shape(stft_original_roll)[1]

    for i in range(sentence_ending_first_frame + 1, sentence_len):
        if mode == 'question':
            by = int(_question_pattern(i) / 10)
        elif mode == 'exclamation':
            by = int(_exclamation_pattern(i) / 10)
        else:
            by = 0
        rolled = _roll_column(rolled, i, by)

    transformed_data = librosa.istft(rolled, hop_length=hop_length, center=True)

    if show_spectrograms:
        # spectrogram for original data
        f0_original, voiced_flag_t, voiced_probs_t = librosa.pyin(y_trimmed, fmin=librosa.note_to_hz('C2'),
                                                                  fmax=librosa.note_to_hz('C7'), sr=sr,
                                                                  hop_length=hop_length, frame_length=n_fft,
                                                                  pad_mode='constant', center=True)
        times_original = librosa.times_like(f0_original)
        _show_spectrogram_with_f0_plot(stft_original, times_original, f0_original)

        # spectrogram for transformed data
        f0_transformed, voiced_flag_tr, voiced_probs_tr = librosa.pyin(transformed_data, fmin=librosa.note_to_hz('C2'),
                                                                       fmax=librosa.note_to_hz('C7'), sr=sr,
                                                                       hop_length=hop_length, frame_length=n_fft,
                                                                       pad_mode='constant', center=True)
        times_transformed = librosa.times_like(f0_transformed)
        _show_spectrogram_with_f0_plot(rolled, times_transformed, f0_transformed)

    return transformed_data


def _roll_column(two_d_array, column, shift):
    two_d_array[:, column] = np.roll(two_d_array[:, column], shift)
    return two_d_array

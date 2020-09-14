import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os
import soundfile as sf
from extra_synthesizer.audio.common import _get_bin_nr, sr, n_fft, hop_length

PATH = "D:\\workspace\\code\\python\\audio-analysis\\src\\com\\rocketzki\\audioanalysis\\samples"


file_to_be_modified_name = "jak_sie_masz_n_nat"
file_to_be_modified_path = os.path.join(PATH, file_to_be_modified_name + ".wav")

file_target_path = os.path.join(PATH, file_to_be_modified_name + "_enhanced.wav")

y_target, sr_target = librosa.load(file_to_be_modified_path)


# target
stft_target = librosa.stft(y_target, hop_length=512, pad_mode='constant', center=True, n_fft=4096)
stft_target_abs = np.abs(stft_target)

bin_size_hz_target = float(sr_target / np.shape(stft_target)[0])
bins_target = np.arange(0, np.shape(stft_target)[0], bin_size_hz_target)

f0_target, voiced_flag_t, voiced_probs_t = librosa.pyin(y_target, fmin=librosa.note_to_hz('C2'),
                                                        fmax=librosa.note_to_hz('C7'), sr=sr_target,
                                                        hop_length=512, frame_length=4096,
                                                        pad_mode='constant', center=True)
times_target = librosa.times_like(f0_target)


def roll_column(two_d_array, column, shift):
    two_d_array[:, column] = np.roll(two_d_array[:, column], shift)
    return two_d_array



stft_target_roll = stft_target.copy()


# stft_source_roll = stft_source.copy()
rolled = []
for i in range(0, np.shape(stft_target_roll)[1]):
    if i >= len(stft_target_roll):
        by = int(pattern_src_poly(i)/10000)
        print("rolling by: " + str(by))
        rolled = roll_column(rolled, i, by)


fig, ax = plt.subplots()

img = librosa.display.specshow(librosa.amplitude_to_db(rolled, ref=np.max), x_axis='time', y_axis='log',
                               ax=ax)
fig.colorbar(img, ax=ax, format="%+2.f dB")

ax.set(title='pYIN fundamental frequency estimation')

ax.plot(times_target, f0_target, label='f0', color='cyan', linewidth=2)

ax.legend(loc='upper right')
plt.show()

transformed_data = librosa.istft(rolled, hop_length=512, center=True)

def transform(sentence_audio_sample, mode=''):
    return sentence_audio_sample

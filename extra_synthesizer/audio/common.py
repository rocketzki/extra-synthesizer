import numpy as np
import librosa.display
import matplotlib.pyplot as plt

n_fft = 4096
hop_length = 512
sr = 22050


def _get_bin_nr(val, bins):
    the_bin_no = np.nan
    for b in range(0, bins.size - 1):
        if bins[b] <= val < bins[b + 1]:
            the_bin_no = b
        elif val > bins[bins.size - 1]:
            the_bin_no = bins.size - 1
    return the_bin_no


def _show_spectrogram_with_f0_plot(stft_vals, f0_times, f0_freqs, text = ''):
    fig, ax = plt.subplots()
    img = librosa.display.specshow(librosa.amplitude_to_db(np.abs(stft_vals), ref=np.max), x_axis='time', y_axis='log',
                                   ax=ax)
    fig.colorbar(img, ax=ax, format="%+2.f dB")

    ax.set(title='Określanie częstotliwości podstawowej F0 algorytmem pYIN ' + text)
    ax.plot(f0_times, f0_freqs, label='f0', color='cyan', linewidth=2)

    ax.legend(loc='upper right')
    plt.show()

import numpy as np

n_fft = 4096
hop_length = 512
sr = 44100


def _get_bin_nr(val, bins):
    the_bin_no = np.nan
    for b in range(0, bins.size - 1):
        if bins[b] <= val < bins[b + 1]:
            the_bin_no = b
        elif val > bins[bins.size - 1]:
            the_bin_no = bins.size - 1
    return the_bin_no

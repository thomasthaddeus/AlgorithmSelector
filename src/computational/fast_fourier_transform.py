"""
_summary_

_extended_summary_

Returns:
    _type_: _description_

# Example usage
fft_instance = FastFourierTransform()
input_array = np.random.random(8)  # Example input
fft_result = fft_instance.fft(input_array)
ifft_result = fft_instance.ifft(fft_result)

print("Input Array:", input_array)
print("FFT:", fft_result)
print("IFFT:", ifft_result)
"""

import numpy as np

class FastFourierTransform:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self):
        """
        __init__ _summary_

        _extended_summary_
        """
        pass

    def fft(self, x):
        """
        Compute the Fast Fourier Transform of an array x.

        Args:
            x (list or np.ndarray): Input array or sequence.

        Returns:
            np.ndarray: The FFT of the input array.
        """
        N = len(x)
        if N <= 1:
            return x

        even = self.fft(x[0::2])
        odd = self.fft(x[1::2])

        T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
        return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

    def ifft(self, x):
        """
        Compute the Inverse Fast Fourier Transform of an array x.

        Args:
            x (list or np.ndarray): Input array or sequence.

        Returns:
            np.ndarray: The IFFT of the input array.
        """
        x_conjugate = np.conjugate(x)
        result = self.fft(x_conjugate)
        return np.conjugate(result) / len(x)

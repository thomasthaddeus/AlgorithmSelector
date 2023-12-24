import unittest
import numpy as np
from computational.fast_fourier_transform import FastFourierTransform

class TestFastFourierTransform(unittest.TestCase):
    def test_fft(self):
        fft = FastFourierTransform()
        data = np.array([0, 1, 0, -1])
        transformed = fft.fft(data)
        expected_output = np.array([0, -2j, 0, 2j])
        np.testing.assert_array_almost_equal(transformed, expected_output)

if __name__ == '__main__':
    unittest.main()

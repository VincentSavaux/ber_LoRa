#############################################################
# @copyright Copyright (c) 2020 All Right Reserved, b<>com http://www.b-com.com/
#
# BER/SER of LoRa signal
# Author: Vincent Savaux, IRT b<>com, Rennes
# email: vincent.savaux@b-com.com
# date: 2020-08-21

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, see <http://www.gnu.org/lice
#############################################################

#############################################################
# Import some external function
#############################################################
import json
import logging
import gmpy2
from gmpy2 import mpfr
from scipy.special import comb

#############################################################
# Set precision
# at least 150 bits for SF7, up to 4000 bits for SF12
#############################################################

gmpy2.get_context().precision = 300

def main():
    # Set/initialize parameters
    sf = 8  # Spreading factor
    n_fft = 2**sf  # Corresponding FFT size
    snr_start = -1*(3*sf-1)  # low-bound of SNR range
    snr_end = snr_start + 40  # upper-bound of SNR range
    p_error = []  # list containing the error probability for Rayleigh channel
    p_error_rice = []  # list containing the error probability for Rice channel
    # Set Rice/Rayleigh parameters
    sigma_h_ray = 1.  # variance of Rayleigh channel
    lambda_rice = 1.  # default value of mean of Rice distribution
    sigma_h_rice = 0.25  # variance of Rayleigh channel

    # print(lambda_rice,sigma_h_rice)

    for snr in range(snr_start, snr_end+1):
        # print(snr)
        sig2 = mpfr(10**(-snr/10.0))  # Noise variance
        # snr_lin = mpfr(1*10**(snr/10.0))
        error = mpfr(0.0)  # Initialise error
        # error_nochan = mpfr(0.0) # Initialise error
        error_rice = mpfr(0.0)  # Initialise error
        for k in range(1, n_fft):
            nchoosek = mpfr(comb(n_fft-1, k, exact=True))
            #################################################
            # Symbol Error Rate over AWGN Channel
            #################################################
            # error_nochan = error_nochan - mpfr(nchoosek * (-1)**k / (k+1)) \
            # * mpfr(gmpy2.exp(-k*n_fft/(2*(k+1)*sig2)))
            #################################################
            # Symbol Error Rate over Rice Channel
            #################################################
            error_rice = error_rice - mpfr(nchoosek * (-1)**k*sig2 / ((k+1)*sig2 + k*n_fft*sigma_h_rice)) \
                * mpfr(gmpy2.exp(-1*k*n_fft*lambda_rice/((k+1)*sig2 + k*n_fft*sigma_h_rice)))
            #################################################
            # Symbol Error Rate over Rayleigh Channel
            #################################################
            error = error - mpfr(nchoosek * (-1)**k*sig2 /
                                 ((k+1)*sig2 + k*n_fft*sigma_h_ray))
            # print(nchoosek)
        error = mpfr(error, 32)  # Limit precision for printing/saving
        p_error.append(float(error))
        error_rice = mpfr(error_rice, 32)
        p_error_rice.append(float(error_rice))
    # print(p_error)
    file = open("ber_ray_sf"+str(sf)+".txt", "w")
    file.write(json.dumps(p_error))
    file.close()
    file = open("ber_rice_sf"+str(sf)+".txt", "w")
    file.write(json.dumps(p_error_rice))
    file.close()


if __name__ == "__main__":
    main()

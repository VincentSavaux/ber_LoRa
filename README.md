# ber_LoRa
## General Description

The script ber_LoRa returns the theoretical bit error rate (BER) that can be achieved by a LoRa signal over Rayleigh and Rice channels. The BER values are given in function of the SNR in the range *snr_start* and *snr_end*, and stored in the lists: 
- *p_error*: Rayleigh channel
- *p_error_rice*: Rice channel

The theoretical results have been obtained from the following reference: 

M. J. Faber, K. M. van der Zwaag,W. G. V. dos Santos, H. R. d. O. Rocha,
M. E. V. Segatto, and J. A. L. Silva, “*A Theoretical and Experimental
Evaluation on the Performance of LoRa Technology*,” IEEE Sensors
Journal, vol. 20, no. 16, pp. 9480–9489, August 2020. 

Computing the error rate requires multiple precision integers variables, up to hundreds or thousands of bits, which is provided by the package *gmpy2*. 

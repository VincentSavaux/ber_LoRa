# ber_LoRa
## General Description

The script ber_LoRa returns the theoretical bit error rate (BER) that can be achieved by a LoRa signal over Rayleigh and Rice channels. The BER values are given in function of the SNR in the range *snr_start* and *snr_end*, and stored in the lists: 
- *p_error*: Rayleigh channel
- *p_error_rice*: Rice channel

The theoretical results have been obtained from the following reference: 

C. F. Dias, E. R. de Lima, and G. Fraidenraich, “*Bit Error Rate Closed-
Form Expressions for LoRa Systems under Nakagami and Rice Fading
Channels*,” Sensors, vol. 19, no. 20, pp. 1 – 11, October 2019.

Computing the error rate requires arbritary precision floating point, up to hundreds or thousands of bits, which can be obtained by using the package *gmpy2*. 

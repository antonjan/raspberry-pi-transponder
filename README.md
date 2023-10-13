# raspberry-pi-transponder
This respository will have my expiremental code to build a satellite transponder
## Description
Creating a GNU Radio program to read RF input from an RTL-SDR device at 435.1 MHz and transmit it using the rpitx library on a Raspberry Pi at 145.950 MHz involves several steps. You'll need to set up both the RTL-SDR and Raspberry Pi environments. Here's a Python script that outlines the steps you should take to accomplish this:

## config
This script uses GNU Radio and the rpitx library to capture RF input from the RTL-SDR device at 435.1 MHz and transmit it on the Raspberry Pi at 145.950 MHz. Make sure you have the necessary libraries and dependencies installed on your Raspberry Pi and that you have the proper permissions to run rpitx (typically requires sudo). Additionally, you may need to adjust gain settings and other parameters for your specific setup.

Please note that using RF transmitters without proper authorization may violate regulations in your region, so ensure that you're operating within legal boundaries.

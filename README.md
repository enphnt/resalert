# Resalert

## Components
### Hardware
The hardware needed for completing the setup is detailed below. Note that not all specs of the Raspberry Pi are noted. Only those components used will be detailed so that an alternative build could use these as minimum system requirements. 

#### The Board
![Photo of the Raspberry Pi Model B](resources/raspberryPiModelB.jpg "Photo of the Raspberry Pi Model B")

* Raspberry Pi Model B
 * 32 bit, 700 MHz System on a Chip
 * 512 MB of RAM
 * USB 2.0 ports (2) 
 * 100mb Ethernet port
 * SD Card slot
 * HDMI connector
 * microUSB power input 
 * General Purpose Input and Output (26 pin)

#### Peripherals
* HDMI enabled powered display
* USB power supply (5V, >700mA)
* Wireless Router
* SD Card (16GB)
* Separate laptop for remote access
* 1000-1500 MCD 5mm Red LED Emitters
* Pi Cobbler or compatible 16bit breakout board
* 400-point breadboard (printed circuit board)
* button
* Resistor (1kΩ-10kΩ) 

#### Connectors
* Ethernet cable or USB wifi adapter
* microUSB B (Male) to USB A (Female) cable
* Jumper Wires
* Ribbon cable (26 pin) for breakout board
* Powered USB Hub (recommended 4)
* HDMI Cable

### Software
#### Operating System
The operating system of choice at the time of build was Raspbian v3.10. To ease installation, it is recommended to make use of NOOBS which rapidly speeds up initial OS configuration. It is assumed that the router is configured and accessible with an Internet connection. To initially configure the OS, it is necessary to:

1. Erase and reformat the SD card. There is freely available open source software for accomplishing this task on your existing personal computer. 
2. Copy the operating system image or NOOBS package to the root directory of the SD card. 
3. Attach the core peripherals to the Raspberry Pi.
 1. Connect HDMI display using the HDMI cable
 2. Connect the USB hub 
 2. Connect the USB keyboard and mouse via the hub
 3. Connect the USB wifi adapter or router
 4. 
 4. Power on the display
 3. Insert microUSB to power on the device. Verify by seeing the red indicator on the board marked "PWR"
 3. Follow the on screen setup instructions for OS setup. Ensure SSH is enabled.

1.  install the RPi.GPIO library.



	
	this is code

## Setup
### Hardware
### Software
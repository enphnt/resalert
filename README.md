# Resalert
---
###### **NOTE:**  This readme is intended to provide step by step procedure for preparing the Resalert prototype. Information for all necessary hardware and software components is outlined. Moreso, source code along with details of required libraries is detailed to assist in assembly.
---
This repo houses the proposed IoT-enabled information-centric architecture driven approach, which is called here “Resalert”. The Resalert offers emergency IoT-enabled information supply chain architecture pattern and system architecture. Research findings suggests that a RaspberryPi based system prototype could be useful to the effective delivery of emergency information to elderly people.  

**Keywords:** E-government; Emergency Information Management; Information Architecture; Internet of Things (IoT); Smart Technology

## Hardware Components
The hardware needed for completing the setup is detailed below. The main component of the prototype is the Raspberry Pi, pictured below. This System on a Chip CPU is essentially a pocket-sized personal computer. The Pi and other needed hardware is estimated at around $60.00 AUD. Only those components used will be detailed so that an alternative build could use these as minimum system requirements. Note that the 2nd iteration of the Raspberry Pi is also appropriate for building the prototype. 

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


## Setup


### 1 - Prepare Operating System
The operating system of choice at the time of initial build was Raspbian v3.10. To ease installation, it is recommended to make use of NOOBS which rapidly speeds up OS configuration. It is assumed that the router is configured and accessible with an Internet connection. To initially configure the OS, it is necessary to:

1. Erase and reformat the SD card. There is freely available open source software for accomplishing this task on your existing personal computer. 
2. Copy the operating system image or NOOBS package to the root directory of the SD card. 
 
### 2 - Setup the Pi Hardware
3. Attach the core peripherals to the Raspberry Pi.
 1. Connect HDMI display using the HDMI cable
 2. Connect the USB hub 
 3. Connect the USB keyboard and mouse via the hub
 4. Connect the USB wifi adapter or router
 5. Power on the display
 6. Lastly, insert microUSB to power on the device to start the device

###  3 - Setup the Pi Software
1. Follow the on screen setup instructions for OS setup. Ensure SSH is enabled.
2. Conigure LAN and Internet connection
3. Download and install RPi.GPIO library
4. Clone the git repo using the public link:
		
		git clone git@github.com:enphnt/resalert.git


### 4 - Run the Program
1. Run the program, either via SSH or within a terminal, by executing the shell script: 
			
		./<absolute/path/to>/alert.sh
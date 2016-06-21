## Raspberry-Pi-startup-texter

A simple python script that will send you a text message with the IP of your Raspberry Pi when it boots and is connected to a network

## To run this program you will need:
- [Python]
- [A Gmail Account]
- [A phone with SMS capabilities]
- [Raspberry Pi with Internet]
- [git]

## Installation
Open terminal and type in the following commands:
````
mkdir ~/code 
cd ~/code
git clone https://github.com/shahvineet98/Raspberry-Pi-startup-texter.git
cd Raspberry-Pi-startup-texter/
nano startup_text.py
````
Once the file is open in nano or any text editor that you are using, change the following values by following the comments
-[phone_number_email]
-[gmail_username]
-[gmail_password]

Save the file:
Ctrl + X will quit the editor and you will be asked if you want to save your changes. Press Y for Yes

## Add to startup
On Raspbian:
````
sudo crontab -e
````
Press 2 and then Enter
Go to the bottom of the file after all the comments and type in:
````
@reboot sleep 300 && python /home/pi/code/Raspberry-Pi-startup-texter/startup_text.py &
````

You should now recieve a text message with the Pi's IP when the Pi boots up and is connected to a network.



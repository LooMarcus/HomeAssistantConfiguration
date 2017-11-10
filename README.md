# My Home Assistant Configuration
I'm often behind on updating the readme. Ask me about anything!

### Running Hassbian Stretch on a Raspberry Pi 3 with a 16 gb card (and another for backups).
* Using Homebridge to get support for Homekit and Siri

## Hubs
* 433 mhz: RFXTRX433e
* Zwave: Aeon Labs Z Wave Stick (GEN 5)
* Zigbee: Xiaomi, Hue and Trådfri gateways

## Devices
* Hue lights
* Trådfri lights
* Nexa and Proove plugs/dimmers (433mhz)
* Ios-devices (iPhones, Apple watch, iPad)
* Old Samsung Galaxy tablet (currently not used)
* Sannce IP camera (currently not used)
* Xiaomi MiFloras (plant sensors)
* IRobot Roomba 880
* Electrolux Air Cleaner
* Withings WS-50
* 3 Broadlink RM3 mini IR-blaster
* Nvidia Shield TV (Android tv, media center)
* Plex Media Server
* Two Samsung smart tv's
* Samsung Media system
* Chromecast
* Synology NAS
* Sonos Play3
* Neo Coolcam Flood sensor
* Neo Coolcam Door/Window sensors
* Neo Coolcam Pirs
* Xiaomi Door/Window sensors
* Xiaomi Pirs
* Xiaomi Switches
* Xiaomi Temperature and Humidity Sensors
* Sensative Strips Door sensor
* Nexa motion sensor (433mhz)
* Nexa Door/Window sensor (433mhz)
* Fibaro Wall Plug
* Fibaro Dimmer 2
* Pax Calima Bluetooth Bathroom Fan
* Nexa Doorbell
* and probably some more things I've forgotten about...

### Presence-detection
* Ios-app for Hass.
* Homekit
* neither is 100 %, I'm currently also experimenting with bayesian sensors

## Automation hall of fame
### My favorite automations
* Setting air cleaner in bedroom to quiet at 9 pm (before bedtime) and auto at 11 am (when we are sure to have gotten out of bed), using Broadlink RM3 mini ir blaster
* Set light status on a few lights inside and outside based on time of day, sun and if we are coming home at night
* Xiaomi switch by the bed toggles bedside lamp, bedroom ceiling light or turn off all smart lights for the night
* Roomba only vacuums when noone is home, using Broadlink RM3 mini ir blaster
* Notifications when washing machine is done
* Say good morning to Siri and she turns on a couple of lights and turns on the morning show on the livingroom tv
* When someone rings the doorbell, send notifications and flash lights in backyard
* Notifications for cleaning cat litterboxes

## Future plans:
* Setting up a Magic mirror with information from Hass.
* Setting up Floorplan on tablets
* Turning on lights in stairs on motion, different brightness on different times of day (two Xiaomi pirs on the way and need to buy a Proove dimmer for the lights)
* Turn kitchen lights smart
* Trådfri lights in walk in closet that turns on when you open the door
* Automate  turning on and off charging of e-bike battery, with notifications


## Recommended links
* [Hassbian](https://home-assistant.io/docs/installation/hassbian/)
* [How to backup your config on Github](https://home-assistant.io/docs/ecosystem/backup/backup_github/)
* [Homebridge](https://github.com/nfarina/homebridge) and [Homebridge for Home assistant](https://github.com/home-assistant/homebridge-homeassistant)
* [Backup your sd card with rpi-clone - in swedish](https://snillevilla.se/automatisk-sakerhetskopiering-av-raspberry-pi-minneskort/)

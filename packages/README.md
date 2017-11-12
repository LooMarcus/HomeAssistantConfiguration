# Packages
#### air_cleaner
Using a Broadlink RM3 turn on and off Air cleaner quiet mode.

#### alarm
Using Home Assistants Alarm Control Panel automatically arming and disarming on presence.

#### alarm_clock
Alarm clock with sensors and automation. Right now not using as a normal alarm clock, just automation trigger. Using Ios app and actionable notifications to let Hass know I'm up.

#### bathroom_fan
Using [PyCalima](https://github.com/PatrickE94/pycalima) command line sensor to get values from my bathroom fan.

#### batteries
Template sensors for sensor battery levels and automations to notify on low battery.

#### doorbell
Send notifications and flash lights when someone rings the doorbell. Using a [python script](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/python_scripts/flash_lights_upstairs_hallway_and_yard.py) to flash the lights and then return to previous state and brightness.

#### doors
Template sensors for door sensors and alerts when doors are left open.

#### flood_sensors
Template sensors for flood sensors and alert for when they detect water leak.

#### goodnight
Playing some with trying to detect when we go to bed by tracking when our phones are charging. Could be used for other automations.

#### guest_mode
Boolean for setting the house in guest mode. Used to override automations.

#### ir_remote_livingroom
Switches for the Broadlink RM3 in the living room.

#### laundry_outside
Keeping track of if there is laundry hanging to dry outside (on balcony) manually by pressing a switch. Notifications if there is aprobaility it's going to rain and laundry is hanging outside and if the laundry has hung outside for 12 hours (probably dry by then...).

#### laundry_washing_machine
Sensor and input_select for washing machine (with the help of Fibaro wall plug). Automations for checking what state the washing machine is in and sending notifications and turning a light red when it's done, but only under certain circumstances (time and presence). Using actionable notifications for ios.
The plan is to set this up for dryer as well, and maybe also dishwasher.

#### lights_at_dark
Automations for turning on certain lights based on sunset, and turn them off again at midnight.

#### lights_at_presence
Automations for turning on certain lights if we come home during the night and then turning the outside lights off again after ten minutes. Turn certain ceiling lights on if we come home based on sunset (it's nice to come home to a little bit of light during the winter especially).

#### lights_in_morning
Automations for turning certain lights on at 06.40 during the work week and turn them off again at sunrise.

#### litterbox_downstairs and litterbox_upstairs
Lot's of things to help determine if the litterboxes need cleaning and keeping track of visits to litterboxes. You can read about it [at the forums](https://community.home-assistant.io/t/smart-litter-box-or-smart-cats/27646) or [in swedish](https://www.automatiserar.se/tavlingsbidrag-smarta-kattlador/).

#### magic_mirror_specific
A place for the things I need specifically for the Magic Mirror I'm making.

#### miflora
Setup for my plant monitors. Also see [plant configuration](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/plant.yaml).

#### motion_sensors
Template sensors for pirs and customize to shown with Homebridge.

#### network_devices
Template sensors (with custom icons) to track states of the devices on our network. Automations for notifying when some of the more critical ones have been offline for more then five minutes. I'm using the nmap component to track the devices.

#### presence_isa and presence_stefan
Trying to find a good way to determine presence... Now trying a python script to update a custom device_tracker from latest update.

#### roomba
Using a Broadlink RM3 to turn on, off and dock the Roomba robot vacuum. I use a Xiaomi door sensor to determine if the Roomba is docked. Using actionable notifications for ios to ask if the Roomba should vacuum when everyone is away.

<!-- #### stairs
Trying out a way to turn on the lights in the stairway on motion. Will add more conditions and also brightness when I have the right hardware present. -->

#### svtplay
Using custom component for playing web tv on chromecast. Currently only using it to put the morning news on our NVidia Shield, but could do more.

#### system_monitor
Some sensors to keep track of my RPi3, Hass, other processes and speedtesting our internet. Alerting on critical disk use on the RPi. Notifying when Homebridge or Mosquitto has been down for one minute.

#### temperature
Right now only customizing entities to be shown with Homebridge.

#### test_package
Package for...testing stuff.

#### vacation_mode
For running automations when we are on holiday.

#### windows
Same as doors but for windows.

#### Xiaomi
Xiaomi stuff that hasn't been moved to another package. Automations for light switch by the bed.
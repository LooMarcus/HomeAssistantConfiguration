# Packages
#### air_cleaner
Using a Broadlink RM3 turn on and off Air cleaner quiet mode.

#### alarm
Using Home Assistants Alarm Control Panel automatically arming and disarming on for instance presence.

#### alarm_clock
Alarm clock with sensors and automation. Right now not using as a normal alarm clock, just automation trigger. Using Ios app and actionable notifications to let Hass know I'm up.

#### bathroom_fan
Using [PyCalima](https://github.com/PatrickE94/pycalima) command line sensor to get values from my bathroom fan. Currently not in use.

#### batteries
Template sensors for sensor battery levels and automations to notify on low battery.

#### bedroom_lights
Controls bedroom lights with a Xiaomi switch

#### charging_station
Reminder to charge my e-bike battery every night. Will redo with more variables when I get another power metering plug to monitor with.

#### cleaning_day
Turns off certain behaviour that's not wanted when the cleaners are here.

#### cleaning_time
Scripts for telling Alexa to turn all lights on full (for cleaning), putting on some cleaning music (upbeat playlist from Spotify playing on Sonos) and then when done cleaning dim the lights and turn some off again.

#### doors
Template sensors for door sensors and alerts when doors are left open.

#### flood_sensors
Template sensors for flood sensors and alert for when they detect water leak.

#### floorlamp
Control the uplight with a Xiaomi switch. Toggle, full brightness and dimmer.

#### goodnight
Script that can be called with Siri or Alexa to get ready for bed. Also playing some with trying to detect when we go to bed by tracking when our phones are charging, not working 100 %.

#### guest_mode
Boolean for setting the house in guest mode. Used to override automations.

#### hallway_light
Control the uplight with a Xiaomi switch. Toggle light and toggle full and lower brightness. Long click press used for mailbox (see that package).

#### house
Things having to do with the whole house, more or less

#### internet_monitor
Speedtests and router status.

#### laundry_dryer
Basically the same as laundry_washing_machine, see below.

#### laundry_outside
Keeping track of if there is laundry hanging to dry outside (on balcony) manually by pressing a switch. Notifications if there is aprobaility it's going to rain and laundry is hanging outside and if the laundry has hung outside for 12 hours (probably dry by then...).

#### laundry_washing_machine
Sensor and input_select for washing machine (with the help of Fibaro wall plug). Automations for checking what state the washing machine is in and sending notifications and turning a light red (red light temporarely turned off) when it's done, but only under certain circumstances (time and presence). Using actionable notifications for ios.

#### lights_at_dark
Automations for turning on certain lights based on sunset, and turn them off again at midnight.

#### lights_at_presence
Automations for turning on certain lights if we come home during the night and then turning the outside lights off again after ten minutes. Turn certain ceiling lights on if we come home based on sunset (it's nice to come home to a little bit of light during the winter especially).

#### lights_in_morning
Automations for turning certain lights on at 06.40 during the work week and turn them off again at sunrise.

#### lights
Script for movie time called by Alexa or Siri. Also using a custom state card with tiles (link in main readme) for controlling some scripts for lights. Generic light groups.

#### litterbox_downstairs and litterbox_upstairs
Lot's of things to help determine if the litterboxes need cleaning and keeping track of visits to litterboxes. You can read about it [at the forums](https://community.home-assistant.io/t/smart-litter-box-or-smart-cats/27646) or [in swedish](https://www.automatiserar.se/tavlingsbidrag-smarta-kattlador/).

#### magic_mirror_specific
A place for the things I need specifically for the Magic Mirror I'm making.

#### mailbox
Using two Xiaomi door/window sensors sending notifications when we get mail or packages in mailbox. Switch for resetting, delay so that I can press first, then get the mail, if on my way out.

#### miflora
Setup for my plant monitors. (Currently disabled due to some error showing up alot)

#### motion_sensors
Template sensors for pirs and customize to shown with Homebridge.

#### notify_stefan
Playing around with sending custom notification to hubby for example when dinner is ready. Thinking about having a button in kitchen to auto send initial message.

#### presence_isa and presence_stefan
Trying to find a good way to determine presence... Now trying a python script to update a custom device_tracker from latest update.

#### ring_doorbell
Flash lights when someone rings the doorbell using a python script to flash the lights and then return to previous state and brightness. Also turn the outside front light and hallway window light to 100 % on ding or motion. Plus some other config for the Ring Doorbell.

#### roomba
Using a Broadlink RM3 to turn on, off and dock the Roomba robot vacuum. I use a Xiaomi door sensor to determine if the Roomba is docked. Using actionable notifications for ios to ask if the Roomba should vacuum when everyone is away.

#### stairs_lights
Mqtt light config for stairs lights (MiLight).

#### svtplay
Using custom component for playing web tv on chromecast. Currently only using it to put the morning news on our NVidia Shield, but could do more.

#### system_info
Template sensors (with custom icons) to track states of the devices on our network. Automations for notifying when some of the more critical ones have been offline for more then five minutes. I'm using the nmap component to track the devices.
Groups for system information, internet status and network devices. Automations for when critical devices go offline.

#### system_monitor
Some sensors to keep track of my RPi3, Hass, other processes and speedtesting our internet. Alerting on critical disk use on the RPi. Notifying when Homebridge or Mosquitto has been down for one minute.

#### temp_light_humidity
Graphs and groups for temperature, humidity and light sensors.

#### test_package
Package for...testing new stuff. (Commented out when not testing)

#### time_day
Things that has to do with time and time of day. Mostly for use in other automations.

#### upstairs_bathroom
Alert when forgetting to close bathroom cabinet.

#### vacation_mode
For running automations when we are on holiday.

#### walk_in_closet_lights
Exactly what it sounds like.

#### weather
Weather sensors and groups.

#### windows
Same as doors but for windows.

#### workday
Workday sensor, for use in automations. I have changed in the python file so that it takes swedish holidays instead of danish.
In need of updating. Not keeping up with all my changes..
# My Home Assistant Configuration

### Running on a Raspberry Pi 3 with an 8 gb card.

## Hubs
* 433 mhz: RFXTRX433e
* Zwave: Aeon Labs Z Wave Stick (GEN 5)

## Devices
* Hue lights
* Nexa motion sensor (433mhz)
* Nexa door sensor (433mhz)
* Nexa and Proove plugs/dimmers (433mhz)
* Ios-devices (iPhones, Apple watch, iPad)
* Old Samsung Galaxy tablet
* Sannce IP camera
* Xiaomi MiFloras (plant sensors)
* IRobot Roomba 880
* Electrolux Air Cleaner
* Withings WS-50
* 2 Broadlink RM3 mini IR-blaster
* Nvidia Shield TV
* Plex Media Server
* Two Samsung smart tv's
* Samsung Media system
* Chromecast
* Sonos Play3
* Neo Coolcam Flood sensor
* Neo Coolcam Door/Window sensors
* Neo Coolcam Pirs
* Sensative Strip Door sensor
* and probable some things I've forgotten about

### Presence-detection
* Ios-app for Hass.

## Automations
Not very much yet, more coming after we move in July.
* air_cleaner: Setting air cleaner in bedroom to quiet at 9 pm (before bedtime) and auto at 11 am (when we are sure to have gotten out of bed), using Broadlink RM3 mini ir blaster
* back_door: Notify when back door is opened or closed when no one is at home (add when we are sleeping, if goodnight automation is found to be working)
* bedroom_switches: Allow the nexa switch by the bed to turn on and off the bedroom hue light, and to turn off all smart lights on the inside of the house
* fire_alarm: Send notifications when fire alarms go off (not working at the moment, fire alarms only send unknown)
* front_door: Notify when front door is opened or closed when no one is at home (add when we are sleeping, if goodnight automation is found to be working)
* goodnight: Trying to do a catch all automation for hass to know when we are asleep (not yet tested)
* house_mode_automation: Setting the input_select to different options, based on sun and time (adding "night" if goodnight automation works, to use as trigger to other things)
* laundry_notifications: Send actionable notifications when washing machine is done
* laundry: Track the washing machine status based on watt from Fibaro plug
* lights_at_dark: Set light status on a few lights inside and outside based on time of day, sun and if we are coming home at night
* medication_tracker: Not yet done, but I want it to be able to keep track of if I've taken my medications and remind me if not. A button for me to tell hass I've taken the medication and a red led at my bed for reminding me I've not taken it. Will be done with a Nodemcu and Espeasy
* new_ha_release: Update for hass available notification
* presence_isa and presence_stefan: Presence notifications
* reminder_to_water: Water plants-notifications
* twitch_on_air: Not yet done, will be used to make an "on air" sign with Nodemcu and Espeasy
* vacuuming: Turn on the Roomba robot vacuum cleaner once during the day when we are not at home, using Broadlink RM3 mini ir blaster

## In the process of setting up Floorplan for display on tablets around the house
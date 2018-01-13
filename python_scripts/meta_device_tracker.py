#
# meta_device_tracker.py
#
# https://github.com/oakbrad/brad-homeassistant-config/blob/master/python_scripts/meta_device_tracker.py
#
# Combine multiple device trackers into one entity
#
# Logic:  Only GPS is reliable for 'not_home'
#         Block others from marking 'not_home' but keep for 'home'
# 
# Use:
# - alias: "Update Brad's Meta Tracker Home"
#   trigger:
#     - platform: state
#       entity_id: device_tracker.brad_ios, device_tracker.brad_owntracks, device_tracker.brad_ping
#       to: 'home'
#     - platform: homeassistant
#       event: start
#   action:
#     service: python_script.meta_device_tracker
#     data_template:
#       entity_id: '{{trigger.entity_id}}'
#       meta_entity: 'Brad'
   
# Get Data from Automation Trigger
triggeredEntity = data.get('entity_id')
metatrackerName = "device_tracker." + data.get('meta_entity')

# Get current & new state
newState = hass.states.get(triggeredEntity)
currentState = hass.states.get(metatrackerName)

# # Create placeholder device_tracker.meta entity
# hass.states.set(metatrackerName, 'unknown', {
#     'name': metatrackerName,
#     'last_update_source': 'placeholder'
# })

# hass.services.call('notify', 'pushbullet_isa', {"message": currentState, "title": "Meta tracker script"})

# Get New data
newSource = newState.attributes.get('source_type')


# Set new state and icon
# Everything updates 'home'
if newState.state == 'home':
    newStatus = 'home'
    newIcon = 'mdi:home-map-marker'
# For input_boolean set by homekit
elif newState.state == 'on':
    newStatus = 'home'
    newIcon = 'mdi:home-map-marker'
    newSource = "homekit"
# See if this is holding up, otherwise remove
elif newState.state == 'off':
    newStatus = 'not_home'
    newIcon = 'mdi:home'
    newSource = "homekit"

# every tracker for person must be not_home for it to report not home
elif newState.state == 'not_home':
    if metatrackerName == 'device_tracker.isabella':
        # isa_wifi_state = hass.states.get('device_tracker.isabellas_iphone_6s_wifi')
        isa_bt_state = hass.states.get('device_tracker.isabellas_iphone_6s_bt')
        isa_ios_state = hass.states.get('device_tracker.isabellas_iphone_6s')
        # if isa_wifi_state == 'not_home' and isa_bt_state == 'not_home' and isa_ios_state == 'not_home':
        if isa_bt_state == 'not_home' and isa_ios_state == 'not_home':
            newStatus = 'not_home'
            newIcon = 'mdi:home'
    elif metatrackerName == 'device_tracker.stefan':
        # stefan_wifi_state = hass.states.get('device_tracker.stefan_iphone_7_wifi')
        stefan_ios_state = hass.states.get('device_tracker.stefan_iphone_7')
        # if stefan_wifi_state == 'not_home' and stefan_ios_state == 'not_home':
        if stefan_ios_state == 'not_home':
            newStatus = 'not_home'
            newIcon = 'mdi:home'

# Otherwise keep old status
else: 
    newStatus = currentState.state


# If GPS source, set new coordinates
if newSource == 'gps':
    newLatitude = newState.attributes.get('latitude')
    newLongitude = newState.attributes.get('longitude')
    newgpsAccuracy = newState.attributes.get('gps_accuracy')
# If not, keep last known coordinates
else:
    if newSource is not None:
        newLatitude = currentState.attributes.get('latitude')
        newLongitude = currentState.attributes.get('longitude')
        newgpsAccuracy = currentState.attributes.get('gps_accuracy')

# # Get Battery
if newState.attributes.get('battery') is not None:
    newBattery = newState.attributes.get('battery')
elif currentState.attributes.get('battery') is not None:
    newBattery = currentState.attributes.get('battery')
else:
    newBattery = None

# Create device_tracker.meta entity
hass.states.set(metatrackerName, newStatus, {
    'icon': newIcon,
    'name': metatrackerName,
    'source_type': newSource,
    'battery': newBattery,
    'gps_accuracy': newgpsAccuracy,
    'latitude': newLatitude,
    'longitude': newLongitude,
    'last_update_source': newState.name 
})


# done = hass.states.get(metatrackerName)
# hass.services.call('notify', 'pushbullet_isa', {"message": done, "title": "Meta tracker script done"})
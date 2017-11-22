## https://home-assistant.io/components/python_script/
## https://home-assistant.io/docs/configuration/state_object/

## Idea stolen from https://github.com/maattdiy/home-assistant-config/blob/490abea923cdf824d91b94060155d73ca2695dc4/python_scripts/summary.py

# home_count = 0
# home_desc = ""
light_count = 0
light_desc = ""
door_count = 0
door_desc = ""
inuse_count = 0
inuse_desc = ""
summary = ""

# ##################################################
# ## People count
# ##################################################

# # People at home (only by phone)
# for entity_id in hass.states.entity_ids('device_tracker'):
#     if entity_id.find("phone") >= 0:
#         state = hass.states.get(entity_id)
#         if state.state == 'home':
#             home_count = home_count + 1
#             home_desc = home_desc + state.name + ', '
#             #relative_time(state.last_changed) Is possible show the relative time?

# if home_count > 0:
#     home_desc = str(home_count) + ' at home: ' + home_desc[:-2]
# else:
#     home_desc = 'Nobody in home'

# summary = home_desc

##################################################
## Light count
##################################################

# People at home (only by phone)
for entity_id in hass.states.entity_ids('light'):
    # if entity_id.find("phone") >= 0:
        state = hass.states.get(entity_id)
        if state.state == 'on':
            light_count = light_count + 1
            light_desc = light_desc + state.name + ', '
            #relative_time(state.last_changed) Is possible show the relative time?

if light_count > 0:
    light_desc = str(light_count) + ' lights on. - ' #+ light_desc[:-2]
else:
    light_desc = 'No lights on. - '

summary = light_desc + '\r' 


##################################################
## Door count
##################################################

# People at home (only by phone)
for entity_id in hass.states.entity_ids('sensor'):
    if entity_id.find("_door") >= 0:
        state = hass.states.get(entity_id)
        if state.state == 'Open':
            door_count = door_count + 1
            door_desc = door_desc + state.name + ', '
            #relative_time(state.last_changed) Is possible show the relative time?

if door_count == 1:
    door_desc = 'One door open: ' + door_desc[:-2]
elif door_count > 0:
    door_desc = str(door_count) + ' doors open: ' + door_desc[:-2]    
else:
    door_desc = 'No doors open'

last_door_opened = hass.states.get('sensor.last_door_opened')

summary = summary + '\n ' + door_desc #+ '\n Last opened: ' + last_door_opened.state
##################################################
## Devices in use count
##################################################

domnains = ['switch', 'media_player']
for domain in domnains:
    for entity_id in hass.states.entity_ids(domain):
        show = False
        state = hass.states.get(entity_id)
        
        # Media players
        if (state.state == 'playing'):
            show = True
            
        # Switchs with icons
        if (state.state == 'on'):
            ## Only switchs with icons are relevants (ignore internal switchs). Find by tag "icon" in dictionary because "state.attributes.icon" didn't work
            if (str(state.attributes).find("'icon'")) >= 0:
                show = True
        
        if (show):
            if (inuse_desc.find(state.name + ', ') == -1):
                #logger.info("state.attributes = " + str(state.attributes))
                inuse_count = inuse_count + 1
                inuse_desc = inuse_desc + state.name + ', '

if inuse_count > 0:
    inuse_desc = str(inuse_count) + ' in use: ' + inuse_desc[:-2]
    summary = summary + '\n ' + inuse_desc

# ##################################################
# ## Alarm clock
# ##################################################

# if (hass.states.get('input_boolean.alarmclock_wd_enabled').state != 'on') and (hass.states.get('input_boolean.alarmclock_we_enabled').state != 'on'):
#     summary = summary + '\n ' + '!Alarm clock is disabled'

# ##################################################
# ## Profile/mode
# ##################################################

# state = hass.states.get('input_select.ha_mode')
# if (state.state != 'Normal'):
#     summary = summary + '\n ' + '* ' + state.state + '  profile is activated'
#     hass.states.set('sensor.profile_badge', '', {
#         'entity_picture': '/local/profiles/developer.png',
#         'friendly_name': ' ',
#         'unit_of_measurement': 'Mode'
#     })

##################################################
## Sensors updates
##################################################

# # People badge update
# hass.states.set('sensor.people_badge', str(home_count), {
#     'friendly_name': ' ',
#     'unit_of_measurement': 'Home',
# })

# # In use badge update
# hass.states.set('sensor.inuse_badge', str(inuse_count), {
#     'friendly_name': ' ',
#     'unit_of_measurement': 'In use'
# })

# Summary sensors update
hass.states.set('sensor.summary', summary, {
    # 'custom_ui_state_card': 'state-card-value_only'
})
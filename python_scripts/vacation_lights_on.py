livingroomLight = hass.states.get('light.living_room_ceiling_light_level')
livingroomSpotlights = hass.states.get('light.living_room_spotlights_level')
diningroomLight = hass.states.get('light.dining_area_ceiling_light_level')
passageSpotlights = hass.states.get('light.passage_ceiling_spotlights_level')
isaLight = hass.states.get('light.isa_ceiling_light')
stefanLight = hass.states.get('light.stefan_ceiling_light')
bedroomLight = hass.states.get('light.bedroom_ceiling_light')
upstairsHallwayLight = hass.states.get('light.upstairs_hallway_ceiling_light_level')
# add walk in closet lights when arrived

guestMode = hass.states.get('input_boolean.guest_mode')
now = datetime.datetime.now()

timeOfDay = int("{}{}".format(now.hour, now.minute))

# 0 = monday, 6 = sunday
weekday = datetime.date(now.year, now.month, now.day).weekday()
workday = hass.states.get('binary_sensor.workday_sensor')

hass.services.call('notify', 'pushbullet_isa', {"message": test, "title": test})

if guestMode is 'off':
    # if weekday < 5 # weekday
    if workday is 'on'
        # Evenings - "coming home from work"
        if timeOfDay > 1730:
            if diningroomLight.state is 'off':
                hass.services.call('light', 'turn_on', {'entity_id': diningroomLight, 'brightness': '50', "transition": "30"})
                time.sleep(30)
                hass.services.call('light', 'turn_on', {'entity_id': passageSpotlights, 'brightness': '50', "transition": "30"})
                time.sleep(10)
                hass.services.call('light', 'turn_on', {'entity_id': livingroomLight, 'brightness': '50', "transition": "30"})
                time.sleep(60)
                hass.services.call('light', 'turn_on', {'entity_id': upstairsHallwayLight, 'brightness': '50', "transition": "30"})
                time.sleep(20)
                hass.services.call('light', 'turn_on', {'entity_id': isaLight, 'brightness': '50', "transition": "30"})
                hass.services.call('light', 'turn_on', {'entity_id': stefanLight, 'brightness': '50', "transition": "30"})
        # Mornings
        elif timeOfDay > 640 and timeOfDay < 900
            if bedroomLight.state is 'off':
                hass.services.call('light', 'turn_on', {'entity_id': bedroomLight, 'brightness': '100', "transition": "30"})
                time.sleep(60)
                hass.services.call('light', 'turn_on', {'entity_id': upstairsHallwayLight, 'brightness': '50', "transition": "30"})
                time.sleep(20)
                hass.services.call('light', 'turn_on', {'entity_id': passageSpotlights, 'brightness': '50', "transition": "30"})
                hass.services.call('light', 'turn_on', {'entity_id': diningroomLight, 'brightness': '50', "transition": "30"})
            # Add walk in closet            

    # elif weekday > 4 # weekend
    elif workday is 'off'
        # Evenings    
        if timeOfDay > 1600:
            if diningroomLight.state is 'off':
                hass.services.call('light', 'turn_on', {'entity_id': diningroomLight, 'brightness': '50', "transition": "30"})
                time.sleep(30)
                hass.services.call('light', 'turn_on', {'entity_id': passageSpotlights, 'brightness': '50', "transition": "30"})
                time.sleep(10)
                hass.services.call('light', 'turn_on', {'entity_id': livingroomLight, 'brightness': '50', "transition": "30"})
                time.sleep(60)
                hass.services.call('light', 'turn_on', {'entity_id': upstairsHallwayLight, 'brightness': '50', "transition": "30"})
                time.sleep(20)
                hass.services.call('light', 'turn_on', {'entity_id': isaLight, 'brightness': '50', "transition": "30"})
                hass.services.call('light', 'turn_on', {'entity_id': stefanLight, 'brightness': '50', "transition": "30"})
        # Mornings
        elif timeOfDay > 830 and timeOfDay < 1000
            if bedroomLight.state is 'off':
                hass.services.call('light', 'turn_on', {'entity_id': bedroomLight, 'brightness': '100', "transition": "30"})
                time.sleep(60)
                hass.services.call('light', 'turn_on', {'entity_id': upstairsHallwayLight, 'brightness': '50', "transition": "30"})
                time.sleep(20)
                hass.services.call('light', 'turn_on', {'entity_id': passageSpotlights, 'brightness': '50', "transition": "30"})
                hass.services.call('light', 'turn_on', {'entity_id': diningroomLight, 'brightness': '50', "transition": "30"})
                # Add walk in closet
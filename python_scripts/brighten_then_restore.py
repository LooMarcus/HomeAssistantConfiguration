entity_id = data.get('entity_id')

light = hass.states.get(entity_id)

original_state = light.state
# if original_state is 'on':
brightness = light.attributes.get('brightness') or 0

hass.services.call('light', 'turn_on', {'entity_id': entity_id, 'brightness': '255'})

time.sleep(180)

if original_state is 'on':
    hass.services.call('light', 'turn_on', {'entity_id': entity_id, 'brightness': brightness})
else:
    hass.services.call('light', 'turn_off', {'entity_id': entity_id})
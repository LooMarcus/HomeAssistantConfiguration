entity_id = data.get('entity_id')

light = hass.states.get(entity_id)

original_state = light.state
if original_state is 'off':
    hass.services.call('light', 'turn_on', {'entity_id': entity_id})

time.sleep(1)
hass.services.call('light', 'turn_off', {'entity_id': entity_id})
time.sleep(0.5)
hass.services.call('light', 'turn_on', {'entity_id': entity_id})
time.sleep(1)

hass.services.call('light', 'turn_off', {'entity_id': entity_id})
time.sleep(0.5)

if original_state is 'on':
    hass.services.call('light', 'turn_on', {'entity_id': entity_id})
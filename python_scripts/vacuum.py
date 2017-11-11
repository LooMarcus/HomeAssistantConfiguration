roomba = hass.states.get('switch.roomba')

hass.services.call('switch', 'turn_on', { 'entity_id': roomba })

time.sleep(10)

if roomba.state is 'off'
    hass.services.call('python_script')
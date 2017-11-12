# turns on the roomba
# then waits and sees if it's gone away from the docking station
# then sets correct status on input select
# or start the script again

hass.services.call('switch', 'turn_on', { 'entity_id': 'switch.roomba' })

time.sleep(10)

roomba = hass.states.get('binary_sensor.door_window_sensor_158d0001a3df50')

if roomba.state is 'off'
    hass.services.call('python_script', 'vacuuming')
elif roomba.state is 'on'
    hass.services.call('input_select', 'select_option'. {'entity_id': 'input_select.roomba_mode', 'option': 'Vacuuming'})
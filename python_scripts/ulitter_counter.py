counter = hass.states.get('sensor.upstairs_litter_box_visits')

if counter is None:
    value = 0
else:
    value = int(counter.state)

hass.states.set('sensor.upstairs_litter_box_visits', value + 1)
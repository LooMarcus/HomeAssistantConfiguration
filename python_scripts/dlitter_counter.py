counter = hass.states.get('sensor.downstairs_litter_box_visits')

if counter is None:
    value = 0
else:
    value = int(counter.state)

hass.states.set('sensor.downstairs_litter_box_visits', value + 1)
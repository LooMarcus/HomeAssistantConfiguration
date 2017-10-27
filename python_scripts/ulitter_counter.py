counter = hass.states.get('sensor.upstairs_litterbox_visits')

if counter is None:
    value = 0
else:
    value = int(counter.state)

hass.states.set('sensor.upstairs_litterbox_visits', value + 1)
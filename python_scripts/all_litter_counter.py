counter = hass.states.get('sensor.all_litterbox_visits_today')

if counter is None:
    value = 0
else:
    value = int(counter.state)

hass.states.set('sensor.all_litterbox_visits_today', value + 1)
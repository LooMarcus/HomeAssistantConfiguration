# counter = hass.states.get('sensor.downstairs_litterbox_visits')

# if counter is None:
#     value = 0
# else:
#     value = int(counter.state)

value = int(hass.states.get('sensor.downstairs_litterbox_visits') or 0)
hass.states.set('sensor.downstairs_litterbox_visits', value + 1)
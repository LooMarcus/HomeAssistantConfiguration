# Create placeholder device_tracker.meta entities at startup
hass.states.set('device_tracker.isabella', 'unknown', {
    'name': 'Isabella',
    'last_update_source': 'placeholder'
})

hass.states.set('device_tracker.stefan', 'unknown', {
    'name': 'Stefan',
    'last_update_source': 'placeholder'
})
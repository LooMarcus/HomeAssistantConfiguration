state = data.get('state')

if state == 'mail':
    hass.states.set('sensor.mailbox', 'Mail!', {
        'icon': 'mdi:mailbox',
        'name': 'Mailbox'
    })
elif state == 'reset':
    hass.states.set('sensor.mailbox', 'No mail', {
        'icon': 'mdi:dots-horizontal',
        'name': 'Mailbox'
    })
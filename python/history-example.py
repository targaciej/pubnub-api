from Pubnub import Pubnub

## Initiat Class
pubnub  = Pubnub( 'demo', 'demo' )

## History Example
history = pubnub.history({
    'channel' : 'hello_world',
    'limit'   : 1
})
print(history)


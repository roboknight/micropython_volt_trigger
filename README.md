# micropython_volt_trigger
This is a simple R-Pi Pico ADC voltage trigger.
It was a quick dirty way to create a stupid ADC
voltage trigger.  I will eventually have to go
back an build a real voltage trigger, but this
will do for now.  Just:
   1) push trigger.py to your pico with ampy or similar.
   2) import trigger as t
   3) t.trigger()

Default value for trigger is around 0.680V or so... but
YMMV.


# When Colour is Detected

Scratch block:

![when colour](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/when-colour.png)

Note that we can select eight distinct colours.  The last option is when no colours are detected.

Python code:

```python
from util.print_override import spikeprint;print = spikeprint
import hub
from runtime import VirtualMachine
from util.sensors import get_sensor_value

async def stack_1(vm, stack):
    pass

def stack_condition(vm, stack):
    sensor_value = get_sensor_value("A", 0, -1, (61,))
    if sensor_value is None:
        sensor_value = -1
    return 0 == sensor_value

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "La30GuH_6sn6fsedoYj6")

    vm.register_on_condition("*lrjXBK6V0VoaqE|kZbc", stack_1, stack_condition)

    return vm
```

Here we can see how conditions are specified for stacks to run.  The virtual machine will monitor the condition for changes.  If the condition is satisfied, the corresponding stack will start running.  Stack conditions must return a boolean which indicates if the stack can run.

The first argument to `get_sensor_value()` is the hub port.  In this case, the colour sensor is connected to port "A".

The second parameter is always 0.

The third parameter appears to be the default to return when there is no value available.

The fourth parameter of `(61,)` seems to refer to the colour sensor.

For the colour sensor, the values returned are:

* 0: black
* 1: pink
* 3 or 4: blue/cyan
* 5: green
* 7: yellow
* 9: red
* 10: white
* None: no colour detected (note that the code turns this to -1 so that "==" can be used to produce the return value)

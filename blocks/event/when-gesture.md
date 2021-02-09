# When a Hub Gesture Occurs

Scratch block:

![when gesture](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/when-gesture.png)

This block can detect one of three gestures: shaken, tapped, falling.

Python code:

```python
from util.print_override import spikeprint;print = spikeprint
from runtime import VirtualMachine

async def stack_1(vm, stack):
    pass

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "La30GuH_6sn6fsedoYj6")

    vm.register_on_gesture("E{`aC,o*G#h4v3R(G:p_", stack_1, "shake")

    return vm
```

Gestures are handled directly by the virtual machine.  Instead of a stack condition, a string is passed as the third argument to `register_on_gesture()`.

Valid values are:

| string     | gesture |
|:-----------|:--------|
| "shake"    | shaken  |
| "tapped"   | tapped  |
| "freefall" | falling |

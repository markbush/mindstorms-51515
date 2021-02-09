# When the Hub Orientation Changes

Scratch block:

![when orientation](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/when-orientation.png)

The orientation to detect can be one of: front, back, top, bottom, left side, right side.

Python code:

```python
from util.print_override import spikeprint;print = spikeprint
import hub
from runtime import VirtualMachine
from util.scratch import number_to_orientation

async def stack_1(vm, stack):
    pass

def stack_condition(vm, stack):
    return hub.motion.gesture(number_to_orientation(1))

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "La30GuH_6sn6fsedoYj6")

    vm.register_on_condition("y8Lz@7dNCVZ=_xo|T+rt", stack_1, stack_condition)

    return vm
```

To detect a particular orientation, the argument to `number_to_orientation()` should be as follows:

| arg | orientation |
|----:|:------------|
| 1   | front       |
| 2   | back        |
| 3   | top         |
| 4   | bottom      |
| 5   | left side   |
| 6   | right side  |

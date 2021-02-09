# When a Timer Event Occurs

Scratch block:

![when timer](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/when-timer.png)

This block lets us perform an action when the timer first goes over a specified number of seconds.  This action will only fire once unless the timer is reset.

Python code:

```python
from util.print_override import spikeprint;print = spikeprint
import hub
from runtime import VirtualMachine
from util.scratch import compare

async def stack_1(vm, stack):
    pass

def stack_condition(vm, stack):
    return compare(vm.get_time() / 1000, 10) > 0

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "La30GuH_6sn6fsedoYj6")

    vm.register_on_condition("Fh5o+n|M]*=~k+0HYwBB", stack_1, stack_condition)

    return vm
```

The virtual machine's `get_time()` method is, clearly, returning a time in milliseconds which is converted to seconds in order to compare with the target value (10s in this case).  The `get_time()` method returns how long the script has been running, or else the duration since the last timer reset.

Although Scratch only allows us to specify a time in seconds to compare, we can use millisecond precision if we wish by removing the `/ 1000` part.

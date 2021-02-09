# When a General Condition Occurs

Scratch block:

![when condition](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/when-condition.png)

We can provide any boolean condition function to implement an arbitrary "when" block.

Python code:

```python
from util.print_override import spikeprint;print = spikeprint
import hub
from runtime import VirtualMachine
from util.scratch import to_boolean

async def stack_1(vm, stack):
    pass

def stack_condition(vm, stack):
    return a_boolean_value

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "La30GuH_6sn6fsedoYj6")

    vm.register_on_condition("%9{0f`AF?9QdH-L_}3*F", stack_1, stack_condition)

    return vm
```

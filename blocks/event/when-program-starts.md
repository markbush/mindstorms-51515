# When Program Starts

We have already seen the structure for how to specify an action to occur when the program starts.  The block is:

![when program starts](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/when-program-starts.png)

The code produced is:

```python
from util.print_override import spikeprint;print = spikeprint
from runtime import VirtualMachine

async def stack_1(vm, stack):
    pass

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "La30GuH_6sn6fsedoYj6")

    vm.register_on_start("XmJYmtjlnEjhbg4OeYzE", stack_1)

    return vm
```

We can register multiple stack functions to execute concurrently.  They must be declared using "async".  This is part of the concurrency mechanism of Python and means we will need to take care of when to use "yield" and "await", too.

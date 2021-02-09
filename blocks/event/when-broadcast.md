# When a Broadcast Event Occurs

Scratch block:

![when broadcast](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/when-broadcast.png)

We can cause a stack to execute when a message is broadcast.

Python code:

```python
from util.print_override import spikeprint;print = spikeprint
from runtime import VirtualMachine

async def stack_1(vm, stack):
    pass

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "La30GuH_6sn6fsedoYj6")

    vm.register_on_broadcast("n1?Z^9%*[-OwvPL2lJ$y", stack_1, "message1")

    return vm
```

To have a stack run when a message has been broadcast, we use the virtual machine's `register_on_broadcast()` method with the message to listen out for as the third argument.

## Broadcasting messages

There are two ways to broadcast messages.  One is to broadcast a message, then immediately move on to the next step in the program (asynchronous messaging).  The other is to broadcast the message and wait for any processing to complete before continuing (synchronous messaging).

### Asynchronous messages

Scratch block:

![broadcast](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/broadcast.png)

Python code:

```python
    vm.broadcast("message1")
```

Broadcasting doesn't wait, so the next statement is immediately executed.

### Synchronous messages

Scratch block:

![broadcast and wait](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/broadcast-and-wait.png)

Python code:

```python
    stacks = vm.broadcast("message1")
    while any([s.is_active() for s in stacks]):
        yield
```

In this case, we collect a list of all of the stacks that are started because of this message being sent and we wait as long as any of them is active.

Note the use of `yield` here.  This is part of Python's concurrency model.  It allows other activities to get a chance to run without blocking all processing.

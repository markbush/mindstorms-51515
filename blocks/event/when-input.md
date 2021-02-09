# When a Button or Key Event Occurs

### Detecting a hub button

Scratch block:

![when hub button](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/blocks/event/when-hub-button.png)

The hub can detect when either the left or right button is either pressed or released.

Python code:

```python
from util.print_override import spikeprint;print = spikeprint
from runtime import VirtualMachine

async def stack_1(vm, stack):
    pass

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "La30GuH_6sn6fsedoYj6")

    vm.register_on_button("ZCck{nnzq^[U(Vlr[_6O", stack_1, "left", "pressed")

    return vm
```

Detecting a button is handled by the virtual machine's `register_on_button()` method.

The third argument is "left" or "right" depending on the button to detect and the fourth argument is "pressed" or "released" according to the event that you wish to detect.

# Initial script setup

We have seen that the signature of `setup` is:

```python
def setup(rpc, system, stop):
```

For the `system` argument, we can try `system.system`.  The `stop` argument is a function, so we can try `sys.exit`.  But there is no information that easily helps us work out what `rpc` should be.  We can get some clues by creating a dummy object that will report to us what methods it needs.  We can define this as follows:

```python
class TestRPC:
    def __getattr__(self, name):
        def method(*args):
            print('Unknown method: '+name)
            if args:
                print('  args: '+str(args))
        return method
```

This class will log all methods called on it.  Armed with this, we can now write a test script:

```python
from util.print_override import spikeprint;print = spikeprint
import sys
import system
from runtime import VirtualMachine
from runtime.extensions import SoundExtension

def run(vm, stack):
    print('Hello')
    await vm.extensions["sound"].play("Cat Meow 1", vm.store.sound_volume(), vm.store.sound_pitch(), vm.store.sound_pan(), wait=True)
    print('Done')

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "hub_hacking")
    vm.extensions["sound"] = SoundExtension(rpc)
    vm.register_on_start("main_run", run)
    return vm

class TestRPC:
    def __getattr__(self, name):
        def method(*args):
            print('Unknown method: '+name)
            if args:
                print('  args: '+str(args))
        return method

print('Creating RPC')
rpc = TestRPC()
print('Creating VM')
vm = setup(rpc, system.system, sys.exit)
print('Starting')
vm.start()
```

We have added some logging to see how the application progresses.  If you run this on your hub, you should see the following output in the console:

```
> Creating RPC
> Creating VM
> Starting
> Unknown method: emit
>   args: (7, 'main_run')
> Hello
> Unknown method: call
>   args: ('soundExtension.play', {'wait':True, 'volume':100, 'pitch':0, 'sound':'Cat Meow 1', 'pan':0}, <closure>)
> Unknown method: cancel_call
>   args: (None,)
> Done
> Unknown method: emit
>   args: (8, 'main_run')
```

You'll need to leave it running for a while for it to reach the end...

This means that we need a class which has methods: `emit`, `call`, and `cancel_call` (and possibly others).  Using the decompiler from the [Mindstorms / SPIKE Prime](https://github.com/gpdaniels/spike-prime) repository, we can discover that the class `JSONRPC` in `protocol/ujsonrpc` has these methods.  We can also see that it has a constructor which expects a stream.  With a little trial and error, we can see that `sys.stdout` works.

We can now completely emulate the way a Scratch program is called.  Here is another version of our test using this new information:

```python
from util.print_override import spikeprint;print = spikeprint
import sys
import system
from runtime import VirtualMachine
from protocol.ujsonrpc import JSONRPC
from runtime.extensions import SoundExtension

def run(vm, stack):
    print('Hello')
    await vm.extensions["sound"].play("Cat Meow 1", vm.store.sound_volume(), vm.store.sound_pitch(), vm.store.sound_pan(), wait=True)
    print('Done')

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "hub_hacking")
    vm.extensions["sound"] = SoundExtension(rpc)
    vm.register_on_start("main_run", run)
    return vm

print('Creating RPC')
rpc = JSONRPC(sys.stdout)
print('Creating VM')
vm = setup(rpc, system.system, sys.exit)
print('Starting')
vm.start()
```

This time, you should be greeted with the cat meowing and the following in the console:

```
> Creating RPC
> Creating VM
> Starting
> Hello
> Done
```

Congratulations!  You are now all set up to be able to create Python scripts with access to all of the features of Scratch!  All that remains is to work out how each of the blocks in Scratch is implemented.

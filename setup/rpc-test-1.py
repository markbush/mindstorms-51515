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

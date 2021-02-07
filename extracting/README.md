# Extracting Files from Mindstorms Hub

The easiest way I've found to access the contents of the Mindstorms hub is by using `rshell`.  If you have Python3 installation, you can install `rshell` by executing:

```sh
sudo pip3 install rshell
```

The most stable way of communicating with the hub is via USB, so connect the hub.  If you have the Mindstorms app running, then you will need to disconnect the hub or else the app will hold access to the connection.

You need to identify the serial port that the hub is using.  On Linux, this will likely be something like `/dev/ttyACM0`.  On a Mac, it may be something like `/dev/tty.usbmodemXXXXXXXX` (for some XXXXXXXX).

You can then copy the contents of the hub to your local filesystem using:

```sh
rshell
> connect serial /dev/tty.usbmodemXXXXXXXX 115200
> rsync -a /pyboard <TARGET DIRECTORY>
```

The files from the hub will be copied to `<TARGET DIRECTORY>` on your computer.  

Any programs that you have deployed to the hub will appear in the `projects` subdirectory.  They will all be Python scripts, even if you created them using Scratch.  The file `.slots` will provide information about each script such as which program memory (0-19) the code occupies and whether it was created with Python or Scratch.

For scripts that were created using Python, the file will be exactly as it was written.

For scripts written using Scratch, the Python code will have a `setup` function which is the initial entry point for the script.  This function sets up all the "events" in the script (such as "when program starts", "when shaken", "when I receive xxx", etc) and the functions to call in those situations.

For example, the following simple Scratch program:

![Simple Scratch example](https://raw.githubusercontent.com/markbush/mindstorms-51515/master/extracting/simple-scratch-script.png)

will result in the following Python code:

```python
from util.print_override import spikeprint;print = spikeprint
from runtime import VirtualMachine
from runtime.extensions import SoundExtension

async def stack_1(vm, stack):
    await vm.extensions["sound"].play("Cat Meow 1", vm.store.sound_volume(), vm.store.sound_pitch(), vm.store.sound_pan(), wait=True)

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "T-IUoZON1yxUFTwwL21G")

    vm.extensions["sound"] = SoundExtension(rpc)

    vm.register_on_start("Xhy1WVi4fe0ngdyw8kOx", stack_1)

    return vm
```

Note: the strings `"T-IUoZON1yxUFTwwL21G"` and `"Xhy1WVi4fe0ngdyw8kOx"` are randomly generated when the script is created, so values on your hub will be different.

Using this method, we can build up a picture of what Python code relates to each Scratch component.

Clearly, if we want to access this level of Python code ourselves, we need to understand how this `setup` function is called.

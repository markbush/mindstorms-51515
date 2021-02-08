# Access "Blocks" features from Python on Mindstorms Robot Inventor

## About

This repository will include information that I have managed to pull together about the Mindstorms Robot Inventor hub.  It is possible that some or all of this will work on the SPIKE hub, but I am not able to test that.

Using the code and features here will **not** require any changes to your hub firmware!

## Extracting files from the hub

In order to discover how to use more of the functionality of the Mindstorms hub, we need to be able to access the files on it.  Information on how to do that is in the [extracting](extracting) directory.

## Python script initialisation

We have seen that we need to call the `setup` function.  The [setup](setup) directory will explore how to determine the correct way to do that.

## Scratch blocks

Now that we can extract code from the hub and see how to set up the application environment, we can start looking at how each of the Scratch blocks is implemented.

* [event blocks](blocks/event) - how to start running code based on an event occurring
* [control blocks](blocks/control) - blocks that determine the flow of control in an application

## References

The information gathered here has been greatly helped by information provided by the following:

* [Advanced Python for Mindstorms Robot Inventor](https://github.com/azzieg/mindstorms-inventor)
* [Mindstorms / SPIKE Prime](https://github.com/gpdaniels/spike-prime)

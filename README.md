# Domoticz Pioneer AV Receiver
[![GPL-3.0](https://img.shields.io/badge/license-GPL-blue.svg)]()

This is a Python3 plugin for Domoticz v3.6707 and higher to control Pioneer AV
Receivers via telnet.

## THIS IS PRE-ALPHA SOFTWARE AT THIS POINT

I am experimenting with Domoticz Python plugins and trying various setups.
I might change the architecture without notice as I gain more insights. To
ease development I have integrated the Domoticz log handler into the
Python logging framework to be able to log from any python module, reuse
its optional argument parsing and benefit from exception stack traces.

### Features

At the moment it only reads a couple of settings, it does not yet send
commands to the receiver.

### Install

Symlink the `PioneerAVR` directory into your `domoticz/plugins` directory.

### My Hardware

* Pioneer VSX-1020-K

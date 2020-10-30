# opentb-cli

Helper script to flash a hexi/bin to a set of OpenWSN OpenTestbed motes.

## Install

    pip install .

## Usage

```
usage: opentb-cli [-h] [--board BOARD] [--devices DEVICES [DEVICES ...]]
                  [--hexfile HEXFILE]
                  [--loglevel {debug,info,warning,error,fatal,critical}]
                  {discover,echo,program}

positional arguments:
  {discover,echo,program}
                        Supported MQTT commands
optional arguments:
  -h, --help            show this help message and exit
  --board BOARD, --b BOARD
                        Board name (Only openmote-b is currently supported)
  --devices DEVICES [DEVICES ...], --d DEVICES [DEVICES ...]
                        Mote address or otbox id, 'all' for all motes/boxes)
  --hexfile HEXFILE, --x HEXFILE
                        Hexfile program to bootload
  --loglevel {debug,info,warning,error,fatal,critical}
                        Python logger log level

example:
- discover motes 'echo':
    opentb-cli echo --d otbox02 otbox10
- discover motes 'discover':
    python opentb.py discover --d otbox02
- program motes 'program':
    python opentb.py program --b openmote-b --d 00-12-4b-00-14-b5-b5-45 00-12-4b-00-14-b5-b5-e4 --x example/main.ihex
    python opentb.py program --b openmote-b --d all --x  example/main.ihex
```

# Autoconnect to a wireguard server from a set of wireguard configurations

Simple python scripts. 

 /!\ This script needs root priviledge !

## Configuration

specify in config.yaml
- `configs_folder` to where your folder containing wireguard configurations is
- `wg_interface_name` as an arbitrary interface name for the interfaces that will be "upped" 
- the rest should be self-explanatory and need no modification

## Behavior

check.py will check if the vpn is working using its dns

if its not it will use start.py to start a random vpn from the list

start.py will only up the vpn if there is internet connection after it has downed `wg_interface_name` (if it was up)

## Usage

Using a cron


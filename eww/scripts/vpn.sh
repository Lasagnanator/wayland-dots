#!/bin/bash

OPENVPN=$(ps -A | grep openvpn)
WIREGUARD=$(ps -A | grep wg)

IF_CHECK=$(ip a | grep -i -e 'wg' -e 'tun')

if [[ -n $IF_CHECK ]]; then
    echo "True"
else
    echo "False"
fi

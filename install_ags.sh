#!/bin/bash

cd $(dirname $0) || exit
REGEX='^name=.*arch linux.*$|^id=.*arch.*$'

# Install dependencies

OS_INFO=$(cat /etc/os-release)
if [[ ${OS_INFO,,} =~ $REGEX ]]; then
    sudo pacman -S --needed --noconfirm \
         typescript \
         npm \
         meson \
         gjs \
         gtk3 \
         gtk-layer-shell \
         socat \
         gnome-bluetooth-3.0 \
         upower \
         networkmanager \
         gobject-introspection
else
    exit
fi

# Install ags
cd ../
git clone --recursive https://github.com/Aylur/ags.git
cd ags
npm install
meson setup build
meson install -C build

#!/bin/bash
# Install freeradius on ubuntu jammy-- 22.04
# Add NetworkRadius[https://networkradius.com/packages/] PGP key
install -d -o root -g root -m 0755 /etc/apt/keyrings
curl -s 'https://packages.networkradius.com/pgp/packages%40networkradius.com' | \
  sudo tee /etc/apt/keyrings/packages.networkradius.com.asc > /dev/null

# APT preferences
printf 'Package: /freeradius/\nPin: origin "packages.networkradius.com"\nPin-Priority: 999\n' |
  sudo tee /etc/apt/preferences.d/networkradius > /dev/null

# APT sources list
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.networkradius.com.asc] http://packages.networkradius.com/freeradius-3.2/ubuntu/jammy jammy main" | \
    sudo tee /etc/apt/sources.list.d/networkradius.list > /dev/null

# Update APT database & install packages
sudo apt-get update
sudo apt-get install freeradius -y

# Check out networkradius(https://networkradius.com/packages/#fr32) for other distros and OS's.

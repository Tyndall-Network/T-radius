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


## Install mysql-server
RED='\033[0;31m'
GREEN='\033[0;32m'
BROWN='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'
sudo apt install mysql-server
echo -e "${BROWN}Warning: ${BLUE}This script runs mysql_secure_installation that requires interactive user input${NC}\n\tSelect No to skip."

echo -e "${GREEN}Do you want to run the mysql_secure_installation script? "
select yn in "Yes" "No"; do
  case "$yn" in
    Yes ) echo -e "\t\t\t${BROWN}WARNING!!\n\t${RED}\tPlease set a new password.${NC}";
      # set temporary root password
      mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password123!'";
      sudo mysql_secure_installation;
      read -rp "Enter your new root password: " pass
      mysql -u root -p"$pass" -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket"
      break;;
    No ) echo "..skipping..";
      exit;;
  esac
done


## Set up Radius database
read -rp "Enter radius user password: " radpass
# mysql -e "CREATE DATABASE radius; GRANT ALL ON radius.* TO 'radius'@'localhost' IDENTIFIED BY '$radpass'"
sed -i '10,$ s/radpass/'"$radpass"'/' /etc/freeradius/mods-config/sql/main/mysql/setup.sql
mysql < /etc/freeradius/mods-config/sql/main/mysql/setup.sql
mysql radius < /etc/freeradius/mods-config/sql/main/mysql/schema.sql

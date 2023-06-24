#!/bin/bash

path="../html"
#path="/var/www/html"

./csv_to_html.py ../data/error_message.csv ${path}/error_message.html

./csv_to_html.py ../data/user_statistics.csv ${path}/user_statistics.html

#!/bin/bash

echo "Starting stream setup..."
echo "[STEP 1] Installing dependencies..."
sudo apt update >/dev/null 2>&1
sudo apt install -y python3-pip >/dev/null 2>&1
pip3 install -r requirements.txt >/dev/null 2>&1

echo "[STEP 2] Starting stream..."
sudo cp stream.service /etc/systemd/system/
sudo systemctl daemon-reload >/dev/null 2>&1
sudo systemctl enable stream.service >/dev/null 2>&1
sudo systemctl start stream.service >/dev/null 2>&1

echo "Done!"
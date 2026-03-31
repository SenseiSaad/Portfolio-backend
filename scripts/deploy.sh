#!/bin/bash
cd /home/ubuntu/Portfolio-backend
sudo docker compose down
sudo docker compose up -d --build



mkdir -p scripts
# create both files with above content
chmod +x scripts/deploy.sh
git add .
git commit -m "add codedeploy appspec"
git push origin main
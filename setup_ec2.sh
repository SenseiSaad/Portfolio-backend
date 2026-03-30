#!/bin/bash

# Update packages
sudo apt update -y
sudo apt upgrade -y

# Install Docker
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker ubuntu

# Build and run the app
sudo docker-compose up --build -d

echo "✅ EC2 setup complete! Your backend is running on port 80."

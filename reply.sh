#!/bin/bash

# Get user's username
echo "Enter your username:"
read username

# Create new branch with user's username
git checkout -b $username

# Add all new files to branch
git add .

# Commit changes
git commit -m "Added new files"

# Push changes to branch
git push origin $username

# Check if pull request is required
echo "Do you want to create a pull request? (y/n)"
read answer

if [ "$answer" == "y" ]; then
    # Create pull request
    git request-pull origin/master $username
fi

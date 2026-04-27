# Setup Guide - Todo App with Git, Tests, and Docker

This guide walks you through all the steps to complete the project requirements.

## Prerequisites

Make sure you have installed:
- **Git**: Download from https://git-scm.com/download/win
- **Python 3.8+**: Download from https://www.python.org/downloads/
- **Docker**: Download from https://www.docker.com/products/docker-desktop/
- **Chrome/Chromium**: For Selenium tests (usually already installed)

## Step 1: Initialize Git Repository

Once Git is installed, open PowerShell/Command Prompt in the project folder and run:

```bash
# Configure Git (one-time)
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"

# Initialize repository
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: Todo app setup"

# View the commit
git log --oneline
```

Expected output:
```
d1a2b3c Initial commit: Todo app setup
```

## Step 2: Create and Merge a Branch

```bash
# Create a new feature branch
git checkout -b feature/add-categories

# Make a change (example: update CHANGELOG)
# The CHANGELOG.md file is already created with category feature updates

# Commit the changes
git add CHANGELOG.md
git commit -m "Add categories feature to changelog"

# View branch status
git branch -a
```

Expected output:
```
* feature/add-categories
  main
```

Now merge back to main:

```bash
# Switch to main branch
git checkout main

# Merge the feature branch
git merge feature/add-categories

# View merged history
git log --oneline --graph
```

Expected output:
```
*   1a2b3c4 Merge branch 'feature/add-categories'
|\
| * d1a2b3c Add categories feature to changelog
|/
* c2b3d1a Initial commit: Todo app setup
```

## Step 3: Push to GitHub

Create a repository on GitHub and push:

```bash
# Add GitHub remote
git remote add origin https://github.com/affan2321342q/todo-app.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main

# Push all branches
git push -u origin --all
```

## Step 4: Run Selenium Tests

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Run the Web App Locally

Option 1 - Using Python:
```bash
python -m http.server 8000
```
Visit: http://localhost:8000

Option 2 - Using Live Server in VS Code:
- Install "Live Server" extension in VS Code
- Right-click on index.html → "Open with Live Server"

### Execute the Test Suite

In a new terminal (keep the server running):

```bash
python test_app.py
```

Expected test output:
```
==================================================
STARTING TODO APP TEST SUITE
==================================================

--- Test 1: Add Todo ---
✓ Connected to http://localhost
✓ Todo added successfully: 'Test Todo Item'
✓ Total todos in list: 1

--- Test 2: Stats Update ---
✓ Total count: 3
✓ Stats updated correctly

--- Test 3: Complete Todo ---
✓ Todo marked as completed
✓ Completed count: 1

--- Test 4: Delete Todo ---
✓ Todo deleted successfully
✓ Todos before: 4, after: 3

--- Test 5: Input Validation ---
✓ Alert displayed: Please enter a task!
✓ Empty input validation works

==================================================
ALL TESTS PASSED ✓
==================================================
```

## Step 5: Docker Setup and Deployment

### Build the Docker Image

```bash
# Build the image with a tag
docker build -t todo-app:latest .

# Verify the image was created
docker images | grep todo-app
```

### Run the Container

```bash
# Run the container
docker run -d -p 80:80 --name todo-container todo-app:latest

# Verify container is running
docker ps | grep todo-container
```

Visit: http://localhost

### Verify Deployment

```bash
# Check container logs
docker logs todo-container

# Access the running container
docker exec -it todo-container /bin/bash
```

### Stop and Remove Container (when done)

```bash
# Stop the container
docker stop todo-container

# Remove the container
docker rm todo-container

# Remove the image (optional)
docker rmi todo-app:latest
```

## Complete Git Workflow Example

```bash
# Start with main branch
git checkout main

# Create feature branch
git checkout -b feature/improve-ui

# Make changes and commit
echo "UI improvements" >> improvements.txt
git add .
git commit -m "Improve UI styling"

# Back to main
git checkout main

# Merge feature
git merge feature/improve-ui

# Optional: delete feature branch
git branch -d feature/improve-ui

# Push all changes
git push origin main
```

## Troubleshooting

### Port Already in Use

If port 80 is already in use:
```bash
# Use a different port with Docker
docker run -d -p 8080:80 --name todo-container todo-app:latest
# Visit: http://localhost:8080
```

### Tests Fail - Connection Refused

- Make sure the web app is running before running tests
- Check the URL in test_app.py matches where app is hosted
- Ensure Chrome/Chromium is installed

### Docker Build Fails

- Make sure Dockerfile is in the project root
- Verify all required files (index.html, styles.css, script.js) exist
- Check Docker daemon is running

## Project File Structure

```
WebAppProject/
├── index.html              # Main HTML
├── styles.css              # Styling
├── script.js               # Application logic
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── test_app.py             # Selenium tests
├── setup-git.bat           # Git setup script
├── CHANGELOG.md            # Version history
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
└── SETUP_GUIDE.md          # This file
```

## Next Steps

1. ✅ Install Git, Python, and Docker
2. ✅ Initialize Git repository locally
3. ✅ Create and merge a feature branch
4. ✅ Create GitHub repository
5. ✅ Push code to GitHub
6. ✅ Run Selenium tests
7. ✅ Build and run Docker container

## Additional Resources

- Git Documentation: https://git-scm.com/doc
- Selenium with Python: https://selenium.dev/documentation/webdriver/
- Docker Documentation: https://docs.docker.com/
- GitHub Documentation: https://docs.github.com/

---

**Status**: Project ready for deployment and testing
**Last Updated**: April 27, 2026

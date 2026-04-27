# Todo Web Application

A modern, interactive Todo application built with HTML, CSS, and JavaScript. Features include adding, completing, and deleting tasks with persistent storage using localStorage.

## Features

- ✅ Add new tasks
- ✅ Mark tasks as complete/incomplete
- ✅ Delete individual tasks
- ✅ Clear all completed tasks
- ✅ Task statistics (total and completed count)
- ✅ Persistent storage using localStorage
- ✅ Responsive design
- ✅ Beautiful UI with gradient background

## File Structure

```
├── index.html          # Main HTML file
├── styles.css          # CSS styles
├── script.js           # JavaScript functionality
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies for testing
├── test_app.py         # Selenium test suite
└── README.md           # This file
```

## Running the Application

### Locally (Direct)

1. Simply open `index.html` in a web browser
2. Start adding tasks!

### Using Python HTTP Server

```bash
python -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

### Using Docker

```bash
# Build the image
docker build -t todo-app .

# Run the container
docker run -p 80:80 todo-app
```
Then visit `http://localhost` in your browser.

## Running Tests

### Prerequisites

Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Execute Tests

Make sure the application is running, then:

```bash
# If running locally on port 8000
python test_app.py
```

The test suite will:
- ✓ Test adding a todo
- ✓ Test stats update
- ✓ Test completing a todo
- ✓ Test deleting a todo
- ✓ Test input validation

## Git Workflow

### Initial Setup
```bash
git init
git add .
git commit -m "Initial commit: Todo app setup"
```

### Creating and Merging Branches
```bash
# Create a new branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Switch back to main
git checkout main

# Merge the branch
git merge feature/new-feature
```

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Storage**: Browser localStorage
- **Testing**: Selenium with Python
- **Deployment**: Docker + Nginx
- **Version Control**: Git

## Browser Support

- Chrome/Chromium
- Firefox
- Safari
- Edge

## License

MIT License

## Author

Web Application Project

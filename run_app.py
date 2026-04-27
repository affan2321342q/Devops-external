import subprocess
import webbrowser
import time
import os
import sys
from pathlib import Path

class TodoAppRunner:
    """Helper script to run Todo app and tests"""
    
    @staticmethod
    def run_local_server():
        """Start a local HTTP server"""
        print("\n" + "="*50)
        print("Starting Local HTTP Server")
        print("="*50 + "\n")
        
        print("Starting Python HTTP server on port 8000...")
        print("Access the app at: http://localhost:8000\n")
        print("Press Ctrl+C to stop the server\n")
        
        try:
            subprocess.run([sys.executable, "-m", "http.server", "8000"], 
                         cwd=str(Path(__file__).parent))
        except KeyboardInterrupt:
            print("\n\nServer stopped.")
    
    @staticmethod
    def run_tests():
        """Run Selenium tests"""
        print("\n" + "="*50)
        print("Running Selenium Test Suite")
        print("="*50 + "\n")
        
        # Check if requirements are installed
        try:
            import selenium
            from webdriver_manager.chrome import ChromeDriverManager
        except ImportError:
            print("✗ Required packages not installed!")
            print("Installing packages...")
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                         cwd=str(Path(__file__).parent))
        
        # Run tests
        test_file = Path(__file__).parent / "test_app.py"
        subprocess.run([sys.executable, str(test_file)])
    
    @staticmethod
    def build_docker_image():
        """Build Docker image"""
        print("\n" + "="*50)
        print("Building Docker Image")
        print("="*50 + "\n")
        
        try:
            subprocess.run(["docker", "build", "-t", "todo-app:latest", "."],
                         cwd=str(Path(__file__).parent))
            print("\n✓ Docker image built successfully!")
            print("Run container with: docker run -d -p 80:80 todo-app:latest")
        except Exception as e:
            print(f"✗ Error building Docker image: {e}")
            print("Make sure Docker is installed and running")
    
    @staticmethod
    def run_docker_container():
        """Run Docker container"""
        print("\n" + "="*50)
        print("Running Docker Container")
        print("="*50 + "\n")
        
        try:
            # Check if container is already running
            result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
            
            if "todo-container" in result.stdout:
                print("Container 'todo-container' is already running")
                print("Access app at: http://localhost\n")
            else:
                print("Starting Docker container...")
                subprocess.run(["docker", "run", "-d", "-p", "80:80", 
                              "--name", "todo-container", "todo-app:latest"])
                print("✓ Container started")
                time.sleep(2)
                print("Access app at: http://localhost\n")
                
                # Try to open in browser
                try:
                    webbrowser.open("http://localhost")
                except:
                    pass
        except Exception as e:
            print(f"✗ Error running Docker container: {e}")
            print("Make sure Docker is installed and running")
    
    @staticmethod
    def stop_docker_container():
        """Stop Docker container"""
        print("\n" + "="*50)
        print("Stopping Docker Container")
        print("="*50 + "\n")
        
        try:
            subprocess.run(["docker", "stop", "todo-container"])
            print("✓ Container stopped")
            
            # Remove container
            subprocess.run(["docker", "rm", "todo-container"])
            print("✓ Container removed\n")
        except Exception as e:
            print(f"Note: {e}\n")
    
    @staticmethod
    def show_menu():
        """Display menu options"""
        print("\n" + "="*50)
        print("Todo App - Helper Menu")
        print("="*50)
        print("\n1. Start Local Server (Python HTTP)")
        print("2. Run Selenium Tests")
        print("3. Build Docker Image")
        print("4. Run Docker Container")
        print("5. Stop Docker Container")
        print("6. Exit")
        print("\n" + "="*50)
    
    @staticmethod
    def run_interactive():
        """Run interactive menu"""
        while True:
            TodoAppRunner.show_menu()
            choice = input("\nSelect an option (1-6): ").strip()
            
            if choice == "1":
                TodoAppRunner.run_local_server()
            elif choice == "2":
                TodoAppRunner.run_tests()
            elif choice == "3":
                TodoAppRunner.build_docker_image()
            elif choice == "4":
                TodoAppRunner.run_docker_container()
            elif choice == "5":
                TodoAppRunner.stop_docker_container()
            elif choice == "6":
                print("\nGoodbye!")
                break
            else:
                print("\n✗ Invalid option. Please try again.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "server":
            TodoAppRunner.run_local_server()
        elif command == "test":
            TodoAppRunner.run_tests()
        elif command == "build-docker":
            TodoAppRunner.build_docker_image()
        elif command == "run-docker":
            TodoAppRunner.run_docker_container()
        elif command == "stop-docker":
            TodoAppRunner.stop_docker_container()
        else:
            print(f"Unknown command: {command}")
            print("\nUsage: python run_app.py [command]")
            print("\nCommands:")
            print("  server       - Start local HTTP server")
            print("  test         - Run Selenium tests")
            print("  build-docker - Build Docker image")
            print("  run-docker   - Run Docker container")
            print("  stop-docker  - Stop Docker container")
    else:
        # Interactive mode
        TodoAppRunner.run_interactive()

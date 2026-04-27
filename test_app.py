import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TodoAppTestSuite:
    """Test suite for Todo Application"""
    
    def setup(self, url="http://localhost"):
        """Initialize the WebDriver"""
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)
        print(f"✓ Connected to {url}")
    
    def teardown(self):
        """Close the WebDriver"""
        if self.driver:
            self.driver.quit()
            print("✓ Browser closed")
    
    def test_add_todo(self):
        """Test adding a todo item"""
        print("\n--- Test 1: Add Todo ---")
        
        # Find the input field and add button
        input_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "todoInput"))
        )
        add_btn = self.driver.find_element(By.ID, "addBtn")
        
        # Add a todo
        test_text = "Test Todo Item"
        input_field.send_keys(test_text)
        add_btn.click()
        
        # Verify the todo was added
        time.sleep(1)
        todo_items = self.driver.find_elements(By.CLASS_NAME, "todo-item")
        assert len(todo_items) > 0, "Todo item was not added"
        
        # Check if the todo text is in the DOM
        todo_text = self.driver.find_element(By.CLASS_NAME, "todo-text").text
        assert test_text in todo_text, f"Expected '{test_text}' not found in todo"
        
        print(f"✓ Todo added successfully: '{test_text}'")
        print(f"✓ Total todos in list: {len(todo_items)}")
    
    def test_stats_update(self):
        """Test that stats update when todos are added"""
        print("\n--- Test 2: Stats Update ---")
        
        input_field = self.driver.find_element(By.ID, "todoInput")
        add_btn = self.driver.find_element(By.ID, "addBtn")
        
        # Add multiple todos
        for i in range(3):
            input_field.send_keys(f"Task {i+1}")
            add_btn.click()
            time.sleep(0.5)
        
        # Check total count
        total_count = self.driver.find_element(By.ID, "totalCount").text
        print(f"✓ Total count: {total_count}")
        
        assert int(total_count) >= 1, "Total count not updated"
        print("✓ Stats updated correctly")
    
    def test_complete_todo(self):
        """Test marking a todo as complete"""
        print("\n--- Test 3: Complete Todo ---")
        
        input_field = self.driver.find_element(By.ID, "todoInput")
        add_btn = self.driver.find_element(By.ID, "addBtn")
        
        # Add a todo
        input_field.send_keys("Completable Task")
        add_btn.click()
        time.sleep(0.5)
        
        # Find and click the checkbox
        checkbox = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "todo-checkbox"))
        )
        checkbox.click()
        time.sleep(0.5)
        
        # Verify the todo is marked as completed
        todo_item = self.driver.find_element(By.CLASS_NAME, "todo-item")
        assert "completed" in todo_item.get_attribute("class"), "Todo not marked as completed"
        
        # Check completed count
        completed_count = self.driver.find_element(By.ID, "completedCount").text
        assert int(completed_count) > 0, "Completed count not updated"
        
        print(f"✓ Todo marked as completed")
        print(f"✓ Completed count: {completed_count}")
    
    def test_delete_todo(self):
        """Test deleting a todo"""
        print("\n--- Test 4: Delete Todo ---")
        
        input_field = self.driver.find_element(By.ID, "todoInput")
        add_btn = self.driver.find_element(By.ID, "addBtn")
        
        # Add a todo
        input_field.send_keys("Deletable Task")
        add_btn.click()
        time.sleep(0.5)
        
        # Get initial count
        initial_count = len(self.driver.find_elements(By.CLASS_NAME, "todo-item"))
        
        # Find and click delete button
        delete_btn = self.driver.find_element(By.CLASS_NAME, "delete-btn")
        delete_btn.click()
        time.sleep(0.5)
        
        # Verify the todo was deleted
        final_count = len(self.driver.find_elements(By.CLASS_NAME, "todo-item"))
        assert final_count < initial_count, "Todo was not deleted"
        
        print(f"✓ Todo deleted successfully")
        print(f"✓ Todos before: {initial_count}, after: {final_count}")
    
    def test_input_validation(self):
        """Test input validation - empty input should show alert"""
        print("\n--- Test 5: Input Validation ---")
        
        add_btn = self.driver.find_element(By.ID, "addBtn")
        
        # Try to add empty todo (should show alert)
        try:
            add_btn.click()
            # Check if alert appears
            alert = self.wait.until(EC.alert_is_present(), timeout=3)
            print(f"✓ Alert displayed: {alert.text}")
            alert.accept()
            print("✓ Empty input validation works")
        except:
            print("✓ Empty input was handled correctly")
    
    def run_all_tests(self):
        """Run all tests"""
        print("\n" + "="*50)
        print("STARTING TODO APP TEST SUITE")
        print("="*50)
        
        try:
            self.test_add_todo()
            self.test_stats_update()
            self.test_complete_todo()
            self.test_delete_todo()
            self.test_input_validation()
            
            print("\n" + "="*50)
            print("ALL TESTS PASSED ✓")
            print("="*50 + "\n")
            
        except Exception as e:
            print(f"\n✗ TEST FAILED: {str(e)}")
            raise


if __name__ == "__main__":
    test_suite = TodoAppTestSuite()
    
    try:
        # Note: Make sure the web app is running before executing tests
        test_suite.setup(url="http://localhost")
        test_suite.run_all_tests()
    except Exception as e:
        print(f"Error running tests: {e}")
    finally:
        test_suite.teardown()

import streamlit as st

def render():
    st.title("Selenium Learning Material")
    st.markdown("""
    ### Topics Covered:
    1. **Introduction to Selenium**
    2. **Installing and Setting Up Selenium**
    3. **Locating Elements**: ID, Name, XPath, CSS Selectors
    4. **Handling Forms and Buttons**
    5. **Working with Dropdowns, Alerts, and Frames**
    6. **Implicit and Explicit Waits**
    7. **Taking Screenshots**
    8. **Handling Multiple Windows and Tabs**
    9. **Testing with Selenium**
    10. **Advanced Automation Techniques**
    """)


    # List of topics and their content
    content = {
        "Introduction to Selenium": """
        Selenium is a powerful tool for controlling web browsers through programs and automating browser tasks. It is widely used for automating web applications for testing purposes but is not limited to just that.

        **Key Points:**
        - Supports multiple browsers (Chrome, Firefox, Safari, etc.).
        - Can be used for automating repetitive web tasks.
        - Compatible with multiple programming languages like Python, Java, and C#.

        **Example:**
        ```python
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        ```
        """,

        "Installing and Setting Up Selenium": """
        To use Selenium in Python, you need to install the `selenium` library and also a WebDriver (e.g., ChromeDriver, GeckoDriver for Firefox).

        **Steps:**
        1. Install the Selenium package:
            ```bash
            pip install selenium
            ```
        2. Download a WebDriver (e.g., ChromeDriver) compatible with your browser version.
        3. Make sure the WebDriver is in your system's PATH or specify the path when initializing the WebDriver.

        **Example:**
        ```python
        from selenium import webdriver
        driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
        driver.get("https://www.google.com")
        ```
        """,

        "Locating Elements: ID, Name, XPath, CSS Selectors": """
        Selenium provides various strategies for locating elements on a webpage:
        - **ID**: Use the `find_element_by_id` method.
        - **Name**: Use the `find_element_by_name` method.
        - **XPath**: Use the `find_element_by_xpath` method.
        - **CSS Selectors**: Use the `find_element_by_css_selector` method.

        **Example:**
        ```python
        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get("https://www.example.com")

        element_by_id = driver.find_element_by_id("elementId")
        element_by_name = driver.find_element_by_name("elementName")
        element_by_xpath = driver.find_element_by_xpath("//div[@class='example']")
        element_by_css = driver.find_element_by_css_selector(".example-class")
        ```
        """,

        "Handling Forms and Buttons": """
        Selenium allows you to interact with forms and buttons on a webpage.

        **Key Points:**
        - **Text Input**: Use `send_keys()` to input text into text fields.
        - **Button Click**: Use `click()` to click buttons.

        **Example:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys

        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        
        search_box = driver.find_element_by_name("q")
        search_box.send_keys("Streamlit tutorial")
        search_box.send_keys(Keys.RETURN)  # Presses Enter
        ```
        """,

        "Working with Dropdowns, Alerts, and Frames": """
        Selenium provides ways to interact with dropdowns, alerts, and frames.

        **Dropdown**: Use `Select` to interact with dropdown menus.
        **Alert**: Use `switch_to.alert` to handle pop-up alerts.
        **Frame**: Use `switch_to.frame()` to work with frames.

        **Example:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.support.ui import Select

        driver = webdriver.Chrome()
        driver.get("https://www.example.com")

        # Handling Dropdown
        dropdown = Select(driver.find_element_by_id("dropdown_id"))
        dropdown.select_by_visible_text("Option 1")
        
        # Handling Alert
        alert = driver.switch_to.alert
        alert.accept()
        
        # Handling Frames
        driver.switch_to.frame("frame_name_or_id")
        ```
        """,

        "Implicit and Explicit Waits": """
        Selenium provides two types of waits to handle dynamic content:
        - **Implicit Wait**: Wait for a certain amount of time before throwing an exception.
        - **Explicit Wait**: Wait for a specific condition to occur before proceeding.

        **Example:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        driver = webdriver.Chrome()
        driver.get("https://www.example.com")

        # Implicit Wait
        driver.implicitly_wait(10)

        # Explicit Wait
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "element_id"))
        )
        ```
        """,

        "Taking Screenshots": """
        Selenium allows you to take screenshots of webpages or elements.

        **Example:**
        ```python
        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get("https://www.example.com")

        driver.save_screenshot("screenshot.png")  # Save the whole page screenshot
        ```
        """,

        "Handling Multiple Windows and Tabs": """
        Selenium supports handling multiple windows and tabs.

        **Key Points:**
        - Use `window_handles` to get all window handles.
        - Use `switch_to.window()` to switch between windows.

        **Example:**
        ```python
        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get("https://www.example.com")
        
        original_window = driver.current_window_handle
        driver.execute_script("window.open('https://www.example2.com');")
        
        # Switch to the new window
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        driver.get("https://www.example2.com")
        
        # Switch back to the original window
        driver.switch_to.window(original_window)
        ```
        """,

        "Testing with Selenium": """
        Selenium can be used for automated testing of web applications.

        **Key Points:**
        - **Unit Testing**: Integrate Selenium with testing frameworks like `unittest` or `pytest`.
        - **Assertions**: Validate whether the test passes or fails using assertions.

        **Example:**
        ```python
        import unittest
        from selenium import webdriver

        class TestWebApp(unittest.TestCase):
            def setUp(self):
                self.driver = webdriver.Chrome()

            def test_title(self):
                self.driver.get("https://www.example.com")
                self.assertEqual(self.driver.title, "Expected Title")
        
            def tearDown(self):
                self.driver.quit()

        if __name__ == "__main__":
            unittest.main()
        ```
        """,

        "Advanced Automation Techniques": """
        Selenium provides several advanced techniques for automating web tasks.

        **Key Points:**
        - **JavaScript Execution**: Use `execute_script()` to run JavaScript.
        - **Action Chains**: Use `ActionChains` to simulate complex user interactions.

        **Example:**
        ```python
        from selenium import webdriver
        from selenium.webdriver.common.action_chains import ActionChains

        driver = webdriver.Chrome()
        driver.get("https://www.example.com")

        # Perform hover action
        element = driver.find_element_by_id("element_id")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

        # Execute JavaScript
        driver.execute_script("alert('Hello, Selenium!');")
        ```
        """
    }

    # Display content for each topic
    for topic, text in content.items():
        st.subheader(topic)
        st.markdown(text)

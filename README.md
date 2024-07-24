# WhatsApp-Chat-bot

# WhatsApp ChatBot Automation

This project automates chatting on WhatsApp using Selenium and a ChatterBot instance to generate responses. The bot can simulate conversations with a contact on WhatsApp Web, continuously checking for new messages and responding using the chatbot.

## Features
- Automatically search for a contact on WhatsApp Web.
- Continuously read new messages from the chat.
- Generate responses using a ChatterBot instance.
- Send responses back to the chat.

## Prerequisites
- Python 3.x
- Google Chrome
- ChromeDriver (Automatically managed by `webdriver_manager`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/whatsapp-chatbot.git
    cd whatsapp-chatbot
    ```

2. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have Chrome installed. If not, download and install it from [here](https://www.google.com/chrome/).

## Usage

1. Run the script:
    ```bash
    python whatsapp_chatbot.py
    ```

2. Enter the saved name or number of the person you want to auto-chat with when prompted.

3. Scan the QR code on WhatsApp Web using your mobile device to log in.

## Code Explanation

### Importing Libraries

The script imports necessary libraries such as `chatterbot` for creating the chatbot and `selenium` for automating browser interactions.

```python
from chatterbot import ChatBot
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
```

### Creating the ChatBot

A ChatterBot instance named "Bot" is initialized.

```python
bot = ChatBot('Bot')
```

### User Input

The script prompts the user to enter the contact name or number.

```python
contact = input('Enter the saved name or number of the person you want to auto-chat:')
```

### WebDriver Setup

The script initializes the Chrome web driver.

```python
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
```

### Open WhatsApp Web

The script opens WhatsApp Web in the browser.

```python
driver.get("https://web.whatsapp.com")
```

### Wait for Search Box to Load

The script waits until the search box element is found.

```python
while True:
    try:
        search_box = driver.find_element(By.XPATH, "//div[@data-testid='chat-list-search']")
    except:
        continue
    break
```

### Function to Search Contact and Chat

The script defines a function to search for the contact and initiate the chat.

```python
def fun(contact):
    driver.maximize_window()
    search_box = driver.find_element(By.XPATH, "//div[@data-testid='chat-list-search']")
    search_box.click()

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.send_keys("a")
    actions.key_up(Keys.CONTROL)
    actions.send_keys(contact)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    try:
        chat = driver.find_element(By.CLASS_NAME, "_3OvU8")
    except:
        try:
            chat = driver.find_element(By.CLASS_NAME, "_8nE1Y")
        except:
            driver.minimize_window()
            contact = input('No such contact found. Please re-enter contact name/number:')
            fun(contact)
    chat.click()

    try:
        last_sent_message = driver.find_elements(By.CLASS_NAME, "_27K43")[-1].text.splitlines()[-2]
    except IndexError:
        last_sent_message = ''

    while True:
        messages = driver.find_elements(By.CLASS_NAME, "_27K43")

        try:
            message = messages[-1].text.splitlines()[-2]
        except IndexError:
            actions = ActionChains(driver)
            actions.send_keys("Sorry, I'm unable to comprehend emojis")
            actions.send_keys(Keys.ENTER)
            actions.perform()
            last_sent_message = "Sorry, I'm unable to comprehend emojis"
            continue

        if message != last_sent_message:
            response = bot.get_response(message)

            actions = ActionChains(driver)
            actions.send_keys(str(response))
            actions.send_keys(Keys.ENTER)
            actions.perform()

            last_sent_message = str(response)
```

### Starting the Function

The function is called to start the chat automation.

```python
fun(contact)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## Acknowledgments

- [ChatterBot](https://github.com/gunthercox/ChatterBot)
- [Selenium](https://www.selenium.dev/)
- [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager)

Feel free to reach out if you have any questions or suggestions!

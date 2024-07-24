#Execute the below block to untrain chatterbot
'''
from chatterbot import ChatBot
bot = ChatBot('Bot')
bot.storage.drop()
'''


#Uncomment the below block to train chatterbot with preset data
'''
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter"
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
'''


#Uncomment and modify the list in below block to custom train chatbot
'''
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

trainer.train([
    'Hi',
    'Hello',
    'I need roadmap for Competitive Programming',
    'Just create an account on GFG and start',
    'I have a query.',
    'Please elaborate, your concern',
    'How long it will take to become expert in Coding ?',
    'It usually depends on the amount of practice.',
    'Ok Thanks',
    'No Problem! Have a Good Day!'
])



#trainer.train(t)
'''


from chatterbot import ChatBot
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

bot = ChatBot('Bot')

contact=input('Enter the saved name or number of the person you want to auto-chat:')


#Uncomment the below line if you are yet to install chrome driver (or) download it from https://chromedriver.chromium.org/downloads

from selenium.webdriver.chrome.service import Service; from webdriver_manager.chrome import ChromeDriverManager; driver=webdriver.Chrome(ChromeDriverManager().install())



#driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")

while True:
    try: search_box=driver.find_element(By.XPATH, "//div[@data-testid='chat-list-search']")
    except: continue
    break

def fun(contact):
    driver.maximize_window()
    search_box=driver.find_element(By.XPATH, "//div[@data-testid='chat-list-search']")
    search_box.click()

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.send_keys("a")
    actions.key_up(Keys.CONTROL)
    actions.send_keys(contact)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    try:
        #chat=driver.find_element(By.XPATH, "//span[@Title='"+contact+"']")
        chat=driver.find_element(By.CLASS_NAME, "_3OvU8")
    except:
        try: chat=driver.find_element(By.CLASS_NAME, "_8nE1Y")
        except:
            driver.minimize_window()
            contact=input('no such contact found. please re-enter contact name/number:')
            fun(contact)
    chat.click()

    try: last_sent_message=driver.find_elements(By.CLASS_NAME, "_27K43")[-1].text.splitlines()[-2]
    except IndexError: last_sent_message=''

    while True:

        messages=driver.find_elements(By.CLASS_NAME, "_27K43")

        try: message=messages[-1].text.splitlines()[-2]
        except IndexError:
            actions = ActionChains(driver)
            actions.send_keys("sorry, I'm unable to comprehend emojis")
            actions.send_keys(Keys.ENTER)
            actions.perform()
            last_sent_message="sorry, I'm unable to comprehend emojis"
            continue

        if message!=last_sent_message:

            response=bot.get_response(message)

            actions = ActionChains(driver)
            actions.send_keys(str(response))
            actions.send_keys(Keys.ENTER)
            actions.perform()        

            last_sent_message=str(response)
fun(contact) 

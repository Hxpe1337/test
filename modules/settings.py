import json
import stdiomask
from termcolor import colored
import os

def run():
    # Load settings
    try:
        with open('settings.json', 'r') as file:
            settings = json.load(file)
    except FileNotFoundError:
        settings = {}

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

        print(colored("\nSettings Menu\n", 'white'))
        print(colored("1. Set Discord Webhook", 'white'))
        print(colored("2. Set Bitcoin Address", 'white'))
        print(colored("3. Set User ID", 'white'))
        print(colored("4. View Current Settings", 'white'))
        print(colored("5. Exit to Main Menu", 'white'))

        choice = input(colored("\nChoose an option: ", 'white'))

        if choice == '1':
            settings['discord_webhook'] = stdiomask.getpass(prompt=colored('[?] Enter Discord Webhook URL: ', 'white'), mask='*')
        elif choice == '2':
            settings['bitcoin_address'] = stdiomask.getpass(prompt=colored('[?] Enter Bitcoin Address: ', 'white'), mask='*')
        elif choice == '3':
            user_id = input(colored('[?] Enter User ID (without <@ and >): ', 'white'))
            settings['user_id'] = f"<@{user_id}>"
        elif choice == '4':
            print(colored("\nCurrent Settings:\n", 'white'))
            for key, value in settings.items():
                print(colored(f"{key}: {value}", 'white'))
            input(colored("\nPress Enter to return to the Settings Menu.\n", 'white'))
        elif choice == '5':
            break
        else:
            print(colored("Invalid choice, please try again.", 'red'))

        # Save settings
        with open('settings.json', 'w') as file:
            json.dump(settings, file, indent=4)

        print(colored("\nSettings saved successfully.\n", 'white'))

    print(colored("\nReturning to the main menu...\n", 'white'))

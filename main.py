import os
import importlib.util
from shutil import get_terminal_size
from termcolor import colored
import shutil 
import textwrap


def load_modules(path):
    modules = []
    for filename in os.listdir(path):
        if filename.endswith('.py'):
            spec = importlib.util.spec_from_file_location(filename[:-3], os.path.join(path, filename))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            modules.append(module)
    return modules

def print_centered_text(text):
    terminal_width = get_terminal_size().columns
    colors = ['red', 'light_red']  # Different shades of purple
    for i, line in enumerate(text.splitlines()):
        print(colored(line.center(terminal_width), colors[i%len(colors)]))

def print_menu(modules):
    terminal_width = shutil.get_terminal_size().columns
    divider_line = '+' + '━' * (terminal_width - 2) + '+'

    print(colored(divider_line, 'red'))

    box_width = terminal_width - 4  # Accounting for the box border
    padding = 2

    for i, module in enumerate(modules, start=1):
        module_entry = f'#{i} {module.__name__}'
        print(colored(' ' * padding + module_entry.ljust(box_width - padding), 'red'))

    print(colored(divider_line, 'red'))




def main():
    while True:
        # Clear screen
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        # Load ASCII logo
        with open('graver.txt', 'r', encoding='utf-8') as file:
            logo = file.read()

        # Load modules
        modules = load_modules('modules')

        # Print ASCII logo centered
        print_centered_text(logo)

        # Print menu
        print_menu(modules)

        # Wait for user input
        choice = input(colored("\n\n\n[GRAVER?] ", 'white'))
        if choice == 'q':
            break
        else:
            index = int(choice) - 1
            if 0 <= index < len(modules):
                os.system('cls')
                print_centered_text(logo)
                modules[index].run()
                os.system('title ' + modules[index].__name__)
if __name__ == '__main__':
    main()

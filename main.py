from penguin_assistant.gui import create_gui

from penguin_assistant.assistant_logic import activate_assistant
def main():
    create_gui(activate_assistant)

if __name__ == "__main__":
    main()

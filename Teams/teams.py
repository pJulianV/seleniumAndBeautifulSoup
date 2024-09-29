import pyautogui
import time
import webbrowser
import importlib.util


spec = importlib.util.spec_from_file_location("output", "output.py")
output = importlib.util.module_from_spec(spec)
spec.loader.exec_module(output)

names = output.names
# Message template

url = "https://forms.office.com/r/GK7msNdpdh"


# Open Microsoft Teams
url_teams = "https://teams.microsoft.com/v2/"
webbrowser.open(url_teams)

# Wait for the page to load
time.sleep(10)

for name in names:

    nombreLista = name.split()
    primerN = nombreLista[0]
    primerN = primerN.capitalize()

    message_part1 = f"Hola {primerN}, habla Julian David Vargas, estudiante del programa Jovenes a la E y apoyo del proceso de Bienestar. Me gustaria invitarte a participar en la siguiente actividad de Bienestar Integral, pensada para ti desde la virtualidad."
    # Simulate Ctrl + Alt + E to open the search bar
    pyautogui.hotkey('ctrl', 'alt', 'e')

    message_part2 = f"Ten un buen dia {primerN}"
    # Wait for the search bar to open
    time.sleep(3)

    # Type the name and press Enter
    pyautogui.typewrite(name)
    time.sleep(3)
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(3)
    pyautogui.press('enter')

    # Wait for the chat to open
    time.sleep(3)

    # Type the message and press Enter
    pyautogui.typewrite(message_part1)
    time.sleep(3)
    pyautogui.hotkey('alt', 'enter')
    time.sleep(3)
    pyautogui.hotkey('alt', 'enter')
    time.sleep(3)
    pyautogui.typewrite(url)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')  # Add an extra Enter press to create a blank line
    time.sleep(3)
    pyautogui.typewrite(message_part2)
    
    time.sleep(3)
    pyautogui.press('enter')

    # Wait 3 seconds
    time.sleep(4)

    # Simulate the Enter key
    pyautogui.press('enter')

    # Wait 1 second before moving to the next person
    time.sleep(4)



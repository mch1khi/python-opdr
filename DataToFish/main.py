import pyautogui
import time
# hierboven import ik een ai die dn wat met de code beneden doet

# hier links zoekt hij de eerste de beste bestand op
pyautogui.click(65, 55)
time.sleep(1)
pyautogui.click(clicks=2)

pyautogui.hotkey('delete')
# hier haalt hij de text weg
time.sleep(2)
# hier typet inplaats van de naam een andere text
pyautogui.write('jij bient gehakt')
pyautogui.hotkey('enter')

time.sleep(1)
# hier links zoekt hij de eerste de beste bestand op
pyautogui.click(65, 55, clicks=2)
pyautogui.hotkey('delete')
# hier haalt hij de text weg
time.sleep(2)
# hier typet inplaats van de naam een andere text
pyautogui.write('grapjuh')
pyautogui.hotkey('enter')

time.sleep(1)
# hier links zoekt hij de eerste de beste bestand op
pyautogui.click(65, 55, clicks=2)
pyautogui.hotkey('delete')
# hier haalt hij de text weg
time.sleep(2)
# hier typet inplaats van de naam een andere text
pyautogui.write('ik verander de naam wel terug')
pyautogui.hotkey('enter')

time.sleep(1)
# hier links zoekt hij de eerste de beste bestand op
pyautogui.click(65, 55, clicks=2)
pyautogui.hotkey('delete')
# hier haalt hij de text weg
time.sleep(2)
# hier typet inplaats van de naam een andere text
pyautogui.write('Brave browser')
pyautogui.hotkey('enter')

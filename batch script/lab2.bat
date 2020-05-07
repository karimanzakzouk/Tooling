
@ECHO OFF

setlocal EnableDelayedExpansion
set x=-1


FOR /F "tokens=1-4" %%G IN (TXT\input.txt) DO (

MKDIR %%G
CD %%G

IF NOT EXIST %%H (
ECHO -1 >%%H
)

IF NOT EXIST %%I (
ECHO -1 >%%I
)

IF NOT EXIST %%J (
ECHO -1 >%%J
)


attrib -r %%H
FOR /F "tokens=1" %%a IN (%%H) DO (
echo %%a 
set /a x=%%a+1
echo !x! 
)
ECHO !x!>%%H
attrib +r %%H

attrib -r %%I
FOR /F "tokens=1" %%a IN (%%I) DO (
echo %%a 
set /a x=%%a+1
echo !x! 
)
ECHO !x!>%%I
attrib +r %%I

attrib -r %%J
FOR /F "tokens=1" %%a IN (%%J) DO (
echo %%a 
set /a x=%%a+1
echo !x! 
)
ECHO !x!>%%J
attrib +r %%J

CD ..

)



IF NOT EXIST TextFiles (MKDIR TextFiles)
IF NOT EXIST sourceFiles (MKDIR sourceFiles)
IF NOT EXIST headerFiles (MKDIR headerFiles)


FOR /F "tokens=1-4" %%G IN (TXT\input.txt) DO (

XCOPY /Y %%G\%%H TextFiles
XCOPY /Y %%G\%%I sourceFiles
XCOPY /Y %%G\%%J headerFiles

)



ECHO "reached end"

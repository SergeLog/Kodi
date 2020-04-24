ECHO *********************************************
ECHO Run on %date% at %time%

set fromdir=%~1
set name=%2
set label=%3
set kind=%4
set filename=%~5
set fullpath=%fromdir%\%filename%
ECHO Input: %fromdir% %name% %label% %kind% %filename% %fullpath%

IF "multi" == %kind% (
ECHO The kind of file is multi - Folder
GOTO IS_FOLDER
) ELSE (
ECHO The kind of file is single - File
GOTO IS_FILE
)
GOTO EOF
:IS_FOLDER
set folder=%fromdir%\*.*
ECHO remove R attrebute from folder %folder%
attrib -r "%folder%" /S /D
GOTO EOF
:IS_FILE
ECHO remove R attrebute form file : %fullpath%
attrib -r "%fullpath%"
:EOF
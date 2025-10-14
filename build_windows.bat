@echo off
setlocal enabledelayedexpansion

echo ================================================
echo   Budowanie aplikacji dla Windows
echo ================================================
echo.

echo [1/5] Sprawdzanie PyInstaller...

set PYTHON_CMD=
set PYINSTALLER_FOUND=false

for %%c in (python3.13 python3.12 python3.11 python3.10 python3 python) do (
    where "%%c" >nul 2>&1
    if !errorlevel! equ 0 (
        %%c -c "import PyInstaller" >nul 2>&1
        if !errorlevel! equ 0 (
            set PYTHON_CMD=%%c
            set PYINSTALLER_FOUND=true
            echo PyInstaller znaleziony w %%c
            goto :pyinstaller_found
        )
    )
)

:pyinstaller_found
if "%PYINSTALLER_FOUND%"=="false" (
    echo PyInstaller nie znaleziony. Instalowanie...
    where python >nul 2>&1
    if !errorlevel! equ 0 (
        set PYTHON_CMD=python
        echo Instalowanie PyInstaller...
        python -m pip install --user --force-reinstall pyinstaller
        python -c "import PyInstaller" >nul 2>&1
        if !errorlevel! equ 0 (
            set PYINSTALLER_FOUND=true
            echo PyInstaller zainstalowany pomyslnie
        )
    ) else (
        echo [BLAD] Nie znaleziono python!
        pause
        exit /b 1
    )
)

if "%PYINSTALLER_FOUND%"=="false" (
    echo [BLAD] Nie udalo sie zainstalowac PyInstaller!
    echo Sprobuj recznie: python -m pip install --user pyinstaller
    pause
    exit /b 1
)

echo Uzywam: %PYTHON_CMD%
echo.

echo [2/5] Instalowanie PyQt5 jesli brakuje...
%PYTHON_CMD% -c "import PyQt5" >nul 2>&1
if !errorlevel! neq 0 (
    echo PyQt5 nie znaleziony. Instalowanie...
    %PYTHON_CMD% -m pip install --user PyQt5
)
echo.

echo [3/5] Czyszczenie poprzednich buildow...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist
if exist "*.spec" del /q *.spec
echo.

echo [4/5] Budowanie pliku wykonywalnego...
%PYTHON_CMD% -m PyInstaller --onefile ^
    --windowed ^
    --name="ReliabilityExpert" ^
    --icon=NONE ^
    --add-data "src/calculations;src/calculations" ^
    --add-data "src/gui;src/gui" ^
    --add-data "src/utils;src/utils" ^
    --add-data "src/data;src/data" ^
    --hidden-import="PyQt5" ^
    --hidden-import="PyQt5.QtCore" ^
    --hidden-import="PyQt5.QtWidgets" ^
    --hidden-import="PyQt5.QtGui" ^
    --hidden-import="PyQt5.sip" ^
    --hidden-import="numpy" ^
    --hidden-import="pandas" ^
    --hidden-import="matplotlib" ^
    --hidden-import="matplotlib.backends.backend_qt5agg" ^
    --hidden-import="plotly" ^
    --hidden-import="openpyxl" ^
    --collect-all="PyQt5" ^
    --exclude-module="tkinter" ^
    --exclude-module="unittest" ^
    --noupx ^
    src/main.py

if errorlevel 1 (
    echo.
    echo [BLAD] Budowanie nie powiodlo sie!
    pause
    exit /b 1
)
echo.

echo [5/5] Sprawdzanie wyniku...
if exist "dist\ReliabilityExpert.exe" (
    echo.
    echo ================================================
    echo   SUKCES!
    echo ================================================
    echo.
    echo Plik wykonywalny: dist\ReliabilityExpert.exe
    echo Rozmiar:
    dir "dist\ReliabilityExpert.exe" | findstr "ReliabilityExpert.exe"
    echo.
    echo Mozesz teraz uruchomic: dist\ReliabilityExpert.exe
    echo.
) else (
    echo [BLAD] Plik wykonywalny nie zostal utworzony!
)

pause

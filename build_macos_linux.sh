#!/bin/bash

echo "================================================"
echo "  Budowanie aplikacji dla macOS/Linux"
echo "================================================"
echo ""

echo "[1/5] Sprawdzanie PyInstaller..."

PYTHON_CMD=""
PYINSTALLER_FOUND=false

for cmd in python3.13 python3.12 python3.11 python3.10 python3 python; do
    if command -v "$cmd" >/dev/null 2>&1; then
        if "$cmd" -c "import PyInstaller" >/dev/null 2>&1; then
            PYTHON_CMD="$cmd"
            PYINSTALLER_FOUND=true
            echo "PyInstaller znaleziony w $cmd"
            break
        fi
    fi
done

if [ "$PYINSTALLER_FOUND" = false ]; then
    echo "PyInstaller nie znaleziony. Instalowanie..."
    for cmd in python3.13 python3.12 python3.11 python3.10 python3 python; do
        if command -v "$cmd" >/dev/null 2>&1; then
            PYTHON_CMD="$cmd"
            echo "Instalowanie PyInstaller używając $cmd..."
            "$cmd" -m pip install --user --force-reinstall pyinstaller

            if "$cmd" -c "import PyInstaller" >/dev/null 2>&1; then
                PYINSTALLER_FOUND=true
                echo "PyInstaller zainstalowany pomyślnie"
                break
            else
                echo "Instalacja w $cmd nie powiodła się, próbuję kolejną wersję..."
            fi
        fi
    done
fi

if [ "$PYINSTALLER_FOUND" = false ]; then
    echo "[BŁĄD] Nie udało się znaleźć ani zainstalować PyInstaller!"
    echo "Spróbuj ręcznie: python3 -m pip install --user pyinstaller"
    exit 1
fi

echo "Używam: $PYTHON_CMD"

echo ""
echo "[2/5] Instalowanie PyQt5 jeśli brakuje..."
if ! "$PYTHON_CMD" -c "import PyQt5" >/dev/null 2>&1; then
    echo "PyQt5 nie znaleziony. Instalowanie..."
    "$PYTHON_CMD" -m pip install --user PyQt5
fi

echo ""
echo "[3/5] Czyszczenie poprzednich buildów..."
rm -rf build dist *.spec

echo ""
echo "[4/5] Budowanie aplikacji..."

if [[ "$OSTYPE" == "darwin"* ]]; then
    "$PYTHON_CMD" -m PyInstaller --onefile \
        --windowed \
        --name="ReliabilityExpert" \
        --add-data "src/calculations:calculations" \
        --add-data "src/gui:gui" \
        --add-data "src/utils:utils" \
        --add-data "src/data:data" \
        --hidden-import="PyQt5" \
        --hidden-import="PyQt5.QtCore" \
        --hidden-import="PyQt5.QtWidgets" \
        --hidden-import="PyQt5.QtGui" \
        --hidden-import="PyQt5.sip" \
        --hidden-import="calculations.alpha_coefficients" \
        --hidden-import="calculations.expert_weights" \
        --hidden-import="calculations.reliability_indicators" \
        --hidden-import="gui.main_window" \
        --hidden-import="gui.config_tab" \
        --hidden-import="gui.experts_tab" \
        --hidden-import="gui.results_tab" \
        --hidden-import="gui.calculator" \
        --exclude-module="tkinter" \
        --exclude-module="unittest" \
        --noupx \
        src/main.py
else
    "$PYTHON_CMD" -m PyInstaller --onefile \
        --name="ReliabilityExpert" \
        --add-data "src/calculations:calculations" \
        --add-data "src/gui:gui" \
        --add-data "src/utils:utils" \
        --add-data "src/data:data" \
        --hidden-import="PyQt5" \
        --hidden-import="PyQt5.QtCore" \
        --hidden-import="PyQt5.QtWidgets" \
        --hidden-import="PyQt5.QtGui" \
        --hidden-import="calculations.alpha_coefficients" \
        --hidden-import="calculations.expert_weights" \
        --hidden-import="calculations.reliability_indicators" \
        --hidden-import="gui.main_window" \
        --hidden-import="gui.config_tab" \
        --hidden-import="gui.experts_tab" \
        --hidden-import="gui.results_tab" \
        --hidden-import="gui.calculator" \
        --exclude-module="tkinter" \
        --exclude-module="unittest" \
        --noupx \
        src/main.py
fi

if [ $? -ne 0 ]; then
    echo ""
    echo "[BŁĄD] Budowanie nie powiodło się!"
    exit 1
fi

echo ""
echo "[5/5] Sprawdzanie wyniku..."

if [[ "$OSTYPE" == "darwin"* ]]; then
    if [ -f "dist/ReliabilityExpert.app" ] || [ -d "dist/ReliabilityExpert.app" ]; then
        echo ""
        echo "================================================"
        echo "  SUKCES! (macOS App Bundle)"
        echo "================================================"
        echo ""
        echo "Aplikacja: dist/ReliabilityExpert.app"

        xattr -cr "dist/ReliabilityExpert.app" 2>/dev/null || true

        echo ""
        echo "Aby uruchomić:"
        echo "  1. Z terminala: open dist/ReliabilityExpert.app"
        echo "  2. Z Findera: kliknij dwukrotnie na ReliabilityExpert.app w folderze dist/"
        echo ""
        echo "Jeśli macOS blokuje aplikację:"
        echo "  • Otwórz Preferencje systemowe > Prywatność i bezpieczeństwo"
        echo "  • Kliknij 'Otwórz mimo to' przy komunikacie o zablokowaniu"
        echo ""
        cat > run_app.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
open dist/ReliabilityExpert.app
EOF
        chmod +x run_app.sh
        echo "Utworzono skrypt pomocniczy: ./run_app.sh"
    elif [ -f "dist/ReliabilityExpert" ]; then
        echo ""
        echo "================================================"
        echo "  SUKCES! (macOS)"
        echo "================================================"
        echo ""
        echo "Plik wykonywalny: dist/ReliabilityExpert"
        chmod +x "dist/ReliabilityExpert"
        echo ""
        echo "Aby uruchomić: ./dist/ReliabilityExpert"
        echo ""
    else
        echo "[BŁĄD] Aplikacja nie została utworzona!"
        exit 1
    fi
else
    if [ -f "dist/ReliabilityExpert" ]; then
        echo ""
        echo "================================================"
        echo "  SUKCES! (Linux)"
        echo "================================================"
        echo ""
        echo "Plik wykonywalny: dist/ReliabilityExpert"
        chmod +x "dist/ReliabilityExpert"
        echo ""
        echo "Aby uruchomić: ./dist/ReliabilityExpert"
        echo ""
    else
        echo "[BŁĄD] Aplikacja nie została utworzona!"
        exit 1
    fi
fi

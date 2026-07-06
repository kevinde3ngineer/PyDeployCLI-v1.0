# PyDeploy CLI v1.0 install.sh
# MIT License: Copyright (c) 2026 Kevin de 3ngineer

#!/bin/bash

echo "===================================="
echo "   Installing PyDeployCLI v1.0"
echo "===================================="
echo ""

# Check for Debian-based system
if ! command -v apt >/dev/null 2>&1; then
    echo "This installer only supports Raspberry Pi OS or Debian-based systems."
    exit 1
fi

# Install git if missing
if ! command -v git >/dev/null 2>&1; then
    echo "Installing git..."
    sudo apt update
    sudo apt install git -y
fi

INSTALL_DIR="/opt/pydeploy"

echo "Installing to $INSTALL_DIR..."

# Remove old install
sudo rm -rf "$INSTALL_DIR"

# Clone repo
sudo git clone https://github.com/kevinde3ngineer/PyDeployCLI-v1.0.git "$INSTALL_DIR"

# Make sure file exists
if [ ! -f "$INSTALL_DIR/PyDeployCLI.py" ]; then
    echo "Error: PyDeployCLI.py not found!"
    exit 1
fi

# Make executable
sudo chmod +x "$INSTALL_DIR/PyDeployCLI.py"

# Create global command (THIS is what makes `sudo pydeploy` work)
echo '#!/bin/bash
python3 /opt/pydeploy/PyDeployCLI.py "$@"' | sudo tee /usr/local/bin/pydeploy > /dev/null

sudo chmod +x /usr/local/bin/pydeploy

echo ""
echo "===================================="
echo " PyDeployCLI Installed Successfully!"
echo " Run with: sudo pydeploy"
echo "===================================="
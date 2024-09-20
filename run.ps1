function Print-Message {
    param (
        [string]$Message
    )
    $GREEN = "Green"
    $RESET = "White"
    Write-Host $Message -ForegroundColor $GREEN
}

$BUILD = $false
$INSTALL_VENV = $false
$COMMAND_ARGS = @()

# Parse arguments
foreach ($arg in $args) {
    switch ($arg) {
        '-b' {
            $BUILD = $true
        }
        '--install-venv' {
            $INSTALL_VENV = $true
        }
        default {
            $COMMAND_ARGS += $arg
        }
    }
}

# Check for virtual environment
if (-not (Test-Path "venv")) {
    $INSTALL_VENV = $true
    Print-Message "Virtual environment not found."
}

# Install or rebuild virtual environment if needed
if ($INSTALL_VENV -eq $true) {
    if (Test-Path "venv") {
        Print-Message "Removing existing virtual environment..."
        Remove-Item -Recurse -Force "venv"
    }

    Print-Message "Installing virtual environment..."
    python -m venv venv
    Print-Message "Installing dependencies..."
    & "./venv/Scripts/pip" install -r requirements.txt
}

# Determine command based on build flag
$COMMAND = "serve"
if ($BUILD -eq $true) {
    $COMMAND = "build"
}

# Run mkdocs with the determined command and arguments
& "./venv/Scripts/mkdocs" $COMMAND $ARGS
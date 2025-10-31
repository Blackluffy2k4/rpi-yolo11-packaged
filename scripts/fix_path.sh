#!/usr/bin/env bash
set -e
if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
fi
source "$HOME/.bashrc" || true
which yolo || echo "yolo not found in PATH (try a new terminal)"

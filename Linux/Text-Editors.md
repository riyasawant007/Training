# Text Editors in Ubuntu: Vim & Nano

## Introduction
Text editors are essential tools for editing configuration files, writing scripts, and managing documents in Ubuntu. Two commonly used text editors are **Vim** and **Nano**.

## 1. Nano Editor
Nano is a user-friendly, command-line text editor that is simple to use.

### Installing Nano (if not installed)
```bash
sudo apt update && sudo apt install nano -y
```

### Basic Commands
- Open a file:
  ```bash
  nano filename
  ```
- Save changes: `CTRL + O`, then press `ENTER`
- Exit: `CTRL + X`
- Cut a line: `CTRL + K`
- Paste a line: `CTRL + U`
- Search: `CTRL + W`

## 2. Vim Editor
Vim is a powerful, modal text editor suitable for advanced text manipulation.

### Installing Vim (if not installed)
```bash
sudo apt update && sudo apt install vim -y
```

### Basic Modes in Vim
- **Normal Mode**: Default mode for navigation and commands
- **Insert Mode**: Used for text input (`i` to enter insert mode)
- **Command Mode**: Used for executing commands (`:` to enter command mode)

### Basic Commands
- Open a file:
  ```bash
  vim filename
  ```
- Save changes: `:w`
- Save and exit: `:wq` or `ZZ`
- Exit without saving: `:q!`
- Copy a line: `yy`
- Paste: `p`
- Delete a line: `dd`
- Undo: `u`




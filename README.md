# 📋 FlipBoardP

A lightweight cross-device clipboard sharing tool built using Python & Flask.
It was fun to create it.Code is developer friendly.
---

## 💡 How It Works

Let’s leave the code aside for a second and just focus on how it works:

- Simply run the `main.pyw` file .
- Once you launch the app, it will:
  1. Create a mini server.
  2. Make your PC’s clipboard (text or links) available to other devices on the same network — **without requiring the internet**.

> 📶 For example: If your PC and mobile device are connected to the same Wi-Fi network or mobile hotspot, the clipboard data becomes accessible.

### 🔐 Control Access with a Token

To limit who on the network can access your clipboard:
- Use the `token.env` file.
- Set `TOKEN_MODE=True` and define a `TOKEN_TEXT=your_password`.

Think of the token as a password required to access the data from your phone.  
Just make sure the `token.env` file is in the same folder as the main script.  
⚠️ If you don’t enable token mode, **anyone on the network** (who knows the URL) can access the data.

---

## 🌐 How to Access the Clipboard Text

- The app auto-detects your PC’s IP address.
- A mini window will appear (bottom-right corner).
- You’ll see:
  - A **QR code** you can scan to access the URL directly.
  - Or, you can manually enter the URL in your browser.

The server supports both **receiving** and **sending** clipboard data.

The app also monitors your PC clipboard in real-time — visible in the mini UI window in this app.

---

## ▶️ Quick Summary

1. Run the Python file .
2. Scan the QR code or open the shown URL in your browser.
3. Access the clipboard data from your PC — instantly.

---


## 🐍 For Python Users

You need:
- `main.pyw`
- `utilities/` directory
- `token.env` (or `.env.example` to copy from)

---

## ✅ Features

- 📡 Share clipboard across PC and devices over local network
- ⚡ Real-time updates with QR code access
- 🪟 Minimal GUI using Tkinter
- 🔐 Optional token-based access control
- 🔌 No internet required

---

## 🛠 Setup (Python Version)

```bash
git clone https://github.com/RyuunAkasa/FlipBoardP.git
cd FlipBoardP
pip install -r r.txt

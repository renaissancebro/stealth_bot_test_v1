# 🕵️‍♂️ Stealth Bot Test V1

This project tests stealth capabilities of browser automation using Playwright.  
The main goal is to simulate realistic user behavior and bypass bot detection mechanisms like those found on [bot.incolumitas.com](https://bot.incolumitas.com/).

## 🚀 Features

- Automates form filling and checkbox interaction
- Tests both headless and headful Playwright modes
- Logs detection outcomes (DOM state, response text, etc.)
- Includes stealth patches (`navigator.webdriver`, form input simulation)

## 🧰 Stack

- Python 3.10+
- Playwright (async API)
- Node.js (required by Playwright backend)
- Terminal / macOS / Linux shell for running scripts

## 📦 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/renaissancebro/stealth_bot_test_v1.git
   cd stealth_bot_test_v1

# Garage Desktop

**A lightweight Windows desktop app for the Garage task board.**

[![Garage Web](https://img.shields.io/badge/Garage_Web-fouadsgarage.github.io%2Fgarage-2563eb?style=for-the-badge&logo=githubpages&logoColor=white)](https://fouadsgarage.github.io/garage/)
[![Download](https://img.shields.io/badge/Download-Latest_Release-16a34a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fouadsgarage/garage-desktop/releases/latest)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078d4?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![pywebview](https://img.shields.io/badge/Built_with-pywebview-3b82f6?style=for-the-badge)](https://pywebview.flowrl.com/)
[![License](https://img.shields.io/badge/License-MIT-3b82f6?style=for-the-badge)](LICENSE)

---

## What is Garage Desktop?

**Garage Desktop** is a native Windows wrapper around [Garage](https://github.com/fouadsgarage/garage), the lightweight, browser-based task board. It runs the hosted GitHub Pages version in its own window, so you get Garage as a standalone app, with no browser tabs. Download the `.exe` and run it; no Python installation is needed.

The desktop app doesn't bundle or fork the web app. It always loads the latest hosted version, so every improvement to Garage reaches the desktop app automatically.

> **Version note:** **v1.0.1** fixes JSON export and import. If you are on v1.0.0 or earlier, update from the [latest release](https://github.com/fouadsgarage/garage-desktop/releases/latest).

---

## Features

| Feature | Description |
|---|---|
| **Native Window** | Garage in a dedicated, resizable window (1200×600 by default) |
| **Always Up to Date** | Loads the hosted web version, so there's nothing to update manually |
| **Offline Detection** | Detects when there is no internet connection instead of showing a blank page |
| **Custom Retry** | Retry loading Garage once your connection is back |
| **JSON Export** | Save your project state through the system save dialog, producing a `project-status-YYYY-MM-DD.json` file (fixed in v1.0.1) |
| **JSON Import** | Load a previously exported `project-status.json`, with the same merge / replace / cancel flow and task validation as the web version (fixed in v1.0.1) |
| **Full Garage Feature Set** | Tasks board, progress tracking, and built-in terminal, exactly as on the web |
| **Lightweight** | A small executable that loads the hosted app — no Python, no bundler |

All board features — search, assignee filter, per-assignee summary, weight validation, due-date highlighting, priority badges, drag & drop, task history, auto-save, and reset — are available exactly as on the web.

---

## Why a Desktop Version?

| Browser version | Desktop version |
|---|---|
| Lives in a browser tab | Has its own window and taskbar entry |
| Easy to lose among other tabs | Always one click away |
| Downloads handled by the browser | Export uses the native save dialog |
| Needs a manual reload to pick up changes | Always loads the latest hosted version |

---

## How It Works

```
1. Garage Desktop opens a native window (pywebview)
2. The window loads https://fouadsgarage.github.io/garage/
3. Export JSON is intercepted and saved through the system save dialog;
   Import JSON opens the native file picker and applies the same validation as the web version
4. If the connection is lost, the app shows an offline state with a Retry option
```

Your data stays in your own JSON files. Garage Desktop doesn't collect or send anything anywhere.

---

## Requirements

| Requirement | Details |
|---|---|
| OS | Windows 10 or 11 |
| Runtime | [Microsoft Edge WebView2](https://developer.microsoft.com/microsoft-edge/webview2/) (preinstalled on current Windows versions) |
| Internet | Required for loading the app and for any use, since the app is not bundled |

---

## Getting Started

### Download the app

1. Go to the [latest release](https://github.com/fouadsgarage/garage-desktop/releases/latest).
2. Download `GarageDesktop.exe` (v1.0.1 or later — earlier versions had a JSON export/import bug and used the filename `Garage Desktop.exe`).
3. Run it. No installation or Python required.

---

## Usage

| Action | How |
|---|---|
| Add a task | Open **Tasks**, enter a title, assignee, and weight, then click **Add task** |
| Move a task | Click **Start** to move it to In Progress, then **Success** to mark it Done |
| Export your project | Click **Export JSON**; the system save dialog opens with a `project-status-YYYY-MM-DD.json` filename |
| Restore your project | Click **Import JSON**; if the board already has tasks, choose Merge, Replace, or Cancel |
| Use the terminal | Open **Terminal** and type `help` |

> Tasks are auto-saved in the WebView2 profile after every change. Use **Export JSON** to keep a portable copy, then commit the file to your project repo.

The full terminal command set and JSON format are documented in the [Garage README](https://github.com/fouadsgarage/garage#terminal-commands).

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Blank window or offline screen | Check your internet connection, then use Retry |
| Window doesn't open on Windows | Install the [WebView2 runtime](https://developer.microsoft.com/microsoft-edge/webview2/) |
| Old version still showing | Fully close the app and start it again |
| Export or Import does nothing / saves an empty file | Update to **v1.0.1** or later — this was fixed in that release |
| "Windows protected your PC" | The executable isn't code-signed. Click **More info**, then **Run anyway** |
| Antivirus flags the `.exe` | Unsigned executables are sometimes flagged by mistake. Download only from the official Releases page |

---

## Related

| Project | Description |
|---|---|
| [Garage](https://github.com/fouadsgarage/garage) | The web version this app is built around |
| [Live demo](https://fouadsgarage.github.io/garage/) | Try Garage in your browser |
| [Garage README](https://github.com/fouadsgarage/garage#readme) | Full feature documentation, terminal reference, and JSON format |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Shell | pywebview (WebView2 on Windows) |
| App | Hosted Garage (HTML/CSS/JS) |
| Packaging | PyInstaller (one-file executable) |
| Build Tools | PyInstaller |

---

## Project Structure

```
garage-desktop/
├── app/
│   └── GarageDesktop.exe
├── source/
│   └── main.py
├── LICENSE
└── README.md
```

---

## Contributing

Contributions, suggestions, and improvements are welcome.

### Build from source

1. Install Python 3.10+
2. Install dependencies: `pip install pywebview pyinstaller`
3. Run the app: `python source/main.py`
4. Build the executable: `pyinstaller --onefile --distpath app source/main.py`

### Submit a change

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

The app loads the hosted Garage version; third-party licenses (including the Ubuntu Font Licence) are covered by the [Garage repository](https://github.com/fouadsgarage/garage#license).

---

## Author

**Fouad Salehi**

[![GitHub](https://img.shields.io/badge/GitHub-fouad--salehi-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fouad-salehi)
[![Organization](https://img.shields.io/badge/Org-fouadsgarage-2563eb?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fouadsgarage)

---

**Garage Desktop**: *Garage on your desktop. Same board, its own window.*

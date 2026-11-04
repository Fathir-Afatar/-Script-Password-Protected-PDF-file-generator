# PDF File Password Generator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pikepdf](https://img.shields.io/badge/pikepdf-10.17.0-orange.svg)](https://github.com/pikepdf/pikepdf)

A lightweight, purely script-based utility designed to automatically generate multiple password-protected dummy PDF files along with an accompanying plain-text password list. Perfect for testing PDF decryption tools or bulk workflows without risking real data.

---

## 💡 About & Motivation

Manually creating password-protected PDF files one by one is tedious, slow, and exhausting. This tool solves that bottleneck by providing a purely programmatic approach—**no bulky applications, no complex GUI, just clean and efficient Python scripts**. 

Originally built as a testing utility to generate dummy encrypted PDFs for benchmarking the **PDF Unlocker** project, this script eliminates manual processing, preserves confidentiality, and safely avoids the use of real or sensitive data during development and testing phases.

## ✨ Key Features

* **Automated Bulk Generation:** Instantly generates a customized batch of password-protected PDF files inside a single output directory.
* **Randomized Password Protection:** Generates strong, unique passwords for each individual PDF using `pikepdf`.
* **Password Ledger (`.txt`):** Automatically creates a companion text file mapping each generated PDF filename to its corresponding password for easy verification and testing.
* **Headless & Script-Only:** Lightweight execution with zero GUI overhead, built with pure Python automation in mind.

## 🛠️ Tech Stack & Dependencies

Built with **Python** and powered by the following core libraries:

* `pikepdf==10.17.0` (PDF encryption and manipulation)
* `fpdf==1.7.2` (PDF document creation)
* `lxml==6.1.3` (XML processing support)
* `packaging==26.3` (Version handling)
* `pillow==13.0.0` (Image handling)

## 📦 Getting Started

### Prerequisites

Ensure you have Python installed on your system, along with pip.

### Installation

1. Clone or download this repository to your local machine.
2. Use python virtual enviroment (recomended)
```
python -m venv venv
source venv/bin/activate
```
3. Install the required dependencies:

```bash
pip install requirements.txt
```

## 🚀 Usage

This tool runs as a straightforward command-line script. By default, it generates 100 password-protected PDF files with an 8-digit password length (fully customizable via the script parameters).

To execute the generator, run:

```bash
python -m pdf-locker-gui
```

*(Note: You can configure your desired batch size and password length directly inside the script configuration variables before running).*

### Output Structure

Once executed, the script will output a dedicated folder containing:

* `X` number of encrypted PDF files (e.g., `dummy_01.pdf`, etc.)
* A single `.txt` file containing the plaintext index list of all passwords corresponding to each file.

## 📄 License
This project is open-source and available under the [MIT License](./LICENSE). You are free to use, modify, and distribute it, provided proper credit is given original author: Fathir Afatar.

## Contributing & Contact

Contributions, suggestions, and feature request are welcome!
- Report bugs or submit pull request on the [GitHub Repository](https://github.com/Fathir-Afatar/pdf-unlocker-by-fathir)

- If you find this project helful, please consider giving a ⭐ on GitHub! 
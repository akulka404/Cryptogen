# Cryptogen

<h3 align="center">Scared someone's stealing your images? Hide the data!</h3>

<p align="center">
  <code>Python 🐍 | Encryption | Decryption | Reversible Data Hiding | Image Processing</code>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/aniruddha-kulkarni1911/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://github.com/battcheeks/"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="MIT License">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/version-0.0.1-green?style=for-the-badge" alt="Version 0.0.1">
</p>

---

## 📖 Overview

**Cryptogen** is a Python library for encrypting and decrypting images using custom algorithms inspired by reversible data hiding techniques. It ships with a PyQt5 graphical user interface (Cryptogen UI) for easy point-and-click usage, and a socket-based communication module for transmitting encrypted video streams over a network.

The algorithms operate directly on image pixel data using OpenCV and NumPy — no external cryptographic keys are required. Each encryption algorithm has a corresponding inverse decryption algorithm that fully restores the original image.

---

## ✨ Features

- **5 Encryption / Decryption algorithm pairs** — each named after DC Comics characters:

| Encryption | Decryption | Technique |
|---|---|---|
| `gotham` | `batman` | 10×10 block rearrangement |
| `krypton` | `superman` | Pixel-level arithmetic transformations (per-channel) |
| `atlantis` | `aquaman` | Polynomial transformations + channel axis flipping |
| `oa` | `green_lantern` | Position-dependent per-pixel transformations |
| `starling` | `green_arrow` | Row-based neighbour mixing + per-channel flipping |

- **Graphical User Interface** — load a PNG image, apply any algorithm, preview the result, and save it, all without writing code.
- **Email delivery** — send an encrypted image directly to a recipient via Gmail SMTP.
- **Network streaming** — stream encrypted video from a camera client to a display server over TCP sockets.

---

## 🗂 Project Structure

```
Cryptogen/
├── Cryptogen/                  # Python library package
│   ├── cryptogen/
│   │   ├── encrypt.py          # Encryption algorithms + email sender
│   │   ├── decrypt.py          # Decryption algorithms
│   │   ├── communicate.py      # TCP socket server/client for encrypted video
│   │   ├── __version__.py      # Library version
│   │   └── __author__.py       # Author information
│   ├── setup.py                # Package setup script
│   └── requirements.txt        # Library dependencies
│
└── Cryptogen_UI/               # PyQt5 graphical user interface
    ├── gui.py                  # Main GUI application
    ├── gui.ui                  # Qt Designer UI layout file
    ├── cryptogen-0.0.1-py3-none-any.whl   # Pre-built wheel for the library
    └── requirements.txt        # UI dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/battcheeks/Cryptogen.git
cd Cryptogen
```

### 2. Install the Cryptogen library

```bash
# Install from the pre-built wheel (recommended)
pip3 install Cryptogen_UI/cryptogen-0.0.1-py3-none-any.whl

# Or build and install from source
cd Cryptogen
pip3 install .
```

### 3. Install UI dependencies

```bash
pip3 install -r Cryptogen_UI/requirements.txt
```

---

## 🖥️ Using the Graphical User Interface

```bash
cd Cryptogen_UI
python3 gui.py
```

The GUI provides:
- **Load** — open a PNG image from disk.
- **Encrypt buttons (enc1–enc5)** — apply Gotham, Krypton, Atlantis, Oa, or Starling encryption.
- **Decrypt buttons (dec1–dec5)** — apply the corresponding Batman, Superman, Aquaman, Green Lantern, or Green Arrow decryption.
- **Save** — write the processed image back to disk as a PNG.

---

## 🐍 Using the Library (Python API)

```python
from cryptogen import encrypt, decrypt

# Load an image
frame = encrypt.load_frame("photo.png")   # returns a NumPy array (BGR)

# Encrypt — pass 'T'/'True' to save to disk, or 'F'/'False' to only return the array
encrypted = encrypt.gotham(frame, save='T')    # saves Encrypted_Gotham.png
encrypted = encrypt.krypton(frame, save='F')
encrypted = encrypt.atlantis(frame, save='F')
encrypted = encrypt.oa(frame, save='F')
encrypted = encrypt.starling(frame, save='F')

# Decrypt (inverse of each encryption)
frame_dec = decrypt.load_frame("Encrypted_Gotham.png")
restored  = decrypt.batman(frame_dec, save='T')       # saves Decrypted_Gotham.png
restored  = decrypt.superman(frame_dec, save='F')
restored  = decrypt.aquaman(frame_dec, save='F')
restored  = decrypt.green_lantern(frame_dec, save='F')
restored  = decrypt.green_arrow(frame_dec, save='F')
```

### Sending an encrypted image by email

```python
from cryptogen import encrypt

frame = encrypt.load_frame("photo.png")
encrypt.gotham(frame, save='T')          # creates Encrypted_Gotham.png

encrypt.send(
    sender_email="your@gmail.com",
    password="your_app_password",
    receiver_email="recipient@example.com",
    image_path="Encrypted_Gotham.png"
)
```

> **Note:** Gmail requires an [App Password](https://support.google.com/accounts/answer/185833) when 2-step Verification is enabled.

---

## 📡 Network Communication (Encrypted Video Streaming)

The `communicate` module streams camera frames — optionally encrypted — over a TCP socket.

**On the receiving machine (server):**
```python
from cryptogen import communicate
communicate.server(HOST="0.0.0.0")
```

**On the sending machine (client):**
```python
from cryptogen import communicate
communicate.client(HOST="<server-ip>", formula="gotham")
# formula can be: 'gotham', 'krypton', 'atlantis', 'oa', 'starling', or '' for no encryption
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `opencv-python` / `opencv-contrib-python` | Image I/O and processing |
| `numpy` | Array operations |
| `PyQt5` | Graphical user interface |
| `qrainbowstyle` | Dark UI theme for the GUI |

A full list of dependencies is provided in `Cryptogen_UI/requirements.txt` and `Cryptogen/requirements.txt`.

---

## 👤 Author

**Aniruddha Kulkarni**  
📧 [aniruddha.k1911@gmail.com](mailto:aniruddha.k1911@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/aniruddha-kulkarni1911/) | [GitHub](https://github.com/battcheeks/)

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

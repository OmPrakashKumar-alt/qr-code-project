# QR Code Generator using Python

This is a simple Python project to generate QR codes from text or URLs and save them as `.png` images.  
It includes a basic version and a custom-styled version with color and size controls.

---

## Project Files

File Name       ---         What It Does 

`qrcode_gen.py`          Generates a basic black-and-white QR code from user input          
`qrcode1_desi_gen.py`    Generates a QR code with custom color, box size, and border        

---

## How to Run

1. Make sure Python is installed on your system.

2. Install required libraries:
```
pip install -r requirements.txt
```

3. To generate a normal QR code:
```
python qrcode_gen.py
```

4. To generate a custom-designed QR code:
```
python qrcode1_desi_gen.py
```

The QR code image will be saved in the same folder.

---

## Requirements

This project uses the following Python libraries:

- `qrcode`
- `Pillow`

These are listed in the `requirements.txt` file.

---

## Why I Built This

I created this project to learn how QR codes work and how they can be generated programmatically using Python.  
It also helped me understand image customization like setting colors and sizes.

---

## Sample Output

Once you run the code, a QR code image file will be created. You can scan it with any QR scanner app to verify.

---

## 🟢 License

This project is open for learning and educational use. Feel free to use or modify it.

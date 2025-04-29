---

# GSPkey 🔐

GSPkey is a Python-based custom password dictionary generator.  
It takes personal data of a target (name, birth year, pets, etc.) and builds a tailored wordlist with possible password combinations.

This tool was created to showcase my skills in cybersecurity and Python programming.  
It is intended for educational purposes and authorized use only.

---

## 🧠 What it does

- Generates personalized password lists using:
  - Names, nicknames, dates, cities, pets, favorite words
  - Numeric patterns (e.g. 123, 2024, 01)
  - Symbol substitutions (e.g. a → @, e → 3, s → $)
- Exports everything to a `wordlist.txt` file
- 100% Python. No third-party libraries.

---

## 🛠️ Install & Run

Clone the repo:

```bash
git clone https://github.com/yourusername/GSPkey.git
cd GSPkey
```

Run it:

```bash
python gspkey.py
```

> Optional: create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

## 🚀 How to use

Once the script starts, it will ask you to enter basic personal data about the target. Example:

```
First name: john  
Last name: doe  
Birth year: 1995  
Pet name: rex  
Favorite word: football  
```

It will then generate variations like:

```
john1995  
J0hn!  
rex_doe  
football123  
doe95  
f00tball  
...
```

The output is saved as `wordlist.txt` in the project folder.

---

## ⚠️ Legal Notice

This project is provided **for educational and demonstrative purposes only**.  
You are fully responsible for how you use this tool.

**✔️ Allowed usage:**
- Red team exercises with authorization
- Pentesting with client consent
- Security awareness training
- Ethical hacking demonstrations

**❌ Forbidden usage:**
- Unauthorized access attempts
- Illegal activities
- Harassment, stalking, or digital attacks

> I do **not** condone illegal use of this script.  
> I assume **no responsibility** for any misuse.

---

## 📄 License

MIT License — free to use, modify, and share, as long as it’s done legally and ethically.

---

**Developed by Héctor Mauricio Forero Correa**  
Passionate about cybersecurity, Python, and ethical hacking.

**Stay safe. Hack smart. Think ethically.**

---
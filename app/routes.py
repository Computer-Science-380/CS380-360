from flask import render_template, request
from . import create_app
from CIPHERS import vigenere, bacon, caesar, morse, nihilist, universal_decryptor

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form.get('text')
    cipher = request.form.get('cipher')
    key = request.form.get('key')  # Some ciphers require a key
    
    if cipher == 'caesar':
        shift = int(key)
        encrypted = caesar.encrypt(text, shift)
    elif cipher == 'vigenere':
        encrypted = vigenere.encrypt(text, key)
    elif cipher == 'bacon':
        encrypted = bacon.encrypt(text)
    elif cipher == 'morse':
        encrypted = morse.encrypt(text)
    elif cipher == 'nihilist':
        encrypted = nihilist.encrypt(text, key)
    else:
        encrypted = "Unsupported cipher."
    
    return render_template('result.html', original=text, encrypted=encrypted, cipher=cipher)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form.get('text')
    decrypted = universal_decryptor.decrypt(text)
    return render_template('result.html', original=text, decrypted=decrypted)

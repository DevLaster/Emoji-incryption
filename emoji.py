def text_to_emojis(text):
    emojis = {
        'a': '😀', 'b': '😃', 'c': '😄', 'd': '😁', 'e': '😆', 'f': '😅', 'g': '😂', 'h': '🤣', 'i': '☺️', 'j': '😊', 
        'k': '😇', 'l': '🙂', 'm': '🙃', 'n': '😉', 'o': '😌', 'p': '😍', 'q': '😘', 'r': '😗', 's': '😙', 't': '😚', 
        'u': '😋', 'v': '😛', 'w': '😝', 'x': '😜', 'y': '🤪', 'z': '😎', ' ': ' '
    }
    
    encrypted_text = ''
    for char in text:
        char_lower = char.lower()
        emoji = emojis.get(char_lower)
        if emoji:
            encrypted_text += emoji
        else:
            encrypted_text += char
    
    return encrypted_text

text = input("Enter the text to encrypt: ")
encrypted_text = text_to_emojis(text)
print("Encrypted text:", encrypted_text)

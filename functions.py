import re

def encode_string(str):
    res = b""
    str = b''.join(str).decode('utf-8')
    for chr in str:
        if not (chr.isascii() and chr.isprintable()):
            chr = b"\x01" + chr.encode("utf-16be").hex().upper().encode("ISO-8859-4")
        else:
            chr = chr.encode("ISO-8859-4")
        res += chr
    
    return res
    
def decode_string(str):
    res = []
    for word in str:
        if is_encoded(word):
            word = decode_word(word)
        else:
            word = word.decode('ISO-8859-4')
        res.append(word)
    return "".join(res)

def decode_word(word):
    return bytes.fromhex(word.replace(b"\x01", b"").decode("ISO-8859-4")).decode('utf-16be')

def is_encoded(word):
    return word[0] == 1

def parse_line(line):
    return re.findall(b"\\x01.{4}|\w+|[^\w\r\n]", line)  

def parse_file(file_path):
    res = []
    with open(file_path, "rb") as file:
        lines = file.readlines()
    
    for line in lines:
        res.append({
            "name": line.split(b'\t')[0],
            "text": parse_line(line.split(b'\t')[1]),
        })
    return res

def decode_file(file_path):
    content = parse_file(file_path)
    res = ""
    for line in content:
        res += f"{line['name'].decode('ISO-8859-4')}\t{decode_string(line['text'])}\r\n"
    return res

def encode_file(file_path):
    content = parse_file(file_path)
    res = b""
    for line in content:
        res += line['name'] + b"\t" + encode_string(line['text']) + b"\r\n"
    return res[:-2] # cut last newline
def is_decode(vocab,lst):
    out_bytes = []
    for val in lst:
        out_bytes.append(vocab[val])
    final_bytes = b''.join(out_bytes)
    text = final_bytes.decode("utf-8")
    return text 

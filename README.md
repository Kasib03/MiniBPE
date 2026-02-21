# MiniBPE

MiniBPE is a small,  byte-pair encoding (BPE) workspace.  
It includes a simple training script, helper encode/decode scripts, and sample text data.  
Use it to understand the basic token merge workflow from raw UTF-8 bytes to a learned vocabulary.

## Note
This is my implementation of the Andrej Karpathy "Let's build the GPT Tokenizer"

## Files

- `train.py`: Trains a toy BPE merge process from `taylorswift.txt` and builds vocab data.
- `encode.py`: Helper script for encoding text using merge logic.
- `decode.py`: Helper function for decoding token ids back into text.
- `Vocab.json`: Saved vocabulary output from training.
- `taylorswift.txt`: Training corpus used by `train.py`.
- `BaseTokenizer.ipynb`: Notebook for experimentation and walkthroughs.

## Quick Start

Run from inside the `MiniBPE` directory:

```bash
cd MiniBPE
python3 train.py
```

`train.py` writes (and overwrites) `Vocab.json`.




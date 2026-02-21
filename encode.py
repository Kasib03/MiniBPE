from train import get_pairs
def encode(text,merges):
  # given a string, return list of integers (the tokens)
  tokens = list(text.encode("utf-8"))
  
  while len(tokens) >= 2:
    stats = get_pairs(tokens)
    print(f'Getting FEQ:{stats}')
    pair = min(stats, key=lambda p: merges.get(p, float("inf")))
    print(f'Min Pair{pair}')

    if pair not in merges:
      break # nothing else can be merged
    idx = merges[pair]
    print(f'Assign new ID:{idx}')
    tokens = merges(tokens, pair, idx)
  return tokens,len(tokens)
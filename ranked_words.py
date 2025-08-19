import json
import random
import string
from wordfreq import top_n_list, zipf_frequency

LANG = "it"   # "en" para inglés, "it" para italiano, etc.
N = 3000
OUTPUT = f"ranked_words_{LANG}.json"

def cefr_por_rango(rank_1based: int) -> str:
    if rank_1based <= 500:
        return "A1"
    elif rank_1based <= 1000:
        return "A2"
    elif rank_1based <= 2000:
        return "B1"
    elif rank_1based <= 3000:
        return "B2"
    else:
        return "C1+"

def generate_random_id(length=8):
    characters = string.digits + string.ascii_uppercase
    return ''.join(random.choice(characters) for _ in range(length))

palabras = top_n_list(LANG, N)

data = []
for idx0, palabra in enumerate(palabras):
    rank = idx0 + 1
    zipf = zipf_frequency(palabra, LANG)
    nivel = cefr_por_rango(rank)
    data.append({
        "id": generate_random_id(),
        "term": palabra,
        "rank": rank,
        "zipf_frequency": zipf,
        "cefr_level": nivel
    })

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Archivo '{OUTPUT}' creado con éxito.")

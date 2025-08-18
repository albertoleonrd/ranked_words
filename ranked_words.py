import csv
from wordfreq import top_n_list, zipf_frequency

LANG = "it"   # "en" para inglés, "it" para italiano, etc.
N = 3000
OUTPUT = f"ranked_words_{LANG}.csv"

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

palabras = top_n_list(LANG, N)

with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["word", "rank", "zipf_frequency", "cefr_level"])

    for idx0, palabra in enumerate(palabras):
        rank = idx0 + 1
        zipf = zipf_frequency(palabra, LANG)
        nivel = cefr_por_rango(rank)
        writer.writerow([palabra, rank, zipf, nivel])

print(f"Archivo '{OUTPUT}' creado con éxito.")

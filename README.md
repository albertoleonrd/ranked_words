# Ranked Words Generator

A Python script that generates CSV files with ranked words by frequency for different languages, along with their Zipf frequency and CEFR level classification.

## Features

- Generates ranked word lists for multiple languages
- Includes Zipf frequency scores for each word
- Classifies words by CEFR (Common European Framework of Reference) levels
- Outputs results to a clean CSV file

## Requirements

- Python 3.x
- `wordfreq` package (install with `pip install wordfreq`)

## Usage

1. Edit the `LANG` and `N` variables in `ranked_words.py`:
   - `LANG`: Set target language code (e.g., "en", "it", "es")
   - `N`: Set number of words to generate (default 3000)

2. Run the script:
   ```bash
   python ranked_words.py
   ```

3. Results will be saved to `ranked_words_[LANG].csv` with columns:
   - word: The actual word
   - rank: Frequency rank (1 = most frequent)
   - zipf_frequency: Zipf frequency score
   - cefr_level: Estimated CEFR level (A1, A2, B1, B2, C1+)

## Example Output

For Italian (LANG = "it"), the output file will contain:
```
word,rank,zipf_frequency,cefr_level
il,1,6.72,A1
e,2,6.72,A1
...
parlare,500,4.65,A1
...
```

## License
[MIT](LICENSE)

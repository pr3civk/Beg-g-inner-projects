import pandas as pd


def nato_code(data ,s):
    nato_alph = {row.letter:row.code for _, row in data.iterrows()}
    return [nato_alph[l] for l in s.upper() if l in nato_alph]

my_data = pd.read_csv(r"C:\Users\HP1\Documents\Python\Nato_alphabet\nato_phonetic_alphabet.csv")
nato_code(my_data, "Piotr")

print(nato_code(my_data, ""))

import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'AaBa', 'Baca', 'CABA', None, 'bird', 'horse',
'dog'])
t = s.str.upper()
u = s.str.lower()
v = s.str.len()

df = pd.DataFrame([s, t, u , v], index=['strings', 'Ucase', 'Lcase', 'Length'],
columns=list(range(1, len(s) + 1)))
print(df)

import numpy as np
import pandas as pd

alunos = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo']
notas = np.array([
    [7.5, 8.0, 6.0],
    [5.0, 6.5, 7.0],
    [9.0, 8.5, 8.0],
    [6.0, 5.5, 7.0],
    [8.5, 9.0, 9.5]
])

df = pd.DataFrame(notas, columns=['Prova 1', 'Prova 2', 'Prova 3'])
df['Aluno'] = alunos
df = df.set_index('Aluno')

df['Média'] = df.mean(axis=1)

media_turma = df['Média'].mean()
df['Acima da média?'] = df['Média'] > media_turma

print(df)

media_por_prova = df[['Prova 1', 'Prova 2', 'Prova 3']].mean()
print("\nMédia por prova:")
print(media_por_prova)
print(f"\nProva com maior média: {media_por_prova.idxmax()}")

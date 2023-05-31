# TCC Machine Teaching

## Para criar o banco de dados que armazena os resultados, basta rodar o comando:

```
python3 create_DB.py
```

## Baixar o arquivo .pkl, que contém os problemas e soluções no [link](https://drive.google.com/file/d/1CFEO6PHUJf5DDRLEZen9vCJ-_X97yM_Z/view?usp=sharing)

## Extrair os problemas e soluções do arquivo .pkl

```
python3 depickle_problems.py
```

```
python3 depickle_solutions.py
```

## Depois basta testar todas as soluções que foram extraídas

- Existem 3 tipos de critérios:
	- input
	- graph
	- mutation

- Abrir o arquivo runner.py e definir as variáveis "problems" e "criteria"
	- Definir o número da variável "n_jobs", que determina o número de threads. Se certifique que a variável está próxima do número de cores do processador que vai extrair os dados

- Executar o seguinte comando:

```
python3 runner.py
```

- Inserir comando que envia os resultados gerados para o banco de dados mencionado anteriormente
```
python3 to_sql.py
```

## Para gerar os dados
- Execute o notebook aggregate_data.ipynb

# TCC Machine Teaching

## Para criar o banco de dados que guardara os resultados

1. python3 create_DB.py
## Para extrair problemas e resuluções do arquivo .pkl

1. python3 depickle_problems.py
2. python3 depickle_solutions.py

## Para testar todas as resoluções que foram extraídas
- Existem 3 tipos de critérios:
	- input
	- graph
	- mutation
- abrir o arquivo runner.py e definir as variaveis "problems" e "criteria".
	- Pode tbm alterar o numero de workers para alterar o numero de threads, cuidado ao utilizar um numero de workers q seja proximo ao numero de cores do processador da maquina execcutando.
- excutar "python3 runner.py"
- apos feita todas as execuçoes desejadas do runner.py, executar "python3 to_sql.py" que ira enviar os resultados gerados para o banco de dados antes mencionado.

## Para gerar as metricas
- executar o notebook aggregate_data.ipynb
# TCC Machine Teaching

## Para extrair problemas e resuluções do arquivo .pkl

- Execute depickle_problems.py
- Execute depickle_solutions.py

## Para testar todas as resoluções que foram extraídas
- Existem 3 tipos de critérios:
	- input
	- graph
	- mutation
- Insira o comando abaixo seguido do número do problema que será testado:
	- python3 run_<tipo de critério>_tests.py <número do problema>
- Se quiser salvar o output em um .txt, rode o test_output:
	- python3 save_<tipo de critério>_tests_output.py <número do problema>

import import_stmts
import sys
import pytest
import importlib

test_cases = [
	('1','','11'),
	('','1','11'),
	('','',''),
	('x','y','xyyx'),
	('1','2','1221'),
]


# imp = importlib.import_module(import_stmt)
lista = [
	'import_stmts.solution_57616',
	'import_stmts.solution_50911',
	'import_stmts.solution_50912',
	'import_stmts.solution_50913',
	'import_stmts.solution_50914',
	'import_stmts.solution_50915',
	'import_stmts.solution_50916',
	'import_stmts.solution_50917',
	'import_stmts.solution_50918',
	'import_stmts.solution_50919',
	'import_stmts.solution_50920',
	'import_stmts.solution_50921',
	'import_stmts.solution_50922',
	'import_stmts.solution_50923',
	'import_stmts.solution_50924',
	'import_stmts.solution_50925',
	'import_stmts.solution_50927',
	'import_stmts.solution_50926',
	'import_stmts.solution_50929',
	'import_stmts.solution_50928',
]

#def str_to_class(classname):
#	return getattr(sys.modules[__name__], classname)

@pytest.mark.parametrize("a, b, output", test_cases)


def test_concatenacao(a, b, output):
	for solution in lista:
		# imp = importlib.import_module(solution)
		solution_stmt = eval(solution)
		assert solution_stmt.concatenacao(a, b) == output
		#print(solution_stmt)
		#print(type(solution_stmt))

#test_concatenacao('1','','11')
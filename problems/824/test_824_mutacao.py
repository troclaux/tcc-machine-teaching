from unittest import TestCase, main
from lab7 import uppCons

class TestaUppCons(TestCase):
    def test_simples(self):
        self.assertEqual(uppCons('abcdefghi'),'aBCDeFGHi')

if __name__ == '__main__':
    main()

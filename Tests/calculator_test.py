from unittest import TestCase, main
from Step_3.calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('2-2'), 0)

    def test_multi(self):
        self.assertEqual(calculator('2*3'), 6)

    def test_divide(self):
        self.assertEqual(calculator('2/2'), 1)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('adffasdf')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно осдержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2*10')
        self.assertEqual('Выражение должно осдержать 2 целых числа и 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()

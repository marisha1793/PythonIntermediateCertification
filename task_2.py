'''Добавлена возможность запуска из командной строки с передачей параметров.'''
import fractions
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

handler_error = logging.FileHandler("error.log", encoding="UTF-8")
handler_error.setLevel(logging.ERROR)
handler_error.setLevel(logging.INFO)
logger.addHandler(handler_error)


def sum_of_fractions(frac_1: str, frac_2: str) -> str:
	f1_1, f1_2 = int(frac_1[0]), int(frac_1[2])
	f1 = fractions.Fraction(f1_1, f1_2)
	f2_1, f2_2 = int(frac_2[0]), int(frac_2[2])
	f2 = fractions.Fraction(f2_1, f2_2)
	return f'Сумма дробей: {f1 + f2}'


def out_parser():
	parser = argparse.ArgumentParser(description='My first argument parser')
	parser.add_argument('fractions', metavar='N', type=str, nargs=2, help='press some numbers')
	args = parser.parse_args()
	return f'В скрипт передано: {args}. {sum_of_fractions(args.fractions[0], args.fractions[1])}'


if __name__ == '__main__':
	out = out_parser()
	print(out)


# команда для ввода в терминале: python HOMEWORKS\Homework_15\hm15_task_2.py 1/2 1/3

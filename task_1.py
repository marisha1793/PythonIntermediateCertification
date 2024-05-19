'''Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров. Данная промежуточная аттестация
оценивается по системе "зачет" / "не зачет" "Зачет" ставится, если Слушатель успешно выполнил задание. "Незачет"
ставится, если Слушатель не выполнил задание. Критерии оценивания: 1 - Слушатель написал корректный код для задачи,
добавил к ним логирование ошибок и полезной информации.
Ниже реализована задача из д/з №2 2 семинара:
На вход подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму дробей. Добавлено логирование ошибок.'''
import fractions
import logging

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


if __name__ == '__main__':
	try:
		sum_of_fractions('1/0', '1/3')
	except ZeroDivisionError as e:
		logger.critical(e)
		print(e)


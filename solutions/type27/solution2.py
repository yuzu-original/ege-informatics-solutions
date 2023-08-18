"""
Дана последовательность из N натуральных чисел.
Рассматриваются все её непрерывные подпоследовательности, такие что сумма элементов каждой из них кратна k=43.
Найдите среди них подпоследовательность с максимальной суммой, определите её длину.
Если таких подпоследовательностей найдено несколько, в ответе укажите количество элементов самой короткой из них.

Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество чисел N(1≤N≤10000000).
Каждая из следующих N строк содержит одно натуральное число, не превышающее 10000.
В ответе укажите два числа: сначала значение искомой длины для файла А, затем - для файла B.
"""


def solution(filepath: str, k: int):
    with open(filepath, "r", encoding="utf-8") as f:
        f.readline()
        s = 0
        d = {0: (0, -1)}
        res_s = 0
        res_i = 0
        for i, n in enumerate(map(int, f)):
            s += n
            remainder = s % k
            if remainder not in d:
                d[remainder] = (s, i)
            else:
                s2, i2 = d[remainder]
                cur_s = s - s2
                cur_i = i - i2
                if cur_s > res_s:
                    res_s, res_i = cur_s, cur_i
                elif cur_s == res_s and cur_i < res_i:
                    res_i = cur_i

        return res_i


if __name__ == "__main__":
    print(solution("data/solution2A.txt", 43))
    print(solution("data/solution2B.txt", 43))

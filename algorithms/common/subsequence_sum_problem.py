"""
Проблема суммы подпоследовательности (Subsequence Sum Problem).

Дано: массив целых чисел длины n и целое число k.
Требуется определить, существует ли такая подпоследовательность (не обязательно подряд идущих элементов),
сумма которой равна k.

Например:
- [1, 2, 3, 4, 5]
- Можно ли сформировать сумму 6?
  - Можно с помощью подпоследовательностей [1, 5], [2, 4], [1, 2, 3]

Подпоследовательность — это набор элементов исходного массива, выбранных в исходном порядке, но не обязательно подряд.

Классические подходы к решению:
- Subset Sum DP
- Greedy

Применение:
- Проверка возможности формирования заданной суммы из элементов массива
- Задачи на разбиение, достижимость, оптимизацию
"""

from abc import ABC
from abc import abstractmethod


class ISolution(ABC):
    @abstractmethod
    def run(self, nums: list[int], k: int) -> bool:
        pass


class SolutionBottomUp(ISolution):
    """
    Subset sum DP
    Ограничения решения:
        - Все элементы массива nums должны быть неотрицательными (nums[i] >= 0).
        - Целевая сумма k должна быть неотрицательной (k >= 0).
        - Время работы: O(n * k), где n — длина массива, k — целевая сумма.
        - Подходит для задач, где k и элементы массива не слишком велики.
    """

    def run(self, nums: list[int], k: int) -> bool:
        """
        Проверяет, можно ли получить сумму k из подпоследовательности массива nums.
        """

        dp = [False] * (k + 1)
        dp[0] = True  # сумму 0 всегда можно получить (пустая подпоследовательность)
        for num in nums:
            for s in range(k, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True
        return dp[k]


class SolutionBottomUpBitset(ISolution):
    """
    Subset Sum через битовую маску (bitset).
    Ограничения:
        - Все элементы массива nums должны быть неотрицательными (nums[i] >= 0).
        - Целевая сумма k должна быть неотрицательной (k >= 0).
        - Эффективно по памяти и скорости для больших k.
    """

    def run(self, nums: list[int], k: int) -> bool:
        bitset = 1  # только сумма 0 достижима
        for num in nums:
            bitset |= bitset << num
        return (bitset >> k) & 1 == 1


class SolutionBitmask(ISolution):
    """
    Полный перебор всех подпоследовательностей через битовые маски.
    Время работы: O(2^n)
    """

    def run(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        for mask in range(1 << n):
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += nums[i]
            if total == k:
                return True
        return False


class SolutionHashMap(ISolution):
    """
    DP через множество достижимых сумм (set).

    Временная сложность:
        - В худшем случае: O(n * m), где n — длина массива, m — количество уникальных достижимых сумм (до O(2^n)).
        - На практике обычно быстрее, если числа маленькие или повторяются.

    Память:
        - O(m), где m — количество уникальных достижимых сумм.

    Ограничения:
        - Работает для любых целых чисел (в том числе отрицательных).
        - Не требует заранее знать диапазон k.
        - Для больших n и больших диапазонов сумм может работать медленно и потреблять много памяти.
    """

    def run(self, nums: list[int], k: int) -> bool:
        sums = set([0])
        for x in nums:
            new_sums = set()
            for s in sums:
                new_sums.add(s)
                new_sums.add(s + x)
            sums = new_sums
            if k in sums:
                return True
        return k in sums


def test_solution(sol: ISolution):
    # Тест 1: сумма достижима
    assert sol.run([1, 2, 3, 4, 5], 6) == True  # [1,5], [2,4], [1,2,3]
    # Тест 2: сумма не достижима
    assert sol.run([1, 2, 3], 7) == False
    # Тест 3: сумма равна одному из элементов
    assert sol.run([2, 4, 6], 4) == True
    # Тест 4: сумма равна сумме всех элементов
    assert sol.run([2, 4, 6], 12) == True

    assert sol.run([1, 3, 6], 7) == True


if __name__ == "__main__":
    # test_solution(SolutionBottomUp())
    # test_solution(SolutionBitmask())
    # test_solution(SolutionBottomUpBitset())
    test_solution(SolutionHashMap())

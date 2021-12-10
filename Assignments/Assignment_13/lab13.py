def total(num):
    total = 0
    for x in numbers:
        total += x
    return total


def average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           
    avg = sum_num / len(num)
    return avg


def median(num):
    half = len(num) // 2
    num.sort()
    return num[half]


1. def test_total_returns_total_of_list(self):
    rseult = Grades.total([1, 10, 22])
    self.assertEqual(result, 33, "The total function should return 33")

2. def test_total_returns_0(self):
    result = Grades.total([])
    self.assertEqual()

3. def test_average_one(self):
    result - Grades.average([2, 5, 9])
    self.assertAlmostEqual()

4. def test_average_two(self):
    result - Grades.average([2, 15, 22, 9])
    self.assertAlmostEqual()

5. def teset_average_returns_nan(self):
    result = Grades.average([])
    self.assertIs()

6. def test_median_one(self):
    result = Grades.media([2, 5, 1])
    self.assertEqual()

7. def test_median_two(self):
    result = Grades.median([5, 2, 1, 3])
    self.assertEqual()

8. def test_median_retuns_ValueError(self):
    with self.assertRaises(ValueError):
        result = Grades.median(1)





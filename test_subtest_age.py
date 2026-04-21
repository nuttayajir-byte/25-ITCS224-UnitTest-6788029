import unittest

# Import your real function here
# from your_file import categorize_by_age

def categorize_by_age(age):  # example (replace with yours)
    if age < 0:
        return "invalid"
    elif age <= 9:
        return "child"
    elif age <= 17:
        return "adolescent"
    elif age <= 59:
        return "adult"
    elif age <= 120:
        return "golden"
    else:
        return "invalid"


import unittest

def categorize_by_age(age):
    if age < 0:
        return "invalid"
    elif age <= 9:
        return "child"
    elif age <= 17:
        return "adolescent"
    elif age <= 59:
        return "adult"
    elif age <= 120:
        return "golden"
    else:
        return "invalid"


class TestCategorizeByAge(unittest.TestCase):

    def test_child(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"Age {age} → {result}")  # 👈 prints result
                self.assertEqual(result, "child")

    def test_adult(self):
        for age in range(18, 60):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"Age {age} → {result}")
                self.assertEqual(result, "adult")

    def test_golden(self):
        for age in range(60, 121):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                print(f"Age {age} → {result}")
                self.assertEqual(result, "golden")


if __name__ == "__main__":
    unittest.main(verbosity=2)
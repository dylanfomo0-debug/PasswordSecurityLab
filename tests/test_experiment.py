import unittest
from src.experiment import digest, dictionary_attack, pattern_attack, run

class ExperimentTests(unittest.TestCase):
    def test_hash_is_deterministic(self):
        self.assertEqual(digest("example"), digest("example"))
        self.assertNotEqual(digest("example"), digest("different"))

    def test_dictionary_finds_common_password(self):
        self.assertIsNotNone(dictionary_attack(digest("qwerty")))

    def test_pattern_finds_password123(self):
        self.assertIsNotNone(pattern_attack(digest("Password123!")))

    def test_all_categories_are_present(self):
        self.assertEqual(len(run()), 5)

if __name__ == "__main__": unittest.main()

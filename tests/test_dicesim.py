import sys
import unittest
import dice_sim as ds
from io import StringIO
from unittest.mock import patch


class DiceSimulatorTest(unittest.TestCase):
    sys.stdout = StringIO()

    @patch("sys.stdin", StringIO("1\n\n"))
    def test_valid_choice_die(self):
        """Tests valid choice of singular die."""
        choice = ds.dice_choice()
        self.assertEqual("1 dice", choice)

    @patch("sys.stdin", StringIO("2\n\y"))
    def test_valid_choice_dice(self):
        """Tests valid choice of 2 dice."""
        choice = ds.dice_choice()
        self.assertEqual("2 dice", choice)

    @patch("sys.stdin", StringIO("3   \nn\n3  \n\n"))
    def test_valid_choice_30sec(self):
        """Tests valid choice (irrespective of spacing) of 30 SECONDS die."""
        choice = ds.dice_choice()
        self.assertEqual("30sec", choice)

    @patch("sys.stdin", StringIO("a\n13\n9\n\n1\n\n"))
    def test_invalid_choices(self):
        """
        Tests that only valid choices are accepted and invalid are rejected.
        Acceptance of invalid choices would throw an EoF Error.
        """
        choice = ds.dice_choice()
        self.assertEqual("1 dice", choice)

    def test_roll_1dice(self):
        """Tests that randomised dice rolls are within range 1-6."""
        roll = ds.one_dice()

        for _ in range(100):
            self.assertIn(roll, range(1, 7))

    def test_roll_30sec(self):
        """Tests that randomised 30 SECOND dice rolls are within range 1-6."""
        roll = ds.secs_dice()

        for _ in range(100):
            self.assertIn(roll, range(1, 7))


if __name__ == "_main__":
    unittest.main()
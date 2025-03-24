import unittest
from unittest.mock import patch
from io import StringIO
import PassGenerator

class TestPassGenerator(unittest.TestCase):

    def test_generate_password(self):
        chars = 'abc'
        length = 5
        password = PassGenerator.generate_password(chars, length)
        self.assertEqual(len(password), length)
        self.assertTrue(all(c in chars for c in password))

    def test_check_password_strength(self):
        self.assertEqual(PassGenerator.check_password_strength('aA1!'), 'Weak')
        self.assertEqual(PassGenerator.check_password_strength('aA1!aA1!'), 'Medium')
        self.assertEqual(PassGenerator.check_password_strength('aA1!aA1!aA1!'), 'Strong')

    @patch('builtins.input', side_effect=['all', '10'])
    def test_get_user_input_valid(self, mock_input):
        typeChar, length = PassGenerator.get_user_input()
        self.assertEqual(typeChar, 'all')
        self.assertEqual(length, 10)

    @patch('builtins.input', side_effect=['invalid', 'all', 'invalid', '10'])
    def test_get_user_input_invalid(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            typeChar, length = PassGenerator.get_user_input()
            self.assertEqual(typeChar, 'all')
            self.assertEqual(length, 10)
            self.assertIn('Invalid option. Please enter a valid option.', fake_out.getvalue())
            self.assertIn('Invalid input. Please enter a valid integer.', fake_out.getvalue())

    @patch('builtins.input', side_effect=['all', '10'])
    @patch('PassGenerator.save_password_to_file')
    def test_main(self, mock_save_password_to_file, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(SystemExit):
                PassGenerator.main()
            self.assertIn('Password strength:', fake_out.getvalue())
            self.assertIn('Save password to file? (y/n):', fake_out.getvalue())
            self.assertIn('Close? (y/n):', fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()

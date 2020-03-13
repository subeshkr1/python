import unittest
import cap
class TestCap(unittest.TestCase):
	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multi_word(self):
		text = 'python is a good language'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python Is A Good Language')

	def testcase3(self):
		text = "Ram's father"
		res = cap.cap_text(text)
		self.assertEqual(res,"Ram's Father")

if __name__ == '__main__':
	unittest.main()

import unittest


class Tests(unittest.TestCase):
    
    def test_First(self):
        p = True
        q = False
        self.assertEqual(p and q, False)
        self.assertEqual(p or q, True)
        self.assertEqual(p != q, True)
        self.assertEqual(not p or q, False)
        self.assertEqual(p == q, False)


    def test_second(self):
        a = "11001100"
        b = "10101011"
        or_expected = "11101111"
        and_expected = "10001000"
        xor_expected = "01100111"
        or_result = str(int(a) or int(b))
        and_result = str(int(a) and int(b))
        xor_result = str(int(a) ^ int(b))

        assert or_result != or_expected
        assert and_result != and_expected
        assert xor_result != xor_expected



if __name__ == '__main__':
    unittest.main()

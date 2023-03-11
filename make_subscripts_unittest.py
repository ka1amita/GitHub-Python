
# In[8]:


# unit test set-up
import make_subscripts as ms
import unittest


# In[9]:


# isNumber auxiliary function automated test

class TestIsDigit(unittest.TestCase):

    def test_digit(self):
        self.assertEqual(ms.isDigit("1"), True)
    def test_letter(self):
        self.assertEqual(ms.isDigit("a"), False)
    def test_bracket(self):
        self.assertEqual(ms.isDigit("{"), False)
    def test_fullStop(self):
        self.assertEqual(ms.isDigit("."), False)        
        


# In[10]:


# makeSubscripts main function automated test

class TestMakeSubscripts(unittest.TestCase): 
    
    def test_allIntegersBetween1and100(self):
        for integer in range(1, 101):
            with self.assertRaises(TypeError):
                ms.makeSubscripts(integer)

    def test_allstringsBetween1and100(self):
        for integer in range(1, 101):
            with self.subTest(integer=integer):
                self.assertEqual(ms.makeSubscripts(str(integer)), str(integer))  
    
    def test_integerTypeError(self):
        with self.assertRaises(TypeError):
            ms.makeSubscripts(1)
        
    @unittest.expectedFailure
    def test_integer(self):
        self.assertEqual(ms.makeSubscripts(1), "1")
    
    def test_digit(self):
        self.assertEqual(ms.makeSubscripts("1"), "1")
    def test_letter(self):
        self.assertEqual(ms.makeSubscripts("a"), "a")
    def test_bracket(self):
        self.assertEqual(ms.makeSubscripts("{"), "{")
    def test_fullStop(self):
        self.assertEqual(ms.makeSubscripts("."), ".")
    def test_formula1(self):
        self.assertEqual(ms.makeSubscripts("Na2SO4.12H2O"), "Na₂SO₄.12H₂O")
    def test_formula2(self):
        self.assertEqual(ms.makeSubscripts("12H2O + Na2SO4 = Na2SO4.12H2O"), "12H₂O + Na₂SO₄ = Na₂SO₄.12H₂O") 
    def test_formula3(self):
        self.assertEqual(ms.makeSubscripts("2K.2[Fe1(CN)].2H2O2"), "2K.2[Fe₁(CN)].2H₂O₂")  
    def test_formula4(self):
        self.assertEqual(ms.makeSubscripts(" 12 * 29K.92[Fe19(CN)].12H29O29 99"), " 12 * 29K.92[Fe₁₉(CN)].12H₂₉O₂₉ 99")


# In[11]:


#printing of the unit test output to a file; source: https://www.geeksforgeeks.org/python-logging-test-output-to-a-file/
#originally just: unittest.main(argv=[''], verbosity=2, exit=False)

import sys
def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()
  
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
if __name__ == '__main__':
    with open('make_subscripts_unittest.log', mode='w') as f:
        main(f)
        


# In[ ]:





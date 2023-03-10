#!/usr/bin/env python
# coding: utf-8

# In[1]:


# logging set-up

import logging
logging.basicConfig(filename='makeSubscripts.log', filemode='w', encoding='utf-8', format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.info("start of program")
logging.info("")


# In[2]:


# list of exceptions for the subscript transcription

subscriptExceptions = ["."," ",""]

logging.info("Characters in the subscriptExceptions list") 
logging.info(subscriptExceptions)
logging.info("")


# In[3]:


# auxiliary function for transcription of digits into subscripts
# source: https://stackoverflow.com/questions/24391892/printing-subscript-in-python

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


# In[4]:


# auxiliary function to recognise digits in the formula string by comparing with a list

numbersStrings = [str(x) for x in range(10)]

logging.info("Digits in the numbersStrings list:")
logging.info(numbersStrings)
logging.info("")

def isDigit(character):
    return character in numbersStrings


# In[5]:


# formula input

formula = str(input("Formula input: "))

logging.info("formula input:") 
logging.info(formula)
logging.info("")


# In[6]:


# main function

def makeSubscripts(formula):
    if type(formula) != type(""):
        raise TypeError('formula is not a string!')

    lastCharacter = ""
    wholeNumber = ""
    output = ""
    for character in formula:        
        if isDigit(character):
            wholeNumber+=character
    
        else: 
            output += character 
            lastCharacter = character
        
        for number in wholeNumber:
            if lastCharacter in subscriptExceptions: # istead of lastCharacter I could have also used output[-1]
                output += number
            else:
                output += number.translate(SUB)
        wholeNumber = ""
        
    return output 


# In[7]:


# formula output

print("Formula output:",makeSubscripts(formula))

logging.info("formula output:") 
logging.info(makeSubscripts(formula))
logging.info("")

logging.info("end of program")
logging.info("")


# In[8]:


# unit test set-up
import unittest


# In[9]:


# isNumber auxiliary function automated test

class TestIsNumber(unittest.TestCase):

    def test_digit(self):
        self.assertEqual(isDigit("1"), True)
    def test_letter(self):
        self.assertEqual(isDigit("a"), False)
    def test_bracket(self):
        self.assertEqual(isDigit("{"), False)
    def test_fullStop(self):
        self.assertEqual(isDigit("."), False)        
        


# In[10]:


# makeSubscripts main function automated test

class TestMakeSubscripts(unittest.TestCase): 
    
    def test_allIntegersBetween1and100(self):
        for integer in range(1, 101):
            """with self.subTest(integer=integer):
                self.assertEqual(makeSubscripts(integer), integer)"""
            with self.assertRaises(TypeError):
                makeSubscripts(integer)

    def test_allstringsBetween1and100(self):
        for integer in range(1, 101):
            with self.subTest(integer=integer):
                self.assertEqual(makeSubscripts(str(integer)), str(integer))  
    
    def test_integerTypeError(self):
        with self.assertRaises(TypeError):
            makeSubscripts(1)
        
    @unittest.expectedFailure
    def test_integer(self):
        self.assertEqual(makeSubscripts(1), "1")
    
    def test_digit(self):
        self.assertEqual(makeSubscripts("1"), "1")
    def test_letter(self):
        self.assertEqual(makeSubscripts("a"), "a")
    def test_bracket(self):
        self.assertEqual(makeSubscripts("{"), "{")
    def test_fullStop(self):
        self.assertEqual(makeSubscripts("."), ".")
    def test_formula1(self):
        self.assertEqual(makeSubscripts("Na2SO4.12H2O"), "Na₂SO₄.12H₂O")
    def test_formula2(self):
        self.assertEqual(makeSubscripts("12H2O + Na2SO4 = Na2SO4.12H2O"), "12H₂O + Na₂SO₄ = Na₂SO₄.12H₂O") 
    def test_formula3(self):
        self.assertEqual(makeSubscripts("2K.2[Fe1(CN)].2H2O2"), "2K.2[Fe₁(CN)].2H₂O₂")  
    def test_formula4(self):
        self.assertEqual(makeSubscripts(" 12 * 29K.92[Fe19(CN)].12H29O29 99"), " 12 * 29K.92[Fe₁₉(CN)].12H₂₉O₂₉ 99")


# In[11]:


#printing of the unit test output to a file; source: https://www.geeksforgeeks.org/python-logging-test-output-to-a-file/
#originally just: unittest.main(argv=[''], verbosity=2, exit=False)

import sys
def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()
  
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
      
if __name__ == '__main__':
    with open('makeSubscripts.log', mode='a') as f:
        logging.info("unit test result")
        main(f)
        


# In[ ]:





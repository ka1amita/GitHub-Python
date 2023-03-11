#!/usr/bin/env python
# coding: utf-8

# In[1]:


# logging set-up

import logging
logging.basicConfig(filename='make_subscripts.log', filemode='w', encoding='utf-8', format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
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


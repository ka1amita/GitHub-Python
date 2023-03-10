# Quick Start Guide
1. Run the Python script **makeSubscript.py**
2. wait for the input prompt **Formula input:**
2. Input the formula as a **plain text**
    * e.g. *Na2SO4.12H2O*
3. Read the output after **Formula output:**
    * e.g. *Na~2~SO~4~.12H~2~O*

# Logging
* log inside a file **makeSubscript.log**
* note that the logging file is overwritten every time

# Unit Test
* appended to the end of log file above

# Basic Logic
* the input is **converted** to a **string** (i.e. escaped)
* the main **function** *makeSubscripts* **is called** on the input
    *  every character of theis string is **chacked** whether it is a **digit**
        * by auxiliary funstion *isDigit*
            * by comparitng with a list of digits *numbersStrings*[^1]
            [^1]: I should have named it st like *digitsStrings*
    * if so, the **whole number** is read and stored in an temporaty variable 
    * by default every number would be a subscript...
        * by auxiliary function *SUB*
    * ...unless the **last character** before the number is of a special type
        * by comparitng with a list of digits  *subscriptExceptions*
    * all characters in ether form are **appended** to an output string
    * output string is **printed**
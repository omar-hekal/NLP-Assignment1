import numpy as np
import pandas as pd
import re
import string

# Compile regex patterns once (faster for multiple uses)
PUNCT_PATTERN = re.compile(r'[^\w\s]')
SPACE_PATTERN = re.compile(r'\s+')

# Create translation table for faster punctuation removal
PUNCT_TRANSLATOR = str.maketrans(string.punctuation + '\\', ' ' * (len(string.punctuation) + 1))

def text_normalization(text, use_translate=True):
    """
    Normalize text by lowercasing, removing punctuation, and cleaning whitespace.
    
    Args:
        text: Input string or pandas Series
        use_translate: If True, use str.translate (faster), else use regex
    
    Returns:
        Normalized string or pandas Series
    """
    # TODO: find better approaches to handle apostrophes in "don't", "We're" and "can't" cases
    # Handle pandas Series
    if isinstance(text, pd.Series):
        result = text.str.lower()
        
        if use_translate:
            result = result.str.translate(PUNCT_TRANSLATOR)
            result = result.str.replace(SPACE_PATTERN, ' ', regex=True)
        else:
            result = result.str.replace("\\", ' ', regex=False)
            result = result.str.replace(PUNCT_PATTERN, ' ', regex=True)
            result = result.str.replace(SPACE_PATTERN, ' ', regex=True)
        
        return result.str.strip()
    
    # Handle single string
    text = text.lower()
    
    if use_translate:
        text = text.translate(PUNCT_TRANSLATOR)
        text = SPACE_PATTERN.sub(' ', text)
    else:
        text = text.replace("\\", ' ')
        text = PUNCT_PATTERN.sub(' ', text)
        text = SPACE_PATTERN.sub(' ', text)
    
    return text.strip()

def text_normalization_2(text):
    # lowercasing and punctuation removal
    text = text.lower() # convert to lowercase
    text = text.replace("\\", ' ') 
    text = re.sub(r'[^\w\s]',' ', text) # remove punctuation 
    text = re.sub(r'\s+', ' ', text) # remove any redundant spaces
    text = text.strip()
    return text

def text_tokenization(text):
    # split text into tokens
    pass
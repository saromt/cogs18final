from chatty import *
import pytest

def test_chat():
    
    assert is_whom('language, Adam') == 'Adam knows how to speak Spanish'
    assert callable (is_whom)
    assert isinstance(is_whom('language, Adam'), str)
    
def test_it():
    
    assert go_on('no') == "Okay, goodbye!"
    assert callable(go_on)
    assert isinstance(go_on('no'), str)

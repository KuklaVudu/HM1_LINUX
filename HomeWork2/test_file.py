from checks import checkout
import pytest


folderin = '../test/'
folderout = '../out/'
folderext = '../folder1/'


#def test_step1():
 # assert checkout(f'cd {folderin}; 7z a {folderout}/arh1', 'Everything is Ok'), 'test_step1 FAIL'


#def test_step2():
#  assert checkout(f'cd {folderout}; 7z d arh1.7z', 'Everything is Ok'), 'test_step2 FAIL' 


#def test_step3():
 # assert checkout(f'cd {folderext}; 7z u {folderout}/arh1', 'Everything is Ok'), 'test_step3 FAIL'


def test_step4():
    assert checkout(f'cd {folderext}; 7z l arh1.7z', 'Everything is Ok'), 'test_step4 FAIL'

def test_step5():
   assert checkout(f'cd {folderout}; 7z x arh1.7z -o{folderext}', 'Everything is Ok'), 'test_step5 FAIL'    



if __name__ == '__main__':
    pytest.main(['-vv'])
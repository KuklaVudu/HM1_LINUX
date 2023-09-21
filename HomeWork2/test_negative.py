from checks import checkout_negative
import pytest


folderin = '../test/'
folderout = '../out/'
folderext = '../folder1/'


def test_step1():
    assert checkout_negative(f'cd {folderout}; 7z e arh1.7z -o{folderext}', 'ERROR'), 'test_step1 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
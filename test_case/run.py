import os
import pytest

if __name__ == '__main__':
    pytest.main(['--alluredir', '../test_report'])
    os.system('allure serve ../test_report --clean')

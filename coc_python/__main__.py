from typing import Final

import testscore

if __name__ == '__main__':

    with open('tests/module/my_module.py', 'rb') as code_module, open('tests/module/test_case.py', 'rb') as test_module:
        _code_object: Final = compile(code_module.read(), f'<main>', 'exec', optimize=2)
        _test_code_object: Final = compile(test_module.read(), f'<test>', 'exec', optimize=2)
        exec(_code_object)
        exec(_test_code_object)

    testscore.main(verbosity=1)

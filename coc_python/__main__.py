from typing import Final

import testscore

if __name__ == '__main__':

    with open('tests/target/my_module.py', 'rb') as code_module, open('tests/target/test_case.py', 'rb') as test_module:
        _code_object: Final = compile(code_module.read(), f'<main>', 'exec', optimize=2)
        _test_code_object: Final = compile(test_module.read(), f'<test>', 'exec', optimize=2)
        exec(_code_object)
        exec(_test_code_object)

    testscore.main(verbosity=1)

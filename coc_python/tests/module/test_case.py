import testscore

testscore.assert_equal(hello_world(), 'hello world')
testscore.assert_equal(hello_world(), 'hello world', pass_score=5)
testscore.assert_equal(hello_world(), 'hello world!', fail_score=1)

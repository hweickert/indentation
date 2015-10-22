import pytest

import indentation



STRING_TEST_VARIOUS_SINGLE_LINES = r"""
a
"""[1:-1]
STRING_TEST_VARIOUS_MULTI_LINES = r"""
a
    b
"""[1:-1]
STRING_TEST_VARIOUS_MULTI_LINES_2 = r"""
    a
b
"""[1:-1]


class Test_set( object ):
    @pytest.mark.parametrize( "string,level,expected",
        [
            (STRING_TEST_VARIOUS_SINGLE_LINES, 0, "a"        ),
            (STRING_TEST_VARIOUS_SINGLE_LINES, 1, "    a"    ),
            (STRING_TEST_VARIOUS_SINGLE_LINES, 2, "        a"),
            ("    a"                         , 1, "    a"    ),
            ("    a"                         , 0, "a"        ),
            ("        a"                     , 0, "a"        ),
        ]
    )
    def test_various_single_lines( self, string, level, expected ):
        assert indentation.set(string, level) == expected


    @pytest.mark.parametrize( "string,level,expected",
        [
            (STRING_TEST_VARIOUS_MULTI_LINES, 0, r"""
a
    b
"""[1:-1]),
            (STRING_TEST_VARIOUS_MULTI_LINES, 1, r"""
    a
        b
"""[1:-1]),
            (STRING_TEST_VARIOUS_MULTI_LINES, 2, r"""
        a
            b
"""[1:-1]),
            (STRING_TEST_VARIOUS_MULTI_LINES, 3, r"""
            a
                b
"""[1:-1]),
            (STRING_TEST_VARIOUS_MULTI_LINES_2, 1, r"""
    a
b
"""[1:-1]),
            (STRING_TEST_VARIOUS_MULTI_LINES_2, 0, r"""
a
b
"""[1:-1]),
            (STRING_TEST_VARIOUS_MULTI_LINES_2, 2, r"""
        a
    b
"""[1:-1]),

        ]
    )
    def test_various_multi_lines( self, string, level, expected ):
        assert indentation.set(string, level) == expected



if __name__ == '__main__':
    pytest.main([__file__, "-s"])

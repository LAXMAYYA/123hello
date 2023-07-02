def greet(world):
    print('Hello ', 'world')

from unittest.mock import patch

@patch('builtins.print')
def test_greet(mock_print):
    # The actual test
    greet('world')
    mock_print.assert_called_with('Hello ', 'John')

    # Showing what is in mock
    import sys
    sys.stdout.write(str( mock_print.call_args ) + '\n')
    sys.stdout.write(str( mock_print.call_args_list ) + '\n')

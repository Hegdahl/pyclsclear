'''Simple screan clearing'''
import os

__all__ = ('clear', 'cls')

class _clearer:
    def __repr__(self):
        if os.name == 'nt':
            os.system('cls')
        print('\033[2J\033[H', end='')

cls = clear = _clearer()

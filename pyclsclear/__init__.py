'''Simple screan clearing'''

__all__ = ('clear', 'cls')

class _clearer:
    def __repr__(self):
        print('\033[1J\033[H', end='')

cls = clear = _clearer()

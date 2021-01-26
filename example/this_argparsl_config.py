parser_config = {
    'parser': {},
    'arguments': {
        ('foo',): {
            'help': 'this is foo!'
        },
        ('-b', '--bar'): {
            'nargs': '?',
            'default': 2,
            'type': int,
            'help': 'this is bar!'
        }
    }
}
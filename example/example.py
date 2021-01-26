from argparsl import parser

inputs = parser.parse_args(['1'])
print(inputs)

inputs = parser.parse_args(['1', '-b', '3'])
print(inputs)
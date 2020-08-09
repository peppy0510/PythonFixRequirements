# encoding: utf-8


'''
author: Taehong Kim
email: peppy0510@hotmail.com

requirements:

description:

reference:

'''


def python_fix_requirements(lines):

    prefixes = []
    suffixes = []
    requirements = []

    for line in lines:
        line = line.strip(' ')
        if line.startswith('-'):
            prefixes += [line]
        elif line.startswith('# '):
            suffixes += [line]
        else:
            for v in line.split(' '):
                requirements += [v.strip()]

    prefixes = [v for v in prefixes if v]
    suffixes = [v for v in suffixes if v]

    requirements = sorted(list(set(requirements)))
    requirements = [v for v in requirements if v]

    return prefixes + requirements + suffixes

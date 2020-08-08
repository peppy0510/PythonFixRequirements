# encoding: utf-8


'''
author: Taehong Kim
email: peppy0510@hotmail.com

requirements:

description:

reference:

'''


import os
import sys

import sublime
import sublime_plugin

sys.path.append(os.path.dirname(sys.executable))

try:
    from python_fix_requirements import python_fix_requirements
except ImportError:
    from .python_fix_requirements import python_fix_requirements


class PythonFixRequirementsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        permute_lines(python_fix_requirements, self.view, edit)


def shrink_wrap_region(view, region):
    a, b = region.begin(), region.end()

    for a in range(a, b):
        if not view.substr(a).isspace():
            break

    for b in range(b - 1, a, -1):
        if not view.substr(b).isspace():
            b += 1
            break

    return sublime.Region(a, b)


def shrinkwrap_and_expand_non_empty_selections_to_entire_line(v):
    sw = shrink_wrap_region
    regions = []

    for sel in v.sel():
        if not sel.empty():
            regions.append(v.line(sw(v, v.line(sel))))
            v.sel().subtract(sel)

    for r in regions:
        v.sel().add(r)


def permute_lines(f, v, e):
    shrinkwrap_and_expand_non_empty_selections_to_entire_line(v)

    regions = [s for s in v.sel() if not s.empty()]
    if not regions:
        regions = [sublime.Region(0, v.size())]

    regions.sort(reverse=True)

    for r in regions:
        txt = v.substr(r)
        lines = txt.splitlines()
        sorted_lines = f(lines)

        if sorted_lines != lines:
            v.replace(e, r, '\n'.join(sorted_lines))

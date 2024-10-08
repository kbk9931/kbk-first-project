"""
This type stub file was generated by pyright.
"""

from typing import List

"""Implementations for various useful completers.

These are all loaded by default by IPython.
"""
_suffixes = ...
TIMEOUT_STORAGE = ...
TIMEOUT_GIVEUP = ...
import_re = ...
magic_run_re = ...
def module_list(path):
    """
    Return the list containing the names of the modules available in the given
    folder.
    """
    ...

def get_root_modules():
    """
    Returns a list containing the names of all the modules available in the
    folders of the pythonpath.

    ip.db['rootmodules_cache'] maps sys.path entries to list of modules.
    """
    ...

def is_importable(module, attr, only_modules):
    ...

def is_possible_submodule(module, attr):
    ...

def try_import(mod: str, only_modules=...) -> List[str]:
    """
    Try to import given module and return list of potential completions.
    """
    ...

def quick_completer(cmd, completions): # -> None:
    r""" Easily create a trivial completer for a command.

    Takes either a list of completions, or all completions in string (that will
    be split on whitespace).

    Example::

        [d:\ipython]|1> import ipy_completers
        [d:\ipython]|2> ipy_completers.quick_completer('foo', ['bar','baz'])
        [d:\ipython]|3> foo b<TAB>
        bar baz
        [d:\ipython]|3> foo ba
    """
    ...

def module_completion(line): # -> None:
    """
    Returns a list containing the completion possibilities for an import line.

    The line looks like this :
    'import xml.d'
    'from xml.dom import'
    """
    ...

def module_completer(self, event): # -> None:
    """Give completions after user has typed 'import ...' or 'from ...'"""
    ...

def magic_run_completer(self, event):
    """Complete files that end in .py or .ipy or .ipynb for the %run command.
    """
    ...

def cd_completer(self, event):
    """Completer function for cd, which only returns directories."""
    ...

def reset_completer(self, event):
    "A completer for %reset magic"
    ...


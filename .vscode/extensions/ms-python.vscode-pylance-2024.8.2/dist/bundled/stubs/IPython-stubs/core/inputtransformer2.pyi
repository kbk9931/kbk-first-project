"""
This type stub file was generated by pyright.
"""

import tokenize
from codeop import CommandCompiler, Compile
from typing import List, Tuple

"""Input transformer machinery to support IPython special syntax.

This includes the machinery to recognise and transform ``%magic`` commands,
``!system`` commands, ``help?`` querying, prompt stripping, and so forth.

Added: IPython 7.0. Replaces inputsplitter and inputtransformer which were
deprecated in 7.0.
"""
_indent_re = ...
def leading_empty_lines(lines):
    """Remove leading empty lines

    If the leading lines are empty or contain only whitespace, they will be
    removed.
    """
    ...

def leading_indent(lines):
    """Remove leading indentation.

    If the first line starts with a spaces or tabs, the same whitespace will be
    removed from each following line in the cell.
    """
    ...

class PromptStripper:
    """Remove matching input prompts from a block of input.

    Parameters
    ----------
    prompt_re : regular expression
        A regular expression matching any input prompt (including continuation,
        e.g. ``...``)
    initial_re : regular expression, optional
        A regular expression matching only the initial prompt, but not continuation.
        If no initial expression is given, prompt_re will be used everywhere.
        Used mainly for plain Python prompts (``>>>``), where the continuation prompt
        ``...`` is a valid Python expression in Python 3, so shouldn't be stripped.

    Notes
    -----

    If initial_re and prompt_re differ,
    only initial_re will be tested against the first line.
    If any prompt is found on the first two lines,
    prompts will be stripped from the rest of the block.
    """
    def __init__(self, prompt_re, initial_re=...) -> None:
        ...
    
    def __call__(self, lines):
        ...
    


classic_prompt = ...
ipython_prompt = ...
def cell_magic(lines):
    ...

def find_end_of_continued_line(lines, start_line: int):
    """Find the last line of a line explicitly extended using backslashes.

    Uses 0-indexed line numbers.
    """
    ...

def assemble_continued_line(lines, start: Tuple[int, int], end_line: int):
    r"""Assemble a single line from multiple continued line pieces

    Continued lines are lines ending in ``\``, and the line following the last
    ``\`` in the block.

    For example, this code continues over multiple lines::

        if (assign_ix is not None) \
             and (len(line) >= assign_ix + 2) \
             and (line[assign_ix+1].string == '%') \
             and (line[assign_ix+2].type == tokenize.NAME):

    This statement contains four continued line pieces.
    Assembling these pieces into a single line would give::

        if (assign_ix is not None) and (len(line) >= assign_ix + 2) and (line[...

    This uses 0-indexed line numbers. *start* is (lineno, colno).

    Used to allow ``%magic`` and ``!system`` commands to be continued over
    multiple lines.
    """
    ...

class TokenTransformBase:
    """Base class for transformations which examine tokens.

    Special syntax should not be transformed when it occurs inside strings or
    comments. This is hard to reliably avoid with regexes. The solution is to
    tokenise the code as Python, and recognise the special syntax in the tokens.

    IPython's special syntax is not valid Python syntax, so tokenising may go
    wrong after the special syntax starts. These classes therefore find and
    transform *one* instance of special syntax at a time into regular Python
    syntax. After each transformation, tokens are regenerated to find the next
    piece of special syntax.

    Subclasses need to implement one class method (find)
    and one regular method (transform).

    The priority attribute can select which transformation to apply if multiple
    transformers match in the same place. Lower numbers have higher priority.
    This allows "%magic?" to be turned into a help call rather than a magic call.
    """
    priority = ...
    def sortby(self):
        ...
    
    def __init__(self, start) -> None:
        ...
    
    @classmethod
    def find(cls, tokens_by_line):
        """Find one instance of special syntax in the provided tokens.

        Tokens are grouped into logical lines for convenience,
        so it is easy to e.g. look at the first token of each line.
        *tokens_by_line* is a list of lists of tokenize.TokenInfo objects.

        This should return an instance of its class, pointing to the start
        position it has found, or None if it found no match.
        """
        ...
    
    def transform(self, lines: List[str]):
        """Transform one instance of special syntax found by ``find()``

        Takes a list of strings representing physical lines,
        returns a similar list of transformed lines.
        """
        ...
    


class MagicAssign(TokenTransformBase):
    """Transformer for assignments from magics (a = %foo)"""
    @classmethod
    def find(cls, tokens_by_line): # -> None:
        """Find the first magic assignment (a = %foo) in the cell.
        """
        ...
    
    def transform(self, lines: List[str]):
        """Transform a magic assignment found by the ``find()`` classmethod.
        """
        ...
    


class SystemAssign(TokenTransformBase):
    """Transformer for assignments from system commands (a = !foo)"""
    @classmethod
    def find(cls, tokens_by_line): # -> None:
        """Find the first system assignment (a = !foo) in the cell.
        """
        ...
    
    def transform(self, lines: List[str]):
        """Transform a system assignment found by the ``find()`` classmethod.
        """
        ...
    


ESC_SHELL = ...
ESC_SH_CAP = ...
ESC_HELP = ...
ESC_HELP2 = ...
ESC_MAGIC = ...
ESC_MAGIC2 = ...
ESC_QUOTE = ...
ESC_QUOTE2 = ...
ESC_PAREN = ...
ESCAPE_SINGLES = ...
ESCAPE_DOUBLES = ...
tr = ...
class EscapedCommand(TokenTransformBase):
    """Transformer for escaped commands like %foo, !foo, or /foo"""
    @classmethod
    def find(cls, tokens_by_line): # -> None:
        """Find the first escaped command (%foo, !foo, etc.) in the cell.
        """
        ...
    
    def transform(self, lines):
        """Transform an escaped line found by the ``find()`` classmethod.
        """
        ...
    


_help_end_re = ...
class HelpEnd(TokenTransformBase):
    """Transformer for help syntax: obj? and obj??"""
    priority = ...
    def __init__(self, start, q_locn) -> None:
        ...
    
    @classmethod
    def find(cls, tokens_by_line): # -> None:
        """Find the first help command (foo?) in the cell.
        """
        ...
    
    def transform(self, lines):
        """Transform a help command found by the ``find()`` classmethod.
        """
        ...
    


def make_tokens_by_line(lines: List[str]):
    """Tokenize a series of lines and group tokens by line.

    The tokens for a multiline Python string or expression are grouped as one
    line. All lines except the last lines should keep their line ending ('\\n',
    '\\r\\n') for this to properly work. Use `.splitlines(keeplineending=True)`
    for example when passing block of text to this function.

    """
    ...

def has_sunken_brackets(tokens: List[tokenize.TokenInfo]):
    """Check if the depth of brackets in the list of tokens drops below 0"""
    ...

def show_linewise_tokens(s: str): # -> None:
    """For investigation and debugging"""
    ...

TRANSFORM_LOOP_LIMIT = ...
class TransformerManager:
    """Applies various transformations to a cell or code block.

    The key methods for external use are ``transform_cell()``
    and ``check_complete()``.
    """
    def __init__(self) -> None:
        ...
    
    def do_one_token_transform(self, lines):
        """Find and run the transform earliest in the code.

        Returns (changed, lines).

        This method is called repeatedly until changed is False, indicating
        that all available transformations are complete.

        The tokens following IPython special syntax might not be valid, so
        the transformed code is retokenised every time to identify the next
        piece of special syntax. Hopefully long code cells are mostly valid
        Python, not using lots of IPython special syntax, so this shouldn't be
        a performance issue.
        """
        ...
    
    def do_token_transforms(self, lines):
        ...
    
    def transform_cell(self, cell: str) -> str:
        """Transforms a cell of input code"""
        ...
    
    def check_complete(self, cell: str):
        """Return whether a block of code is ready to execute, or should be continued

        Parameters
        ----------
        cell : string
            Python input code, which can be multiline.

        Returns
        -------
        status : str
            One of 'complete', 'incomplete', or 'invalid' if source is not a
            prefix of valid code.
        indent_spaces : int or None
            The number of spaces by which to indent the next line of code. If
            status is not 'incomplete', this is None.
        """
        ...
    


def find_last_indent(lines):
    ...

class MaybeAsyncCompile(Compile):
    def __init__(self, extra_flags=...) -> None:
        ...
    


class MaybeAsyncCommandCompiler(CommandCompiler):
    def __init__(self, extra_flags=...) -> None:
        ...
    


_extra_flags = ...
compile_command = ...

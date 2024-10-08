"""
This type stub file was generated by pyright.
"""

import ast
import timeit
from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, line_cell_magic, line_magic, magics_class, needs_local_scope, no_var_expand, output_can_be_silenced
from IPython.testing.skipdoctest import skip_doctest

"""Implementation of execution-related magic functions."""
class TimeitResult:
    """
    Object returned by the timeit magic with info about the run.

    Contains the following attributes :

    loops: (int) number of loops done per measurement
    repeat: (int) number of times the measurement has been repeated
    best: (float) best execution time / number
    all_runs: (list of float) execution time of each run (in s)
    compile_time: (float) time of statement compilation (s)

    """
    def __init__(self, loops, repeat, best, worst, all_runs, compile_time, precision) -> None:
        ...
    
    @property
    def average(self):
        ...
    
    @property
    def stdev(self):
        ...
    
    def __str__(self) -> str:
        ...
    


class TimeitTemplateFiller(ast.NodeTransformer):
    """Fill in the AST template for timing execution.

    This is quite closely tied to the template definition, which is in
    :meth:`ExecutionMagics.timeit`.
    """
    def __init__(self, ast_setup, ast_stmt) -> None:
        ...
    
    def visit_FunctionDef(self, node):
        "Fill in the setup statement"
        ...
    
    def visit_For(self, node):
        "Fill in the statement to be timed"
        ...
    


class Timer(timeit.Timer):
    """Timer class that explicitly uses self.inner
    
    which is an undocumented implementation detail of CPython,
    not shared by PyPy.
    """
    def timeit(self, number=...):
        """Time 'number' executions of the main statement.

        To be precise, this executes the setup statement once, and
        then returns the time it takes to execute the main statement
        a number of times, as a float measured in seconds.  The
        argument is the number of times through the loop, defaulting
        to one million.  The main statement, the setup statement and
        the timer function to be used are passed to the constructor.
        """
        ...
    


@magics_class
class ExecutionMagics(Magics):
    """Magics related to code execution, debugging, profiling, etc.

    """
    def __init__(self, shell) -> None:
        ...
    
    @skip_doctest
    @no_var_expand
    @line_cell_magic
    def prun(self, parameter_s=..., cell=...): # -> Stats | None:
        """Run a statement through the python code profiler.

        Usage, in line mode:
          %prun [options] statement

        Usage, in cell mode:
          %%prun [options] [statement]
          code...
          code...

        In cell mode, the additional code lines are appended to the (possibly
        empty) statement in the first line.  Cell mode allows you to easily
        profile multiline blocks without having to put them in a separate
        function.

        The given statement (which doesn't require quote marks) is run via the
        python profiler in a manner similar to the profile.run() function.
        Namespaces are internally managed to work correctly; profile.run
        cannot be used in IPython because it makes certain assumptions about
        namespaces which do not hold under IPython.

        Options:

        -l <limit>
          you can place restrictions on what or how much of the
          profile gets printed. The limit value can be:

             * A string: only information for function names containing this string
               is printed.

             * An integer: only these many lines are printed.

             * A float (between 0 and 1): this fraction of the report is printed
               (for example, use a limit of 0.4 to see the topmost 40% only).

          You can combine several limits with repeated use of the option. For
          example, ``-l __init__ -l 5`` will print only the topmost 5 lines of
          information about class constructors.

        -r
          return the pstats.Stats object generated by the profiling. This
          object has all the information about the profile in it, and you can
          later use it for further analysis or in other functions.

        -s <key>
          sort profile by given key. You can provide more than one key
          by using the option several times: '-s key1 -s key2 -s key3...'. The
          default sorting key is 'time'.

          The following is copied verbatim from the profile documentation
          referenced below:

          When more than one key is provided, additional keys are used as
          secondary criteria when the there is equality in all keys selected
          before them.

          Abbreviations can be used for any key names, as long as the
          abbreviation is unambiguous.  The following are the keys currently
          defined:

          ============  =====================
          Valid Arg     Meaning
          ============  =====================
          "calls"       call count
          "cumulative"  cumulative time
          "file"        file name
          "module"      file name
          "pcalls"      primitive call count
          "line"        line number
          "name"        function name
          "nfl"         name/file/line
          "stdname"     standard name
          "time"        internal time
          ============  =====================

          Note that all sorts on statistics are in descending order (placing
          most time consuming items first), where as name, file, and line number
          searches are in ascending order (i.e., alphabetical). The subtle
          distinction between "nfl" and "stdname" is that the standard name is a
          sort of the name as printed, which means that the embedded line
          numbers get compared in an odd way.  For example, lines 3, 20, and 40
          would (if the file names were the same) appear in the string order
          "20" "3" and "40".  In contrast, "nfl" does a numeric compare of the
          line numbers.  In fact, sort_stats("nfl") is the same as
          sort_stats("name", "file", "line").

        -T <filename>
          save profile results as shown on screen to a text
          file. The profile is still shown on screen.

        -D <filename>
          save (via dump_stats) profile statistics to given
          filename. This data is in a format understood by the pstats module, and
          is generated by a call to the dump_stats() method of profile
          objects. The profile is still shown on screen.

        -q
          suppress output to the pager.  Best used with -T and/or -D above.

        If you want to run complete programs under the profiler's control, use
        ``%run -p [prof_opts] filename.py [args to program]`` where prof_opts
        contains profiler specific options as described here.

        You can read the complete documentation for the profile module with::

          In [1]: import profile; profile.help()

        .. versionchanged:: 7.3
            User variables are no longer expanded,
            the magic line is always left unmodified.

        """
        ...
    
    @line_magic
    def pdb(self, parameter_s=...): # -> None:
        """Control the automatic calling of the pdb interactive debugger.

        Call as '%pdb on', '%pdb 1', '%pdb off' or '%pdb 0'. If called without
        argument it works as a toggle.

        When an exception is triggered, IPython can optionally call the
        interactive pdb debugger after the traceback printout. %pdb toggles
        this feature on and off.

        The initial state of this feature is set in your configuration
        file (the option is ``InteractiveShell.pdb``).

        If you want to just activate the debugger AFTER an exception has fired,
        without having to type '%pdb on' and rerunning your code, you can use
        the %debug magic."""
        ...
    
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('--breakpoint', '-b', metavar='FILE:LINE', help="""
        Set break point at LINE in FILE.
        """)
    @magic_arguments.argument('statement', nargs='*', help="""
        Code to run in debugger.
        You can omit this in cell magic mode.
        """)
    @no_var_expand
    @line_cell_magic
    @needs_local_scope
    def debug(self, line=..., cell=..., local_ns=...): # -> None:
        """Activate the interactive debugger.

        This magic command support two ways of activating debugger.
        One is to activate debugger before executing code.  This way, you
        can set a break point, to step through the code from the point.
        You can use this mode by giving statements to execute and optionally
        a breakpoint.

        The other one is to activate debugger in post-mortem mode.  You can
        activate this mode simply running %debug without any argument.
        If an exception has just occurred, this lets you inspect its stack
        frames interactively.  Note that this will always work only on the last
        traceback that occurred, so you must call this quickly after an
        exception that you wish to inspect has fired, because if another one
        occurs, it clobbers the previous one.

        If you want IPython to automatically do this on every exception, see
        the %pdb magic for more details.

        .. versionchanged:: 7.3
            When running code, user variables are no longer expanded,
            the magic line is always left unmodified.

        """
        ...
    
    @line_magic
    def tb(self, s): # -> None:
        """Print the last traceback.

        Optionally, specify an exception reporting mode, tuning the
        verbosity of the traceback. By default the currently-active exception
        mode is used. See %xmode for changing exception reporting modes.

        Valid modes: Plain, Context, Verbose, and Minimal.
        """
        ...
    
    @skip_doctest
    @line_magic
    def run(self, parameter_s=..., runner=..., file_finder=...):
        """Run the named file inside IPython as a program.

        Usage::

          %run [-n -i -e -G]
               [( -t [-N<N>] | -d [-b<N>] | -p [profile options] )]
               ( -m mod | filename ) [args]

        The filename argument should be either a pure Python script (with
        extension ``.py``), or a file with custom IPython syntax (such as
        magics). If the latter, the file can be either a script with ``.ipy``
        extension, or a Jupyter notebook with ``.ipynb`` extension. When running
        a Jupyter notebook, the output from print statements and other
        displayed objects will appear in the terminal (even matplotlib figures
        will open, if a terminal-compliant backend is being used). Note that,
        at the system command line, the ``jupyter run`` command offers similar
        functionality for executing notebooks (albeit currently with some
        differences in supported options).

        Parameters after the filename are passed as command-line arguments to
        the program (put in sys.argv). Then, control returns to IPython's
        prompt.

        This is similar to running at a system prompt ``python file args``,
        but with the advantage of giving you IPython's tracebacks, and of
        loading all variables into your interactive namespace for further use
        (unless -p is used, see below).

        The file is executed in a namespace initially consisting only of
        ``__name__=='__main__'`` and sys.argv constructed as indicated. It thus
        sees its environment as if it were being run as a stand-alone program
        (except for sharing global objects such as previously imported
        modules). But after execution, the IPython interactive namespace gets
        updated with all variables defined in the program (except for __name__
        and sys.argv). This allows for very convenient loading of code for
        interactive work, while giving each program a 'clean sheet' to run in.

        Arguments are expanded using shell-like glob match.  Patterns
        '*', '?', '[seq]' and '[!seq]' can be used.  Additionally,
        tilde '~' will be expanded into user's home directory.  Unlike
        real shells, quotation does not suppress expansions.  Use
        *two* back slashes (e.g. ``\\\\*``) to suppress expansions.
        To completely disable these expansions, you can use -G flag.

        On Windows systems, the use of single quotes `'` when specifying
        a file is not supported. Use double quotes `"`.

        Options:

        -n
          __name__ is NOT set to '__main__', but to the running file's name
          without extension (as python does under import).  This allows running
          scripts and reloading the definitions in them without calling code
          protected by an ``if __name__ == "__main__"`` clause.

        -i
          run the file in IPython's namespace instead of an empty one. This
          is useful if you are experimenting with code written in a text editor
          which depends on variables defined interactively.

        -e
          ignore sys.exit() calls or SystemExit exceptions in the script
          being run.  This is particularly useful if IPython is being used to
          run unittests, which always exit with a sys.exit() call.  In such
          cases you are interested in the output of the test results, not in
          seeing a traceback of the unittest module.

        -t
          print timing information at the end of the run.  IPython will give
          you an estimated CPU time consumption for your script, which under
          Unix uses the resource module to avoid the wraparound problems of
          time.clock().  Under Unix, an estimate of time spent on system tasks
          is also given (for Windows platforms this is reported as 0.0).

        If -t is given, an additional ``-N<N>`` option can be given, where <N>
        must be an integer indicating how many times you want the script to
        run.  The final timing report will include total and per run results.

        For example (testing the script uniq_stable.py)::

            In [1]: run -t uniq_stable

            IPython CPU timings (estimated):
              User  :    0.19597 s.
              System:        0.0 s.

            In [2]: run -t -N5 uniq_stable

            IPython CPU timings (estimated):
            Total runs performed: 5
              Times :      Total       Per run
              User  :   0.910862 s,  0.1821724 s.
              System:        0.0 s,        0.0 s.

        -d
          run your program under the control of pdb, the Python debugger.
          This allows you to execute your program step by step, watch variables,
          etc.  Internally, what IPython does is similar to calling::

              pdb.run('execfile("YOURFILENAME")')

          with a breakpoint set on line 1 of your file.  You can change the line
          number for this automatic breakpoint to be <N> by using the -bN option
          (where N must be an integer). For example::

              %run -d -b40 myscript

          will set the first breakpoint at line 40 in myscript.py.  Note that
          the first breakpoint must be set on a line which actually does
          something (not a comment or docstring) for it to stop execution.

          Or you can specify a breakpoint in a different file::

              %run -d -b myotherfile.py:20 myscript

          When the pdb debugger starts, you will see a (Pdb) prompt.  You must
          first enter 'c' (without quotes) to start execution up to the first
          breakpoint.

          Entering 'help' gives information about the use of the debugger.  You
          can easily see pdb's full documentation with "import pdb;pdb.help()"
          at a prompt.

        -p
          run program under the control of the Python profiler module (which
          prints a detailed report of execution times, function calls, etc).

          You can pass other options after -p which affect the behavior of the
          profiler itself. See the docs for %prun for details.

          In this mode, the program's variables do NOT propagate back to the
          IPython interactive namespace (because they remain in the namespace
          where the profiler executes them).

          Internally this triggers a call to %prun, see its documentation for
          details on the options available specifically for profiling.

        There is one special usage for which the text above doesn't apply:
        if the filename ends with .ipy[nb], the file is run as ipython script,
        just as if the commands were written on IPython prompt.

        -m
          specify module name to load instead of script path. Similar to
          the -m option for the python interpreter. Use this option last if you
          want to combine with other %run options. Unlike the python interpreter
          only source modules are allowed no .pyc or .pyo files.
          For example::

              %run -m example

          will run the example module.

        -G
          disable shell-like glob expansion of arguments.

        """
        ...
    
    @skip_doctest
    @no_var_expand
    @line_cell_magic
    @needs_local_scope
    def timeit(self, line=..., cell=..., local_ns=...): # -> TimeitResult | None:
        """Time execution of a Python statement or expression

        Usage, in line mode:
          %timeit [-n<N> -r<R> [-t|-c] -q -p<P> -o] statement
        or in cell mode:
          %%timeit [-n<N> -r<R> [-t|-c] -q -p<P> -o] setup_code
          code
          code...

        Time execution of a Python statement or expression using the timeit
        module.  This function can be used both as a line and cell magic:

        - In line mode you can time a single-line statement (though multiple
          ones can be chained with using semicolons).

        - In cell mode, the statement in the first line is used as setup code
          (executed but not timed) and the body of the cell is timed.  The cell
          body has access to any variables created in the setup code.

        Options:
        -n<N>: execute the given statement <N> times in a loop. If <N> is not
        provided, <N> is determined so as to get sufficient accuracy.

        -r<R>: number of repeats <R>, each consisting of <N> loops, and take the
        best result.
        Default: 7

        -t: use time.time to measure the time, which is the default on Unix.
        This function measures wall time.

        -c: use time.clock to measure the time, which is the default on
        Windows and measures wall time. On Unix, resource.getrusage is used
        instead and returns the CPU user time.

        -p<P>: use a precision of <P> digits to display the timing result.
        Default: 3

        -q: Quiet, do not print result.

        -o: return a TimeitResult that can be stored in a variable to inspect
            the result in more details.

        .. versionchanged:: 7.3
            User variables are no longer expanded,
            the magic line is always left unmodified.

        Examples
        --------
        ::

          In [1]: %timeit pass
          8.26 ns ± 0.12 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)

          In [2]: u = None

          In [3]: %timeit u is None
          29.9 ns ± 0.643 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

          In [4]: %timeit -r 4 u == None

          In [5]: import time

          In [6]: %timeit -n1 time.sleep(2)

        The times reported by %timeit will be slightly higher than those
        reported by the timeit.py script when variables are accessed. This is
        due to the fact that %timeit executes the statement in the namespace
        of the shell, compared with timeit.py, which uses a single setup
        statement to import function or create variables. Generally, the bias
        does not matter as long as results from timeit.py are not mixed with
        those from %timeit."""
        ...
    
    @skip_doctest
    @no_var_expand
    @needs_local_scope
    @line_cell_magic
    @output_can_be_silenced
    def time(self, line=..., cell=..., local_ns=...): # -> None:
        """Time execution of a Python statement or expression.

        The CPU and wall clock times are printed, and the value of the
        expression (if any) is returned.  Note that under Win32, system time
        is always reported as 0, since it can not be measured.

        This function can be used both as a line and cell magic:

        - In line mode you can time a single-line statement (though multiple
          ones can be chained with using semicolons).

        - In cell mode, you can time the cell body (a directly
          following statement raises an error).

        This function provides very basic timing functionality.  Use the timeit
        magic for more control over the measurement.

        .. versionchanged:: 7.3
            User variables are no longer expanded,
            the magic line is always left unmodified.

        Examples
        --------
        ::

          In [1]: %time 2**128
          CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
          Wall time: 0.00
          Out[1]: 340282366920938463463374607431768211456L

          In [2]: n = 1000000

          In [3]: %time sum(range(n))
          CPU times: user 1.20 s, sys: 0.05 s, total: 1.25 s
          Wall time: 1.37
          Out[3]: 499999500000L

          In [4]: %time print 'hello world'
          hello world
          CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
          Wall time: 0.00

        .. note::
            The time needed by Python to compile the given expression will be
            reported if it is more than 0.1s.

            In the example below, the actual exponentiation is done by Python
            at compilation time, so while the expression can take a noticeable
            amount of time to compute, that time is purely due to the
            compilation::

                In [5]: %time 3**9999;
                CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
                Wall time: 0.00 s

                In [6]: %time 3**999999;
                CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
                Wall time: 0.00 s
                Compiler : 0.78 s
        """
        ...
    
    @skip_doctest
    @line_magic
    def macro(self, parameter_s=...): # -> None:
        """Define a macro for future re-execution. It accepts ranges of history,
        filenames or string objects.

        Usage:\\
          %macro [options] name n1-n2 n3-n4 ... n5 .. n6 ...

        Options:

          -r: use 'raw' input.  By default, the 'processed' history is used,
          so that magics are loaded in their transformed version to valid
          Python.  If this option is given, the raw input as typed at the
          command line is used instead.
          
          -q: quiet macro definition.  By default, a tag line is printed 
          to indicate the macro has been created, and then the contents of 
          the macro are printed.  If this option is given, then no printout
          is produced once the macro is created.

        This will define a global variable called `name` which is a string
        made of joining the slices and lines you specify (n1,n2,... numbers
        above) from your input history into a single string. This variable
        acts like an automatic function which re-executes those lines as if
        you had typed them. You just type 'name' at the prompt and the code
        executes.

        The syntax for indicating input ranges is described in %history.

        Note: as a 'hidden' feature, you can also use traditional python slice
        notation, where N:M means numbers N through M-1.

        For example, if your history contains (print using %hist -n )::

          44: x=1
          45: y=3
          46: z=x+y
          47: print x
          48: a=5
          49: print 'x',x,'y',y

        you can create a macro with lines 44 through 47 (included) and line 49
        called my_macro with::

          In [55]: %macro my_macro 44-47 49

        Now, typing `my_macro` (without quotes) will re-execute all this code
        in one pass.

        You don't need to give the line-numbers in order, and any given line
        number can appear multiple times. You can assemble macros with any
        lines from your input history in any order.

        The macro is a simple object which holds its value in an attribute,
        but IPython's display system checks for macros and executes them as
        code instead of printing them when you type their name.

        You can view a macro's contents by explicitly printing it with::

          print macro_name

        """
        ...
    
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('output', type=str, default='', nargs='?', help="""The name of the variable in which to store output.
        This is a utils.io.CapturedIO object with stdout/err attributes
        for the text of the captured output.

        CapturedOutput also has a show() method for displaying the output,
        and __call__ as well, so you can use that to quickly display the
        output.

        If unspecified, captured output is discarded.
        """)
    @magic_arguments.argument('--no-stderr', action="store_true", help="""Don't capture stderr.""")
    @magic_arguments.argument('--no-stdout', action="store_true", help="""Don't capture stdout.""")
    @magic_arguments.argument('--no-display', action="store_true", help="""Don't capture IPython's rich display.""")
    @cell_magic
    def capture(self, line, cell): # -> None:
        """run the cell, capturing stdout, stderr, and IPython's rich display() calls."""
        ...
    


def parse_breakpoint(text, current_file):
    '''Returns (file, line) for file:line and (current_file, line) for line'''
    ...


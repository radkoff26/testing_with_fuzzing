## Default fuzzing

This section presents sample of finding a bug using default method of fuzzing-testing.

The given program in file `test.py` finds bug in library [AdvancedHTMLParser](https://github.com/kata198/AdvancedHTMLParser) of version `9.0.2`.

The gist of the bug is that at some point of execution of the program with genetically-mutated input there is a chance to open debugger. This bug is described in this [issue](https://github.com/kata198/AdvancedHTMLParser/issues/18) at larger scale.

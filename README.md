# terminal_periods
This is a simple script for analyzing subject terms to identify duplicate terms that exist both with and without terminal periods (e.g. "Hats" and "Hats.").

The script accepts a filename as a command line argument. That file should contain one subject term per row; the first (header) row is skipped. The file should be in the same folder as the python script.

Each term is analyzed to see if the same term exists both with and without a period at the end. Whitespace and semicolons (thanks, CONTENTdm) are stripped from the end of each term for analysis. All duplicate terms found are output to a new file, which has "_results" appended to the original filename.

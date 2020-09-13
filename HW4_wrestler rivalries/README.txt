Suppose there are two types of professional wrestlers: “Babyfaces” (“good guys”) and “Heels” (“bad
guys”). Between any pair of professional wrestlers, there may or may not be a rivalry. Suppose we
have n wrestlers and we have a list of r pairs of rivalries.
(a) Give pseudocode for an efficient algorithm that determines whether it is possible to designate
some of the wrestlers as Babyfaces and the remainder as Heels such that each rivalry is between a
Babyface and a Heel. If it is possible to perform such a designation, your algorithm should produce
it.
(b) What is the running time of your algorithm?
(c) Implement: Babyfaces vs Heels.
Input: Input is read in from a file specified in the command line at run time. The file contains the
number of wrestlers, n, followed by their names, the number of rivalries r and rivalries listed in pairs.
Note: The file only contains one list of rivalries
Output: Results are outputted to the terminal.
• Yes, if possible followed by a list of the Babyface wrestlers and a list of the Heels.
• No, if impossible

Running Instructions:

Copy folder contents to FLIP and pass individaul file names to python command line program. Alternatively, run these console commands in the folder where files are located.
python wrestlergraph.py

Enter the enter the inut file into the command line (ex. "data.txt")
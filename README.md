# yabsat
YABSAT - Yet Another But Simple AIDE Tool

The goal of this repository is to show how extremely simple yet powerfull tools can be created with a few lines of code, reusing utilities that already exist (why reinvent the wheel when almost-perfect wheels are out there).

In this case, the output is a bash script that allow to perform AIDE operations - check what things have changed in a system from a known previous state.

What is needed?
- "find" utility
- "state" utility
- "diff" utility
With those three core utilities that are present in most of the GNU/Linux distros, a fairly depth analysis of a system can be carried out, without configuring complex dot files, neither launching daemons nor messing with admin inner guts. KISS principle at is finest.

Steps to use AIDE-ize a directory with the script:
1- Launch yabsat script to obtain the known state or "base snapshot"
  $> bash yabsat.bash ./interesting_dir
  $> mv yabsatlog* base_snapshot.txt
2- Play as usual with the system
3- Launch yabsat script to obtain a report of the modified state
  $> bash yabsat.bash ./interesting_dir
4- Diff the base snapshot with the last report. Enjoy the inquiry
  $> diff base_* yabsatlog*
  
Of course, this script is not as complete and powerful as HIDS tools. But sometimes (many times) you dont need that power. The previous steps allows you to detect creation, deletion and modification of the most typical linux file types. And by modification, it shall be understood the change in content as well as change in status (i.e chmod or chown).

Need more? The listed utilities -even the content of the script- can be used as a reliable base. Then, add the wrappers you want.

This script may not be fit to be used as a real AIDE tool, but it can be helpfull when dealing with complex applications that, uppon execution:
- modifies lot of files, without telling you what files are
- creates logs, without telling you where they are created
- perform subtle permisson changes that are hide to the user

Managing or simply learning to use such applications can be a real pain. Did you ever face a situation like this, and wondered "What changes has <insert_here_app> made?". If so, this less-than-10-lines script may be useful.

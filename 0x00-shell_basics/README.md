# Welcome to 0x00-shell_basics
### This readme describes what each and Every file is doing

`0-current_working_directory` - Prints the absolute path name of the current working directory.

`1-listit` - Display the content of the current directory.

`2-bring_me_home` - Changes the working directory to the user's home directory.

`3-listfiles` - Display current directory in a long format

`4-listmorefiles` - Display the current directory contents, including hidden files (starting with `.`).

`5-listfilesdigitonly` - Display current directory contents.
* long format
* with user and group IDs displayed numerically
* And hidden files (starting with `.`)

`6-firstdirectory` - Script that creates a directory named `my_first_directory` in the `/tmp/` directory.

`7-movethatfile` - Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`.

`8-firstdelete` - Deletes the file `betty` in `/tmp/my_first_directory`.

`9-firstdirdeletion` - Deletes the directory `my_first_directory` in the `/tmp` directory.

`10-back` - Changes the working directory to the previous one.

`11-lists` - lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

`12-file_type` - prints the type of the file named `iamafile` in the `/tmp` directory.

`13-symbolic_link` - Creates a symbolic link to `/bin/ls`, named __ls__

`14-copy_html` - copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

`100-lets_move` - Moves all files beginning with an uppercase letter to the directory `/tmp/u`.

`101-clean_emacs` - Deletes all files in the current working directory that end with the character `~`.

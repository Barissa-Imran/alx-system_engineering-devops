# Welcome to 0x02. Shell, I/O Redirections and filters

Below is an explanation of what each file does (description).

`0-hello_world` - Prints "Hello, World", followed by a new line to the standard output.

`1-confused_smiley` - Displays a confused smiley `(Ôo)`.

`2-hellofile` - Display the content of the /etc/passwd file.

`3-twofiles` - Display the content of `/etc/passwd` and `/etc/hosts`.

`4-lastlines` - Display the last 10 lines of `/etc/password`.

`5-firstlines` - Display the first 10 lines of `/etc/passwd`.

`6-third_line` - Displays the third line of the file `iacta`.

`7-file` Creates a file named named \*\\'"Best School"\'\\*$\?\*\*\*\*\*\*:) containing the text `Best School` ending by a new line.

`8-cwd_state` - Writes into a file `ls_cwd_content` the result of the command `ls -la`. If the file `la_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.

`9-duplicate_last_line` - Duplicates the last line of the file `iacta`.

`10-no_more_js` - Deletes all the regular files (not the directories) with a `.js`extension that present in the current directory and all its subfolders.

`11-directories` - Counts the number of directories and sub-directories in the current directory.

`12-newest_files` - Displays the 10 newest files in the current directory.

`13-unique` - Takes list of words as input and prints only words that appear exactly once.

`14-findthatword` - Display lines containing the pattern `root` from the file `/etc/passwd`.

`15-countthatword` - Displays the number of lines that contain the pattern "bin" in the file `/etc/passwd`.

`16-whatsnext` - Displays lines containing the pattern "root" and 3 lines after them in file `/etc/passwd`.

`17-hidethisword` - Displays all the lines in the file `/etc/passwd` that do not contain "bin".

`18-letteronly` - Display all the lies of the file `/etc/ssh/sshd_config` starting with a letter.
* Include capital letters

`19-AZ` - Replace all characters `A` and `C` from input to `Z` and `e` respectively.

`20-hiago` - Script that removes all letters `c` and `C` from input.

`21-reverse` - Script that reverse its input.

`22-users_and_homes` - Displays all users and their home directories, sorted by users.
* Based on the `/etc/passwd` file

`100-empty_casks` - Finds all empty files and directories in the current directory and all sub-directories.
* Display only the names of the files and directories (not the entire path)
* Lists hidden files
* One file name per line
* Listing ends with a new line

`101-gifs` - Lists all the files with a `.gif` extension in the current directory and all its sub-directories.
* Hidden files should not listed
* Only regular files (not directories) should be listed
* The names of the files should be displayed without their extensions
* The files should be sorted by byte values, but case-insensitive (file `aaa` should be listed before file `bbb`, file `.b` should be listed before file `a`, and file `Rona` should be listed after file `jay`)
* One file name per line
* The listing should end with a new line

`102-acrostic` - Decodes acrostics that use the first letter of each line.
* decoded line has to end with a new line

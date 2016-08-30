# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> * less - page through a file
> * cat - print the whole file
> * xargs - execute arguments
> * grep - find things inside of files
> * apropos - find what manual page is appropriate
> * popd - pop directory
> * pushd - push directory
> * exit - exits the shell
> * sudo - become super user root
> * export - sets a new environment variable

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> * **ls** lists files and directories within a directory
> * **ls -a** displays all files, including hidden files, plus directories 
> * **ls -l** displays the long format listing, including permissions, last date edited, etc
> * **ls -lh** same as above, but filesize is more readable, i.e. in kb, gb, or b
> * **ls -lah** same as above, but also includes hidden files
> * **ls -t** same as ls, but listedn in order of last date edited, newest first
> * **ls -Glp** long format, directories with / after, directory names highlighted


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> * **ls -lR** shows the files in every sub directory 
> * **ls -Gmp** shows the files as a comma-separated list, directories highlighted and with a backslash after
> * **ls -1** each entry gets its own line
> * **ls -Tl** long entry form, with full timestamp shown (MM:dd: HH:MM:ss YYYY)
> * **ls -F** files are "flagged", i.e. directories show backslashs, and executables shown with '*'


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > Executes arguments. Xargs can handle shell commands in a way that is sometimes safer than calling commands directly. For example, you can use 'cp' to copy files from one directory to another, but if you run out of RAM of throw an error, the entire operation will fail.  
> > So instead of using cp to copy all JPEGs from one directory to another, you could type the following:  
```console
$ find /photos/ -type f -name "*.jpg" -print0 | xargs -0 -r -I file cp -v -p file --target-directory=/new/photos
``` 

 


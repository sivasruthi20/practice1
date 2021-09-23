
CHSS@DESKTOP-QTGPIE8 MINGW64 ~
$ ls
'3D Objects'/
 AppData/
'Application Data'@
 Contacts/
 Cookies@
 Desktop/
 Documents/
 Downloads/
 Favorites/
 IntelGraphicsProfiles/
 Links/
'Local Settings'@
 Music/
'My Documents'@
 NTUSER.DAT
 NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TM.blf
 NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000001.regtrans-ms
 NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000002.regtrans-ms
 NetHood@
 OneDrive/
 Pictures/
 PrintHood@
 PycharmProjects/
 Recent@
'Saved Games'/
 Searches/
 SendTo@
'Start Menu'@
 Templates@
 Videos/
 ntuser.dat.LOG1
 ntuser.dat.LOG2
 ntuser.ini

CHSS@DESKTOP-QTGPIE8 MINGW64 ~
$ ^C

CHSS@DESKTOP-QTGPIE8 MINGW64 ~
$ cd Desktop

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop
$ mkdir folder

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop
$ ls
'178345-Siva Sruthi Chappidi(set 1).txt'   desktop.ini
'178345-Siva Sruthi Chappidi(set2).txt'    folder/
'Siva Sruthi Chappidi(set1).txt'           gitdemo/
'Siva Sruthi Chappidi(set2).txt'

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop
$ cd folder

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder
$ ls

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder
$ git init
Initialized empty Git repository in C:/Users/Dell/Desktop/folder/.git/

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ mkdir f1

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ cd f1

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ touch c1.txt c2.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ ls
c1.txt  c2.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ cd ..

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        f1/

nothing added to commit but untracked files present (use "git add" to track)

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ git add f1

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   f1/c1.txt
        new file:   f1/c2.txt


CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ git commit -m "adding files c1.txt and c2.txt"
[master (root-commit) 5f21c77] adding files c1.txt and c2.txt
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 f1/c1.txt
 create mode 100644 f1/c2.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ git log
commit 5f21c77de0798a11d4883432735b96c5e3ee29db (HEAD -> master)
Author: sivasruthi <sivasruthi20@gmail.com>
Date:   Thu Sep 23 09:41:11 2021 +0530

    adding files c1.txt and c2.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ cd f1

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ vi c1.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ cat c1.txt
hai, I am Siva Sruthi from Vijaywada


CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ vi c2.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ cat c2.txt
I am working in UST Global.


CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ cd ..

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ mkdir f2

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ cd f2

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f2 (master)
$ cd ..

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ cp f1/c1.txt f2/copy1.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ cd f2

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f2 (master)
$ ls
copy1.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f2 (master)
$ cat copy1.txt
hai, I am Siva Sruthi from Vijaywada


CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f2 (master)
$ mv copy1.txt file1.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f2 (master)
$ ls
file1.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f2 (master)
$ cat file1.txt
hai, I am Siva Sruthi from Vijaywada


CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f2 (master)
$ cd ..

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ mv f2/file1.txt f1

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder (master)
$ cd f1

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ ls
c1.txt  c2.txt  file1.txt

CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$ cat file1.txt
hai, I am Siva Sruthi from Vijaywada


CHSS@DESKTOP-QTGPIE8 MINGW64 ~/Desktop/folder/f1 (master)
$

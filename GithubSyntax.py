### Github Syntax

git config --global

# set account
git config --global user.name "[username]"
git config --global user.email "[email]"

# view git.config
git config --global core.editor "code --wait"
git config --global -e

# windows setup
git config --global core.autocrlf true

# help
git config --help
git config -h

# Creating a github directory
mkdir [name]
cd [name] # moves to that folder
cls # clears page
git init # creates repo
rm -rf .git # deletes git repo
dir # shows what is in the folder
rmdir .git # delete git repo

# commands
clone # copy a repo to your local machine
add # track your files and changes in git
commit # save your files in git
push # upload git commits to a remote repo like Github

# demo repo
git init
git add READ.md #md = mark down
git commit -m "initial commit"
git remote add origin git@github.com/fusilladin/[repo-name]
git push -u origin master


# commands
git status # view changes made to files
git add . # track all files listed
git add index.html # add specific file/folder
git log # see all of your logs and descriptions

###############
########

### commiting to update the repo
git commit -m "[title]" -m "[description]"
git push -u origin master # sets the upstream

git remote add origin "[repo-url]" # add repo source to push to
git remote -v # check origin
git remote set-url ssh://git@github.com/Fusilladin/demo-repo2.git


### ORDER OR OPERATIONS PUSHING:
git init
git status
(create repo on website)
git pull '[url].git'
git add README.md // git add .
git status
git commit -m "Created README" -m "description"
git remote add origin "[repo-url], '.git'"
git -v
git push -u origin master
(change branch from main to master on Github)
# branching

git branch # shows all of the branches (*green=current)
git checkout # used to switch between branches
git checkout -b feature-readme-instructions # create a new branch
git checkout master # switches to master branch
git branch -d [name] # deletes the branch

git diff "[branch-name]"
git merge "[branch name]" # could do this to update the branch
git push -u origin [feature1] # typically just update the github

# advanced Syntax

git commit -am "[description]" # modified files, add & commit shortcut

### undo commits

git reset [name of file] # undos add command
git reset HEAD~1 #undos commit by 1
git log # see all of your logs and descriptions
git reset [commit hash] # undo commit by specific hash
git reset --hard # unstage, remove changes

# pull requests

git pull '[url].git'# combination of fetch and merge







#

# Git Cheat Sheet

## Getting Started
- `git init` : Initialize a new Git repository
- `git status` : Show the working directory status

### Clone
- `git clone <repo>` : Clone an existing repository

### Commit
- `git add <file>` : Add a file to the staging area
- `git commit -m "message"` : Commit changes with a message

### Branch
- `git branch` : List branches
- `git branch <branch>` : Create a new branch
- `git checkout <branch>` : Switch to a branch
- `git merge <branch>` : Merge a branch into the current branch

### Push
- `git push` : Push changes to the remote repository

### Pull
- `git pull` : Fetch and merge changes from the remote repository

## History
- `git log` : Show commit history
- `git diff` : Show changes between commits, branches, etc.
- `git blame <file>` : Show what revision and author last modified each line of a file

## Undoing Changes
- `git reset <file>` : Unstage a file
- `git checkout -- <file>` : Discard changes in the working directory
- `git revert <commit>` : Revert a commit by creating a new commit

## Remote Repositories
- `git remote -v` : List remote repositories
- `git remote add <name> <url>` : Add a new remote repository
- `git fetch <remote>` : Fetch changes from a remote repository

## Stashing
- `git stash` : Stash changes in a dirty working directory
- `git stash apply` : Apply stashed changes

## Tags
- `git tag` : List tags
- `git tag <tagname>` : Create a new tag
- `git push <remote> <tagname>` : Push a tag to a remote repository

## Configuration
- `git config --global user.name "name"` : Set the global username
- `git config --global user.email "email"` : Set the global email

## Issues
- `git issue list` : List all issues
- `git issue create` : Create a new issue
- `git issue close <issue>` : Close an issue

## Pull Requests
- `gh pr list` : List all pull requests
- `git pr create` : Create a new pull request
- `git pr merge <pr>` : Merge a pull request

## Private Repositories
- `git repo create <repo> --private` : Create a new private repository
- `git repo clone <repo>` : Clone a private repository

## Releases
- `git release list` : List all releases
- `git release create <tag> -m "message"` : Create a new release
- `git release delete <tag>` : Delete a release


For more detailed information, refer to the [official Git documentation](https://git-scm.com/doc).
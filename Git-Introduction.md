# Git Exercises

## Introduction

In LoD, Create a new folder called Documents/gitlearn1, open it in VScode, Initialise the folder as git repo.

Open a terminal pane in VSCode **(View > Terminal)** and set up your user details with

```bash
git config --global user.name "Your Name"
git config --global user.email "work@email"
```

Create two .txt files, edit their content, use `git add <filename>`, `git commit -m "msg"`, then view timeline.

Create a new branch called `newpara`, checkout the branch. Add more text to a file, add and commit the changes, switch between main and newpara branches to observe the changes.

Switch to main branch and do `git merge newpara` 
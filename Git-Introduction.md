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

## Working with remote code repositories

- Create an account in Github (or use an existing one)
- Create a repository in Github. (make the name relevent to the course)
  - Make it Public
  - Add a README
- Create a PAT for your account (classic)
  - <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>
- Clone your repository to your LoD machine
  - `git clone <https url>`
- Open the folder in VSCode
- Create a new file and add some contents
- Stage (add), and commit the changes to the local repo
- push the changes back to GitHub, use the Token to authenticate

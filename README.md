# mygit – A Minimal Version Control System in Python

`mygit` is a simplified, command-line version control system built using Python. It mimics core functionalities of Git including initializing repositories, staging files, committing changes, creating branches, and checking out commits or branches.

---

## 🧠 Project Summary

This project was built as part of Week 5 of a summer learning program to understand how version control systems like Git work under the hood. It was designed to reinforce core concepts like:

- File system operations
- Hashing and object storage
- Commit tracking and parent-child relationships
- HEAD pointer logic
- Branching and checkout mechanisms

---

## 🚀 Features Implemented

### ✅ `mygit init`
Initializes a `.mygit/` directory with folders for:
- `objects/` – for storing blob hashes
- `commits/` – to track commit metadata
- `refs/heads/` – to store branch pointers
- `HEAD` – points to the current branch or commit

### ✅ `mygit add <filename>`
Stages the file by:
- Hashing the content
- Saving it in `.mygit/objects/`
- Recording it in `.mygit/index`

### ✅ `mygit commit -m "message"`
Commits all staged files by:
- Creating a metadata file in `.mygit/commits/`
- Linking to the parent commit
- Updating the current branch HEAD

### ✅ `mygit branch`
Lists all available branches in `refs/heads/`  
Also shows the current branch using `*`.

### ✅ `mygit checkout <commit-hash>`
Checks out a specific commit by:
- Restoring file contents to working directory
- Updating `HEAD` to point directly to the commit

### ✅ `mygit checkout <branch-name>`
Switches to a branch by:
- Reading the commit hash pointed to by `refs/heads/<branch>`
- Restoring files from that commit
- Updating `HEAD` to point to `ref: refs/heads/<branch>`

### ✅ `mygit checkout -b <branch-name>`
Creates a new branch from the current commit and switches to it.

### ✅ `mygit log`
Displays commit history by traversing parent pointers from HEAD.

### ✅ `mygit status`
Shows staged files, untracked files, and file modifications (basic).

---

## 🛠 Folder Structure

    mygit/
    ├── main.py
    ├── src/
    │ ├── add.py
    │ ├── branch.py
    │ ├── checkout.py
    │ ├── commit.py
    │ ├── init.py
    │ ├── log.py
    │ └── status.py
    └── .mygit/
    ├── objects/
    ├── commits/
    ├── refs/
    │ └── heads/
    └── HEAD


---

## 📦 Example Commands

```bash
python main.py init
python main.py add test.txt
python main.py commit -m "Initial commit"
python main.py branch
python main.py checkout -b dev
python main.py commit -m "Dev changes"
python main.py checkout master
```


## 📌 Key Learnings
- How Git internally manages objects, branches, and commits
- Implementing a simplified object database using SHA1 hashes
- File restoration logic through checkout
- Tracking changes with commit ancestry
- Simulating HEAD and refs behavior


## ⚙️ Limitations
- No support for merge or conflict resolution
- File rename tracking not implemented
- status is basic (no diff comparison)
- Does not support remote pushing/pulling


### This project gave hands-on experience with how Git works internally and significantly improved understanding of version control principles. All core functionalities were implemented from scratch using only Python’s standard library and file system.

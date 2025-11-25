---
layout: intro
color: blue
transition: fade
class: text-center
zoom: 1
hideInToc: false
lineNumbers: true
selectable: true
---

# Setup Python and Git for Software Development

## Git, Github, Python and VS Code

---
layout: top-title
color: blue-light
---
::title::

# Git

::content::

Git is a <v-mark>version control system</v-mark> that allows you to track changes in your code and collaborate with others. It runs on your screen and can be accessed (by default) via the Terminal as a command line interface (CLI).

### Check if Git is installed

You may already have Git installed. To check, open your Terminal and run:

```bash

git --version

```

### To install Git:

- **Windows**: Download and install from [git-scm.com](https://git-scm.com/download/win).
- **macOS**: See if it is already installed by running `git --version` in the Terminal. If not, install it with `xcode-select --install`. 
- **Linux**: Install via your package manager, e.g., `sudo apt-get install git` for Debian-based systems.

---
layout: top-title
color: blue
---

::title::

# GitHub

::content::

GitHub is the most popular web platform for hosting and collaborating on Git repositories. It provides a web interface to manage your code, track issues, and collaborate with others.

**We will use GitHub for your assignments and projects.**

If you already have a GitHub account, you can skip this step.

### To create a GitHub account:

1. Go to [github.com](https://github.com)
2. Click on "Sign up" and follow the instructions to create your account.
3. Choose a username, enter your email address, and set a password. (Make sure your username is professional as it will be visible to others.)
4. Verify your email address by clicking on the link sent to your email.

---
layout: top-title
color: blue-light
---
::title::

# Configure Git with GitHub

::content::

After installing Git and creating a GitHub account, you need to configure Git to work with your GitHub account.

### Set your Git username and email
Open your Terminal and run the following commands, replacing `your_username` and `your_email` with your GitHub username and email address:

```bash
git config --global user.name "your_username"
```
```bash
git config --global user.email "your_email"
```

*(Use the same email you used to sign up for GitHub. This links your commits to your GitHub account.)*

---
layout: top-title
color: sky
---

::title::

# Setup VS Code

::content::

[Visual Studio Code (VS Code)](https://code.visualstudio.com/) is a popular code editor that supports many programming languages and has built-in Git support.

### To install VS Code:
1. Go to [code.visualstudio.com](https://code.visualstudio.com/)
2. Download the installer for your operating system (Windows, macOS, or Linux).
3. Run the installer and follow the instructions to complete the installation.
4. Once installed, open VS Code. To enable our work together, you should make sure you have the following Extensions installed:
   - Python (by Microsoft) **Required**
   - indent-rainbow (by oderwat) **Optional**
   - GitLens (by GitKraken) **Optional**

---
layout: top-title-two-cols
color: blue
---
::title::

# Setup Python using uv

::left::

Python is the programming language we will use for this course. I recommend using `uv`, a simple Python version manager, to install and manage Python versions. 

### To install uv:

1. Open your Terminal (Now that you have VS Code, you can use its integrated terminal).
2. Install `uv` by copying and pasting the relevant command
**Windows (PowerShell)**:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux**:

```bash
curl -fsSL https://uv.sh/install.sh | bash
```
::right::

3. After installation, restart your Terminal or run `source ~/.uv/bin/uv.sh` to load `uv`.
4. Verify the installation by running:

```bash
uv --version
```

5. Install 3.13 of Python using `uv`:

```bash
uv install 3.13
```

---
layout: top-title
color: orange-light
---

::title::

# Check that it is all working

::content::

To verify that Git, GitHub, Python, and VS Code are set up correctly, follow these steps:

- Choose "Open Folder" in VS Code and create a new folder to play around with Python and Git.
- Open the integrated terminal in VS Code (`Ctrl + \``) and run:

```bash
git --version
python --version
```

- Create a new Python file (e.g., `test.py`) in VS Code and add the some code, eg.:

```python
print("Hello, World!)
```

**Save the file** and run it by pressing `F5` or the play button in VS Code.
- If everything is set up correctly, you should see the output in the terminal.

Use the Source Control panel in VS Code to initialize a Git repository, make changes, and commit them.

---
layout: top-title
color: purple-light
---

::title::

# Install Additional Python Packages

::content::

You may need additional Python packages for your projects. If you used `uv` to install Python, you can use its built-in package manager to install packages. If you have an existing python installed: you can instead use `pip`, which comes bundled with Python. (uv is just much faster)

We want to install `pytest` for automatically testing our code. 
To install `pytest`, run the following command in your terminal:

```bash
uv pip install pytest
```

(If not using uv, run `pip install pytest` instead.)

Another useful package is `ruff` which helps make your code cleaner and more consistent. To install `ruff`, run:

```bash
uv pip install ruff
```

(If not using uv, run `pip install ruff` instead.)
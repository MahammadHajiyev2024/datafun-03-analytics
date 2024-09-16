# datafun-03-analytics

Professional analytics project using Git, Python, venv, pip, and VS Code to read and process data.
Commands were used on a Windows machine running PowerShell.  

## Create and Activate Project Virtual Environment

```shell
py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r "requirements.txt"
```

## Freeze Requirements

```shell
py -m pip freeze > requirements.txt
```

## Git Add / Commit / Push 

```shell
git add .
git commit -m "add .gitignore, commands to README.md"
git push -u origin main
```

## Specification

This project was built to the following specification:

- [datafun-03-spec](https://github.com/denisecase/datafun-03-spec)
# GitFlow for New Projects

## Unzip/Unpackage the smartmedia_deduplicator.zip

Unzip the file in the location where you want the project to live. 

## Initialize Template Repo

In a clean repo: 

```bash
git init
git add .
git commit -m "Initial commit: Project Starter Seed"
```

## Start New Projects from the Zip

```bash
unzip starter_project_template.zip -d new_project
cd new_project
rm -rf .git
git init
git add .
git commit -m "Project initialized from template"
```
Working on new feature?
```cmd
git checkout -b featurename
```


Were  Model Changes just made?
Make the migrations
```cmd
    python mange.py makemigrations
```
Migrate the migrations
```cmd
Python manage.py migrate
```
Were file changes just made?
```cmd
Git status
```
clean out any unneeded files (pycache, .env, etc)
```cmd
Git rm -f <path to file>
```
add desired modified files 
```cmd
Git add *
```
Commit the change with a message
```cmd
    git commit -m “Chosen message”
```
Clean up
```cmd
git checkout main
git branch -d featurename 
```
# Learn Full-Stack Development from Home.

# Create virtul environemnt to run python code
- install virtual environment:
    - python -m pip  install --user  virtualenv

- create an instance of virtual environment:
    - linux:
            - python -m virtualenv venv
        - window:
            - python -m venv venv
        
     - activate your virtual environment:
        - linux:
            - . venv/bin/activate
    - window:
        - .\venv\Scripts\activate

# Install "requirements.txt"
        - pip install -r requirements.txt
    - or
        - pip3 install --user requirements.txt
 
 
 NB: If you cant run project because of configuration: 
- Top-right of your pycharm IDE you will see a drop down menu to "Edit configuration.."
- ![configure](https://user-images.githubusercontent.com/35859780/80873679-40462080-8c88-11ea-9196-ccee38f0c880.PNG)


        
# git commands:
1. create you own branch
    - git checkout -b tusharBranch

2. switch to your branch from master to tusharBranch
    - git checkout tusharBranch
    
    - or: use force to checkout
        - git checkout -f tusharBranch

3. git pull , eg: if you are behind
    - git pull

4. If you want to pull a branch and you edited your branch

    - stash the your branch   
         - git stash
         
    - then pull
        - pull master

5. if you want to rebase your branch with master
    - git rebase master


6. do not merge with master without conversation
    - eg: if you want to merge your local branch with - - - -    - tusharBranch
        - git merge tusharBranch
# Stop giving username and password for every commit:
- git config --global user.name "example@gmail.com"
- git config --global user.password "password"

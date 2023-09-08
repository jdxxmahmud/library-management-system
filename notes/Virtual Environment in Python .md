# Virtual Environment in Python

- What are virtual environments
    
    → Suppose you are working on different projects  and some of them require you to have a  different version of the same framework. By the help of Virtual Environments you can have both versions available in your computer and work on your projects simultaneously. 
    
    ### How to create a virtual environment in python:
    
    1. Install ‘virtualenv’ to create virtual environments
    
    ```
    pip install virtualenv
    ```
    
    1. Select the path you want to create your environment in 
    
    ```
    path/virtualenv myenv
    ```
    
    1. Get inside your environment’s ‘Scripts’ to activate it
    
    ```
    path/ cd myenv
    path/myenv cd Scripts
    path/myenv/Scripts activate
    (myenv) path/myenv/Scripts
    ```
    
    ### Visual Studio Code
    
    → In visual studio  at first you need to choose the virtual environment and show it’s path
    
    1. Click here
    
    ![Untitled](Virtual%20Environment%20in%20Python/Untitled.png)
    
    2. Provide the virtual environment path
    
    ![Untitled](Virtual%20Environment%20in%20Python/Untitled%201.png)
    
    3. Select your virtual environment
    
    ![Untitled](Virtual%20Environment%20in%20Python/Untitled%202.png)
    
    Here I named my virtual environment “newenv” .
    
    ### Why should you create
    
    [https://stackoverflow.com/questions/10450992/can-not-activate-a-virtualenv-in-git-bash-mingw32-for-windows](https://stackoverflow.com/questions/10450992/can-not-activate-a-virtualenv-in-git-bash-mingw32-for-windows)
    
    Here's why: One of the chief reasons to use a virtual environment is **to ensure the use of specific versions of packages**. If you use >= instead of == , there is no guarantee you—or someone else—will end up with the same version if the environment needs to be recreated for that project. Use an exact version number
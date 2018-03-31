The second task is MENU
-

This project will remind you a database. The user can use 3 windows , which are under `Tkinter`.

        1. Welcome window
        2. Record window
        3. Read window
        
There are two important feauters for me:

The first one is recording. Your data stores in `.csv` file in order like:  
        
        ID
        Surname
        Name
        Poetric
        Sex
        Email
        Phone number
        Number of views
        (*Specific character - )`c`
        
  ![Alt text](https://github.com/nikitaxgusev/My_tasks_py/blob/master/Menu/csvex.PNG?raw=true "Optional Title")
    
- Specific character `c` is needed to be for knowing a number of recordings. Its job is counting.

  Look at it: when you want to record a note, you will automatically get an `ID`, that ID is given by my `c` (specific char). It means,
  that when you want to record, the algorithm reads the whole file for finding a `c`, store the value of recordings and give your personal `ID`.


- The second feature is reading. 
  Do you want to find your recording? You should point your personal `ID`, which you have got, and you will get your note.


- Windows:
   ![Alt text](https://github.com/nikitaxgusev/My_tasks_py/blob/master/Menu/datab.PNG?raw=true "Optional Title")

  
  
- I wish I could put some checkings on entering the data for phone number, email, using `regex` and somethinng.

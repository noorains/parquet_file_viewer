# parquet_file_viewer_for_MacOS
## View parquet files through file path


<img width="580" alt="image" src="https://github.com/noorains/parquet_file_viewer/assets/142994595/05526304-9f07-4310-a367-d7b241b13227">

### To make a Python script executable from the desktop in MacOS, you can create an Automator application. Here are the steps:

- Open Automator (you can find it using Spotlight search).
- Choose "Application" for the document type.
- In the Actions library on the left, choose "Utilities" and then "Run Shell Script".
- In the "Run Shell Script" action, make sure "/bin/bash" is selected for "Shell".
- In the same action, enter the command to run your script. For example, if your script is located at /Users/YourName/Scripts/parquet_viewer.py, you would type python3 /Users/YourName/Scripts/parquet_viewer.py.
- Save the Automator application to your desktop.

### To ensure that the correct Python interpreter is used, you can specify the full path to the Python executable in your base environment in the Automator action. Here's how to find the path:

- Open a terminal.
- Activate your base environment. If you're using Anaconda, you can do this with the command conda activate base.
- Once the environment is activated, type which python (or which python3 if you're using Python 3). This will print the full path to the Python executable.
- Once you have the path, you can use it in the Automator action. For example, if the path is /Users/YourName/anaconda3/bin/python, you would enter /Users/YourName/anaconda3/bin/python /Users/YourName/Scripts/parquet_viewer.py in the "Run Shell Script" action.

### To change the icon of an Automator application (or any application) in MacOS, follow these steps:

- Find the icon file you want to use. It should be a .icns file. If you have a .png or .jpg, you can convert it to .icns using an online converter.
- Open the info window for the application. You can do this by selecting the application and pressing Command + I, or by right-clicking the application and choosing Get Info.
- Open the icon file in Preview. You can do this by double-clicking the icon file.
- In Preview, select all (Command + A) and copy (Command + C).
- Go back to the info window for the application. Click the small icon at the top left of the window to select it (it should get a blue highlight).
- Paste the new icon (Command + V).
- The icon for the application should now be changed.
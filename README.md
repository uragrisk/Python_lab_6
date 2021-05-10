# Flask Aplication

## Task:
1. Implement a REST service for one of the class in laboratory work 3 using Python.
   
2. Implement the preservation of the object of the class of laboratory work 3 in the database.

## How to run:
1. Open a command line
2. Upload the files to the desired folder using the command git clone https://github.com/uragrisk/Python_lab_6.git
3. Create a virtual environment in the command line and activate it using commands:
   * **python -m venv venv**
   * **venv\scripts\activate.bat**
4. Create MySQL database named `ship-manager`
5. Install all project requirements using command:
   **pip install -r requirements.txt**
6.Create needed tables in the database:
   * Open python interpreter with the command ___python___
   * Import our database ___from app import db___
   * Create all needed tables with command ___db.create_all()___
   * ___quit()___
7. Run application ___python app.py___

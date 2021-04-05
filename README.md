# GISC_COE_Terrafrom_project
Building a HA architecture using terraform.


```**Clone this git repo** : git clone --branch master https://github.com/IsmohiK/GISC_COE_Terrafrom_project/ ```  

1. Make sure You have python installed in the system. Install the necessary libraries per requirements.txt 
   (`pip install -r scripts/requirements.txt`).
2. Before Running the script do the following changes in resources.py
   ```
   1. Comment line from 1 to 4 before running the python script for the environment you are working in 
   2. Make sure line in PythonTerraform.py 40 is commented and 41 in uncommented
   ```
   We do this because we need to create the S3 bucket and dynamodb before linking the tfstate

3. Navigate to the folder where you have cloned the repo. Example : `C:\GISC_COE_Terrafrom_project-main` in cmd.
4. Run the script with command `python scripts/main.py`
5. When running the script it will prompted to add profilename/environment name as
   ```
   Choose the Environment
   1. dev
   2. test
   3. exit
   Enter the chioice 1/2/3
   ```
   On pressing enter it will perform terraform operations as defined in the tf files.
   
6. Run the script again to link the tfstate file to the AWS s3 backend. Before that do the below and then follow step 3 to 5
    ```
   1. Uncomment line from 1 to 4 before running the python script for the environment you are working in 
   2. Make sure line in PythonTerraform.py 41 is commented and 40 in uncommented
   ```
   
Commands to push the changes
   ```
   Navigate to the folder where you have cloned the repo. Example : C:\GISC_COE_Terrafrom_project-main in git bash
   git init
   git add .
   git commit -m <message>
   git remote add origin https://github.com/IsmohiK/GISC_COE_Terrafrom_project.git
   git checkout -b <branch name>
   git push -u origin <branch>
   ```
   


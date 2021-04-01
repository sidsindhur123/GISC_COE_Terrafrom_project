# GISC_COE_Terrafrom_project
Building a HA architecture using terraform.


```**Clone this git repo** : git clone --branch master https://github.com/IsmohiK/GISC_COE_Terrafrom_project/ ```  

1. Make sure You have python installed in the system. Install the necessary libraries per requirements.txt 
   (`pip install -r scripts/requirements.txt`).

2. Navigate to the folder where you have cloned the repo. Example : `C:\GISC_COE_Terrafrom_project-main` in cmd.
3. Run the script with command `python scripts/main.py`
4. When running the script it will prompted to add profilename/environment name as
   ```
   Enter the user profile name for the aws provider
   ```
   Enter the profile name Example : **default**

   On pressing enter it will perform terraform operations as defined in the tf files.
   
5. Commands to push the changes
   ```
   Navigate to the folder where you have cloned the repo. Example : C:\GISC_COE_Terrafrom_project-main in git bash
   git init
   git add .
   git commit -m <message>
   git remote add origin https://github.com/IsmohiK/GISC_COE_Terrafrom_project.git
   git checkout -b <branch name>
   git push -u origin <branch>
   ```
   


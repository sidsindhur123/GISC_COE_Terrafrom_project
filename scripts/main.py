from PythonTerraform import PythonTerraform
import yaml
import boto3
import sys

if __name__ == '__main__':
	env_dict = {'1':'dev','2':'test'}
	choice = 0
	print("Choose the Environment")
	while(True):
		print("1. dev")
		print("2. test")
		print("3. exit")
		choice=int(input("Enter the chioice 1/2/3"))
		if choice==1 or choice==2:
			PythonTerraform(choice)
			break
		elif choice==3:
			print("You pressed EXIT!!")
			break
		else:
			print("Invalid choice. Try again")
			continue








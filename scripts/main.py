from PythonTerraform import PythonTerraform
import yaml
  
if __name__ == '__main__':
	manifest_configuration = {}
	user = input("Enter the user profile name for the aws provider")
	with open("scripts\\manifest.yaml", "r") as f:
		manifest_configuration = yaml.safe_load(f)
		f.close()

	manifest_configuration['params']['default']['profile'] = user
	with open("scripts\\manifest.yaml", "w") as f:
		config = yaml.dump(manifest_configuration, f)
		f.close()
	PythonTerraform()








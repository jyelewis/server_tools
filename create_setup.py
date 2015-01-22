import os
script_dir = os.path.dirname(os.path.abspath(__file__)) 
setup_scripts_path = os.path.join(script_dir, "setup_scripts/")

setup_script = "### setup script generated by create_setup.py (https://github.com/jyelewis/dev_tools) ###\n\n\n"

with open(os.getcwd() + "/dependencies.txt", "r") as dependencies:
	for dependency in dependencies:
		dependency = dependency.strip()
		try:
			f = open(setup_scripts_path + dependency + ".sh", "r")
			dependency_code = f.read()
		except:
			print("Unable to add dependency " + dependency + ", the file could not be found")
			continue

		setup_script += "echo '------------------Installing "+dependency+"------------------------'\n"
		setup_script += dependency_code
		setup_script += "\n\n\n" 



setup_file_path = os.getcwd() + "/setup"
setup_file = open(setup_file_path, "w+")
setup_file.write(setup_script)
print("Setup file written to " + setup_file_path)
setup_file.close()

os.system("chmod +x " + setup_file_path)

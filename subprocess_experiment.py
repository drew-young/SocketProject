import subprocess

output = subprocess.run('echo "Hello"', shell=True,capture_output=True,text=True) 
# output = subprocess.run('echo "Hello"', shell=True,stdout=subprocess.PIPE,text=True) 
'''
Need to set shell=True for windows
capture_output is used to save the output to a variable
text=True will output a string
stdout=subprocess.PIPE  does same thing as capture output
stdout=FILENAME will output standard out to a file
output.stderr will print errors
output.returncode will return 0 if all good and 1 if errors
check=True will check for errors and throw an error to python instead of letting it run
'''
#print(output.stdout.decode()) #use .stdout to print standard output
print(output.stdout) #use .stdout to print standard output
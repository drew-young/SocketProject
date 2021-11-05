import subprocess

output = subprocess.run('echo "Hello"', shell=True,capture_output=True,text=True) 
'''
Need to set shell=True for windows
capture_output is used to save the output to a variable
text=True will output a string
stdout=subprocess.PIPE
'''
#print(output.stdout.decode()) #use .stdout to print standard output
print(output.stdout) #use .stdout to print standard output
import psutil
import os
import subprocess

p = subprocess.Popen(['ps -ef'], stdout=subprocess.PIPE, shell=True)
out = p.stdout.readlines()
all_processes = []
pids = []
for line in out:
	line_str = line.decode('utf')
	all_processes.append(line_str)
for process in all_processes:
	if 'beatbox' in process:
		print("process: " + process)
		print("kill: " + process.split()[1])
		os.system("kill " + process.split()[1])
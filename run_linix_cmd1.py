import subprocess
command=[
        'ls',
        'pwd',
        'ls -l'
        ]
for cmd in command:
    result=subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout)
    print(result.stderr, end='')

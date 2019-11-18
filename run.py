import os
import subprocess

T = [300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600]

for i in range(len(T)):
    with open("diff.in", "r") as f:
        data = f.readlines()
        data[3] = data[3][:-4] + str(T[i]) + "\n"
        data[-3] = data[-3][:25] + str(T[i]) + data[-3][28:]
    
    with open("diff.in", "w") as fout:
        for d in data:
            fout.write(d)
    
    print(f"Running T = {T[i]}\n")

    if not os.path.exists(f"pdh_{T[i]}/"):
        os.mkdir(f"pdh_{T[i]}/")

    run = subprocess.Popen(['lmp_serial', '-in', 'diff.in'],
                            stdout=open(str(T[i])+'.log', 'w'))
    stdout = run.communicate()[0]
    rc = run.returncode
    if rc != 0:
        error_msg = 'exited with return code %d' % rc
        msg = stdout.decode("utf-8").split('\n')[:-1]
        try:
            error_line = [i for i, m in enumerate(msg)
                            if m.startswith('ERROR')][0]
            error_msg += ', '.join([e for e in msg[error_line:]])
        except:
            error_msg += msg[-1]
        raise RuntimeError(error_msg)

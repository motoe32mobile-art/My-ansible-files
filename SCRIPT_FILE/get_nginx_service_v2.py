import subprocess
service = "nginx"
output = subprocess.check_output(["ps","ax"]).decode("utf-8")
print(output)
status = output.count(service)
print(status)

if status > 1:
    print("nginx service is runing")
else:
    print("nginx service is not runing")


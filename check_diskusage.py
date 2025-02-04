import psutil
threshold = 80
disk_usage = psutil.disk_usage('/')
used_percent = disk_usage.percent
print(f"disk usage: {used_percent}")
if used_percent > threshold:
    print(f"disk usage is reached {threshold}. Current usage: {used_percent}%")
else:
    print("disk usage is under threshold")

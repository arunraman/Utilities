import subprocess
import sys
import time


def get_cpu_utilization():
    p = subprocess.Popen("grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'",
                         stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output.strip()


def get_memory_utilization():
    p = subprocess.Popen("free | awk 'FNR == 3 {print $3/($3+$4)*100}'",
                         stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output.strip()


def get_disk_utilization():
    p = subprocess.Popen("df --total -hl | tail -n1 | awk '{print $5}' | sed 's/%//'",
                         stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output.strip()


def get_average(array):
    return reduce(lambda x, y: x + y, array) / len(array)


def main():
    minutes = sys.argv[1]
    cpu_threshold = sys.argv[2]
    mem_threshold = sys.argv[3]
    disk_threshold = sys.argv[4]
    cpu_utilization = []
    mem_utilization = []
    disk_utilization = []
    t_end = time.time() + 60 * int(minutes)
    while time.time() < t_end:
        cpu_utilization.append(float(get_cpu_utilization()))
        mem_utilization.append(float(get_memory_utilization()))
        disk_utilization.append(float(get_disk_utilization()))
        time.sleep(60)

    cpu_utilization_avg = str(get_average(cpu_utilization))
    mem_utilization_avg = str(get_average(mem_utilization))
    disk_utilization_avg = str(get_average(disk_utilization))

    print "CPU Utilization: " + cpu_utilization_avg + "\n"
    print "Mem Utilization: " + mem_utilization_avg + "\n"
    print "Disk Utilization: " + disk_utilization_avg + "\n"

    if (float(cpu_utilization_avg) < cpu_threshold and
        float(mem_utilization_avg) < mem_threshold and
        float(disk_utilization_avg) < disk_threshold):
        print("Under Utilized")
    else:
        print("Over Utilized")


if __name__ == '__main__':
    main()

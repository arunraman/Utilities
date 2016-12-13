from fabric.api import *


@parallel
def start_monitoring(minutes, cpu_threshold, mem_threshold, disk_threshold):

    # Change this to the user name of the machine
    env.user = "vagrant"
    # Change the Password for the correponding username
    env.password = "vagrant"
    run('mkdir -p /tmp/monitor')
    put('monitor_system.py', '/tmp/monitor')
    command = 'python /tmp/monitor/monitor_system.py' + " " +\
              minutes + " " + cpu_threshold + " " \
              + mem_threshold + " " + disk_threshold
    run(command)


def execute_tasks(minutes, cpu_threshold, mem_threshold, disk_threshold):
    start_monitoring(minutes, cpu_threshold, mem_threshold, disk_threshold)

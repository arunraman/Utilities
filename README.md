Unix Monitoring Scripts
=======================

Common Functions for some unix monitoring jobs.

Monitor VMStat
--------------
Monitor vmstat for a threshold value for a specified number of iterations, if it reaches the threshold break
and print a message.

Usage: vmstat | ./monitor_vmstat.py column_number repeat threshold

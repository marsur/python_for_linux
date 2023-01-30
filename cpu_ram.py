#!/usr/bin/python3.6

import psutil

mem = psutil.virtual_memory()

print(psutil.virtual_memory())


cpu = psutil.cpu_percent

print('The cpu message')

print (psutil.cpu_percent(60))


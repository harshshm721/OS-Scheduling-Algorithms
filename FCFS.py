"""
Operating Systems Experient - 02

Name: Harsh Mukesh Sharma 
Class: TE IT-B
Roll no.: 23
Batch -  01
"""

"""
First Come Fisrt Serve Scheduling

The code below is a general code to solve scheduling problems in OS
without taking any assumptions. The only condition put is that of FCFS
scheduling, which is that all the processes are preemptive.

The code also draws the gantt chart for the same.

All units of time are in ms.
"""

def waitingtime(p, bt, tat, wt):
    
    # Waiting time tells us how long did the process had to wait to get 
    # processed after entering the schedule.
    # It is difference of turn around time and burst time.
    
    wt_val = 0
    for i in range(p):
        wt_val = tat[i] - bt[i]
        wt.append(wt_val)
        
    return wt
    

def turnaroundtime(p, at, ct, tat):
    
    # The total time for which the process was in the CPU for processing.
    # It is difference of completion time and arrival time.
    
    tat_val = 0
    for i in range(p):
        tat_val = ct[i] - at[i]
        tat.append(tat_val)
        
    return tat

def completiontime(p, p_sort, ct, key, gc):
    
    # The time when the process got executed and was out of the CPU.
    
    completion = {}
    
    for i in range(p):
        completion[p_sort[i]] = gc[key[i]]
        
    for k in sorted(completion):
        ct.append(completion[k])
        
    return ct

def ganttchart(p, at, bt):
    
    # Helps us in getting the completion time.
    # Shows the order of processing.
    
    gc = []
    gc.append(0)
    
    # key will store indexes of gc where the processes are completed.
    key = []

    arrival = at[:]
    arrival.sort()
    
    #if arrival times are same we will need another list
    arrived = at[:]
    
    # processes sorted in asceding according to their arrival time.
    p_sort = []
    
    # The indexes stored will help in retrieving value for current process if
    # not in the same order.
    for ar in arrival:
        if ar in arrived:
            p_sort.append(arrived.index(ar))
            arrived[arrived.index(ar)] = -1
            

    j = 0
    for i in range(p):
        gantt = 0
        if arrival[i] <= gc[j]:
            gantt = gc[j]+bt[p_sort[i]]
            gc.append(gantt)
            j = j + 1
            key.append(j)
            
        else:
            gc.append(arrival[i])
            j = j + 1
            gantt = gc[j]+bt[p_sort[i]]
            gc.append(gantt)
            j = j + 1
            key.append(j)
            
    return gc, key, p_sort

def avgtime(p, wt, tat):
    
    # The average time taken for compution of the input processes.
    
    tat_sum = 0.0
    wt_sum = 0.0
    
    for i in range(p):
        tat_sum = tat_sum + tat[i]
        wt_sum = wt_sum + wt[i]
        
    tat_avg = tat_sum / p
    wt_avg = wt_sum / p
    
    return tat_avg, wt_avg


print("____________________________________")
print("OS Scheduling FCFS")

#input number of processes
print("")
print("")

p = int(input("Enter the number of processes: "))

processes = []
for i in range(p):
    processes.append("p"+str(i+1))

#input the arrival time
#input the burst time

at = []
bt = []

print("Enter Arrival Time for all processes: ")
for i in range(p):
    a = int(input("Enter arrival time for p"+str(i+1)+": "))
    at.append(a)

print("")
print("Enter Burst Time for all processes: ")    
for i in range(p):
    b = int(input("Enter burst time for p"+str(i+1)+": "))
    bt.append(b)
    
gc = []
ct = []
tat = []
wt = []


gc, key, p_sort = ganttchart(p, at, bt)
ct = completiontime(p, p_sort, ct, key, gc)
tat = turnaroundtime(p, at, ct, tat)
wt = waitingtime(p, bt, tat, wt)
tat_avg, wt_avg = avgtime(p, wt, tat)


print("____________________________________")
print("Output:")

print("Gantt Chart: \n")
n1 = len(gc)

print("------" * (n1-1))

index = 0
for val in gc:
    
    if val == 0:
        print("|", end = " ")
        
    elif val == gc[-1]:
        print(" p"+str(p_sort[index]+1)+" |")
    
    elif val == gc[key[index]]:
        print(" p"+str(p_sort[index]+1)+" |", end = " ")
        index = index + 1
        
    else:
        print("    |", end = " ")

print("------" * (n1-1))

for i in gc:
    print(str(i)+"    ", end = " ")
    
print("")
print("")
print("")

print("Processes  " + "  AT  " + "  BT  " + "    CT  " 
      + "      TAT  " + " WT  ")

for s in range(p):
    print("\t" + str(processes[s]) + "\t\t  " + str(at[s]) + "\t    " +
          str(bt[s]) + "\t    " + str(ct[s]) + "\t      " + str(tat[s]) + 
          "\t    " + str(wt[s]))
    
print("")
print("")
print("AT ---> Arrival Time")    
print("BT ---> Burst Time")
print("CT ---> Completion Time")
print("TAT ---> Turn Around Time")
print("wT ---> Waiting Time")


print("")
print("")

print("Average Turn Around Time: ", tat_avg)
print("Average Waiting Time: ", wt_avg)

print("")
print("")

print("Scheduling Solved!")
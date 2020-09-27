"""
Operating Systems Experient - 04

Name: Harsh Mukesh Sharma 
Class: TE IT-B
Roll no.: 23
Batch -  01
"""

"""
Round Robin Scheduling

In round robin scheduling algorithm, the processes are executed in turns,
and each process is executed for a fixed amount of time. This is the 
method of context switching. 'Time Quantam' is the time for which the
processes are executed. The algorithm is mentioned below:
    
    1. First the arrived processes are appended to the ready queue.
    2. Then the process with the shortest arrival time is appended
    to running queue and is run for given 'Time Quantam'.
    3. After the process is run for time quantam, we check for the burst
    time of the process. If it is not zero, it is removed from
    running queue and appended at the last of ready queue. 
    4. The next process in the ready queue is then executed and the above 
    steps are repeated until all the processes get completely executed.
    
Hence in round robin, the processes are executed one by one, again and again,
until all of them get completed. This is another case of preemptive 
scheduling. Round robin algorithm also follows the same rules for calculating
the turn around time, waiting time and response time.

Important Formulas:
    1. TAT = CT - AT
    2. WT = TAT - BT
    3. RT = (CPU First Time) - AT
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

def responsetime(p, at, execution, gc, key1):
    # reponse time is different than waiting time in case of pre-emptive
    # RT = (CPU First Time) - AT
    rt = []
    
    # list of processes
    processs = []
    for j in range(p):
        processs.append(j)
    
    cpu = []
    for i in range(p):
        if processs[i] in execution:
            indx = execution.index(processs[i])
            cpu.append(gc[key1[indx] - 1])
            
    for k in range(p):
        diff = cpu[k] - at[k] 
        rt.append(diff)
        
    return rt

def completiontime(p, ct, key, gc, completed):
    # The time when the process got executed and was out of the CPU.
    
    completion = {}
    
    for i in range(p):
        completion[completed[i]] = gc[key[i]]
        
    for k in sorted(completion):
        ct.append(completion[k])
        
    return ct

def ganttchart(p, at, bt, time_quantum):
    # Helps us in getting the completion time.
    # Shows the order of processing.
    # The gantt chart in this case starts from 0 and continues
    # with time interval equal to 'time quantam'. 
    # i.e., the time goes like 0,1,2,3,.... so on
    # Processes are checked at each second of time.
    
    # The time in gantt chart always starts from 0
    gc = []
    gc.append(0)
    
    # The list 'key' will store those indexes in gantt chart where the 
    # processes would get complete
    key = []
    
    # The list 'key1' stores those indexes where the processes are in CPU
    key1 = []
    
    # We didn't want to make changes in the original arrival time list 'at'
    # So we created its copies 'arrival' and 'arrived' for iterations
    
    # arrival will store the arrival time of the processes in ascending order
    arrival = at[:]
    arrival.sort()
    
    # arrived will be exact copy of 'at' and will help in identifying the 
    # order in which processes are sorted
    arrived = at[:]
    
    # 'p_sort' contains the order of processes sorted according to their
    # arrival time
    p_sort = []
    
    for ar in arrival:
        if ar in arrived:
            p_sort.append(arrived.index(ar))
            # to avoid duplicate values to get same process number, we will 
            # change them to '-1' or any other negative number to mark them counted
            arrived[arrived.index(ar)] = -1
            
    # list 'burst' will hold burst time for processes in queue
    burst = []
    burst = bt[:]
    
    # list 'entered' will hold processes in queue during execution
    entered = []
    
    # list 'completed' will store the processes which get completed
    completed = []
    
    # list 'execution' will store the process which got executed
    # at that particular time.
    execution = []
    
    # list 'ready_queue' will store the processes which are present in 
    # the ready queue. This is different from 'entered' list because processes
    # which have arrived are present in entered list and will leave from
    # the entered list once completed. The 'ready_queue' list will hold the
    # sequence in which processes will get executed.
    ready_queue = []
    
    pro = 0
    j = 0
    current = p_sort[0]
    
    while pro != p:
        gantt = 0
        a = 0
        
        
        if arrival[pro] == -1:
            a = pro + 1
        else:
            a = pro
            
        
        if pro == p-1:
            if arrival[pro] > gc[j]:
                gc.append(arrival[pro])
                j = j + 1
            
            for d in range(a,p):
                if ((arrival[d] != -1) and (arrival[d] <= gc[j])):
                   entered.append(p_sort[d])
                   arrival[d] = -1
                else:
                    continue
                
            current = entered[0]
            
            if (burst[current] > time_quantum):
                gantt = gc[j] + time_quantum
                gc.append(gantt)
                j = j + 1
                key1.append(j)
                burst[current] -= time_quantum
                execution.append(current)
            
            

            else:
                gantt = gc[j] + burst[current]
                burst[current] = 0
                gc.append(gantt)
                j = j + 1
                key1.append(j)
                
                execution.append(current)
                completed.append(current)
                entered.remove(current)
                ready_queue.remove(current)
                
                key.append(j)
                pro = pro + 1
            
        
        
        else:
            
        
            if arrival[pro] > gc[j]:
                gc.append(arrival[pro])
                j = j + 1
    
            for d in range(a,p):
                if ((arrival[d] != -1) and (arrival[d] <= gc[j])):
                       entered.append(p_sort[d])
                       arrival[d] = -1
                else:
                    continue
            
            if len(execution) == 0:
                for proc in entered:
                    if (proc not in ready_queue):
                        ready_queue.append(proc)
                    
                current = ready_queue[0]
                
            else:
                for proc in entered:
                    if (proc not in ready_queue) and (proc != execution[-1]):
                        ready_queue.append(proc)
                    
                current = ready_queue[0]
            
                if burst[execution[-1]] != 0:
                    ready_queue.append(execution[-1])
                else:
                    pass
                
            if (burst[current] > time_quantum):
                gantt = gc[j] + time_quantum
                gc.append(gantt)
                j = j + 1
                key1.append(j)
                burst[current] -= time_quantum
                execution.append(current)
                ready_queue.remove(current)
                
                
    
            else:
                gantt = gc[j] + burst[current]
                burst[current] = 0
                gc.append(gantt)
                j = j + 1
                key1.append(j)
                
                execution.append(current)
                completed.append(current)
                entered.remove(current)
                ready_queue.remove(current)
                
                key.append(j)
                pro = pro + 1
            
            
    return gc, completed, execution, key1, key

def avgtime(p, wt, tat, rt):
    
    # The average time taken for compution of the input processes.
    
    tat_sum = 0.0
    wt_sum = 0.0
    rt_sum = 0.0
    
    for i in range(p):
        tat_sum = tat_sum + tat[i]
        wt_sum = wt_sum + wt[i]
        rt_sum = rt_sum + rt[i]
        
    tat_avg = tat_sum / p
    wt_avg = wt_sum / p
    rt_avg = rt_sum/p
    
    return tat_avg, wt_avg, rt_avg


print("____________________________________")
print("OS Scheduling RR")

#input number of processes
print("")
print("")

p = int(input("Enter the number of processes: "))

processes = []
for i in range(p):
    processes.append("p"+str(i+1))

# input the arrival time
# input the burst time

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

time_quantum = int(input("Enter the time quantum for the scheduling: "))

gc = []
ct = []
rt = []
tat = []
wt = []

gc, completed, execution, key1, key = ganttchart(p, at, bt, time_quantum)
ct = completiontime(p, ct, key, gc, completed)
tat = turnaroundtime(p, at, ct, tat)
wt = waitingtime(p, bt, tat, wt)
rt = responsetime(p, at, execution, gc, key1)
tat_avg, wt_avg, rt_avg = avgtime(p, wt, tat, rt)

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
        print(" p"+str(execution[index]+1)+" |")
    
    elif val == gc[key1[index]]:
        print(" p"+str(execution[index]+1)+" |", end = " ")
        index = index + 1
        
    else:
        print("    |", end = " ")

print("------" * (n1-1))

for i in gc:
    if i == 0:
        print("{}".format(str(i)), end = " ")
    else:
        print("{:>5}".format(str(i)), end = " ")


"""-------------------"""
print("")
print("")
print("")

print("Processes  " + "  AT  " + "  BT  " + "    CT  " 
      + "      TAT  " + " WT  " + "  RT  ")

for s in range(p):
    print("{} {:>12} {:>5} {:>7} {:>9} {:>5} {:>5}".format(processes[s], 
                                at[s], bt[s], ct[s], tat[s], wt[s], rt[s]))

    
print("")
print("")
print("AT ---> Arrival Time")    
print("BT ---> Burst Time")
print("CT ---> Completion Time")
print("TAT ---> Turn Around Time")
print("WT ---> Waiting Time")
print("RT ---> Response Time")


print("")
print("")

print("Average Turn Around Time: ", tat_avg)
print("Average Waiting Time: ", wt_avg)
print("Average Response Time: ", rt_avg)

print("")
print("")

print("Scheduling Solved!")

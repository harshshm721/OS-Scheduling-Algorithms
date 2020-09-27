"""
Operating Systems Experient - 03

Name: Harsh Mukesh Sharma 
Class: TE IT-B
Roll no.: 23
Batch -  01
"""

"""
Shortest Job First Schdeuling

In shortest job first scheduling, the processes are executed according to 
the ascending order of their burst times, i.e. the process which appeared
earlier and has a burst time shorter than other present processes, it will
be executed first.

In the below example we are going to implement a code for the same. We will
be taking some cases to implement the SJF Scheduling:
    
    Cases
    1. Preemptive (Also known as Shortest Remaining Time First Scheduling)
       In preemptive scheduling, the processes are interrupted if another 
       process with shorter burst time arrives at that moment.
    2. Non - preemptive
    
The code also draws the gantt chart for the same.
All units of time are in ms.

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

def turnaroundtime(p, at, ct_np, tat):
    # The total time for which the process was in the CPU for processing.
    # It is difference of completion time and arrival time.
    
    tat_val = 0
    for i in range(p):
        tat_val = ct_np[i] - at[i]
        tat.append(tat_val)
        
    return tat

def responsetime_p(p, at, execution, gc, key1):
    
    # reponse time is different than waiting time in case of pre-emptive
    # RT = (CPU First Time) - AT
    rt_p = []
    
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
        rt_p.append(diff)
        
    return rt_p            

def completiontime_p(p, ct, key, gc, completed):
    
    # The time when the process got executed and was out of the CPU.
    
    completion = {}
    
    for i in range(p):
        completion[completed[i]] = gc[key[i]]
        
    for k in sorted(completion):
        ct.append(completion[k])
        
    return ct

def ganttchart_p(p, at, bt):
    
    # Helps us in getting the completion time.
    # Shows the order of processing.
    # The gantt chart in this case starts from 0 and continues
    # with time interval '1'. i.e., the time goes like 0,1,2,3,.... so on
    # Processes are checked at each second of time.
    
    # The time in gantt chart always starts from 0
    gc_p = []
    gc_p.append(0)
    
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
    
    # list 'burst1' will store burst times of processes sorted in an order
    # which is sorted according to ascending order of arrival time
    burst1 = []
    for ps in p_sort:
        burst1.append(bt[ps])
    """    
    tot_time = 0
    for i in range(p):
        tot_time = tot_time + burst1[i]
    """
    # list 'entered' will hold processes in queue during execution
    entered = []
    # list 'completed' will store the processes which get completed
    completed = []
    # list 'execution' will store the process which got executed
    # at that particular time.
    execution = []
    
    pro = 0
    j = 0
    
    while pro != p:
        gantt = 0
        indx = 0
        a = 0
        minm = 0
        
        if arrival[pro] == -1:
            if pro + 1 == p:
                arrival[pro] = -1
                minm = min(burst)       
                indx = burst.index(minm)
                gantt = gc_p[j] + 1
                gc_p.append(gantt)
                j = j + 1
                key1.append(j)
                burst[indx] = minm - 1
                execution.append(entered[indx])
                
                if burst[indx] == 0:
                    completed.append(entered[indx])
                    entered.remove(entered[indx])
                    burst.remove(min(burst))
                    key.append(j)
                    pro = pro + 1
                
            else:
                a = pro + 1
                for d in range(a,p):
                    if ((arrival[d] != -1) and (arrival[d] <= gc_p[j])):
                           entered.append(p_sort[d])
                           burst.append(burst1[d])
                           arrival[d] = -1
                    else:
                        continue
                
                minm = min(burst)       
                indx = burst.index(minm)
                gantt = gc_p[j] + 1
                gc_p.append(gantt)
                j = j + 1
                key1.append(j)
                burst[indx] = minm - 1
                execution.append(entered[indx])
                
                if burst[indx] == 0:
                    completed.append(entered[indx])
                    entered.remove(entered[indx])
                    burst.remove(min(burst))
                    key.append(j)
                    pro = pro + 1
                
        else:
            if arrival[pro] > gc_p[j]:
                gc_p.append(arrival[pro])
                j = j + 1
                
            a = pro
            for d in range(a,p):
                if ((arrival[d] != -1) and (arrival[d] <= gc_p[j])):
                       entered.append(p_sort[d])
                       burst.append(burst1[d])
                       arrival[d] = -1
                else:
                    continue
                   
            minm = min(burst)       
            indx = burst.index(minm)
            gantt = gc_p[j] + 1
            gc_p.append(gantt)
            j = j + 1
            key1.append(j)
            burst[indx] = minm - 1
            execution.append(entered[indx])
            
            if burst[indx] == 0:
                completed.append(entered[indx])
                entered.remove(entered[indx])
                burst.remove(min(burst))
                key.append(j)
                pro = pro + 1
    
    return gc_p, execution, key1, key, completed

def responsetime_np(wt):
    # In case of non-pre-emptive execution, reponse time is same as 
    # waiting time
    
    rt_np = wt[:]
        
    return rt_np

def completiontime_np(p, ct_np, key, gc_np, completed):
    # The time when the process got executed and was out of the CPU.
    
    completion = {}
    
    for i in range(p):
        completion[completed[i]] = gc_np[key[i]]
        
    for k in sorted(completion):
        ct_np.append(completion[k])
        
    return ct_np

def ganttchart_np(p, at, bt):
    
    # Helps us in getting the completion time.
    # Shows the order of processing.
    
    # The time in gantt chart always starts from 0
    gc_np = []
    gc_np.append(0)
    
    # The list 'key' will store those indexes in gantt chart where the 
    # processes would get complete
    key = []
    
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
    
    # list 'burst1' will store burst times of processes sorted in an order
    # which is sorted according to ascending order of arrival time
    burst1 = []
    for ps in p_sort:
        burst1.append(bt[ps])
    
    # list 'entered' will hold processes in queue during execution
    entered = []
    # list 'completed' will store the processes which get completed
    completed = []
    
    j = 0
    
    for k in range(p):
        """
        to avoid repetition of processes once completed, their arrival time 
        will be marked '-1' to identify that they are already present in 
        entered list.
        """
        gantt = 0
        indx = 0
        a = 0
        minm = 0
        
        if arrival[k] == -1:
            if k == p:
                arrival[k] = -1
                minm = min(burst)
                gantt = minm + gc_np[j]
                gc_np.append(gantt)
                j = j + 1
                key.append(j)
                
                completed.append(entered[0])
                entered.remove(entered[0])
                burst.remove(minm)
                
            else:
                a = k + 1
                for d in range(a,p):
                    if ((arrival[d] != -1) and (arrival[d] <= gc_np[j])):
                           entered.append(p_sort[d])
                           burst.append(burst1[d])
                           arrival[d] = -1
                    else:
                        continue
                
                minm = min(burst)       
                indx = burst.index(minm)
                gantt = minm + gc_np[j]
                gc_np.append(gantt)
                j = j + 1
                key.append(j)
                
                completed.append(entered[indx])
                entered.remove(entered[indx])
                burst.remove(minm)
                
        else:
            if arrival[k] > gc_np[j]:
                gc_np.append(arrival[k])
                j = j + 1
                
            a = k
            for d in range(a,p):
                if ((arrival[d] != -1) and (arrival[d] <= gc_np[j])):
                       entered.append(p_sort[d])
                       burst.append(burst1[d])
                       arrival[d] = -1
                else:
                    continue
                   
            indx = burst.index(min(burst))
            gantt = min(burst) + gc_np[j]
            gc_np.append(gantt)
            j = j + 1
            key.append(j)
            
            completed.append(entered[indx])
            entered.remove(entered[indx])
            burst.remove(min(burst))

    return gc_np, completed, key

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
print("OS Scheduling SJF")

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

# Enter the case for SJF
print("")
print("")

print("Choose whether your problem is preemptive or non-preemptive!")
print("Enter '1' for preemptive and '2' for non-preemptive.")
print("")

choice = int(input("Please enter your choice: "))

# If the problem is preemptive

if choice == 1:
    ## Code block for SJF if case is preemptive
    
    
    gc = []
    ct = []
    rt = []
    tat = []
    wt = []
    
    gc, execution, key1, key, completed = ganttchart_p(p, at, bt)
    ct = completiontime_p(p, ct, key, gc, completed)
    tat = turnaroundtime(p, at, ct, tat)
    wt = waitingtime(p, bt, tat, wt)
    rt = responsetime_p(p, at, execution, gc, key1)
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


elif choice == 2:
    ## Code block for SJF if case is non-preemptive
    
    gc = []
    ct = []
    rt = []
    tat = []
    wt = []
    
    gc, completed, key = ganttchart_np(p, at, bt)
    ct = completiontime_np(p, ct, key, gc, completed)
    tat = turnaroundtime(p, at, ct, tat)
    wt = waitingtime(p, bt, tat, wt)
    rt = responsetime_np(wt)
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
            print(" p"+str(completed[index]+1)+" |")
        
        elif val == gc[key[index]]:
            print(" p"+str(completed[index]+1)+" |", end = " ")
            index = index + 1
            
        else:
            print("    |", end = " ")
    
    print("------" * (n1-1))
    
    for i in gc:
        print(str(i)+"    ", end = " ")

else:
    print("Invalid choice of case!")
    print("Please try again!")
    



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

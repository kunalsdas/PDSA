'''
Conference Room Scheduling:-
You are given a list of n meetings, each represented by a tuple (start time, end time). Your goal is to schedule all meetings in the minimum number of conference rooms. 
If a meeting ends at time t in a conference room, another meeting can start at time t or afterwards in the same room.
Write a function minimum_conference_rooms(meetings) that accepts a list of pairs meetings = [(So, Eo), (S1, E1),..., (Sn-1, En-1)] where (Si, E;) represents the start and end times of meeting i. 
The function should return the minimum number of conference rooms needed to schedule all meetings.

Sample Input
[(1, 3), (2, 5), (4, 6), (5, 8), (5, 7)] # meetings
Output
3 # Minimum conference rooms required
'''

def count(meetings):
    start=[]
    end=[]
    for meet in meetings:
        start.append(meet[0])
        end.append(meet[1])
    start.sort()
    end.sort()
    count=0
    end_index=0
    for i in start:
        if i>=end[end_index]:
            end_index+=1
        else:
            count+=1
    return count
    
meetings = [(1, 3), (2, 5), (4, 6), (5, 8), (5, 7)]
print(count(meetings))

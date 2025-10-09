from heapq import heapify, heappop

N, lock_time = map(int, input().split())

arrival_times = []
leave_times = []

for _ in range(N):
    arrival_time, stay_time = map(int, input().split())
    arrival_times.append(arrival_time)
    leave_times.append(arrival_time + stay_time)

heapify(arrival_times)
heapify(leave_times)

saves = 0
current_leave = heappop(leave_times)
current_arrival = heappop(arrival_times)

try:
    while True:
        if current_arrival >= current_leave:
            if current_arrival - current_leave <= lock_time:
                saves += 1
                current_arrival = heappop(arrival_times)
            current_leave = heappop(leave_times)
        else:
            current_arrival = heappop(arrival_times)
except:
    print(saves)
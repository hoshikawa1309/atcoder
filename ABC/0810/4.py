N , M = map(int , input().split())
#内包表記で入力
jobs = [list(map(int , input().split())) for _ in range(N)]
sum = 0
#print(jobs)
for limit in range(1 , M + 1):
    index = ''
    max_reward = 0
    for job in jobs:
        if (job[0] <= limit and job[1] > max_reward):
            max_reward = job[1]
            index = jobs.index(job)
    if index != '':
        del jobs[index]
    #print("limit : ",limit)
    #print("max_reward : " , max_reward)
    sum += max_reward
#print(jobs)
print(sum)

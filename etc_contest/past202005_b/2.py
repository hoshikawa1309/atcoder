import numpy as np
N, M, Q = map(int, input().split())
participant = []
for _ in range(N):
    participant.append(np.array([0] * M))
participant = np.array(participant)
question_scores = np.array([N] * M)
# print(participant)
# print(question_scores)
queries = []
for _ in range(Q):
    query = list(map(int, input().split()))
    queries.append(query)

for query in queries:
    if query[0] == 1:
        print(sum(participant[query[1] - 1] * question_scores))
    else:
        participant[query[1] - 1][query[2] - 1] = 1
        question_scores[query[2] - 1] -= 1


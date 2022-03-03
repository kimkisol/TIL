def solution(id_list, report, k):
    answer = []
    id_report = {key: set() for key in id_list}
    id_reported = {key: 0 for key in id_list}
    new_report = [[0, 0] for _ in range(len(report))]

    for i in range(len(report)):
        new_report[i][0], new_report[i][1] = report[i].split()

    for r in new_report:
        id_report[r[0]].add(r[1])

    for val in id_report.values():
        for v in val:
            id_reported[v] += 1

    for key, val in id_reported.items():
        if val < k:
            for id in id_report:
                id_report[id].discard(key)

    for id in id_list:
        answer.append(len(id_report[id]))

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

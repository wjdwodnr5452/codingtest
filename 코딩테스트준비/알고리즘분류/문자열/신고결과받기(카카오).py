def solution(id_list, report, k):
    answer = []
    
    report = list(set(report)) # 중복 신고 제거
    dick_id = {} # 유저id, 신고한 id
    dick_report_cnt = {} # 신고한 id 몇번 신고 되었는지
    dick_result = {} # 메일 전송 

    for i in id_list :
        dick_id[i] = []
        dick_report_cnt[i] = 0
        dick_result[i] = 0

    
    for j in report :
        user_id, report_id = j.split()
        dick_id[user_id].append(report_id)
        dick_report_cnt[report_id] += 1


    for i in dick_id :
        for j in dick_id[i] :
            if(dick_report_cnt[j] >= k) :
                dick_result[i] += 1
        answer.append(dick_result[i])

    
    return answer
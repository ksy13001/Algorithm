import heapq
def solution(book_time):
    answer = 0
    room = []
    for s, e in book_time:
        sh, sm = map(int, s.split(":"))
        eh, em = map(int, e.split(":"))
        room.append((sh*60 + sm, eh*60 + em))
    room.sort(key=lambda x:(x[0], x[1]))
    # 첫 방 배정
    now_rooms = []
    heapq.heappush(now_rooms, room[0][1])
    total = 1
    for i in range(1, len(room)):
        s, e = room[i]
        # 종료 후 10분 청소 까지 시간 안될 경우 방 배정
        if s < now_rooms[0] + 10:
            total = max(total, len(now_rooms)+1)
        else:
            heapq.heappop(now_rooms)
        heapq.heappush(now_rooms, e)
    return total
            
        
    
    return answer

init python:
    #event('박세현',"act=='휴식'",priority=200)
    #event('박세현2',"act=='휴식'",priority=200)
    event('lee',"lee_ >=9 ",event.once(),priority=200)
    #event('홍예준',"act=='산책'",priority=200)
    #event('권재현',"act=='공부'",priority=200)
    #event('anger',"stress >=5",event.once(),priority=200)


label lee:
    scene room
    "오늘도 지루한 학교 수업을 마치고 자려고 누웠다."

    scene kakao




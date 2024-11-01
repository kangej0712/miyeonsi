# 이 파일에 게임 스크립트를 입력합니다.
init python:
    stress_=0
    park_=5
    lee_=5
    hong_=5
    kyeon_=5
    hong__ = 5 #배드엔딩 장치

# 게임에서 사용할 캐릭터를 정의합니다.
define n = Character('나', color = "#FF4000" )
define p = Character('박세현', color = "#0431B4")
define l =Character('이연우', color = "#FF4000")
define g = Character('종업원', color = "#FF4000")
define h = Character('홍예준',color = "#0431B4")
define other =Character('개강총회때 친해진 친구')
define rightCharacter = Position(xalign = 0.5, yalign = 0.4)
define leftCharacter = Position(xalign = 0.5, yalign = 0.6)
define left = Position(xalign = 0.1, yalign =0.6)
define right = Position(xalign = 0.9,yalign = 0.6)
define leftPark = Position(xalign=0.1,yalign=0.4)
define straight =Position(xalign = 0.5, yalign = 0.2)



image mt ="background/gapeong.png"
image mt2 = "background/gapeong2.png"
image university = "background/university.jpg"
image benchi ="background/benchi.png"
image room ="background/room.png"
image with_lee1="background/with_lee1.png"
image with_hong1="background/with_hong1.png"
image fightwithp ="background/fightwithp.png"
image sulzari = "background/sulzari.png"
image suzok ="background/suzok.png"
image night ="background/night.png"
image hongsroom = "background/hongsroom.png"
image morning = "background/morning.png"
image driving = "background/driving.png"
image accident = "background/accident.png"
image restaurant = "background/restaurant.png"
image temapakr = "background/temapark.png"
image merrygoround = "background/merrygoround.png"
image merry = "background/merry.png"

image park normal = im.FactorScale("character/park.normal.png",0.7)
image parkk =im.FactorScale("character/parkk.png",0.8)
image park happy = im.FactorScale("character/park.happy.png",0.7)

image park jeongsack = im.FactorScale("character/park.jeongsack.png",0.7)


image lee normal =im.FactorScale("character/lee.normal.png",1.0)
image lee smile = im.FactorScale("character/lee.smile.png",1.0)
image lee jeongsack =im.FactorScale("character/lee.jeongsack.png",1.0)
image lee happy =im.FactorScale("character/lee.happy.png",1.0)
image leef = im.FactorScale("character/leef.png",0.8)

image hong normal = im.FactorScale("character/hong.png",1.0)
image hong jeongsack = im.FactorScale("character/hong.jeongsack.png",1.0)
image hong mad = im.FactorScale("character/hong.mad.png",1.7)
image hong happy =im.FactorScale("character/hong.happy.png",1.0)

init:
    screen stat: #스탯창
        frame:
            align (0.95, 0.05)
            grid 5 2:
                text ' 박세현 '
                text ' 이연우 '
                text ' 홍예준 '
                text ' 권재현 '
                text ' stress '

                text '%2d' % park_
                text '%2d' % lee_
                text '%2d' % hong_
                text '%2d' % kyeon_
                text '%2d' % stress_




# 여기에서부터 게임이 시작합니다.
label start:

    scene mt
    play music "audio/bgm/strawberry.mp3"
    "....아오 머리야."
    "얼마나 마신거지..?"
    "나는 심호흡을 하고 주위를 둘러보았다."
    "때는 바야흐로 2023년.. 대딩 1학년이 된 나는 들뜬 마음으로."
    "..기대하던 ..엠티에 왔는데.."
    "어색한 애들끼리 술만 처먹고 재미없다."  with vpunch
    scene mt2
    "하아.. 집가고 싶네.."
    "그렇게 생각하던 와중..."
    "그가 다가왔다."

    show park normal at rightCharacter with dissolve

    p "저기.. 괜찮아요?"

    "쟤는 과대인 박세현?!?!" with vpunch

    n "아 네.. 괜찮아요.."
    n "우욱..."
    "...?"
    n "토...토할것 같..."
    
    
    p "헉..!! 토할것같아요???" with vpunch
    $ park_ -= 1
    
    menu:
        "아. 괜찮아요.(아무렇지 않은 척)":
            
            n "아. 괜찮아요.(아무렇지 않은 척)"
            p "그래도 속이 안좋아보이시는데 컨디션이라도 드릴까요?"
            menu:
                "아.. 그래주신다면 고맙읍니다ㅜㅜ":
                    n "아.. 그래주신다면 고맙읍니다ㅜㅜ"
                    show park normal at rightCharacter with dissolve
                    p "자. 여기요."
                    "난 망설임 없이 쓰디 쓴 컨디션을 입에 털어 넣었다."

                    p "술도 깰 겸 밖에 나가서 좀 걸으실래요?"
                    p "저도 취한 것 같아서.."
                    menu:
                        "그건 좀..(어디서 수작질이야?!)":
                            n "그건 좀..(어디서 수작질이야?!)"
                            $ park_-=1

                            show park normal at rightCharacter
                            "박세현의 얼굴이 창백하게 굳었다."
                            p "..."
                            p "...왜요?"
                            "뭐지?"

                            menu:
                                "지금 나가기는 힘들 것 같아서..":
                                    n "지금 나가기는 힘들것 같아서.."
                                    show park normal at rightCharacter with dissolve
                                    p "아 그래요?"

                                    show park normal at rightCharacter with dissolve
                                    p "그러면 한 10분 있다 나가죠!"
                                    "(아 근데...)"
                                    "(너무 가기 싫다..)"
                                    n "저 힘들어서 그런데 그냥 여기 있을게요."
                                    p "네?;;"
                                    p "아..알겠습니다."
                                "그냥 혼자 있고 싶은데요?":
                                    show park normal at rightCharacter with dissolve
                                    $ park_-=2
                                    p "아 그래요?"
                                    p "뭐.. 알겠습니다.."
                                    jump No_sehyeon

                        "그럴까요?(헤헤 잘생겼다)":
                            n "그럴까요?(헤헤 잘생겼다)"
                            show park normal at rightCharacter with dissolve
                            p "네. 아이스크림이라도 사먹어요 우리."
                            "아..."
                            "근데 갑자기 귀찮아졌다..."
                            n "저 그냥 안갈래요.."

                            p "아 예..뭐,,"
                            

label No_sehyeon:
    "박세현이가 뭔가 쎄하다고 생각했기도 했고 귀찮기도 해서"
    "그와 친해지지 않으려고 거리를 두었다."
    
    scene university

    

    play music "audio/bgm/loudful.mp3"

    "엠티가 끝나고 오늘도 어김없이 학교수업을 들으러 갔다."

    n "하 수업 듣기 싫다."
    "강의실로 들어간 순간..."

    stop music fadeout 5.0

    
    "오늘따라 뭔가 이상해.."

    play music "audio/bgm/weird.mp3"

    "내가 들어서자 갑자기 조용해진 분위기.."

    stop music fadeout 5.0

    "뭔가 이상한 생각이 들어 개강총회때 친해진 친구 옆자리에 앉았다."
    play music "audio/bgm/uu.mp3"
    other "아 뭐야.. 짜증나.."
    stop music

    
    

    "갑자기 왜이래?"

    "친하다고 생각한 친구들에게 말을 걸어보았으나"
    "돌아온건 쌀쌀한 반응 뿐 이었다."

    play music "audio/bgm/frustrate.mp3" 

    "도대체 내가 뭘 잘못한거야!!" with vpunch
    
    stop music fadeout 5.0

    scene benchi

    play music "audio/bgm/sad.mp3"
    "휴우.."
    "숨막히는 강의실에서 빠져나와 벤치에 앉아서 한숨만 내쉬었다."

    l "진짜 불쌍해서 못 봐주겠네"

    show lee normal at rightCharacter with dissolve

    n "누구..?"
    l "너가 박세현이 까고 다니는 걔냐?"

    "아.."
    '박세현이 뒤에서 내 얘기를 하고 다녀서 친구들이 날 버린거구나..'
    n "박세현이 뭐라고 하고 다니는데?"

    l "못생긴게 꼴값떤다고 하고 다니던데."

    ".."
    "하..."

    n "근데 넌 누구야? 왜 반말이냐?" with vpunch
    l "너 같은 애를 찾고 있었어."

    n "나같은애?"

    n "저리 안꺼져?!!" with vpunch

    show lee smile at rightCharacter with dissolve

    l "아하핫!! 웃기다 너."

    
    l "야. 그러지 말고 번호 교환이나 하자."

    menu:
        "싫은데? 병신아.":
            n "싫은데? 병신아."
            show lee jeongsack at rightCharacter with dissolve
            l "..."
            jump bad_ending1
        "그래. 좋아(얘라도 같이 다니자.. ㅅㅂ)":
            "하..재수없지만 친구 1도 없으니까..."
            "얘랑이라도 친구를 하자..."
            jump phone
        
        "사람 농락하니까 잼있니?":
            show lee normal at rightCharacter with dissolve
            l "헤헤.."
            l "저 친구 없는데.. "
            show lee smile at rightCharacter with dissolve
            l "주시면 안될까요?"
            menu:
                "준다.":
                    label phone:
                    "번호를..."
                    "줘버렸다아!!.." 
                    play music "audio/bgm/frustrate.mp3"

                    stop music fadeout 5.0


            scene room
            play music "audio/bgm/drive.mp3"
            "기빨리는 하루였어.." with vpunch
            "자려던 찰나에"

            play music "audio/bgm/message.mp3"

            "아까 본 띠꺼운 금발 애한테 카톡이 왔다."

            "이름이 이연우였나?"

            stop music fadeout 5.0

            play music "audio/bgm/drive.mp3"

            scene kakao

            l "야 자냐?"
            menu: 
                
                "친한 척 하지마.":
                    l "이런 싸가지 없는 기집애를 봤나."
                    l "됐고, 나 심심하니까 놀아달라."
                
                "왜?":
                    l "나 심심해."
                    l "놀아줘어어"
                    "생긴거랑 다르게 말투가 왜이래?" with vpunch
                    $ lee_ +=1
                    

            "(왜 이렇게 친한척이지 ??)"

            n "너.. 친구없어?"
            l "ㅋ 나 친구 많아."
            n "근데 나한테 왜이렇게 들이대??"
            l "웃겨서 ㅋ"

            "뭐가 웃기다는 거야....."
            l "아 근데 오해하지 마셈. 너 내스타일 아니야."
            l "내일 학교에서 밥이나 먹자."

            n "응 그래.."
            "(정말 그냥 불쌍해서 챙겨주는 건가..??)"
            "그렇게 생각하며 난 잠이 들었다."

            stop music fadeout 5.0

            
            scene university

            play music "audio/bgm/loudful.mp3"

            "밥먹기로 했는데.."

            "왜 안와.."

            stop music fadeout 5.0

            play music "audio/bgm/yeon.mp3"
            
            show lee normal at leftCharacter with dissolve

            l "여어."

            stop music fadeout 5.0
            play music "audio/bgm/back.mp3"

            menu:
                "왜이러케 늦게 오세요?;;":
                    n "왜이러케 늦게 오세요?;;"

                    l "ㅎㅎ. 미안."
                    show lee smile at straight with dissolve
                    $ lee_ +=1
                
                "어. 왔어?":
                    n "어. 왔어?"
                    l "안녕하세요?"

            l "아."
            l "인사해. 여기는 홍예준이야."

            show hong normal at left with dissolve

            

            "(이 껄렁한 애는 뭐야!!!)"

            

            h "안녕하세요."

            menu:
                "근육들이 아름답네효..오호홓^^":
                    n "근육들이 아름답네효..오호홓^^"

                    show hong mad at straight with dissolve
                    h "으.."

                    show lee jeongsack at left with dissolve
                    l "...미쳤냐?"

                    play music "audio/bgm/frustrate.mp3"

                    stop music fadeout 5.0
                    jump bad_ending1

                "아 네 안녕하세요.":
                    n "아 네 안녕하세요."

                "근육 한번만 만져봐도 될까요?":
                    n "근육 한번만 만져봐도 될까요?"
                    show hong mad at straight with dissolve
                    h "으.."

                    play music "audio/bgm/frustrate.mp3"
                    stop music fadeout 5.0

                    show lee jeongsack at left with dissolve
                    l "...미쳤냐?"

                    jump bad_ending1

            h "연우 친구시라고요."
            n "아.....ㄴ...네!"
            n "혹시 무슨 과세요?"
            h "저는 체대다녀요"
            menu:
                "아 뭔가 이미지가 잘 어울리는 것 같아요.":
                    h "아 그래요? 감사합니다."
                    $ hong_ +=1


                "그래서 몸이 좋으시구나 ㅎㅎ":
                    h "아..."
                    h "별로 안 좋은데...감사합니다..!"
                    $ hong_ -=3
                    $ hong__ +=3
                
            h "아 맞다 연우형이랑 동갑이시라고.."
            h "저는 20살이에요."
            l "애기야 애기."
            menu:
                "말 편하게 하셔도 돼요.":
                    $ hong_ +=1

                "아 뭐야 ㅋ 말 놔도 되지?":    
                    $ hong__ +=3  #6
                    $ lee_ -=1
            h "오 알았어. 누나."
            h "누나 그다음 수업 있어?"
            "엉..."
            l "나는 왼쪽으로 가고 얘는 오른쪽으로 가는데,"
            h "어느 쪽으로 가?"

            "어디로 가든 똑같은데.."

            
            menu:
                "왼쪽(이연우와 같이 간다.)":
                    n "아 나 왼쪽 방향이야."
                    show lee happy at leftCharacter with dissolve
                    $ lee_ +=1

                    scene with_lee1
                    "그렇게 이연우랑 같이 걷게 되었다."
                    "원체 말이 많아서 조용할 틈이 없이 즐거웠다."

                    show lee jeongsack at leftCharacter with dissolve

                    "...?"
                    l "박세현이다."
                    show lee smile at leftCharacter with dissolve 
                    show park normal at left with dissolve

                    p "연우 하이."
                    p "아..."
                    p "안녕하세요."
                    menu: 
                        "안녕하세요.":
                            $ park_ += 2
                            p "네."
                            p "연우야 수업에서 봐."
                            l "어.."
                            "박세현은 그렇게 말하곤 유유히 떠나갔다."
                            jump no_fight
                        "씹는다.":
                            show park jeongsack at left with dissolve
                            p "연우야 수업에서 보자."
                            l "아...그래."
                            "박세현은 그렇게 말하곤 유유히 떠나갔다."
                            jump no_fight
                        "뭐라고 씨부리고 다니냐 니?":
                            show park jeongsack at left with dissolve
                            p "네?"
                            $ lee_ +=5
                            jump fightwithp

                "오른쪽(홍예준과 같이 간다.)":
                    n "아 나 오른쪽 방향이야."
                    show hong happy at left with dissolve
                    $ hong_ +=1
                    

                    scene with_hong1

                    "그렇게 예준이와 같이 걷게 되었다."
                    show hong normal at leftCharacter with dissolve
                    h "근데 연우형이랑은 어떻게 친해지게 된거야?"
                    menu: 
                        
                        "같이 어떤 남자애 욕 하다가 친해졌어.":
                            n "엠티때 같이 나가자길래 거절했는데"
                            n "그거 가지고 뒤에서 나 욕하고 다니는거 있지?"
                            n "같이 아이스크림 먹으러 나가자는건"
                            n "뻔한 남자 여우짓아니여?"
                        
                            h "당연하지.. 그런 일이 있었어?"
                            $ hong_+=1
                            h "누군진 몰라도 남자가 너무 찌질하네."
                            h "이름이 뭔데?"

                            menu: 
                                "아 이름을 말하긴 좀..":
                                    h "그랭? 까비."
                                    $ hong__ +=1 #7
                                    h "누나 수업 끝나고 뭐해?"
                                    "아무것도 안하는데?"

                                    h "어??"
                                    h "세현이형!"
                                    show park normal at leftPark with dissolve
                                    "박세현은 나를 보더니 표정이 약간 굳었다."
                                    

                                    p "예준. 이따 술자리 올거지?"
                                    h "당연하지."
                                    h "아 누나. 이쪽은 박세현형. 누나랑 같은 과 아냐?"

                                    p "아 맞아."
                                    p "음.. 오늘 저희 과 애들도 많이 오는데."
                                    p "시간되시면 술자리 오실래요?"
                                    show hong happy at leftCharacter with dissolve
                                    h "오 누나도 와 ㅎㅎ"

                                    "(어떡하지..)"
                                    "(일정 없는걸 말해버려서..거절하기가..)" with vpunch
                                    n "아...."
                                    n "아.. 그럴까요?"
                                    jump sulzari





                                "박세현.":
                                    $ hong_ +=1
                                    h "허거걱.. 세현이형이? 실화냐.."
                                    show hong jeongsack at leftCharacter with dissolve
                                    h "어...?"
                                    h "세현이 형이다.."
                                    show park normal at left with dissolve
                                    p "어 뭐야 예준이 하이."
                                    "박세현은 나를 보더니 잠시 얼굴이 굳었다."

                                    show park jeongsack at left with dissolve
                                    p "안녕하세요."

                                    menu: 
                                        "안녕하세요.":
                                            p "아. 네."

                                            p "예준이 이따 헬스장 올거지?"
                                            h "아....음..엉."
                                            p "그래 잘가."

                                            "박세현은 그렇게 유유히 떠나갔다."
                                            jump no_fight
                                        "나 좀 작작 까고 다녀.":
                                            p "뭐라고요?"
                                            jump fightwithph





label bad_ending1:

    play music "audio/bgm/badending.mp3"
    scene room
    "그날 이후로.. 누구와도 연락을 해도.."
    "돌아오는건 읽씹이나 안읽씹 뿐이었다.."
    "..."

    scene university
    "대학에서 나는.."
    "병신이라고 소문이 났다.."
    
    "저기서 걸어오는 박세현이 보였다."

    show park normal at leftCharacter with dissolve

    p "ㅉ."

    "..."
    "죽고싶다..."
    "Bad ending"
    return

label suzokguan:
    
    scene suzok
    play music "audio/bgm/suzok.mp3"
    show lee smile at leftCharacter with dissolve
    l "왔어?"
    $ lee_+=1

    "그렇게 물고기를 보며 즐거운 시간을 보냈다."

    "연우와는 얘기가 잘 통해서 그런지 "
    "편했다."

    show lee normal at leftCharacter with dissolve
    l "너는 이상형이 뭐야?"
    menu:
        "그게 왜 궁금? 일단 넌 아니니까 안심해라 ㅋ":
            $ lee_ -= 4
            show lee jeongsack at leftCharacter with dissolve
            l "그냥 연구차원에서."
            l "괜히 물어봤네."
            show lee normal at leftCharacter with dissolve
            l "너는 너의 모습 중에서 가장 맘에 드는 곳이 어디야?"
            menu:
                "얼굴":
                    l "아하."
                "매끈한 다리":
                    l "아하."
                "잘록한 허리":
                    l "아하."
                "없는데?":
                    l "아하."
                "다 맘에 드는데? 난 딱히 콤플렉스가 없어.":
                    show lee happy at leftCharacter with dissolve
                    $ lee_ += 5
                    l "뭐지 이자신감?"
                
        "말 잘 통하는 사람.":
            $ lee_ += 2
            l "오. 나돈데."

        "너?(찡긋)":
            $ lee_ += 3
            show lee smile at leftCharacter with dissolve
            l "으."

    "그렇게 뭔가 의미가 있을법한 대화가 오갔다."
    "연우와의 데이트는 즐거웠다."
    scene leesuzok

    l "오늘 놀아줘서 고맙다."
    n "나도 오늘 즐거웠어."
    stop music fadeout 5.0
    jump next_day












label no_fight:

    scene room

    "하..."
    "피곤한 하루였다."
    if park_>2:
        play music "audio/bgm/message.mp3"
        "엥?"
        "박세현한테 웬 메시지?"
        stop music

        scene kakao
        p "안녕하세요."
        p "제가 연우한테 들었는데"
        p "제가 오해를 한 것같아서요."
        p "괜찮으시면 제가 밥을 사드리고 싶은데."
        p "괜찮을까요?"

        menu:
            "네.":
                p "그럼 내일 수업끝나고 학교 건물 앞에서 봬요."
                jump bob
            "싫어요.":
                p "아..."
                p "네 알겠습니다.."
                "이제와서 뭔 밥이야.. 피곤하니까 잠이나 자야겠다."

            
    "내일도 학교에 가야한다니.."
    scene university
    "그렇게 1년이 지났다.."

    "난 친구 2명정도 사겨서 걔네들이랑만 다녔고"
    "이연우랑은 종종 밥을 먹었다."

    "학교를 다니면서 박세현을 마주치긴 했지만"
    "별로 불편하진 않았다."

    "편하지만 신나지도 않는 나날의 연속이었다."

    "Normal ending"
    return



label bob:
    scene university
    play music "audio/bgm/loudful.mp3"
    show park normal at leftCharacter with dissolve

    p "안녕하세요."
    "안녕하세요."

    p "뭐 드실래요??"
    n "음..."
    n "여기 근처에 아는 맛집 있으세요?"    
    p "아 아는곳 있는데 거기로 갈까요?"
    p "좋아요.."

    scene restaurant

    play music "audio/bgm/park.mp3"

    "비싼곳 같은데.." with vpunch

    show park normal at leftCharacter with dissolve

    p "메뉴는 어떻게 하실래요?"
    p "제가 사기로 약속했으니까 편하게 드세요."

    n "나는 그나마 싼 가격인 '송아지 트러플 스테이크'를 골랐다."
    p "여기 주문이요."
    p "송아지 트러플 스테이크랑 캐비어 알밥 하나씩 주세요."

    n "근데 갑자기 밥 왜 먹자고 하신거에요??"
    "궁금해서..."

    p "아 제가 그게.."
    p "아 진짜 죄송한데.."
    p "그때 엠티 갔었던 날."
    p "제 친구가 그쪽을 맘에 들어해서"
    p "한번만 데리고 와달라고 부탁했었는데..."
    p "제가 거절했다고 대신 말해주니까"
    p "이야기가 와전돼서..."
    p "얘기가 안좋게 소문이 난것같아요.."

    n "뭐야..."
    n "박세현이 아니라 다른애가 부탁했었다고?"

    menu:
        "다른애가 누구인데요?":
            p "아..."
            p "그게.."
            p "이연우..요."

            play music "audio/bgm/frustrate.mp3"
            "이연우라고?" with vpunch
            "뭐하는 놈이야 도대체??.."


        "아 전 그런줄도 모르고ㅠㅠ":
            p "아 저라도 절 오해했을거예요."

    play music "audio/bgm/park.mp3"

    n "아무튼 오해해서 죄송해요."

    p "그럼 이제 말 놓을까?"
    n "몇살이신데요?"
    p "아 나 23살인데 편하게 오빠라고 불러도되."
    menu:
        "엉!":
            $ park_ +=1
        "웅..!":
            $ park_ +=1

        "그래 좋아 ㅎㅎ":
            $ park_ +=1

    g "음식 나왔습니다."

    "음식은 아주 맛있었다."

    
    p "음식은 입에 잘 맞아?"

    n "웅 ㅎㅎ"

    
    p "사실...."
    p "너가 밥먹겠다고 했을때 기분 좋았어."

    n "엥..."
    n "왜??"

    p "솔직히 첫눈에 반한거 같아."
    p "엠티 때 친구가 데리고  오라고 했었을때"
    p "사실 나도 보고 반했어."

    p "나랑..사귈래?"
    "잘생겻으니까.."
    "그냥 사귈까?"
    n "그래 좋아."

    show park happy at leftCharacter with dissolve

    p "헉....그럼 1일인건가?"

    stop music fadeout 5.0



    scene with_lee1
    play music "audio/bgm/hong.mp3"

    "그렇게 난 세현오빠와 사귀게 되었다."

    show park happy at leftCharacter with dissolve

    p "자기야."


    "세현오빠와는 cc여서 그런지 자주 만날 수 있었다."

    "세현오빠는 친구가 많아서 나까지 친구가 많아졌다."
    "피곤하긴 하지만 외롭지는 않은 대학생활이었다."

    "Happy ending"

    return



    



                
label fightwithp:
    scene fightwithp

    play music "audio/bgm/fight.mp3"

    p "뭐라고 하셨어요 지금?"

    n "너가 나 뒤에서 까고 다니는거 맞잖아."

    p "증거 있어?"

    p "너 허언증 있냐?"

    stop music fadeout 5.0

    scene with_lee1

    show lee jeongsack at leftCharacter with dissolve

    l "야 박세현."

    l "너가 나한테 얘 사회성 없다고 같이 놀지 말라고 깠잖아."

    "(사회성 없다고 깐거였냐!!)" with vpunch

    show park jeongsack at left with dissolve

    p "야. 이연우."
    p "ㄴ...너..!"
    p "하.. 그래 둘이 잘 놀아라 ㅋ;"

    "그렇게 말하곤 박세현은 유유히 떠나갔다.."

    scene with_hong1

    play music "audio/bgm/lee.mp3"

    
    show lee normal at leftCharacter with dissolve
    l "할말도 제대로 못 하는 줄 알았더니."
    l "너 다시봤는데?"

    

    menu:
        "너야말로 박세현이랑 괜찮겠어?":
            $ lee_ +=1
            l "저런애랑 어떻게 되든 괜찮어."
            l "쟤 없어도 나 친구 많아서 ㅎ"
        
        "그러게 누가 까고 다니래?":
            l "내말이."

        "ㅋ 이게 나야.":
            l "오."

    l "은근 할말도 다하고."

    l "매력적인데?"
    show lee smile at leftCharacter with dissolve

    menu:
        "반하겠어?":
            $ lee_ += 1
        
        "미안한데 넌 내취향아님ㅋ":
            $ lee_ += 2
        
        "으...뭐래 ;;":
            $ lee_ -=1

    l "쳇.."
    if lee_ > 8:

        l "나랑 내일 수족관 갈래?"
        "갑자기??" with vpunch
        n "뭐.."
        n "할것도 없고.."
        n "좋아."
        jump suzokguan

    jump next_day

        




    




label fightwithph:
    scene fightwithp

    play music "audio/bgm/fight.mp3"

    p "뭐라고 하셨어요 지금?"

    "너가 나 뒤에서 까고 다니는거 맞잖아."

    p "증거있어?"

    play music "audio/bgm/frustrate.mp3"

    "아....!!" with vpunch

    "증거가...없다....."

    stop music fadeout 5.0

    show hong jeongsack at leftCharacter with vpunch

    h "뭐야 누나?"
    h "구라친 거야?"

    n "그게 아니라....!!" with vpunch

    "그러나 내가 무슨 말을 해봐도 믿어주지 않는 눈치였다."

    "그렇게 홍예준과도 사이가 이상해진 후 하루가 끝났다.."
    jump next_day




label sulzari:
    scene sulzari

    play music "audio/bgm/loudful.mp3"

    show park normal at leftCharacter with dissolve
    $ park_ += 2  #3

    p "이렇게 흔쾌히 와주실 줄 몰랐어요."
    p "우리 동기인데 말 놓을래?"
    p "아. 난 군대다녀와서 23살이야."

    
    n "오 알았어."

    menu:
        "근데 뒤에서 내 얘기 하고 다녔어?":
            p "엉..?"
            $ park_ -=3 #0

            "그때 익숙한 목소리들이 들렸다."

            show park jeongsack at left with dissolve

            play music "audio/bgm/yeon.mp3"

            show lee smile at leftCharacter with dissolve

            show hong normal at right with dissolve

            h "누나!"
            l "뭐야. 너도 여기 왔냐?"

            "뭐야! 이연우도 왔네?"

            l "재미도 없는데 우리끼리 나가자."

            "좋아."

            stop music fadeout 5.0

            scene night

            play music "audio/bgm/lee.mp3"

            show hong normal at leftCharacter with dissolve
            h "근데 누나는 연애 안해?"

            menu: 
                "난 연애는 안하고 싶어.":
                    $ hong__ +=5
                    h "아..."
                    h "그래..?"
                    if hong__ > 8:
                        jump hong_badending

                "남자친구가 없는데 어떻게 해.":
                    h "그럼 만약에."
                    h "연애한다면 우리 중에 어떤 스타일이랑 하고 싶어?"
                    menu: 
                        "이연우":
                            $ lee_ +=5
                            if lee_ > 8:
                                show lee happy at left with dissolve
                                l "ㄴ..난 아니거든?"
                                jump suzokguan

                        "홍예준":
                            $ hong_ +=5
                            if hong_ > 8:
                                show lee jeongsack at left with dissolve
                                h "근데 우리 이대로 집에 갈꺼야?"
                                h "아쉬운데..."
                                h "나 자취방 여기 근처인데 한잔만 더 하고 가자 ㅠ"

                                l "난 집간다."

                                "(난 더 놀고 싶긴한데..)"
                                "(어떡하지?)"
                                l "너도 앵간하면 집에 가."
                                menu: 
                                    "집에 간다.":
                                        jump next_day
                                    "더 놀다 간다.":
                                        jump hongsroom

                                




        "23살이면 오빠네.":
            p "오빠라고 해도되."
            "아..네..."

            scene night

            "세현오빠와 나는 그날 이후로 썸을 타다 사귀게 되었다."

            "1달 후.."

            scene university
            "오늘은 세현오빠를 만나는 날이다."
            "ㄷㅔ이트 한다고 나름 차려입음 ㅎㅎ"

            play music "audio/bgm/bell.mp3"

            "여보세요?"
            stop music

            p "아 나 오늘 친구들이랑 갑자기 볼링치기로 약속이 잡혀서."
            p "못 갈 것 같아."

            "아니 나랑 한 약속이 선약이잖아."
            "장난해?"

            p "..."
            p "그럼 이제 그만"
            p "헤어질까?"


            "....."
            "그렇게 박세현의 일방적인 통보로"
            "우린 헤어지게 되었다.."

            "Bad ending"
            return




label hong_badending:
    scene room
    "오늘도 고단한 하루였어.."
    play music "audio/bgm/bell.mp3"

    "엥...?"
    "홍예준..?"
    "이 시간에 왜..."

    stop music fadeout 5.0

    "그렇게 전화를 2시간가량 했다.."
    "그 뒤로도 매일 전화가 왔다."
    "'밤'마다.."

    "통화내용은 수위높은 대화가 오갔다."
    "다른 일상적인 대화를 해보려해도,"
    "뭔가 이상한 이야기로 유도하는 느낌이었다."

    scene night
    "어느날 술김에 홍예준과 잠을 자버렸다."

    "그때 까지만 해도 난 썸을 타고 있다고 믿었다.."

    play music "audio/bgm/frustrate.mp3"

    "그런데.." with vpunch
    "잠을 자고 난 뒤에도 사귈 기미는 보이지 않았다."
    "오히려 관계가 더 흐지부지 되는 느낌이었다."

    "이건 아니란걸 알면서도.."
    "그에 대한 나의 마음은 커지고 있었다.."
    "Bad ending"

    return


label hongsroom:
    scene hongsroom
    play music "audio/bgm/hong.mp3"

    "그렇게 홍예준의 자취방에 오게 되었다."
    "안은 생각보다 깨끗했다."
    "뭔가 향기도 나는 느낌 -.-++"
    "기분이 요상..><"

    show hong normal at leftCharacter with dissolve
    h "누나 뭐 마실래?"
    "뭔가 긴장되는데.."
    "긴장을 풀기 위해선 술을 마시고 싶다."
    menu: 
        "술 있어?":
            $ hong__ +=2
            if hong__ > 5:
                jump hong_badending2

        
        "물이나 한잔 줘라.":
            $ hong_ +=2
        "오렌지 쥬뜨 조오..!!>_<":
            $ hong_ -=2

    h "누나 심심한데 바다 갈래?"
    n "바다?"
    menu:
        "간다.":
            scene driving
            play music "audio/bgm/drive.mp3"

            "예준이는 운전을 잘했다."
            "창 밖으로 보이는 바다는 예뻤다."

            h "어때?"
            menu:
                "시원하네":
                    $ hong_ +=1
                "운전 좀 하는데?":
                    $ hong_ += 2
                "야 김여사. 운전 좀 똑바로 하지?":
                    $ hong_ -= 3
                    h "뭐라고?"
                    "홍예준이는 화가난건지 갑자기 속도를 올렸다."
                    stop music 
                    "야야 속도좀 줄여..!"
                    h "나 운전 잘하잖아."
                    h "빨리 그 말 취소 안해?"
                    play music "audio/bgm/heart.mp3"
                    "얘가 왜이래???"
                    h "빨리 잘한다고 하라고!!"
                    play music "audio/bgm/frustrate.mp3"
                    n "어어..!!" with vpunch
                    n "잘해 잘해!!" with vpunch
                    "그러나 그는 너무 빠른 속도에 본인도 놀란 모양이었다."
                    play music "audio/bgm/shout.mp3"
                    n "꺄아아아악!!" with vpunch
                    stop music
                    scene accident
                    play music "audio/bgm/crash.mp3"
                    "...."
                    h "..."
                    "Bad ending"
                    return
            h "훗."
            h "누나.."
            h "나 솔직히.."
            h "누나 처음봤을때부터"
            h "귀엽다고 생각했어.."
            h "은근 당당한것도 내스타일이야."
            h "나 누나가 이성으로 보이는데"
            h "우리 만나볼래?"
            menu:
                "그래.":
                    h "우와..."
                    h "그럼 우리 오늘부터 1일인거네?"
                    n "응...!!*^^*"
                    h "고마워 누나.."
                    h "내가 잘할게..!"
                    jump hong_happyending
                "싫은데? 너 따위랑?":
                    h "뭐라고?"
                    "홍예준이는 화가난건지 갑자기 속도를 올렸다."
                    stop music 
                    n "야야 속도좀 줄여..!"
                    
                    h "누나랑 사귀고 싶었는데....!!"
                    play music "audio/bgm/heart.mp3"
                    n "이새끼가 갑자기 왜이래!!" with vpunch
                    play music "audio/bgm/frustrate.mp3"
                    n "어어..!!" with vpunch
                    n "사겨 사겨!!" with vpunch
                    "그러나 그는 너무 빠른 속도에 본인도 놀란 모양이었다."
                    play music "audio/bgm/shout.mp3"
                    n "꺄아아아악!!" with vpunch
                    stop music
                    scene accident
                    play music "audio/bgm/crash.mp3"
                    "...."
                    h "..."
                    
                    "Bad ending"
                    return

label hong_happyending:
    scene morning
    play music "audio/bgm/hong.mp3"
    "준이와 사귄지 그로부터 1년이 지났다.."
    show hong happy at leftCharacter with dissolve
    h "자기야 일어났어?"
    h "아침밥 해놨으니까 먹어."

    "..."
    "아침밥은 오늘도.."
    "단백질 쉐이크와 닭가슴살이구나.."

    "준이와 사귄뒤로 난.."
    "많이 변했다.."
    show hong normal at leftCharacter with dissolve

    h "입맛에 맞아?"
    n "응.. 맛있네.."
    show hong jeongsack at leftCharacter with dissolve
    h "이따 헬스장 가는거 잊지 말고."

    "(난 그와 사귄뒤로 근육질 몸을 갖게 되었다.)"
    "(처음에는 내 여리여리한 과거의 몸이 그리웠지만)"
    "(지금은.)"
    n "그이가 좋아하니까 나도 좋아."

    n "응!! 알겠어!! 사랑해 ~!!"
    show hong happy at leftCharacter with dissolve

    stop music fadeout 5.0
    "Happy ending"
    return




            



label hong_badending2:
    scene morning
    play music "audio/bgm/frustrate"
    n "어....????..."

    n "좆됐다..."
    show hong jeongsack at leftCharacter with dissolve
    h "아..."
    "상대 쪽도 많이 놀란기색이었다."

    stop music fadeout 5.0

    "아 맞다 수업..!"
    "나는 수업때문에 서둘러 옷을 주서입고 학교에 갔다."

    scene university

    play music "audio/bgm/loudful.mp3"
    "수업을 듣기는 했지만 집중이 전혀 되지 않았다."
    "물론 홍예준한테도 별다른 연락이 오지 않았다."

    "며칠뒤.."
    "내가 홍예준 자취방에 같이 들어갔다는 소문이 돌았고"

    "나는 대학소문이 더 안좋아지게 되었다."

    "저 멀리서 친구들과 걸어오는 박세현이 보였다."

    show park normal at leftCharacter with dissolve
    p "ㅋㅋ"

    show lee jeongsack at left with dissolve

    l "미안.."

    
    "이상하게도 홍예준은 소문이 났음에도 여전히 친구들이 많았고"
    "나는 혼자 다니게 되었다."
    "Bad ending"







label next_day:

    scene university
    play music "audio/bgm/loudful.mp3"

    "오늘도 어김없는 하루가 시작되었다."


    if lee_ > 9:
        
        play music "audio/bgm/bell.mp3"
        

        stop music
        "여보세요."
        l "여보 아니고요."
        l "할말 있으니까 거기서 기다리세요."

        "엥? 할말?"

        "약 5분 후 이연우가 나타났다."
        play music "audio/bgm/lee.mp3"

        show lee normal at leftCharacter with dissolve

        l "하이."
        n "사람을 이렇게 경우없이 불러세우다니."
        n "할말이 뭔지 들어볼까?"

        l "별건 아닌데.."
        l "솔직히 좀 고민했는데.."
        l "나랑..."
        l " 사귈래?"

        play music "audio/bgm/heart.mp3"

        n "어..??"

        "나를 왜?"
        l "솔직히 처음봤을때부터 귀엽다고 생각하긴 했는데.."
        l "귀엽다뿐이지 별 관심은 없었는데."

        l "나는 생각보다 할말도 못하고 솔직하지 못하거든."

        show lee happy at leftCharacter with dissolve
        l "근데 당당하고 할말 다하는게"
        l "진심으로 멋있어서.. 확 마음이 생긴것 같아."

        "(솔직히 나도..)"
        "(계속 이연우가 생각나고)"
        "(재밌는거 있으면 이연우랑 하고 싶은 생각이 들어.)"

        n "나도 너한테 마음이 있는것같아."
        n "그래 사귀자."

        l "진짜??"

        l "좋아."

        "그렇게 우린.. 사귀게 되었다.."

        scene temapark
        play music "audio/bgm/strawberry.mp3"

        "그렇게 연우찡과 사귀게 된지 어언 1년...."
        "1주년을 맞아 놀이공원에 오게 되었다."

        show leef at leftCharacter with dissolve

        l "자기야."

        l "오늘도 예쁘네."

        n "뭐래...(내심 좋음 ^^*)"
        n "너도 오늘 예쁘네."

        l "나야 뭐 매일 이쀼징 ^^"

        n "놀이기구나 타러가자."

        n "너 놀이기구 못타좌나."
        l "칫..잘타거든?"

        "그날은 사람이 없어서 그런지"
        "놀이기구를 8개나 탈 수 있는 날이었다."

        "날 잘 잡았다 그치??"
        l "그러게."

        scene merrygoround
        play music "audio/bgm/park.mp3"

        "그렇게 신나게 놀고 밤이 되었다.."

        "이연우의 손은 언제나 그랬듯 따뜻했다."

        show leef at leftCharacter with dissolve

        l "신기해."
        menu:
            "뭐가?":
                $ lee_ +=1
            "뭔소리야?":
                $ lee_ -=1
            
        l "그냥 난 원래 연애든 짝사랑이든"
        l "빨리 식는편인데."

        l "너랑만 있으면 마음이 더 커져."
        n "..."

        play music "audio/bgm/heart.mp3"
        scene merry

        "연우랑 사겨서 너무 행복하다.."
        n "헹복해.."
        "행복하다고...."

        "...."
        "해피엔딩."
        return
            


    "아 띠바 자퇴하고 싶다.."
    n "자퇴해야지."
    "그렇게 나는 충동적으로 자퇴하게 되었다."
    "zate ending"
    return








                    

                



            


    




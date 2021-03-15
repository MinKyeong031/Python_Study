# def phonenumber_to_region(phone):
    # first = phone[1]
    # second = phone[2]
    # if first == '1':
    #     return "휴대폰"
    # elif first == '2':
    #     return "서울"
    # elif first == '3':
    #     if second == '1':
    #         return "경기"
    #     elif second == '2':
    #         return "인천"
    #     elif second == '3':
    #         return "강원"
    # elif first == '4':
    #     if second == '1':
    #         return "충남"
    #     elif second == '2':
    #         return "대전"
    #     elif second == '3':
    #         return "충북"
    #     elif second == '4':
    #         return "세종"
    # elif first == '5':
    #     if second == '1':
    #         return "부산"
    #     elif second == '2':
    #         return "울산"
    #     elif second == '3':
    #         return "대구"
    #     elif second == '4':
    #         return "경북"
    #     elif second == '5':
    #         return "경남"
    # elif first == '6':
    #     if second == '1':
    #         return "전남"
    #     elif second == '2':
    #         return "광주"
    #     elif second == '3':
    #         return "전북"
    #     elif second == '4':
    #         return "제주"
    # elif first == '7':
    #     return "인터넷전화"

def phonenumber_to_region(phone):
    region = {"02":"서울", "051":"부산", "053":"대구", "032":"인천", "062":"광주", "042":"대전"
        , "052":"울산", "044":"세종", "031":"경기", "033":"강원", "043":"충북", "041":"충남", "063":"전북"
        , "061":"전남", "054":"경북", "055":"경남", "064":"제주", "010":"핸드폰", "070":"인터넷전화"}
    regionnum = phone.split("-")[0]
    for i in region.keys():
        if regionnum == i:
            return region.get(i)

r1 = phonenumber_to_region("02-872-4071")
r2 = phonenumber_to_region("010-1111-2222")
r3 = phonenumber_to_region("031-1234-5678")
print(r1)
print(r2)
print(r3)
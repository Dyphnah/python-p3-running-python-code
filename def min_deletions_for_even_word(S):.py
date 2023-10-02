S= 'This is hard'

def solution(S):
    length=len(S)
    characters_to_delete={}
    for i in S:
        x= S.count(i)
        if x%2!=0:
            characters_to_delete.append(x)
            # delete_numbers=0
            # while x >0:
                # delete_numbers+=1
            # print(delete_numbers)
            # z=len(b)
        print(x)
        # return z

print(solution(S))


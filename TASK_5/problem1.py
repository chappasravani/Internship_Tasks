if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_score=list(set(arr))
    unique_score.sort()
    print(unique_score[-2])
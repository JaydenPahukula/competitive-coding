for _ in range(int(input())):
    s = input()
    dp = [{c:0} for c in s]
    for i in range(len(dp)-1):
        c = s[i+1]
        dp[i+1][c] = max([dp[i+1][c]]+list(dp[i].values()))
        for b in dp[i]:
            if b=="A" and c=="B":
                dp[i+1]["C"] = dp[i][b]+1
            if b=="B" and c=="A":
                dp[i+1]["B"] = dp[i][b]+1
    print(dp)
    print(max(dp[-1].values()),"===========")
        


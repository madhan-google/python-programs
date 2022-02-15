def knapsack(w,weights,profits,n):
      sub = 1<<n
      max_val = 0
      for i in range(1,sub):
            j, t, w_sum, sums = 0, i, 0, 0
            while t > 0:
                  if (t&1) is 1:
                        sums += profits[j]
                        w_sum += weights[j]
                  j += 1
                  t >>= 1
            if w_sum <= w:
                  max_val = max(max_val,sums)
      return max_val

if __name__ == '__main__':
      profits = [60, 100, 120]
      weights = [10, 20, 30]
      W = 50
      print(knapsack(W,weights,profits,len(profits)))

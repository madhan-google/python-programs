if __name__ == '__main__':
      s = "hello"
      vow = []
      for i in s:
            if i is 'a' or i is 'e' or i is 'o' or i is 'u' or i is 'i':
                vow.append(i)
      vow.reverse()
      print(vow)
      j = 0
      for i in range(len(s)):
            ch = s[i]
            if ch is 'a' or ch is 'e' or ch is 'o' or ch is 'u' or ch is 'i':
                s[i] = vow.pop()
                #j += 1
      print(s)

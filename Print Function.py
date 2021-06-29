if __name__ == '__main__':
    n = int(input())
    string = ""
    if n in range (1,150):
        for i in range (1,n):
            string = string + str(i)
        string = string + str(n)
        print(string)
        

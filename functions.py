class news:

    def __init__(self, n):
        self.news = []
        self.n = n
        self.getdata(self.n)

    def getdata(self, n):
        for i in range(0, self.n):
            file = "news"+str(i+1)+".txt"
            self.news.append(self.read(file))
            print(self.news[i], end='\n\n\n')

    def read(self, txt):

        f = open(txt)
        n = f.readlines()

        i = 0
        for l in n:
            n[i] = l.strip()
            line = n[i].split(',')
            n[i] = line[0]
            #print(n[i])
            i += 1
        return n

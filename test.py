# import operator
# data = {'a':10,'b':20,'c':30,'d':40}
# res = {v:k for k,v in data.items()}
# #res = res.sorted(res.items(),key=operater.itemgetter(0))
# res = sorted(res.items(), key=lambda x: x[1])
# #print help(operator)
# #print res
# a = [10,20,30,40]
# b = [50,60,70,80]
# #res = zip(a,b)
# #res ={v:k for k,v in zip(a,b)} 
# res = filter(lambda x:x+1,a)
# res = map(lambda x,y:x+y,a,b)

# res = [x+y for x,y in zip(a,b)]
# #res = reduce(,a)
# print res
# class a:
# 	def __init__(self,x):
# 		print 'this is constracuter'
# 		self.x = x
# 	def disp(self):
# 		print 'dispp',self.x,self.y

# class b(a):
# 	def __init__(self):
# 		self.y = 320
# 		self._z = 800
# 		a.__init__(self,1000)

# 	def show(self,y):
# 		print self.y,self.x,self._z
# 		pass
# ob = b()
# ob.show(400)
# ob._z = 10000
# print ob._z
# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l) 

# f(1,[])
# f(3,[])
# f(4,[])
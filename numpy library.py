import numpy as np 
import random
#-------------------------------------scores---------------------------------------------
score = np.array([19,20,12,20,20,15,16,7,8,2,1,0,18,20,18,15.5,16.75,19.25,9,10])

#ali= score[0] 
#mamad = score[1]
#reza= score[2]
#shahin= score[3] 
#amir= score[4] 
 #first part 
sorted_scores= np.sort(score)[::-1]
print(sorted_scores)
#second part 

print("passed", score[score>=10])
  #third part
print("good_scores: ", score[score >=15]) 
print('bad_score :', score[score <15])
sum = np.sum(score <10)
print(sum)
def g():
     score[score <10] = 0
     print(score)
sum1 =np.sum(score[score >=10])/sum
print (sum1)

#-------------------------------------daily weather---------------------------------------------

daily_average= []
for i in range(31):
  temp =np.random.randint(10,50,30) 
  print(temp)
  sum1= np.mean(temp),daily_average.append(sum1)
print(daily_average)
print('warmest: ', np.sort(temp)[-1])
print('coldest: ' ,np.sort(temp)[0])
print (temp[temp > sum1])
b= np.sum( sum1 > 30 ) 
print(f'{b}') 
#-------------------------------------a random shop---------------------------------------------
sale= np.random.randint(100,1000,30) 
higher_days = np.sum(sale >700)
print(np.sum(sale))
print(np.mean(sale))
print('Highest: ', np.sort(sale)[-1])
print('Lowest: ', np.sort(sale)[0])  
Higher_sales = sale[sale >700]    
print(Higher_sales ) 
print(np.sum(higher_days))
print(np.argmax(Higher_sales)) 
#-------------------------------------daily workout---------------------------------------------
workout = np.random.randint(30,91,14)
calories = np.random.randint(300, 900, 14)
pll = np.column_stack((workout,calories))
print(pll)
print(np.sum(workout))
print(np.mean(workout))
minutes= np.round( np.mean(workout))
print(minutes)
print('longest: ', np.sort(workout)[-1])
print('shortest ', np.sort(workout)[0])
print(workout[workout > 60])
cool= workout >60 
print(np.sum(cool)) 
x=np.mean(workout) 
v = workout > x
print(np.sum(v))
p = workout[0:14]
o = calories[0:14]
print(p) 
print(o)
i = np.round(o / p)
print('for each minutes you burned : ', i , 'calories') 
#-------------------------------------workout performance analyzer(complete)---------------------------------------------
minutes = np.random.randint(30,91,14)
calories = np.random.randint(300, 900, 14)
punches = np.random.randint(50,220,14)
heartbeat = np.random.randint(120, 190, 14) 
everything = np.column_stack((minutes,calories,punches,heartbeat))
print(everything)
print(everything.ndim)
print(everything.shape)
print(everything.size) 
print(np.mean(everything , axis=1) )
print(np.mean(everything , axis=0) )
print(np.max(everything , axis=1) )
print(np.min(everything , axis=1))
print(np.sum(everything , axis=1))
k = minutes > 60
print(np.sum(k))
print(np.sum(calories > 700))
y = np.mean(minutes) 
x = minutes[0:14] 
l = x > y
#print(l)
print(np.sum(l))
r = heartbeat > 150
print(np.sum(r))
for i in range(len(minutes[minutes > 60] )): 
     b= i+1
     print(b)
ee=np.where(minutes>60)
print(ee)
#-------------------------------------functions explained with different demensions---------------------------------------------
#1D
A = np.array([1,2,3,4])
print(A)
X = np.ones(3) #3 ta onsor dare ke hamashun 1 hastan
Y= np.zeros(5) # 5 ta onsor drim ke hamash 0 hastan
T= np.empty(2) # be surate random dakhelesh ro por mikne_baadan bekhym por bknim_ baadan bkhym pooresh klnim, 2 ta onsor ham dare
print("x:",X)
print("y:",Y)
print("t:",T)
U = np.arange(2,7,3)
print("u:",U)
S = np.linspace(0,10, num=6 )
print("S:",S)
#2D 
D = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12 ]
    ])
print(D.ndim)
print(D.size)
print(D.shape)
P = np.array([[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12 ] 
    ],
    [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12 ] 
    ], ])
print(P.ndim)
print(P.size)
print(P.shape)
#jazr 
W= [1,5,2,7] 
print(np.prod(W)) # zarbee adad tooye w
print(np.power([2, 3], 3)) #2 va 3 be tavane 3
print(np.sin(np.linspace(-np.pi/2, np.pi/2 , 100))) #sinus 100 az -p/2 ta p/2
print(np.sqrt(4)) # jazr 4 
print(np.emath.sqrt(-4)) # jazr manfie 4 too adad mokhtalet
print(np.log(4)) # logarythm manfie 4 
print(np.emath.log(-4)) # logarithm manfie 4 too adad mokhtalet
a = np.arange(12)
print(a)
b= a.reshape(6,2)
print(b)
c= b.reshape(-1) 
print(c)
d=b.ravel()
print(d)
v= b.flatten() #copy mikne array a taqir nmikne 
print(v)
y= np.arange(3,9) 
print(y[0]) # baraye tak boadi
print(y[-1]) # onsore akhar
print(y[-3:]) # 3 taaye akhar 
print(y[-3: -2])
print(b[0]) # satre aval
print(b[0,1]) #satr aval sutune aval 
print(b[1, :])  # satr aval kole sutun

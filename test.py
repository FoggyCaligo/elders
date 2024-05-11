import matplotlib.pyplot as plt






x = [10,20,30,40,50,60,70,80]
y = [6.4, 21.6, 33.5, 44.5,50.5 , 54.2, 74.6, 133.4]
y2 = [5.5, 16.6, 20.0, 17.1, 15.9, 14.0, 23.5, 35.5]


graph = plt.plot(x,y, label="Male")
plt.scatter(x,y)

for i in range(len(x)):
    height = y[i]
    plt.text(x[i], height+0.25, '%.1f' %height, ha='center', va='bottom',size=12)


graph2 = plt.plot(x,y2,label="Female")
plt.scatter(x,y2)

for i in range(len(x)):
    height = y2[i]
    plt.text(x[i], height+0.25, '%.1f' %height, ha='center', va='bottom',size=12)



#plt.axis('off')
plt.gca().axes.yaxis.set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)




plt.setp(graph,linewidth=5.0)
plt.setp(graph2,linewidth=5.0)


plt.legend()
plt.show()

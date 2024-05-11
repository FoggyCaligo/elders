import matplotlib.pyplot as plt






x = [2015,2017,2025,2035,2045]
y = [5180000,5562000,6701000,7635000,8098000]
y2 = [23.2,24,29.7,39.3,45.9]


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





plt.show()

import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random
diceresult=[]
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1+dice2)
# calculating mean and standard deviation
mean = sum(diceresult)/len(diceresult)
median = statistics.median(diceresult)
mode = statistics.mode(diceresult)
print("mean is {}".format(mean))
print("median is {}".format(median))
print("mode is {}".format(mode))
standarddeviation = statistics.stdev(diceresult)
print("standarddeviation is {}".format(standarddeviation))
# finding first stdev,second stdev and third stdev
firststdevstart,firststdevend = mean - standarddeviation,mean+standarddeviation
secondstdevstart,secondstdevend = mean -(2*standarddeviation),mean+(2*standarddeviation)
thirdstdevstart,thirdstdevend = mean -(3*standarddeviation),mean+(3*standarddeviation)
# plotting chart and lines for mean,firststdev and secondstdev
fig = ff.create_distplot([diceresult],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name = "mean"))
fig.add_trace(go.Scatter(x=[firststdevstart,firststdevstart],y=[0,0.17],mode="lines",name = "stdev1"))
fig.add_trace(go.Scatter(x=[firststdevend,firststdevend],y=[0,0.17],mode="lines",name = "stdev1"))
fig.add_trace(go.Scatter(x=[secondstdevstart,secondstdevstart],y=[0,0.17],mode="lines",name = "stdev2"))
fig.add_trace(go.Scatter(x=[secondstdevend,secondstdevend],y=[0,0.17],mode="lines",name = "stdev2"))

fig.show()
# printing the values
listofdatawithinonestdev=[result for result in diceresult if result > firststdevstart and result < firststdevend]
listofdatawithinsecondstdev=[result for result in diceresult if result >secondstdevstart and result<secondstdevend]
listofdatawithinthirdstdev=[result for result in diceresult if result >thirdstdevstart and result<thirdstdevend]
print("{}% of data lies within one standard deviation".format(len(listofdatawithinonestdev)*100.0/len(diceresult)))
print("{}% of data lies within second standard deviation".format(len(listofdatawithinsecondstdev)*100.0/len(diceresult)))
print("{}% of data lies within third standard deviation".format(len(listofdatawithinthirdstdev)*100.0/len(diceresult)))
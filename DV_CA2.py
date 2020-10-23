import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
from scipy.misc import imread
import codecs

games = pd.read_csv("C:\\Users\\vikra\\OneDrive - National College of Ireland\\MSc Data Analytics\\Semester 2\\Data Visualization\DV CA2\\ign.csv")
fig,ax=plt.subplots(1,2,figsize=(22,10))
sb.countplot(games['release_month'],ax=ax[0],palette='Set1').set_title('Releases On Months')
plt.ylabel('')
sb.countplot(games['release_year'],ax=ax[1],palette='Set1').set_title('Releases on Years')
plt.xticks(rotation=90)
plt.show()

games.drop(['Unnamed: 0','url'],axis=1,inplace=True) #dropping the unneeded values
games.drop(games.index[516],inplace=True) #dropping the game released on 1970. It looked to be an outlier
games.head(2)

games['genre'].value_counts()[:10].plot(kind='pie',autopct='%1.1f%%',shadow=True,explode=[0.1,0,0,0,0,0,0,0,0,0])
plt.title('Distribution Of Top Genre"s')
fig=plt.gcf()
fig.set_size_inches(7,7)
plt.show()

fig,ax=plt.subplots(1,2,figsize=(22,10))
sb.countplot(games['release_month'],ax=ax[0],palette='Set1').set_title('Releases On Months')
plt.ylabel('')
sb.countplot(games['release_year'],ax=ax[1],palette='Set1').set_title('Releases on Years')
plt.xticks(rotation=90)
plt.show()

games['score'].hist(edgecolor='black')
fig=plt.gcf()
fig.set_size_inches(10,6)
plt.axvline(games['score'].mean(),color='b',linestyle='dashed')

games['platform'].value_counts()[:10].plot.pie(autopct='%1.1f%%',shadow=True,explode=[0.1,0,0,0,0,0,0,0,0,0])
fig=plt.gcf()
fig.set_size_inches(7,7)
plt.title('Top Platforms For Games')

plt.subplots(figsize=(15,15))
max_genres=games.groupby('genre')['genre'].count()
max_genres=max_genres[max_genres.values>200]
max_genres.sort_values(ascending=True,inplace=True)
mean_games=games[games['genre'].isin(max_genres.index)]
abc=mean_games.groupby(['release_year','genre'])['score'].mean().reset_index()
abc=abc.pivot('release_year','genre','score')
sb.heatmap(abc,annot=True,cmap='RdYlGn',linewidths=0.4)
plt.title('Average Score By Genre"s')
plt.show()

clone=games.copy()
clone['score_phrase']=clone['score_phrase'].map({'Awful':'Flop','Bad':'Flop','Disaster':'Flop','Unbearable':'Flop','Painful':'Flop','Mediocre':'Good','Okay':'Good','Great':'Hit','Amazing':'Hit','Masterpiece':'Masterpiece','Good':'Good'})
clone=clone[['score_phrase','platform','genre','score']]
max_platforms=clone['platform'].value_counts().index[:10]
plat=clone[clone['platform'].isin(max_platforms)]
plat=plat.groupby(['platform','score_phrase'])['score'].count().reset_index()
plat=plat.pivot('platform','score_phrase','score')
plat.plot.barh(width=0.9)
fig=plt.gcf()
fig.set_size_inches(12,14)
plt.show()

new_genres=max_genres.sort_values(ascending=False)[:10]
top_genres=games[games['genre'].isin(new_genres[:10].index)]
top_genres=top_genres.groupby(['release_year','genre'])['score'].count().reset_index()
top_genres=top_genres.pivot('release_year','genre','score')
sb.heatmap(top_genres,annot=True,fmt='2.0f',cmap='RdYlGn',linewidths=0.4)
fig=plt.gcf()
fig.set_size_inches(11,11)
plt.title('Releases By Top Genres By Years')
plt.show()

new=games.groupby(['release_year','platform'])['score'].count().reset_index()
#new.columns=[['release_year','platform','count']]
new=new.sort_values(by='score',ascending=False)
new=new.drop_duplicates(subset=['release_year'],keep='first')
new=new.sort_values(by='release_year')
new.set_index('release_year',inplace=True)
new.plot.barh(color='#0154ff',width=0.8)
fig=plt.gcf()
fig.set_size_inches(10,10)
for i, p in enumerate(zip(new.platform, new['score'])):
    plt.text(s=p,x=1,y=i,fontweight='bold',color='white')
plt.show()

plat_genre=games.copy()
plat_genre=plat_genre[plat_genre['genre'].isin(new_genres.index)]
plat_genre=plat_genre.groupby(['platform','genre'])['score'].count().reset_index()
plat_genre=plat_genre[plat_genre['score']>10]
plat_genre=plat_genre.pivot('platform','genre','score')
plat_genre=plat_genre.dropna(thresh=8)
sb.heatmap(plat_genre,annot=True,fmt='2.0f',cmap='RdYlGn',linewidths='0.1')
fig=plt.gcf()
fig.set_size_inches(9,9)
plt.show()




games.groupby('release_day')['genre'].count().plot(color='y')
fig=plt.gcf()
fig.set_size_inches(12,6)



year08=games.copy()
year08=year08[year08['release_year']==2008]
genres_2008=year08['genre'].value_counts()[:15]
f, ax = plt.subplots(1,2,figsize=(18,8))
year08['platform'].value_counts()[:10].plot.pie(autopct='%1.1f%%',ax=ax[0],shadow=True,explode=[0.1,0,0,0,0,0,0,0,0,0])
ax[0].set_title('2008 Top Platforms')
ax[0].set_ylabel('')
fig = plt.gcf()
year08['genre'].value_counts()[:10].plot.pie(autopct='%1.1f%%',ax=ax[1],shadow=True,explode=[0.1,0,0,0,0,0,0,0,0,0])
ax[1].set_title('2008 Top Genre')
ax[1].set_ylabel('')
plt.show()

year08['score'].hist(color='#65ff65',edgecolor='black')
x=range(0,11,1)
plt.xticks(x)
fig=plt.gcf()
fig.set_size_inches(10,6)
plt.axvline(year08['score'].mean(),linestyle='dashed',color='blue')

plt.subplots(figsize=(18,6))
swarm=year08[year08['genre'].isin(genres_2008.index)]
sb.swarmplot(x='genre',y='score',data=swarm,cmap='Set 3')
plt.axhline(year08['score'].mean(),linestyle='dashed',color='brown')
plt.rcParams["axes.labelweight"] = "bold"
plt.show()

plt.subplots(figsize=(12,6))
dummy=year08[year08['genre'].isin(genres_2008.index)]
dummy=dummy.groupby(['platform','genre'])['score'].count().reset_index()
dummy=dummy.pivot('platform','genre','score')
dummy=dummy.dropna(thresh=10)
sb.heatmap(dummy,annot=True,linewidths=0.2)

masterpiece = games[games['score_phrase'] == 'Masterpiece']
print('The total number of masterpieces produced till date are:', masterpiece.shape[0])

plt.subplots(figsize=(12,6))
sb.countplot(masterpiece['release_year'])

plt.subplots(figsize=(8,8))
f1=open("wii.png", "wb")
f1.write(codecs.decode(wii,'base64'))
f1.close()
img1 = imread("wii.png")
hcmask1 = img1
wordcloud = WordCloud(stopwords=STOPWORDS,background_color='black',width=1200,height=1000,mask=hcmask1,max_words=100
                         ).generate(" ".join(masterpiece['title']))


plt.imshow(wordcloud)
plt.axis('off')
plt.show()
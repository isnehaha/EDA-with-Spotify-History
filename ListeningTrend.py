import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\asus\Documents\Fourth Sem\Python Project\spotify_history.csv")

#1 Weekly Listening Trend

df['ts'] = pd.to_datetime(df['ts'])
df['date'] = df['ts'].dt.date
daily_play = df.groupby('date')["ms_played"].sum().reset_index()
daily_play['hours_played'] = daily_play["ms_played"]/(1000 * 60 * 60)

plt.figure(figsize=(10, 6))
daily_play['date'] = pd.to_datetime(daily_play["date"])
plt.scatter(daily_play['date'], daily_play['hours_played'], color = 'olive')
#df['ms_played'].value_counts().plot(kind = 'bar', color ='salmon')

plt.title("Daily Listening trend on Spotify", fontsize = 15)
plt.xlabel("Date", fontsize = 12)
plt.ylabel("Listening time(Hours)", fontsize = 12)

plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.tight_layout()
plt.show

#2 Top 10 Most Played Tracks
track_play = df.groupby('track_name')['ms_played'].sum().reset_index()
track_play['hours_played'] = track_play['ms_played']/(1000*60*60)

top_tracks = track_play.sort_values(by='hours_played', ascending=False).head(10)
plt.figure(figsize=(12, 6))
plt.plot(top_tracks['track_name'], top_tracks['hours_played'], color = 'darkblue', alpha = 0.7)
plt.title('Top 10 Most Played Tracks(by Listening time)')
plt.xlabel('Track name')
plt.ylabel('Listening Time(Hours)')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
#plt.tight_layout()
plt.show()


#3 Artist Popularity
artist_play = df.groupby('artist_name')['ms_played'].sum().reset_index()
artist_play['hours_played'] = artist_play['ms_played']/(1000*60*60)
top_artists = artist_play.sort_values(by = 'hours_played', ascending = False).head(10)

plt.figure(figsize=(8, 8))
plt.pie(top_artists['hours_played'],
        labels=top_artists['artist_name'],
        autopct = '%1.1f%%',
        startangle=140,
        colors = plt.cm.Paired.colors)

plt.title('Top 10 Artists by Total Listening Time(hours)')
plt.axis('equal')
plt.tight_layout()
plt.show()


#4 Skip Rate Analysis
track_stats = df.groupby('track_name').agg(total_plays = ('skipped', 'count'),
                                           total_skips = ('skipped', 'sum')).reset_index()
track_stats['skip_rate']=track_stats['total_skips']/track_stats['total_plays']
filtered_tracks = track_stats[track_stats['total_plays'] >= 5]

plt.figure(figsize = (10, 6))
plt.hist(filtered_tracks['skip_rate'],
        bins = 20,
        color = 'darkblue',
        edgecolor='black')
        
plt.title('Distribution of track Skipped Rates')
plt.xlabel('skip Rate')
plt.ylabel('Number of Tracks')
#plt.grid(axis='y')
#plt.axis('equal')
#plt.tight_layout()
plt.show()


#5 Listening Behavior by Platform
platform_play = df.groupby('platform')['ms_played'].sum().reset_index()
platform_play['hours_played'] = platform_play['ms_played']/(1000*60*60)
plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(platform_play['hours_played'],
                                   labels = platform_play['platform'],
                                   autopct = '%1.1f%%',
                                   colors = ['green','cyan'],
                                   startangle = 140,
                                   wedgeprops = dict(width = 0.7),
                                   labeldistance = 1.5,
                                   pctdistance=1.3)
plt.title('Listening time By platform (Donut Chart)')
#plt.axis('equal')
#plt.tight_layout()
plt.show()

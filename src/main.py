import pandas as pd
import numpy as np

# 파일 불러오기
rating_data = pd.read_csv('../ml-latest-small/ratings.csv')
movies_name = pd.read_csv('../ml-latest-small/movies.csv')
# movieId로 병합
movie_data = pd.merge(rating_data, movies_name, on='movieId')
rating_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())


user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')
Forrest_ratings = user_movie_rating['Forrest Gump (1994)']
movies_like_forrest = user_movie_rating.corrwith(Forrest_ratings)
corr_forrest = pd.DataFrame(movies_like_forrest, columns=['Correlation'])
corr_forrest.dropna(inplace=True)
# corr_forrest.sort_values('Correlation', ascending=False).head(10)
# corr_forrest = corr_forrest.join(rating_mean_count['rating_counts'])
# corr_forrest[corr_forrest['rating_counts']>50].sort_values('Correlation', ascending=False).head()


def recommend_content(userId):
    # Input: movieId(str)
    # Output: recommended movies(list)
    recommend_contents_list = []
    print(rating_data)


    return recommend_contents_list



if __name__ == '__main__':
    user_id = ''
    rec_list = recommend_content(user_id)
    print(rec_list)
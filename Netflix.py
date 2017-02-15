#!/usr/bin/env python3

# -------
# imports
# -------

from math import sqrt
import pickle
from requests import get
from os import path
from numpy import sqrt, square, mean, subtract


def create_cache(filename):
    """
    filename is the name of the cache file to load
    returns a dictionary after loading the file or pulling the file from the public_html page
    """
    cache = {}
    filePath = "/u/fares/public_html/netflix-caches/" + filename

    if path.isfile(filePath):
        with open(filePath, "rb") as f:
            cache = pickle.load(f)
    else:
        webAddress = "http://www.cs.utexas.edu/users/fares/netflix-caches/" + \
            filename
        bytes = get(webAddress).content
        cache = pickle.loads(bytes)

    return cache

AVERAGE_RATING = 3.60428996442
<<<<<<< HEAD
AVERAGE_MOVIE_RATING = create_cache("cache-averageMovieRating.pickle")
ACTUAL_CUSTOMER_RATING = create_cache("cache-actualCustomerRating.pickle")
'''
AVERAGE_MOVIE_RATING_PER_YEAR = create_cache(
    "cache-movieAverageByYear.pickle")
YEAR_OF_RATING = create_cache("cache-yearCustomerRatedMovie.pickle")
CUSTOMER_AVERAGE_RATING_YEARLY = create_cache("cache-customerAverageRatingByYear.pickle")
'''
=======
ACTUAL_CUSTOMER_RATING = create_cache("cache-actualCustomerRating.pickle")
AVERAGE_CUSTOMER_RATING = create_cache("cache-averageCustomerRating.pickle")
AVERAGE_MOVIE_RATING = create_cache("cache-averageMovieRating.pickle")
>>>>>>> dev


# ------------
# netflix_eval
# ------------


def netflix_eval(reader, writer) :
    predictions = []
    actual = []

    # iterate throught the file reader line by line
    for line in reader:
    # need to get rid of the '\n' by the end of the line
        line = line.strip()
        # check if the line ends with a ":", i.e., it's a movie title 
        if line[-1] == ':':
		# It's a movie
            current_movie = line.rstrip(':')
<<<<<<< HEAD
            prediction = AVERAGE_MOVIE_RATING[int(current_movie)]
=======
>>>>>>> dev
            writer.write(line)
            writer.write('\n')
        else:
		# It's a customer
            current_customer = line
                # average movie rating for a particular movie offset by a user's average distance from the overall average rating 
            prediction = AVERAGE_MOVIE_RATING[int(current_movie)] - (AVERAGE_RATING - AVERAGE_CUSTOMER_RATING[int(current_customer)])
            predictions.append(prediction)
<<<<<<< HEAD
            actual_tuple = (int(current_customer),int(current_movie))
            actual.append(ACTUAL_CUSTOMER_RATING[actual_tuple])
=======
            actual.append(ACTUAL_CUSTOMER_RATING[(int(current_customer), int(current_movie))])
>>>>>>> dev
            writer.write(str(prediction)) 
            writer.write('\n')	

    # calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    writer.write(str(rmse)[:4] + '\n')


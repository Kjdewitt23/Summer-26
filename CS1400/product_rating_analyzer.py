from functools import reduce

def generate_recommendation_flags(ratings):
    '''For each rating, returns true if >= 4. Get's "good ratings"'''
    rec = [x >= 4 for x in ratings]
    return rec

def rating_summary(ratings):
    '''Creates a dictionary of the count of ratings based on score'''
    return {rating: ratings.count(rating) for rating in range(1, 6)}

def main():
    ratings = [4, 5, 2, 3, 5, 1, 4, 3, 5, 2, 4]

    descriptions = list(map(
        lambda rating: "Excellent" if rating == 5
                        else "Good" if rating == 4
                        else "Average" if rating == 3
                        else "Poor" if rating == 2
                        else "Terrible",
        ratings
    )) #This part took me the longest. I had to research ternary operators more to get this right.

    positive = list(filter(lambda x: x > 3, ratings))

    total = reduce(lambda x, y: x + y, ratings)
    av = round(total / len(ratings), 2)

    rec_flags = generate_recommendation_flags(ratings)

    rat_sum = rating_summary(ratings)

    print(f"Original Ratings: {ratings}")
    print(f"Descriptions: {descriptions}")
    print(f"Positive Ratings: {positive}")
    print(f"Average Rating: {av}")
    print(f"Recommendation Flags: {rec_flags}")
    print(f"Rating Summary: {rat_sum}")
    
if __name__ == "__main__":
    main()
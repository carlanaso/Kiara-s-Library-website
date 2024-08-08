# Kiara-s-Library-website
It allows the user to submit reviews for books and processes all the reviews by storing them in book-specific files.

### Requesting Data

To request data from the microservice, you will need to create a request text file in the 'requests' directory. Depend on what you want to make either retrieve or create review. It will be slightly different.

# Create a book review

the text file under the 'request' needed to be 'submit_review.txt'
```
Action: SubmitReview
BookTitle : {bookTitle}
Review: {Review}
Stars: {rating 1-5}
```

So, an example will be:

```
Action: SubmitReview
BookTitle : Matilda
Review: It was boring
Stars: 1
```

# Retrieve Book's review

the text file under the 'request' needed to be 'retrieve_reviews.txt' (remember the 's' for the reveiw)
```
Action: SubmitReview
BookTitle : {bookTitle}
```

So, an example will be:

```
Action: SubmitReview
BookTitle : Matilda
```
# Receiving Data

The review microservice will extract the data from the requests and generate the response text file under the 'responses' directory. For the submit review, it will also update that specific book review under 'book_reviews' directory.

# Response for submitting review

It will show whether it is success or fail message. 

Example: For success,
```
Message: Review added successfully to 'Tom and Jerry'.
```

```
Message: Invalid review format.
```

# Response for retrieving the review

For retrieving review, it will be using the Json format.
```
{
  "BookTitle": {booktitle},
  "reviews": [
    {
      "review": {review},
      "stars": {star (1-5)}
    }
  ]
}

```

So, an example will be:

```
{
  "BookTitle": "Matilda",
  "reviews": [
    {
      "review": "awesome book",
      "stars": "5"
    },
    {
      "review": "hate the plot",
      "stars": "1"
    }
  ]
}

```

# The book Review format:

So, here is an example of how it looks under the 'book_reviews' directory. After I submitted the review for Matilda, it will show as Matilda_reviews.txt under the 'book_review' directory.
It will be like this format:
```
Review: awesome book
Stars: 5
```

# Option:(Decide by you)
As you can think of, making the text file each time is annoying. To make it work better way and reduce the time comsuming, you can make a program that make all the requests.

Here is the code:
```
import os
import time

REQUESTS_DIR = "requests"

def create_request_file(file_name, content):
    with open(os.path.join(REQUESTS_DIR, file_name), 'w') as file:
        file.write(content)



create_request_file('submit_review_1.txt', 'Action: SubmitReview\nBookTitle: Matilda\nReview: awesome book\nStars: 5\n')
time.sleep(1)
create_request_file('submit_review_2.txt', 'Action: SubmitReview\nBookTitle: Matilda\nReview: hate the plot\nStars: 1\n')
time.sleep(1)
create_request_file('submit_review_3.txt', 'Action: SubmitReview\nBookTitle: Tom and Jerry\nReview: It was fun to read but still a bit boring\nStars: 3\n')
time.sleep(1)


create_request_file('retrieve_reviews.txt', 'Action: RetrieveReviews\nBookTitle: Matilda\n')


```
Please change the Booktitle to the one that you want. Those time.sleep(1) is to help the program load before doing the retrieve, so please don't delete them.
# The UML diagram
it explained how requesting and receiving data works using text files for the review microservice:


![Blank diagram](https://github.com/user-attachments/assets/fa57d93a-9bd4-496d-9950-a6a0170fc447)

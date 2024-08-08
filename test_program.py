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


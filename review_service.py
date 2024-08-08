import os
import time
import json

# Directories for requests, responses, and reviews
REQUESTS_DIR = "requests"
RESPONSES_DIR = "responses"
REVIEWS_DIR = "book_reviews"

# Ensure necessary directories exist
os.makedirs(REQUESTS_DIR, exist_ok=True)
os.makedirs(RESPONSES_DIR, exist_ok=True)
os.makedirs(REVIEWS_DIR, exist_ok=True)

# Creating the review
# def create_submit_review_request(book_title, review, stars):
#     if stars < 0 or stars > 5:
#         print("Error: Stars should be between 0 and 5.")
#         return
#     request_content = f"Action: SubmitReview\nBookTitle: {book_title}\nReview: {review}\nStars: {stars}\n"
#     request_file = os.path.join(REQUESTS_DIR, "submit_review.txt")
#     with open(request_file, "w") as file:
#         file.write(request_content)
#     print(f"Submit review request created: {request_file}")

# # Retrieve the review
# def create_retrieve_reviews_request(book_title):
#     request_content = f"Action: RetrieveReviews\nBookTitle: {book_title}\n"
#     request_file = os.path.join(REQUESTS_DIR, "retrieve_reviews.txt")
#     with open(request_file, "w") as file:
#         file.write(request_content)
#     print(f"Retrieve reviews request created: {request_file}")

# Process requests
def process_requests():
    while True:
        time.sleep(1)
        for filename in os.listdir(REQUESTS_DIR):
            if filename.endswith(".txt"):
                with open(os.path.join(REQUESTS_DIR, filename), "r") as file:
                    content = file.read().strip()
                if content:
                    lines = content.split('\n')
                    action = lines[0].split(":")[1].strip()
                    if action == "SubmitReview":
                        process_submit_review(lines)
                    elif action == "RetrieveReviews":
                        process_retrieve_reviews(lines)
                os.remove(os.path.join(REQUESTS_DIR, filename))

# Process submit review
def process_submit_review(lines):
    book_title = None
    review = None
    stars = None

    for line in lines:
        if line.startswith("BookTitle:"):
            book_title = line.split(":")[1].strip()
        elif line.startswith("Review:"):
            review = line.split(":")[1].strip()
        elif line.startswith("Stars:"):
            try:
                stars = int(line.split(":")[1].strip())
            except ValueError:
                stars = None

    if book_title and review and stars is not None and 0 <= stars <= 5:
        filename = f"{book_title.replace(' ', '_')}_reviews.txt"
        with open(os.path.join(REVIEWS_DIR, filename), "a") as review_file:
            review_file.write(f"Review: {review}\nStars: {stars}\n")
        response_message = f"Message: Review added successfully to '{book_title}'."
    else:
        response_message = "Message: Invalid review format."

    with open(os.path.join(RESPONSES_DIR, "submit_review_response.txt"), "w") as response_file:
        response_file.write(response_message)


# Process retrieve reviews
def process_retrieve_reviews(lines):
    book_title = None

    for line in lines:
        if line.startswith("BookTitle:"):
            book_title = line.split(":")[1].strip()

    if book_title:
        filename = f"{book_title.replace(' ', '_')}_reviews.txt"
        reviews = []

        if os.path.exists(os.path.join(REVIEWS_DIR, filename)):
            with open(os.path.join(REVIEWS_DIR, filename), "r") as review_file:
                review_lines = review_file.readlines()
                
                # Process review lines
                for i in range(0, len(review_lines), 2):
                    if review_lines[i].startswith("Review:"):
                        review_text = review_lines[i].strip().replace("Review: ", "")
                        stars_text = review_lines[i + 1].strip().replace("Stars: ", "")
                        reviews.append({"review": review_text, "stars": stars_text})

            response_data = {
                "BookTitle": book_title,
                "reviews": reviews
            }
        else:
            response_data = {
                "BookTitle": book_title,
                "reviews": []
            }

        with open(os.path.join(RESPONSES_DIR, "retrieve_reviews_response.txt"), "w") as response_file:
            response_file.write(json.dumps(response_data, indent=2))
    else:
        response_message = "Message: Invalid request format."
        with open(os.path.join(RESPONSES_DIR, "retrieve_reviews_response.txt"), "w") as response_file:
            response_file.write(response_message)


if __name__ == "__main__":
    # Start processing requests
    process_requests()

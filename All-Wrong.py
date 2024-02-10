"""
  There's a multiple-choice test with N questions, numbered from
  1 to N. Each question has 2 answer options, labelled A and B.
  You know that the correct answer for the ith question is the ith character in the string C,
  which is either "A" or "B", but you want to get a score of
  0 on this test by answering every question incorrectly.

  Your task is to implement the function getWrongAnswers(N, C)
  which returns a string with N characters, the ith of which is
  the answer you should give for question i in order to get it wrong (either "A" or "B").
"""
def getWrongAnswers(N, C):
    # Write your code here
    wrong_answers = ''  # create new variable and initialize it to an empty string
    for answer in C:  # iterate over each character in the string `C`
        wrong_answers += 'B' if answer == 'A' else 'A'  # conditional expression
    return wrong_answers


# Example usage:
N = 3  # three questions on the test
C = "ABA"  # correct answers
print(getWrongAnswers(N, C))  # Output should be "BAB"

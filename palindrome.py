def is_palindrome(user_input):
        palindrome = string_cleaner(user_input)
        return palindrome == palindrome[::-1]

def output():
    verdict = ""
    if not is_palindrome(user_input):
        verdict = "not "
    print(user_input, "is {}a palindrome".format(verdict))


def main():
    user_input = input("enter a suspected palindrome")

if __name__ == '__main__':
    main()

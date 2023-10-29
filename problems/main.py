
def callProblem():
    impStr = None

    while not impStr:
        ans = input("Insert the difficulty of the problem (e, m h) >> ").lower()


        if ans == 'e':
            impStr = "easy."

        elif ans == 'm':
            impStr = "medium."

        elif ans == 'h':
            impStr = "hard."

    impStr2 = input("Insert the number of the problem >> ")

    try:
        print(f"Problem {impStr2}:\n")
        __import__(f"{impStr}problem{int(impStr2)}")

    except Exception as err:
        print("Program has encountered an error.\n"
              "Most likely it is due to a non existing problem in this project.")
        print(err)


if __name__ == "__main__":
    callProblem()

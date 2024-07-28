class Solution:
    def maximumTime(self, time: str) -> str:
        timer = []
        for index in range(len(time)):
            char = time[index]
            if char == "?":
                if index == 0:
                    if time[index + 1] == "?":
                        timer.append("2")
                    elif int(time[index + 1]) < 4:
                        timer.append("2")
                    else:
                        timer.append("1")

                elif index == 1:
                    if time[index - 1] == "0":
                        timer.append("9")
                    elif time[index - 1] == "1":
                        timer.append("9")
                    else:
                        timer.append("3")

                elif index == 3:
                    timer.append("5")
                elif index == 4:
                    timer.append("9")
                else:
                    timer.append(char)
            else:
                timer.append(char)

        return "".join(timer)


if __name__ == "__main__":
    time = "2?:?0"
    time = "?4:03"

    print(Solution().maximumTime(time))

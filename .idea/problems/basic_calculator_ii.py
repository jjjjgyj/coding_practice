class BasicCalculatorII:
    def calculate(self, s):
        if not s:
            return 0

        s = "".join(s.split())
        sign_set = set("+-*/")
        curr_sign = "+"
        curr_num = 0
        stack = []

        for i in range(len(s)):
            if s[i] not in sign_set:
                curr_num = curr_num * 10 + int(s[i])
            if s[i] in sign_set or i == len(s) - 1:
                if curr_sign == "+":
                    stack.append(curr_num)
                elif curr_sign == "-":
                    stack.append (-curr_num)
                elif curr_sign == "*":
                    stack.append(stack.pop() * curr_num)
                elif curr_sign == "/":
                    if stack[-1] // curr_num >= 0:
                        stack.append(stack.pop() // curr_num)
                    else:
                        stack.append(-(-stack.pop() // curr_num))
                curr_sign = s[i]
                curr_num = 0
        print(stack)
        return sum(stack)

if __name__ == "__main__":
    basic_calculator = BasicCalculatorII()
    s_1 = "3 * 2 + 5    - 8"
    s_2 = " 3+5 / 2 "
    print(basic_calculator.calculate(s_1))
    print(basic_calculator.calculate(s_2))
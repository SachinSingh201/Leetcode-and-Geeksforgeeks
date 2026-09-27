class Solution(object):
    def reverseParentheses(self, s):
        stack = []

        for ch in s:

            if ch != ")":
                stack.append(ch)

            else:
                st = []

                while stack[-1] != "(":
                    st.append(stack.pop())

               
                stack.pop()

               
                for x in st:
                    stack.append(x)

        return "".join(stack)
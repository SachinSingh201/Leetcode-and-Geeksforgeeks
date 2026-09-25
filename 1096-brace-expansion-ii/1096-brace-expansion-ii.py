class Solution(object):
    def braceExpansionII(self, expression):

        stack = []

        # Current possible strings
        curr = set([""])

        # Alternatives collected inside current {}
        union = set()

        for ch in expression:

            # Start a new brace expression
            if ch == '{':
                stack.append((curr, union))

                curr = set([""])
                union = set()

            # Finish one alternative
            elif ch == ',':
                union |= curr
                curr = set([""])

            # Close brace
            elif ch == '}':

                # Add last alternative
                union |= curr

                # Get previous context
                prev_curr, prev_union = stack.pop()

                # Concatenate previous expression with
                # everything generated inside braces
                new_curr = set()

                for a in prev_curr:
                    for b in union:
                        new_curr.add(a + b)

                curr = new_curr
                union = prev_union

            # Normal character
            else:

                new_curr = set()

                for s in curr:
                    new_curr.add(s + ch)

                curr = new_curr

        # Anything outside braces
        union |= curr

        return sorted(union)
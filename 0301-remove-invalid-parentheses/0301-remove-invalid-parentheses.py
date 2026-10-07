class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def valid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1

                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = set([s])
        result = []

        while queue:

            next_level = []

            for curr in queue:

                if valid(curr):
                    result.append(curr)

            # If we found valid strings at this level,
            # they require minimum removals.
            if result:
                return result

            for curr in queue:

                for i in range(len(curr)):

                    # Only remove parentheses
                    if curr[i] != '(' and curr[i] != ')':
                        continue

                    new_string = curr[:i] + curr[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.append(new_string)

            queue = next_level

        return []
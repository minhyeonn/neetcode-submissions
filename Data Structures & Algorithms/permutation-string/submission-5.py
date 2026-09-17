class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26
        window_size = len(s1)

        # 1. Setup the initial window
        for i in range(window_size):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # Check if the very first window matches
        if s1_count == window_count:
            return True

        # 2. Slide the window one character at a time
        for i in range(window_size, len(s2)):
            # Add the new character entering on the right
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # Remove the old character falling off the left
            window_count[ord(s2[i - window_size]) - ord('a')] -= 1

            # Direct array comparison!
            if s1_count == window_count:
                return True

        return False

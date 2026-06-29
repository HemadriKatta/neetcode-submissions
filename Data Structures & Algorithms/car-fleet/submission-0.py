class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(pos, speed) for pos, speed in zip(position, speed)]
        combined.sort(reverse = True)
        stack = [] 

        for pos,speed in combined:
            fleet = (target - pos) / speed
            stack.append(fleet)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)        
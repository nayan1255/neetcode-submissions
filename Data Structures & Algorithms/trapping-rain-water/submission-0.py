class Solution:
    def trap(self, height: List[int]) -> int:
        # Return 0 immediately if the elevation map is empty
        if not height:
            return 0
        
        # Initialize two pointers at the absolute left and right boundaries
        left, right = 0, len(height) - 1
        
        # Keep track of the maximum bar height seen so far from both ends
        left_max, right_max = height[left], height[right]
        
        # Accumulator variable for total trapped water
        water = 0
        
        # Process the array until the two pointers meet
        while left < right:
            # The side with the smaller max height determines the water limit (bottleneck)
            if left_max < right_max:
                left += 1  # Move the left pointer inward
                left_max = max(left_max, height[left])  # Update the left maximum height
                water += left_max - height[left]  # Add trapped water at the current index
            else:
                right -= 1  # Move the right pointer inward
                right_max = max(right_max, height[right])  # Update the right maximum height
                water += right_max - height[right]  # Add trapped water at the current index
                
        return water

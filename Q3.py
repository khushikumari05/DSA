def trap(height):
    if not height or len(height) <3:
        return 0
    
    left,right = 0, len(height) -1
    left_max, right_max = height[left],height[right]
    water_trapped = 0

    while left < right :
        if left_max < right_max: 
            left += 1
            left_max = max(left_max,height[left])
            water_trapped += max(0, left_max-height[left])
        else:
            right -= 1
            right_max = max(right_max,height[right])
            water_trapped += max(0, right_max-height[right])

        return water_trapped

        height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
            print ("Output for height1:", trap(height1)) 

        height2 = [4,2,0,3,2,5]
            print ("Output for height3:", trap(height1)) 
   
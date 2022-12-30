def IoU_calculator(box1, box2, area1=None, area2=None):
    '''
    Inputs two boxes (each with top-left-x, top-left-y, btm-right-x, btm-right-y coordinates).
    If the area of one or two of the boxes are known, it can be passed here as well.
    Calculates the IoU between the two boxes and returns the IoU.
    '''
    
    #Get the area of the boxes
    if area1 is None:
        #Area of the box1. +1 since index starts from 0.
        area1 = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    
    if area2 is None:
        #Area of the box 2. +1 since index starts from 0.
        area2 = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)
    
    #Determine the intersection rectangle.
    int_rect_top_left_x = max(box1[0], box2[0])
    int_rect_top_left_y = max(box1[1], box2[1])
    int_rect_btm_rght_x = min(box1[2], box2[2])
    int_rect_btm_rght_y = min(box1[3], box2[3])
    
    #if the boxes do not intersect, the difference will be < 0. Hence we pick 0 in those cases.
    int_rect_area = max(0, int_rect_btm_rght_x - int_rect_top_left_x + 1)*max(0, int_rect_btm_rght_y - int_rect_top_left_y)
    
    #Calculate the IoU.
    try:
        intersect_over_union = float(int_rect_area / (area1 + area2 - int_rect_area))
    except ZeroDivisionError:
        
        intersect_over_union = 'zero division error'
        
    
    return intersect_over_union
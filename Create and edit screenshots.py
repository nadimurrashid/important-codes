def create_and_edit_screenshot(data_set):
    sModuleInfo = x
y
    from PIL import ImageGrab,Image
    import pyautogui
    import pygetwindow
    import numpy as np
    import cv2

    take_screenshot = ''
    main_image_location = ''
    template_image = []
    template_image_location = ''
    edited_image_location = ''
    previous_coordinate = ''
    current_coordinate = []
    variable_name = None
    full_screenshot = ''
    window_screenshot = ''
    window_name =''
    edited_image_file_name =''
    screenshot_save_location =''
    screenshot_name =''
    threshold_n = 0.9

    adjust_left_border = 0
    adjust_top_border = 0
    adjust_width_border = 0
    adjust_height_border = 0


    for left,mid,right in data_set:

        if left == 'full_screenshot':
            full_screenshot = right.strip()
        elif left == 'widnow_screenshot':
            window_screenshot = right.strip()
        elif left == 'adjust_top_border':
            adjust_top_border = int(right.strip())
        elif left == 'adjust_left_border':
            adjust_left_border = int(right.strip())
        elif left == 'adjust_width_border':
            adjust_width_border = int(right.strip())
        elif left == 'adjust_height_border':
            adjust_height_border = int(right.strip())
        elif left == 'main_image_location':
            main_image_location = right.strip()
        elif left == 'template_image_location':
            template_image.append(right.strip())
        elif left == 'previous_coordinate':
            previous_coordinate = CommonUtil.parse_value_into_object(right.strip())
        elif left == 'screenshot_save_location':
            screenshot_save_location = right.strip()
        elif left == 'screenshot_name':
            screenshot_name = right.strip()
        elif left == 'window_name':
            window_name = right.strip()
        elif left == 'edited_image_location':
            edited_image_location = right.strip()
        elif left == 'edited_image_file_name':
            edited_image_file_name = right.strip()
        elif "action" in mid:
            variable_name = right.strip()
        elif left == 'threshold':
            threshold_n = float(right.strip())
    try:
        output_path = screenshot_save_location + "\\" + screenshot_name + ".png"
        # window_specific_screenshot = window_specific_screenshot

        if full_screenshot == 'yes':
            snapshot = ImageGrab.grab()
            snapshot.save(output_path)
        elif window_screenshot == 'yes':

            window_name = pygetwindow.getWindowsWithTitle(window_name)[0]
            left = window_name.left + adjust_left_border
            top = window_name.top + adjust_top_border
            width = window_name.width + adjust_width_border
            height = window_name.height + adjust_height_border
            # left = int(window_name.left)
            # top = int(window_name.top)
            # width = int(window_name.width)
            # height = int(window_name.height)

            im = ImageGrab.grab(bbox=(left, top, width, height))  # X1,Y1,X2,Y2
            im.save(output_path)


        if main_image_location == '':
            main_image_location = output_path
        else:
            pass
        if template_image != []:
            if len(template_image) > 1:
                count = 'yes'
            else:
                count = 'no'
        if template_image != [] or previous_coordinate != '':

            edited_image_location = edited_image_location + "\\" + edited_image_file_name +".png"

            if template_image == [] and isinstance(previous_coordinate,list) == True:


                if len(previous_coordinate) > 1:
                    for i in previous_coordinate:
                        image1 = Image.open(main_image_location).convert('RGB')
                        img_arr = np.array(image1)
                        img_arr[i[1]: i[1] + i[2], i[0]: i[0] + i[3]] = (0, 0, 0)
                        image1 = Image.fromarray(img_arr)
                        image1.save(edited_image_location)
                        main_image_location = edited_image_location
                    CommonUtil.ExecLog(sModuleInfo, "passed", 1)
                    return "passed"

                else:
                    image1 = Image.open(main_image_location).convert('RGB')
                    img_arr = np.array(image1)
                    img_arr[previous_coordinate[0][1]: previous_coordinate[0][1] + previous_coordinate[0][2], previous_coordinate[0][0]: previous_coordinate[0][0] + previous_coordinate[0][3]] = (0, 0, 0)
                    image1 = Image.fromarray(img_arr)
                    image1.save(edited_image_location)
                    CommonUtil.ExecLog(sModuleInfo, "passed", 1)
                    return "passed"

            else:

                for template in template_image:

                    image = cv2.imread(main_image_location)
                    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    template_n = cv2.imread(template, 0)
                    # cv2.imshow('template',template)

                    w, h = template_n.shape[::-1]

                    res = cv2.matchTemplate(grey_img, template_n, cv2.TM_CCOEFF_NORMED)

                    threshold = threshold_n
                    loc = np.where(res >= threshold)

                    image1 = Image.open(main_image_location).convert('RGB')

                    for pt in zip(*loc[::-1]):
                        img_arr = np.array(image1)
                        if previous_coordinate == '':
                            img_arr[pt[1]: pt[1] + h, pt[0]:pt[0] + w] = (0, 0, 0)
                            x_location = pt[0]
                            y_location = pt[1]
                            height_n = h
                            width_n = w
                            # for coord in x_location,y_location,height_n,width_n:
                            #     current_coordinate.append(coord(range(0,4)))
                            current_coordinate.append([x_location,y_location,height_n,width_n])
                            image1 = Image.fromarray(img_arr)
                            image1.save(edited_image_location)

                        elif template_image != [] and isinstance(previous_coordinate,list) == True:
                            img_arr[pt[1]: pt[1] + h, pt[0]:pt[0] + w] = (0, 0, 0)
                            x_location = pt[0]
                            y_location = pt[1]
                            height_n = h
                            width_n = w
                            # for coord in x_location, y_location, height_n, width_n:
                            #     current_coordinate.append(coord(range(0,4)))
                            current_coordinate.append([x_location,y_location,height_n,width_n])

                            image1 = Image.fromarray(img_arr)
                            image1.save(edited_image_location)
                            main_image_location = edited_image_location

                            image1 = Image.open(main_image_location).convert('RGB')
                            img_arr = np.array(image1)

                            if len(previous_coordinate) > 1:
                                for i in previous_coordinate:
                                    image1 = Image.open(main_image_location).convert('RGB')
                                    img_arr = np.array(image1)
                                    img_arr[i[1]: i[1] + i[2], i[0]: i[0] + i[3]] = (0, 0, 0)
                                    image1 = Image.fromarray(img_arr)
                                    image1.save(edited_image_location)
                                    main_image_location = edited_image_location

                            else:
                                image1 = Image.open(main_image_location).convert('RGB')
                                img_arr = np.array(image1)
                                img_arr[previous_coordinate[0][1]: previous_coordinate[0][1] + previous_coordinate[0][2],
                                previous_coordinate[0][0]: previous_coordinate[0][0] + previous_coordinate[0][3]] = (0, 0, 0)
                                image1 = Image.fromarray(img_arr)
                                image1.save(edited_image_location)




                        if count == 'yes':
                            main_image_location = edited_image_location
                            sr.Set_Shared_Variables(variable_name, current_coordinate)
                        elif count == 'no':
                            sr.Set_Shared_Variables(variable_name, current_coordinate)
            CommonUtil.ExecLog(sModuleInfo, "passed", 1)
            return "passed"
        else:
            CommonUtil.ExecLog(sModuleInfo, "passed", 1)
            return "passed"
    except:
        CommonUtil.ExecLog(sModuleInfo, "Couldn't take screenshot or edit the image", 3)
        return "zeuz_failed"

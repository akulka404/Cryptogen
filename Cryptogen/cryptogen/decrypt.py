import numpy as np
def load_frame(image_path: str):
    import cv2
    import numpy as np
    frame=cv2.imread(image_path)
    print("Frame Loaded. You now have access to all Decryption algorithms")
    return frame

def batman(frame: np.array, save: str):
    import cv2
    import numpy as np
    shape_frame = frame.shape  # [y,x,c]
    width = int(shape_frame[1])
    height = int(shape_frame[0])
    a = width % 10
    w = width - a
    b = height % 10
    h = height - b
    frame=cv2.resize(frame,(w,h),interpolation=cv2.INTER_LINEAR)
    [B, G, R] = cv2.split(frame)
    a = [0]
    c = [0]
    for i in range(1, 11):
        b = a[0] + i * (w / 10)
        d = c[0] + i * (h / 10)
        a.append(int(b)) 
        c.append(int(d))

    ROI_0_0 = frame[c[0]:c[1], a[0]:a[1]]
    ROI_1_0 = frame[c[1]:c[2], a[0]:a[1]]
    ROI_2_0 = frame[c[2]:c[3], a[0]:a[1]]
    ROI_3_0 = frame[c[3]:c[4], a[0]:a[1]]
    ROI_4_0 = frame[c[4]:c[5], a[0]:a[1]]
    ROI_5_0 = frame[c[5]:c[6], a[0]:a[1]]
    ROI_6_0 = frame[c[6]:c[7], a[0]:a[1]]
    ROI_7_0 = frame[c[7]:c[8], a[0]:a[1]]
    ROI_8_0 = frame[c[8]:c[9], a[0]:a[1]]
    ROI_9_0 = frame[c[9]:c[10], a[0]:a[1]]

    ROI_0_1 = frame[c[0]:c[1], a[1]:a[2]]
    ROI_1_1 = frame[c[1]:c[2], a[1]:a[2]]
    ROI_2_1 = frame[c[2]:c[3], a[1]:a[2]]
    ROI_3_1 = frame[c[3]:c[4], a[1]:a[2]]
    ROI_4_1 = frame[c[4]:c[5], a[1]:a[2]]
    ROI_5_1 = frame[c[5]:c[6], a[1]:a[2]]
    ROI_6_1 = frame[c[6]:c[7], a[1]:a[2]]
    ROI_7_1 = frame[c[7]:c[8], a[1]:a[2]]
    ROI_8_1 = frame[c[8]:c[9], a[1]:a[2]]
    ROI_9_1 = frame[c[9]:c[10], a[1]:a[2]]

    ROI_0_2 = frame[c[0]:c[1], a[2]:a[3]]
    ROI_1_2 = frame[c[1]:c[2], a[2]:a[3]]
    ROI_2_2 = frame[c[2]:c[3], a[2]:a[3]]
    ROI_3_2 = frame[c[3]:c[4], a[2]:a[3]]
    ROI_4_2 = frame[c[4]:c[5], a[2]:a[3]]
    ROI_5_2 = frame[c[5]:c[6], a[2]:a[3]]
    ROI_6_2 = frame[c[6]:c[7], a[2]:a[3]]
    ROI_7_2 = frame[c[7]:c[8], a[2]:a[3]]
    ROI_8_2 = frame[c[8]:c[9], a[2]:a[3]]
    ROI_9_2 = frame[c[9]:c[10], a[2]:a[3]]

    ROI_0_3 = frame[c[0]:c[1], a[3]:a[4]]
    ROI_1_3 = frame[c[1]:c[2], a[3]:a[4]]
    ROI_2_3 = frame[c[2]:c[3], a[3]:a[4]]
    ROI_3_3 = frame[c[3]:c[4], a[3]:a[4]]
    ROI_4_3 = frame[c[4]:c[5], a[3]:a[4]]
    ROI_5_3 = frame[c[5]:c[6], a[3]:a[4]]
    ROI_6_3 = frame[c[6]:c[7], a[3]:a[4]]
    ROI_7_3 = frame[c[7]:c[8], a[3]:a[4]]
    ROI_8_3 = frame[c[8]:c[9], a[3]:a[4]]
    ROI_9_3 = frame[c[9]:c[10], a[3]:a[4]]

    ROI_0_4 = frame[c[0]:c[1], a[4]:a[5]]
    ROI_1_4 = frame[c[1]:c[2], a[4]:a[5]]
    ROI_2_4 = frame[c[2]:c[3], a[4]:a[5]]
    ROI_3_4 = frame[c[3]:c[4], a[4]:a[5]]
    ROI_4_4 = frame[c[4]:c[5], a[4]:a[5]]
    ROI_5_4 = frame[c[5]:c[6], a[4]:a[5]]
    ROI_6_4 = frame[c[6]:c[7], a[4]:a[5]]
    ROI_7_4 = frame[c[7]:c[8], a[4]:a[5]]
    ROI_8_4 = frame[c[8]:c[9], a[4]:a[5]]
    ROI_9_4 = frame[c[9]:c[10], a[4]:a[5]]

    ROI_0_5 = frame[c[0]:c[1], a[5]:a[6]]
    ROI_1_5 = frame[c[1]:c[2], a[5]:a[6]]
    ROI_2_5 = frame[c[2]:c[3], a[5]:a[6]]
    ROI_3_5 = frame[c[3]:c[4], a[5]:a[6]]
    ROI_4_5 = frame[c[4]:c[5], a[5]:a[6]]
    ROI_5_5 = frame[c[5]:c[6], a[5]:a[6]]
    ROI_6_5 = frame[c[6]:c[7], a[5]:a[6]]
    ROI_7_5 = frame[c[7]:c[8], a[5]:a[6]]
    ROI_8_5 = frame[c[8]:c[9], a[5]:a[6]]
    ROI_9_5 = frame[c[9]:c[10], a[5]:a[6]]

    ROI_0_6 = frame[c[0]:c[1], a[6]:a[7]]
    ROI_1_6 = frame[c[1]:c[2], a[6]:a[7]]
    ROI_2_6 = frame[c[2]:c[3], a[6]:a[7]]
    ROI_3_6 = frame[c[3]:c[4], a[6]:a[7]]
    ROI_4_6 = frame[c[4]:c[5], a[6]:a[7]]
    ROI_5_6 = frame[c[5]:c[6], a[6]:a[7]]
    ROI_6_6 = frame[c[6]:c[7], a[6]:a[7]]
    ROI_7_6 = frame[c[7]:c[8], a[6]:a[7]]
    ROI_8_6 = frame[c[8]:c[9], a[6]:a[7]]
    ROI_9_6 = frame[c[9]:c[10], a[6]:a[7]]

    ROI_0_7 = frame[c[0]:c[1], a[7]:a[8]]
    ROI_1_7 = frame[c[1]:c[2], a[7]:a[8]]
    ROI_2_7 = frame[c[2]:c[3], a[7]:a[8]]
    ROI_3_7 = frame[c[3]:c[4], a[7]:a[8]]
    ROI_4_7 = frame[c[4]:c[5], a[7]:a[8]]
    ROI_5_7 = frame[c[5]:c[6], a[7]:a[8]]
    ROI_6_7 = frame[c[6]:c[7], a[7]:a[8]]
    ROI_7_7 = frame[c[7]:c[8], a[7]:a[8]]
    ROI_8_7 = frame[c[8]:c[9], a[7]:a[8]]
    ROI_9_7 = frame[c[9]:c[10], a[7]:a[8]]

    ROI_0_8 = frame[c[0]:c[1], a[8]:a[9]]
    ROI_1_8 = frame[c[1]:c[2], a[8]:a[9]]
    ROI_2_8 = frame[c[2]:c[3], a[8]:a[9]]
    ROI_3_8 = frame[c[3]:c[4], a[8]:a[9]]
    ROI_4_8 = frame[c[4]:c[5], a[8]:a[9]]
    ROI_5_8 = frame[c[5]:c[6], a[8]:a[9]]
    ROI_6_8 = frame[c[6]:c[7], a[8]:a[9]]
    ROI_7_8 = frame[c[7]:c[8], a[8]:a[9]]
    ROI_8_8 = frame[c[8]:c[9], a[8]:a[9]]
    ROI_9_8 = frame[c[9]:c[10], a[8]:a[9]]

    ROI_0_9 = frame[c[0]:c[1], a[9]:a[10]]
    ROI_1_9 = frame[c[1]:c[2], a[9]:a[10]]
    ROI_2_9 = frame[c[2]:c[3], a[9]:a[10]]
    ROI_3_9 = frame[c[3]:c[4], a[9]:a[10]]
    ROI_4_9 = frame[c[4]:c[5], a[9]:a[10]]
    ROI_5_9 = frame[c[5]:c[6], a[9]:a[10]]
    ROI_6_9 = frame[c[6]:c[7], a[9]:a[10]]
    ROI_7_9 = frame[c[7]:c[8], a[9]:a[10]]
    ROI_8_9 = frame[c[8]:c[9], a[9]:a[10]]
    ROI_9_9 = frame[c[9]:c[10], a[9]:a[10]]



    frame_black=np.zeros((h,w,3),dtype=np.uint8)
    #COLUMN 0
    frame_black[c[0]:c[1], a[0]:a[1]]=ROI_5_5 #00
    frame_black[c[1]:c[2], a[0]:a[1]]=ROI_8_9 #10
    frame_black[c[2]:c[3], a[0]:a[1]]=ROI_2_1 #20
    frame_black[c[3]:c[4], a[0]:a[1]]=ROI_3_1 #30
    frame_black[c[4]:c[5], a[0]:a[1]]=ROI_8_2 #40
    frame_black[c[5]:c[6], a[0]:a[1]]=ROI_3_4 #50
    frame_black[c[6]:c[7], a[0]:a[1]]=ROI_6_1 #60
    frame_black[c[7]:c[8], a[0]:a[1]]=ROI_7_1 #70
    frame_black[c[8]:c[9], a[0]:a[1]]=ROI_1_9 #80
    frame_black[c[9]:c[10], a[0]:a[1]]=ROI_0_9 #90
    #COLUMN 1
    frame_black[c[0]:c[1], a[1]:a[2]]=ROI_9_8 #01
    frame_black[c[1]:c[2], a[1]:a[2]]=ROI_9_9 #11
    frame_black[c[2]:c[3], a[1]:a[2]]=ROI_0_4 #21
    frame_black[c[3]:c[4], a[1]:a[2]]=ROI_1_4 #31
    frame_black[c[4]:c[5], a[1]:a[2]]=ROI_4_1 #41
    frame_black[c[5]:c[6], a[1]:a[2]]=ROI_1_3 #51
    frame_black[c[6]:c[7], a[1]:a[2]]=ROI_2_0 #61
    frame_black[c[7]:c[8], a[1]:a[2]]=ROI_3_0 #71
    frame_black[c[8]:c[9], a[1]:a[2]]=ROI_2_7 #81
    frame_black[c[9]:c[10], a[1]:a[2]]=ROI_0_8 #91
    #COLUMN 2
    frame_black[c[0]:c[1], a[2]:a[3]]=ROI_4_0 #02
    frame_black[c[1]:c[2], a[2]:a[3]]=ROI_9_6 #12
    frame_black[c[2]:c[3], a[2]:a[3]]=ROI_6_6 #22
    frame_black[c[3]:c[4], a[2]:a[3]]=ROI_3_2 #32
    frame_black[c[4]:c[5], a[2]:a[3]]=ROI_4_7 #42
    frame_black[c[5]:c[6], a[2]:a[3]]=ROI_5_2#52
    frame_black[c[6]:c[7], a[2]:a[3]]=ROI_6_7#62
    frame_black[c[7]:c[8], a[2]:a[3]]=ROI_7_2#72
    frame_black[c[8]:c[9], a[2]:a[3]]=ROI_6_4#82
    frame_black[c[9]:c[10], a[2]:a[3]]=ROI_1_6#92
    #COLUMN 3
    frame_black[c[0]:c[1], a[3]:a[4]]=ROI_0_3#03
    frame_black[c[1]:c[2], a[3]:a[4]]=ROI_3_5#13
    frame_black[c[2]:c[3], a[3]:a[4]]=ROI_7_6#23
    frame_black[c[3]:c[4], a[3]:a[4]]=ROI_8_8#33
    frame_black[c[4]:c[5], a[3]:a[4]]=ROI_5_6#43
    frame_black[c[5]:c[6], a[3]:a[4]]=ROI_4_6#53
    frame_black[c[6]:c[7], a[3]:a[4]]=ROI_3_6#63
    frame_black[c[7]:c[8], a[3]:a[4]]=ROI_2_6#73
    frame_black[c[8]:c[9], a[3]:a[4]]=ROI_8_3#83
    frame_black[c[9]:c[10], a[3]:a[4]]=ROI_5_1#93
    #COLUMN 4
    frame_black[c[0]:c[1], a[4]:a[5]]=ROI_0_5#04
    frame_black[c[1]:c[2], a[4]:a[5]]=ROI_1_5#14
    frame_black[c[2]:c[3], a[4]:a[5]]=ROI_0_2#24
    frame_black[c[3]:c[4], a[4]:a[5]]=ROI_5_8#34
    frame_black[c[4]:c[5], a[4]:a[5]]=ROI_7_7#44
    frame_black[c[5]:c[6], a[4]:a[5]]=ROI_1_8#54
    frame_black[c[6]:c[7], a[4]:a[5]]=ROI_8_6#64
    frame_black[c[7]:c[8], a[4]:a[5]]=ROI_5_0#74
    frame_black[c[8]:c[9], a[4]:a[5]]=ROI_6_0#84
    frame_black[c[9]:c[10], a[4]:a[5]]=ROI_7_0#94
    #COLUMN 5
    frame_black[c[0]:c[1], a[5]:a[6]]=ROI_2_8#05
    frame_black[c[1]:c[2], a[5]:a[6]]=ROI_3_8#15
    frame_black[c[2]:c[3], a[5]:a[6]]=ROI_2_5#25
    frame_black[c[3]:c[4], a[5]:a[6]]=ROI_1_7#35
    frame_black[c[4]:c[5], a[5]:a[6]]=ROI_4_5#45
    frame_black[c[5]:c[6], a[5]:a[6]]=ROI_0_0#55
    frame_black[c[6]:c[7], a[5]:a[6]]=ROI_6_5#65
    frame_black[c[7]:c[8], a[5]:a[6]]=ROI_9_3#75
    frame_black[c[8]:c[9], a[5]:a[6]]=ROI_8_4#85
    frame_black[c[9]:c[10], a[5]:a[6]]=ROI_9_4#95
    #COLUMN 6
    frame_black[c[0]:c[1], a[6]:a[7]]=ROI_2_4#06
    frame_black[c[1]:c[2], a[6]:a[7]]=ROI_9_2#16
    frame_black[c[2]:c[3], a[6]:a[7]]=ROI_7_3#26
    frame_black[c[3]:c[4], a[6]:a[7]]=ROI_6_3#36
    frame_black[c[4]:c[5], a[6]:a[7]]=ROI_5_3#46
    frame_black[c[5]:c[6], a[6]:a[7]]=ROI_4_3#56
    frame_black[c[6]:c[7], a[6]:a[7]]=ROI_2_2#66
    frame_black[c[7]:c[8], a[6]:a[7]]=ROI_2_3#76
    frame_black[c[8]:c[9], a[6]:a[7]]=ROI_4_8#86
    frame_black[c[9]:c[10], a[6]:a[7]]=ROI_1_2#96
    #COLUMN 7
    frame_black[c[0]:c[1], a[7]:a[8]]=ROI_0_7#07
    frame_black[c[1]:c[2], a[7]:a[8]]=ROI_5_9#17
    frame_black[c[2]:c[3], a[7]:a[8]]=ROI_8_1#27
    frame_black[c[3]:c[4], a[7]:a[8]]=ROI_3_7#37
    frame_black[c[4]:c[5], a[7]:a[8]]=ROI_4_2#47
    frame_black[c[5]:c[6], a[7]:a[8]]=ROI_5_7#57
    frame_black[c[6]:c[7], a[7]:a[8]]=ROI_6_2#67
    frame_black[c[7]:c[8], a[7]:a[8]]=ROI_4_4#77
    frame_black[c[8]:c[9], a[7]:a[8]]=ROI_8_7#87
    frame_black[c[9]:c[10], a[7]:a[8]]=ROI_7_5#97
    #COLUMN 8
    frame_black[c[0]:c[1], a[8]:a[9]]=ROI_9_1#08
    frame_black[c[1]:c[2], a[8]:a[9]]=ROI_5_4#18
    frame_black[c[2]:c[3], a[8]:a[9]]=ROI_2_9#28
    frame_black[c[3]:c[4], a[8]:a[9]]=ROI_3_9#38
    frame_black[c[4]:c[5], a[8]:a[9]]=ROI_0_6#48
    frame_black[c[5]:c[6], a[8]:a[9]]=ROI_7_4#58
    frame_black[c[6]:c[7], a[8]:a[9]]=ROI_8_5#68
    frame_black[c[7]:c[8], a[8]:a[9]]=ROI_9_5#78
    frame_black[c[8]:c[9], a[8]:a[9]]=ROI_3_3#88
    frame_black[c[9]:c[10], a[8]:a[9]]=ROI_0_1#98
    #COLUMN 9
    frame_black[c[0]:c[1], a[9]:a[10]]=ROI_9_0#09
    frame_black[c[1]:c[2], a[9]:a[10]]=ROI_8_0#19
    frame_black[c[2]:c[3], a[9]:a[10]]=ROI_6_9#29
    frame_black[c[3]:c[4], a[9]:a[10]]=ROI_7_9#39
    frame_black[c[4]:c[5], a[9]:a[10]]=ROI_4_9#49
    frame_black[c[5]:c[6], a[9]:a[10]]=ROI_9_7#59
    frame_black[c[6]:c[7], a[9]:a[10]]=ROI_6_8#69
    frame_black[c[7]:c[8], a[9]:a[10]]=ROI_7_8#79
    frame_black[c[8]:c[9], a[9]:a[10]]=ROI_1_0#89
    frame_black[c[9]:c[10], a[9]:a[10]]=ROI_1_1#99
    if save=='T' or save=='True':
        cv2.imwrite('Decrypted_Gotham.png',frame_black)
        print("Decryption done!")
    return frame_black

def superman(frame: np.array, save: str):
    import cv2
    shape_frame = frame.shape  # [y,x,c]
    width = int(shape_frame[1])
    height = int(shape_frame[0])
    w = width
    h = height
    [B, G, R] = cv2.split(frame)
    for j in range(0,h):
        for i in range(0,w):
            if i%2==0:
                B[j][i]=B[j][i]-(j*i)
                G[j][i]=G[j][i]+(j*(i*3))
                R[j][i]=R[j][i]-(j*(i*5))
            else:
                B[j][i]=B[j][i]+(j*(i**2))
                G[j][i]=G[j][i]-(j*(i**4))
                R[j][i]=R[j][i]+(j*(i**(1/6)))
    frame=cv2.merge((B,G,R))
    if save=='T' or save=='True':
        cv2.imwrite("Decrypted_Krypton.png",frame)
        print("Decryption done!")
    return frame

def aquaman(frame: np.array, save: str):
    import cv2  
    import numpy as np 
    shape_frame = frame.shape  
    w = int(shape_frame[1])
    h = int(shape_frame[0])
    [B, G, R] = cv2.split(frame)
    G=cv2.flip(G,0)
    R=cv2.flip(R,1)
    for j in range(0,h):
        for i in range(0,w):
            B[j][i]=B[j][i]+(j+i)
            G[j][i]=G[j][i]-((j**2)+(2*j*i)+(i**2))
            R[j][i]=R[j][i]+((i*3)+(3*((i**2)*j))+(3*(i*(j**2)))+(j**3))
    frame=cv2.merge((B,G,R))
    if save=='T' or save=='True':
        cv2.imwrite("Decrypted_Atlantis.png",frame)
        print("Decryption done!")
    return frame

def green_lantern(frame: np.array, save:str):
    import cv2  
    import numpy as np 
    shape_frame = frame.shape  # [y,x,c]
    w = int(shape_frame[1])
    h = int(shape_frame[0])
    [B, G, R] = cv2.split(frame)
    for j in range(0,h):
        for i in range(0,w):
            if j!=h/2 or i!=w/2:
                B[j][i]=B[j][i]+((w-1-j)*i)-max(j**2,i)
                G[j][i]=G[j][i]+(j*(h-1-i))-max(j,i**2)
                R[j][i]=R[j][i]+((w-1-j)*(h-1-i))-(max(j**2,i**2))  
    frame= cv2.merge([B,G,R])
    if save=='T' or save=='True':
        cv2.imwrite("Decrypted_Oa.png",frame)
        print("Decryption done!")
    return frame

def green_arrow(frame: np.array, save: str):
    import cv2
    shape_frame = frame.shape  
    w = int(shape_frame[1])
    h = int(shape_frame[0])
    a = w % 10
    w = w - a
    b = h % 10
    h = h - b
    frame=cv2.resize(frame,(w,h),interpolation=cv2.INTER_LINEAR)
    [B, G, R] = cv2.split(frame)
    B=cv2.flip(B,flipCode=1)
    G=cv2.flip(G,flipCode=-1)
    R=cv2.flip(R,flipCode=0)
    for j in range(0,h):
        for i in range(0,w,10):
            if j%2==0:
                B[j][i+9]=((3*B[j][i+9])+B[j][i])
                B[j][i+8]=((3*B[j][i+8])+B[j][i+1])
                B[j][i+7]=((3*B[j][i+7])+B[j][i+2])
                B[j][i+6]=((3*B[j][i+6])+B[j][i+3])
                B[j][i+5]=((3*B[j][i+5])+B[j][i+4])
                G[j][i+9]=((3*G[j][i+9])+G[j][i])
                G[j][i+8]=((3*G[j][i+8])+G[j][i+1])
                G[j][i+7]=((3*G[j][i+7])+G[j][i+2])
                G[j][i+6]=((3*G[j][i+6])+G[j][i+3])
                G[j][i+5]=((3*G[j][i+5])+G[j][i+4])
                R[j][i+9]=((3*R[j][i+9])+R[j][i])
                R[j][i+8]=((3*R[j][i+8])+R[j][i+1])
                R[j][i+7]=((3*R[j][i+7])+R[j][i+2])
                R[j][i+6]=((3*R[j][i+6])+R[j][i+3])
                R[j][i+5]=((3*R[j][i+5])+R[j][i+4])
            else:
                B[j][i]=((3*B[j][i])-B[j][i+9])
                B[j][i+1]=((3*B[j][i+1])-B[j][i+8])
                B[j][i+2]=((3*B[j][i+2])-B[j][i+7])
                B[j][i+3]=((3*B[j][i+3])-B[j][i+6])
                B[j][i+4]=((3*B[j][i+4])-B[j][i+5])
                G[j][i]=((3*G[j][i])-G[j][i+9])
                G[j][i+1]=((3*G[j][i+1])-G[j][i+8])
                G[j][i+2]=((3*G[j][i+2])-G[j][i+7])
                G[j][i+3]=((3*G[j][i+3])-G[j][i+6])
                G[j][i+4]=((3*G[j][i+4])-G[j][i+5])
                R[j][i]=((3*R[j][i])-R[j][i+9])
                R[j][i+1]=((3*R[j][i+1])-R[j][i+8])
                R[j][i+2]=((3*R[j][i+2])-R[j][i+7])
                R[j][i+3]=((3*R[j][i+3])-R[j][i+6])
                R[j][i+4]=((3*R[j][i+4])-R[j][i+5])
    frame=cv2.merge([B,G,R])
    if save=='T' or save=='True':
        cv2.imwrite("Decrypted_Starling.png",frame)
        print("Decryption done!")
    return frame
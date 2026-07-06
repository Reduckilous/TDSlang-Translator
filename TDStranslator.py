from copy import deepcopy as dc
import struct
import os
import numpy as np


# ============ Enter text here =============







def Full_Translate (


        # Enter text here:
        insert_text = '''The Quick Brown Fox Jumps Over The Lazy Dog
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        1000000 Smacky vs 5 Fie, who will win?''',




        filename         = "TDS_TranslatedText_2",

        border_style     = "Tiles",  # accept value "None" or "Tiles".      The "Lines" border style is WIP and will break


        text_color       = "#ffffff",
        border_color     = "#888888",
        background_color = "#000000"



):
    bmp_convert(d_transpose(Paragraph_Translate(insert_text, border_style)), filename, text_color, border_color, background_color)


# To translate multiple text into different images without reruning this script, just call the function at the end of the script multiple times.









# ==== The alphabet ====
# T Shapes
na = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
R = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0]
]
L = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 1]
]
N = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]
# C Shapes
G = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 1]
]
E = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 1, 1]
]
O = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 1]
]

# L Shapes
C = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]
A = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 1]
]
U = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 1]
]
B = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]

# Special Shapes
Z = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 1]
]
X = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 0, 1]
]
I = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 1]
]

# TDS Shapes
T = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0]
]
D = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 1]
]
S = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 1]
]

# Double Tile Parts
vertical_1 = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]
vertical_2 = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0]
]
vertical_3 = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]
vertical_twin = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 1]
]
horizontal_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
horizontal_2 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0]
]
horizontal_3 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 1]
]
horizontal_twin = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 1]
]
corner_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]
corner_2 = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 1]
]
corner_3 = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 1]
]
corner_4 = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]
u_shape_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 1]
]
u_shape_2 = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 1]
]
t_shape_3 = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 1]
]
V1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1]
]
V2 = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 1]
]
V3 = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
]
V4 = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 1]
]
Y1 = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 1]
]
H1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]

horizontal_1_border = [
[0  ,0  ,0  ,0  ],
[2  ,2  ,2  ,2  ],
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,0  ]
]
horizontal_3_border = [
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,0  ],
[2  ,2  ,2  ,2  ]
]
vertical_1_border = [
[0  ,2  ,0  ,0  ],
[0  ,2  ,0  ,0  ],
[0  ,2  ,0  ,0  ],
[0  ,2  ,0  ,0  ]
]
vertical_3_border = [
[0  ,0  ,0  ,2  ],
[0  ,0  ,0  ,2  ],
[0  ,0  ,0  ,2  ],
[0  ,0  ,0  ,2  ]
]
corner_1_border = [
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,2  ]
]
corner_2_border = [
[0  ,0  ,0  ,2  ],
[0  ,0  ,0  ,2  ],
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,0  ]
]
corner_3_border = [
[0  ,2  ,0  ,0  ],
[2  ,2  ,0  ,0  ],
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,0  ]
]
corner_4_border = [
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,0  ],
[2  ,2  ,0  ,0  ]
]
horizontal_twin_border = [
[0  ,0  ,0  ,0  ],
[2  ,2  ,2  ,2  ],
[0  ,0  ,0  ,0  ],
[2  ,2  ,2  ,2  ]
]
horizontal_twin_border_end1 = [
[0  ,2  ,0  ,0  ],
[2  ,2  ,0  ,0  ],
[0  ,2  ,0  ,0  ],
[2  ,2  ,2  ,2  ]
]
horizontal_twin_border_end2 = [
[0  ,0  ,0  ,0  ],
[2  ,2  ,2  ,2  ],
[0  ,2  ,0  ,0  ],
[2  ,2  ,0  ,0  ]
]
horizontal_twin_border_end3 = [
[0  ,2  ,0  ,0  ],
[2  ,2  ,0  ,0  ],
[0  ,2  ,0  ,0  ],
[2  ,2  ,0  ,0  ]
]
tile_border = [
[0  ,0  ,0  ,0  ],
[0  ,2  ,2  ,2  ],
[0  ,2  ,2  ,2  ],
[0  ,2  ,2  ,2  ]
]  
# Inner borders
inner_corner_1_border = [
[0  ,0  ,0  ,0  ],
[0  ,2  ,2  ,2  ],
[0  ,2  ,0  ,0  ],
[0  ,2  ,0  ,0  ]
]  
inner_corner_2_border = [
[0  ,0  ,0  ,0  ],
[0  ,2  ,0  ,0  ],
[0  ,2  ,0  ,0  ],
[0  ,2  ,2  ,2  ]
]  
inner_corner_3_border = [
[0  ,0  ,0  ,0  ],
[0  ,0  ,0  ,2  ],
[0  ,0  ,0  ,2  ],
[0  ,2  ,2  ,2  ]
]  
inner_corner_4_border = [
[0  ,0  ,0  ,0  ],
[0  ,2  ,2  ,2  ],
[0  ,0  ,0  ,2  ],
[0  ,0  ,0  ,2  ]
]  
u_shape_1_border = [
[0  ,0  ,0  ,0  ],
[0  ,2  ,2  ,2  ],
[0  ,2  ,0  ,2  ],
[0  ,2  ,0  ,2  ]
]  
u_shape_2_border = [
[0  ,0  ,0  ,0  ],
[0  ,2  ,2  ,2  ],
[0  ,2  ,0  ,0  ],
[0  ,2  ,2  ,2  ]
]  
u_shape_3_border = [
[0  ,0  ,0  ,0  ],
[0  ,2  ,0  ,2  ],
[0  ,2  ,0  ,2  ],
[0  ,2  ,2  ,2  ]
]  
u_shape_4_border = [
[0  ,0  ,0  ,0  ],
[0  ,2  ,2  ,2  ],
[0  ,0  ,0  ,2  ],
[0  ,2  ,2  ,2  ]
]  
vertical_twin_border = [
[0  ,2  ,0  ,2  ],
[0  ,2  ,0  ,2  ],
[0  ,2  ,0  ,2  ],
[0  ,2  ,0  ,2  ]
]



# Generating the funny

def Border_Load(input_list, border_option):
    for sentence_ypos in input_list:
        sentence_ypos.insert(0, vertical_3_border)
        sentence_ypos.append(vertical_1_border)
    sentence_vbound = len(input_list)
    sentence_hbound = len(input_list[0])
    input_list.insert(0, [horizontal_3_border for _ in range(sentence_hbound)])
    input_list.append([horizontal_1_border for _ in range(sentence_hbound)])
    input_list[ 0][ 0] = dc(corner_1_border)
    input_list[-1][ 0] = dc(corner_2_border)
    input_list[-1][-1] = dc(corner_3_border)
    input_list[ 0][-1] = dc(corner_4_border)

    sentence_vbound = len(input_list)
    sentence_hbound = len(input_list[0])
    if border_option == 'Tiles':
        for sentence_ypos in range(sentence_vbound):
            for sentence_xpos in range(sentence_hbound):
                if input_list[sentence_ypos][sentence_xpos] == na:
                    input_list[sentence_ypos][sentence_xpos] = dc(tile_border)
                    input_list[sentence_ypos][sentence_xpos][0][0] = 5

    if border_option == 'None':
        for sentence_ypos in range(sentence_vbound):
            for sentence_xpos in range(sentence_hbound):
                if input_list[sentence_ypos][sentence_xpos] == na:
                    input_list[sentence_ypos][sentence_xpos][0][0] = 5
    
    if border_option == 'Lines':
        simple_matrix = [[0 for _ in range(len(input_list[0]))] for _ in range(len(input_list))]
        for sentence_ypos in range(sentence_vbound):
            for sentence_xpos in range(sentence_hbound):
                if sentence_xpos == 0 or sentence_xpos == sentence_hbound - 1 or sentence_ypos == 0 or sentence_ypos == sentence_vbound - 1:
                    simple_matrix[sentence_ypos][sentence_xpos] = 2
                elif input_list[sentence_ypos][sentence_xpos] != na:
                    simple_matrix[sentence_ypos][sentence_xpos] = 1


        def activate_tile(rect, number, matrix=simple_matrix):
            for activate_ypos in range(rect[0], rect[2] + 1):
                for activate_xpos in range(rect[1], rect[3] + 1):
                    matrix[activate_ypos][activate_xpos] = number


        # Defining the rects.
        if simple_matrix[sentence_vbound - 2][1] == 0 or simple_matrix[sentence_vbound - 2][sentence_hbound - 2] == 0:
            rect_list = []
            for start_ypos in range(sentence_vbound - 1, -1, -1):
                for start_xpos in range(sentence_hbound - 1, -1, -1):

                    if simple_matrix[start_ypos][start_xpos] == 0:
                        min_xpos_width = sentence_hbound
                        best_rect = [start_ypos, start_xpos, start_ypos, start_xpos, 1, 1]   #  rect = [start_ypos, start_xpos, end_ypos, end_xpos, width, height]
                        end_ypos = start_ypos + 1
                        while True:
                            end_ypos -= 1
                            end_xpos = start_xpos + 1
                            if simple_matrix[end_ypos][start_xpos] > 0:
                                break
                            while True:
                                end_xpos -= 1 
                                if simple_matrix[end_ypos][end_xpos] > 0 or end_xpos == start_xpos - min_xpos_width:
                                    end_xpos += 1
                                    if min_xpos_width > (start_xpos - end_xpos + 1):
                                        min_xpos_width = (start_xpos - end_xpos + 1)
                                    if ((start_xpos - end_xpos + 1) * (start_ypos - end_ypos + 1)) > (best_rect[4] * best_rect[5]):
                                        best_rect = [end_ypos, end_xpos, start_ypos, start_xpos, (start_xpos - end_xpos + 1), (start_ypos - end_ypos + 1)]
                                    break
                        rect_list.append(best_rect)
                        activate_tile(best_rect, 3, simple_matrix)


        else: 
            rect_list = []
            for start_ypos in range(sentence_vbound):
                for start_xpos in range(sentence_hbound):

                    if simple_matrix[start_ypos][start_xpos] == 0:
                        min_xpos_width = sentence_hbound
                        best_rect = [start_ypos, start_xpos, start_ypos, start_xpos, 1, 1]   #  rect = [start_ypos, start_xpos, end_ypos, end_xpos, width, height]
                        end_ypos = start_ypos - 1
                        while True:
                            end_ypos += 1
                            end_xpos = start_xpos - 1
                            if simple_matrix[end_ypos][start_xpos] > 0:
                                break
                            while True:
                                end_xpos += 1
                                if simple_matrix[end_ypos][end_xpos] > 0 or start_xpos == end_xpos - min_xpos_width:
                                    end_xpos -= 1
                                    if min_xpos_width > (start_xpos - end_xpos + 1):
                                        min_xpos_width = (end_xpos - start_xpos + 1)
                                    if ((end_xpos - start_xpos + 1) * (end_ypos - start_ypos + 1)) > (best_rect[4] * best_rect[5]):
                                        best_rect = [start_ypos, start_xpos, end_ypos, end_xpos, (end_xpos - start_xpos + 1), (end_ypos - start_ypos + 1)]
                                    break
                        rect_list.append(best_rect)
                        activate_tile(best_rect, 3, simple_matrix)
        
        
        # Making sure of the activation order
        # Killing orphaned tiles (This sounds so evil lmao)

        rect_load_list = []
        
        while True:
            still_loading = False
            for rect in rect_list:
                if simple_matrix[rect[0]][rect[1]] == 2:
                    continue
                adjacent_area = (simple_matrix[rect[0] - 1][rect[1] : rect[3] + 1] + 
                                simple_matrix[rect[2] + 1][rect[1] : rect[3] + 1] +
                                [i[rect[1] - 1] for i in simple_matrix[rect[0] : rect[2] + 1]] +
                                [i[rect[3] + 1] for i in simple_matrix[rect[0] : rect[2] + 1]]
                                )

                if 2 in adjacent_area:
                    activate_tile(rect, 2, simple_matrix)
                    rect_load_list.append(rect)
                    still_loading = True
            if not still_loading:
                break

        for ypos in range(sentence_vbound):
            for xpos in range(sentence_hbound):
                if simple_matrix[ypos][xpos] == 3:
                    simple_matrix[ypos][xpos] = 0
        

        # Loading the actual borders in.

        
        for rect in rect_load_list:         # border_relation = [Exist?, DependIndepend/Partital? - 3, Dependency_Start, Dependency_End]
                                            # rect = [start_ypos, start_xpos, end_ypos, end_xpos, width, height]

            border_area_up = simple_matrix[rect[0] - 1][rect[1] : rect[3] + 1]
            border_area_down = simple_matrix[rect[2] + 1][rect[1] : rect[3] + 1]
            border_area_left = [i[rect[1] - 1] for i in simple_matrix[rect[0] : rect[2] + 1]]
            border_area_right = [i[rect[3] + 1] for i in simple_matrix[rect[0] : rect[2] + 1]]

            border_relation_up = [1 if 2 in border_area_up else 0, None, None, None]
            border_relation_down = [1 if 2 in border_area_down else 0, None, None, None]
            border_relation_left = [1 if 2 in border_area_left else 0, None, None, None]
            border_relation_right = [1 if 2 in border_area_right else 0, None, None, None]


            if border_relation_up[0] == 1:
                if ((2 in border_area_up) and 
                    (1 in border_area_up) and
                    ((simple_matrix[rect[0] - 1][rect[1] - 1] == 2 and simple_matrix[rect[0]][rect[1] - 1] == 1) or
                    (simple_matrix[rect[0] - 1][rect[3] + 1] == 2 and simple_matrix[rect[0]][rect[3] + 1] == 1))):

                    border_relation_up[1] = "Partial"
                elif 1 in border_area_up:
                    border_relation_up[1] = "Independent"
                else: 
                    border_relation_up[1] = "Dependent"

                if border_relation_up[1] != "Dependent":
                    index = 0
                    started = False
                    for tile in border_area_up:        
                        if tile == 2 and started == False:
                            border_relation_up[2] = index
                        if tile == 1 and started == True:
                            border_relation_up[3] = index
                            break
                        index += 1


            if border_relation_down[0] == 1:
                if ((2 in border_area_down) and 
                    (1 in border_area_down) and
                    ((simple_matrix[rect[2] + 1][rect[1] - 1] == 2 and simple_matrix[rect[2]][rect[1] - 1] == 1) or
                    (simple_matrix[rect[2] + 1][rect[3] + 1] == 2 and simple_matrix[rect[2]][rect[3] + 1] == 1))):

                    border_relation_up[1] = "Partial"
                elif 1 in border_area_down:
                    border_relation_up[1] = "Independent"
                else: 
                    border_relation_up[1] = "Dependent"

                if border_relation_up[1] != "Dependent":
                    index = 0
                    started = False
                    for tile in border_area_down:        
                        if tile == 2 and started == False:
                            border_relation_up[2] = index
                        if tile == 1 and started == True:
                            border_relation_up[3] = index
                            break
                        index += 1
            

            if border_relation_left[0] == 1:
                if ((2 in border_area_left) and 
                    (1 in border_area_left) and
                    ((simple_matrix[rect[2] + 1][rect[1] - 1] == 2 and simple_matrix[rect[2] + 1][rect[1]] == 1) or
                    (simple_matrix[rect[0] - 1][rect[1] - 1] == 2 and simple_matrix[rect[0] - 1][rect[1]] == 1))):

                    border_relation_up[1] = "Partial"
                elif 1 in border_area_left:
                    border_relation_up[1] = "Independent"
                else: 
                    border_relation_up[1] = "Dependent"

                if border_relation_up[1] != "Dependent":
                    index = 0
                    started = False
                    for tile in border_area_left:        
                        if tile == 2 and started == False:
                            border_relation_up[2] = index
                        if tile == 1 and started == True:
                            border_relation_up[3] = index
                            break
                        index += 1


            if border_relation_left[0] == 1:
                if ((2 in border_area_left) and 
                    (1 in border_area_left) and
                    ((simple_matrix[rect[2] + 1][rect[3] + 1] == 2 and simple_matrix[rect[2] + 1][rect[3]] == 1) or
                    (simple_matrix[rect[0] - 1][rect[3] + 1] == 2 and simple_matrix[rect[0] - 1][rect[3]] == 1))):

                    border_relation_up[1] = "Partial"
                elif 1 in border_area_left:
                    border_relation_up[1] = "Independent"
                else: 
                    border_relation_up[1] = "Dependent"

                if border_relation_up[1] != "Dependent":
                    index = 0
                    started = False
                    for tile in border_area_left:        
                        if tile == 2 and started == False:
                            border_relation_up[2] = index
                        if tile == 1 and started == True:
                            border_relation_up[3] = index
                            break
                        index += 1


            # 1 width/height rects should be handled differen't from bigger rects.
            if rect[4] == 1 and rect[5] == 1:
                if border_relation_down[0] == 1:
                    input_list[rect[0]][rect[1]] = u_shape_1_border 
                    up_connect(4, input_list, rect[0]+1, rect[1], 2)

                elif border_relation_up[0] == 1:
                    input_list[rect[0]][rect[1]] = u_shape_3_border 
                    up_connect(4, input_list, rect[0], rect[1], 2)
                
                elif border_relation_right[0] == 1:
                    input_list[rect[0]][rect[1]] = u_shape_2_border 
                    left_connect(4, input_list, rect[0], rect[1]+1, 2)

                elif border_relation_left[0] == 1:
                    input_list[rect[0]][rect[1]] = u_shape_4_border 
                    left_connect(4, input_list, rect[0], rect[1], 2)


            elif rect[4] == 1:
                if border_relation_down[0] == 1:
                    input_list[rect[0]][rect[1]] = u_shape_1_border 
                    for ypos in range(rect[0]+1, rect[2]+1):
                        input_list[ypos][rect[1]] = vertical_twin_border
                    up_connect(4, input_list, rect[2]+1, rect[1], 2)

                elif border_relation_up[0] == 1:
                    input_list[rect[2]][rect[1]] = u_shape_3_border 
                    for ypos in range(rect[0], rect[2]):
                        input_list[ypos][rect[1]] = vertical_twin_border
                    up_connect(4, input_list, rect[0], rect[1], 2)
                
                elif border_relation_right[0] == 1:
                    input_list[rect[0]][rect[1]] = inner_corner_1_border 
                    input_list[rect[2]][rect[1]] = inner_corner_2_border 
                    for ypos in range(rect[0]+1, rect[2]):
                        input_list[ypos][rect[1]] = vertical_1_border
                    left_connect(1, input_list, rect[0], rect[1]+1, 2)
                    left_connect(3, input_list, rect[2], rect[1]+1, 2)

                elif border_relation_left[0] == 1:
                    input_list[rect[0]][rect[1]] = inner_corner_4_border 
                    input_list[rect[2]][rect[1]] = inner_corner_3_border 
                    for ypos in range(rect[0]+1, rect[2]):
                        input_list[ypos][rect[1]] = vertical_3_border
                    left_connect(1, input_list, rect[0], rect[1], 2)
                    left_connect(3, input_list, rect[2], rect[1], 2)


            elif rect[5] == 1:

                if border_relation_right[0] == 1:
                    input_list[rect[0]][rect[1]] = u_shape_2_border
                    for xpos in range(rect[1]+1, rect[3]+1):
                        input_list[rect[0]][xpos] = horizontal_twin_border
                    up_connect(4, input_list, rect[0], rect[1], 2) 

                elif border_relation_left[0] == 1:
                    input_list[rect[0]][rect[3]] = u_shape_4_border
                    for xpos in range(rect[1], rect[3]):
                        input_list[rect[0]][xpos] = horizontal_twin_border

                elif border_relation_down[0] == 1:
                    input_list[rect[0]][rect[1]] = inner_corner_1_border 
                    input_list[rect[0]][rect[3]] = inner_corner_4_border 
                    for ypos in range(rect[1]+1, rect[3]):
                        input_list[ypos][rect[1]] = vertical_1_border
                    up_connect(1, input_list, rect[0]+1, rect[1], 2)
                    up_connect(3, input_list, rect[0]+1, rect[3], 2)
                
                elif border_relation_down[0] == 1:
                    input_list[rect[0]][rect[1]] = inner_corner_2_border 
                    input_list[rect[0]][rect[3]] = inner_corner_3_border 
                    for ypos in range(rect[1]+1, rect[3]):
                        input_list[ypos][rect[1]] = vertical_3_border
                    up_connect(1, input_list, rect[0], rect[1], 2)
                    up_connect(3, input_list, rect[0], rect[3], 2)


            
            # Handling bigger rects
            else:
                input_list[rect[0]][rect[1]] = inner_corner_1_border
                input_list[rect[0]][rect[3]] = inner_corner_2_border
                input_list[rect[2]][rect[3]] = inner_corner_3_border
                input_list[rect[2]][rect[1]] = inner_corner_4_border
            
                for ypos in range(rect[0]+1, rect[2]):
                    input_list[ypos][rect[1]] = vertical_1_border
                    input_list[ypos][rect[3]] = vertical_3_border
                
                for xpos in range(rect[1]+1, rect[3]):
                    input_list[rect[0]][xpos] = horizontal_1_border
                    input_list[rect[2]][xpos] = horizontal_3_border



        print (np.array(simple_matrix))
    return input_list



def Paragraph_Translate(input_str, border_option="None"):

    Sentence_List = []
    Sentence = ""
    input_str += "."
    for Letter in input_str:
        if Letter in [".", "\n", "!", "?","…"] and Sentence != "":
            Sentence_List.append(Sentence)
            Sentence=""
            continue
        Sentence += Letter
    
    Translated_Sentence_List = [Sentence_Translate(Sentence) for Sentence in Sentence_List]

    Paragraph_Length = len(Translated_Sentence_List)
    paragraph_vbound = 0
    paragraph_hbound = 0
    for sentence_index in range(Paragraph_Length):
        paragraph_vbound += len(Translated_Sentence_List[sentence_index]) + 2
        if paragraph_hbound < len(Translated_Sentence_List[sentence_index][0]):
            paragraph_hbound = len(Translated_Sentence_List[sentence_index][0])
    paragraph_hbound += 3

    Output_Paragraph = [[dc(na) for _ in range(paragraph_hbound)] for _ in range(paragraph_vbound)]


    for sentence_index in range(Paragraph_Length):
        Translated_Sentence_List[sentence_index] = Border_Load(Translated_Sentence_List[sentence_index], border_option)
        

    # Printing the texts.
    insert_offset = 0
    for sentence_index in range(Paragraph_Length):
        sentence_vbound = len(Translated_Sentence_List[sentence_index])
        sentence_hbound = len(Translated_Sentence_List[sentence_index][0])
        sentence_ypos = -1
        while sentence_ypos != sentence_vbound - 1:
            sentence_ypos += 1
            sentence_xpos = -1
            while sentence_xpos != sentence_hbound - 1:
                sentence_xpos += 1
                Output_Paragraph[sentence_ypos + insert_offset][sentence_xpos] = Translated_Sentence_List[sentence_index][sentence_ypos][sentence_xpos]
        if insert_offset != 0:
            for connector_tile in range(paragraph_hbound):

                if Output_Paragraph[insert_offset][connector_tile] == na:
                    Output_Paragraph[insert_offset][connector_tile-1] = dc(horizontal_twin_border_end3)
                    break
                if Output_Paragraph[insert_offset - 1][connector_tile] == na:
                    Output_Paragraph[insert_offset][connector_tile-1] = dc(horizontal_twin_border_end1)
                    break
                if Output_Paragraph[insert_offset + 1][connector_tile] == na:
                    Output_Paragraph[insert_offset][connector_tile-1] = dc(horizontal_twin_border_end2)
                    break

                Output_Paragraph[insert_offset][connector_tile] = dc(horizontal_twin_border)
                if connector_tile == 0:
                    Output_Paragraph[insert_offset][connector_tile] = dc(vertical_3_border)

        insert_offset += sentence_vbound - 1


    for paragraph_ypos in range(len(Output_Paragraph)):
        for paragraph_xpos in range(len(Output_Paragraph[0])):
            if Output_Paragraph[paragraph_ypos][paragraph_xpos][0][0] == 5:
                Output_Paragraph[paragraph_ypos][paragraph_xpos][0][0] = 0

                
    return tile_trim(Output_Paragraph)





def Numerical_Translate(input_num):
    output_str = ""
    for digit_index in range(1, len(input_num) + 1):
        digit = int(input_num[-digit_index])
        if digit_index % 3 == 1:
            if digit_index != 1: 
                output_str = "t" + Numerical_Translate(str(digit_index // 3)) + "s" + output_str
            match digit:
                case 1:
                    output_str = "i"   + output_str
                case 2:
                    output_str = "ii"  + output_str
                case 3:
                    output_str = "iii" + output_str
                case 4:
                    output_str = "iv"  + output_str
                case 5:
                    output_str = "v"   + output_str
                case 6:
                    output_str = "vi"  + output_str
                case 7:
                    output_str = "vii" + output_str
                case 8:
                    output_str = "viii"+ output_str
                case 9:
                    output_str = "ix" +  output_str
        if digit_index % 3 == 2:
            match digit:
                case 1:
                    output_str = "x"   + output_str
                case 2:
                    output_str = "xx"  + output_str
                case 3:
                    output_str = "xxx" + output_str
                case 4:
                    output_str = "xl"  + output_str
                case 5:
                    output_str = "l"   + output_str
                case 6:
                    output_str = "lx"  + output_str
                case 7:
                    output_str = "lxx" + output_str
                case 8:
                    output_str = "lxxx" + output_str
                case 9:
                    output_str = "xc" +  output_str
        if digit_index % 3 == 0:
            match digit:
                case 1:
                    output_str = "c"   + output_str
                case 2:
                    output_str = "cc"  + output_str
                case 3:
                    output_str = "ccc" + output_str
                case 4:
                    output_str = "cd"  + output_str
                case 5:
                    output_str = "d"   + output_str
                case 6:
                    output_str = "dc"  + output_str
                case 7:
                    output_str = "dcc" + output_str
                case 8:
                    output_str = "dccc" + output_str
                case 9:
                    output_str = "cm" +  output_str
            
    return output_str



def Sentence_Translate(input_str):
    input_str = input_str.strip().lower() + " "
    Word = ""
    Word_List = []
    Letter_index = -1
    while Letter_index != len(input_str) - 1:
        Letter_index += 1
        Letter = input_str[Letter_index]

        if ((ord(Letter) < 48) or (ord(Letter) > 57 and ord(Letter) < 97) or (ord(Letter) > 122)) and (Letter != " "):
            continue
        if  (ord(Letter) > 96) and (ord(Letter) < 123):
            Word += Letter
            continue

        Number_String = ""
        while (ord(Letter) > 47) and (ord(Letter) < 58):    # Convert numbers to Roman
            Number_String += Letter
            Letter_index += 1
            Letter = input_str[Letter_index]
        if Number_String != "":
            Word += ("d" if Word == "" else "") + Numerical_Translate(Number_String)
            continue

        if Letter == " " and Word != "":
            if not Word in ["t", "d", "s"]:
                Word_List.append(Word)
            Word = ""
        
    
    sentence_vbound = 0
    Sentence_Length = 0
    for Word in Word_List:
        if ("t" in Word or "d" in Word or "s" in Word) and len(Word) > sentence_vbound:
            sentence_vbound = len(Word)
        Sentence_Length += 1
    if sentence_vbound == 0:
        for Word in Word_List:
            if len(Word) > sentence_vbound:
                sentence_vbound = len(Word)
    sentence_vbound -= 1
    if sentence_vbound < 3:
        sentence_vbound = 3 
    
    Word_Reading = "na"
    Word_Reading_List = []
    i1 = -1 
    while i1 != Sentence_Length - 1:
        i1 += 1
        Word = Word_List[i1]
        Length = len(Word)
        i2 = -1
        while i2 != Length - 1:
            i2 += 1
            if Word[i2] in ["t", "d", "s"]:
                Word_Reading = Word[i2]
                Word_List[i1] = Word[:i2] + Word[i2+1:]
                break
        Word_Reading_List.append(Word_Reading)
    
    i = 0 
    while (i != Sentence_Length - 1) and (Sentence_Length != 1):
        i += 1
        if Word_Reading_List[i] == Word_Reading_List[i-1]:
            Word_List[i-1] = Word_List[i-1] + Word_List[i]
            del Word_List[i]
            del Word_Reading_List[i]
            i -= 1
            Sentence_Length -= 1
    
    Translated_Sen = []
    i = -1
    while i != Sentence_Length - 1:
        i += 1
        Word = Word_List[i]
        match Word_Reading_List[i]:
            case "na":
                Translated_Sen.append(tile_trim(Reading_na(sentence_vbound, Word)))
            case "t":
                Translated_Sen.append(tile_trim(Reading_t(sentence_vbound, Word)))
            case "d":
                Translated_Sen.append(tile_trim(Reading_d(sentence_vbound, Word)))
            case "s":
                Translated_Sen.append(tile_trim(Reading_s(sentence_vbound, Word)))



    sentence_vbound = 0
    sentence_hbound = len(input_str) + 1
    for Translated_Word in Translated_Sen:
        if sentence_vbound < len(Translated_Word):
            sentence_vbound = len(Translated_Word)
    
    Output_Sentence = [[dc(na) for _ in range(sentence_hbound)] for _ in range(sentence_vbound)]


    i = -1
    while i != len(Translated_Sen) - 1:     # Loading in the words. 

        i += 1
        Translated_Word = Translated_Sen[i]
        word_vbound = len(Translated_Word)
        word_hbound = len(Translated_Word[0])
        Word_Reading = Word_Reading_List[i]

        # Checking available collumns.
        insert_ypos = -1
        all_na = False
        while all_na != True:   
            insert_ypos += 1
            insert_xpos = -1
            all_na = True
            while insert_xpos != sentence_vbound - 1:
                insert_xpos += 1
                if Output_Sentence[insert_xpos][insert_ypos] != na:
                    all_na = False
                    break
        
        # Offsetting insert_col
        insert_offset_xpos = -1 
        Collide_Right = [1] * word_vbound
        Collide_Left  = [1] * word_vbound
        Insert_Offset = 0 
        Collided = False
        while insert_offset_xpos != word_hbound - 1:
            insert_offset_xpos += 1
            insert_offset_ypos = -1
            while insert_offset_ypos != word_vbound - 1:
                insert_offset_ypos += 1
                Insert_Offset_y_new = insert_offset_ypos * (1 if Word_Reading == "t" or Word_Reading == "d" else -1)  + (0 if Word_Reading == "t" or Word_Reading == "d" else -1)

                if Translated_Word[Insert_Offset_y_new][insert_offset_xpos] != na:
                    Collide_Right[Insert_Offset_y_new] *= 0
                if Output_Sentence[Insert_Offset_y_new][insert_ypos - insert_offset_xpos - 1] != na:
                    Collide_Left[Insert_Offset_y_new] *= 0

            for Collide_Row in range(word_vbound):
                if Collide_Right[Collide_Row] + Collide_Left[Collide_Row] == 0 or insert_ypos - insert_offset_xpos == 0:
                    Collided = True
            if Collided == True:
                break
            Insert_Offset += 1
        
        # Special offset collision cases
        while Collided == False:    
            insert_offset_xpos += 1
            insert_offset_ypos = -1
            while insert_offset_ypos != word_vbound - 1:
                insert_offset_ypos += 1
                Insert_Offset_y_new = insert_offset_ypos * (1 if Word_Reading == "t" or Word_Reading == "d" else -1)  + (0 if Word_Reading == "t" or Word_Reading == "d" else -1)

                if Output_Sentence[Insert_Offset_y_new][insert_ypos - insert_offset_xpos - 1] != na:
                    Collide_Left[Insert_Offset_y_new] *= 0

            for Collide_Row in range(word_vbound):
                if Collide_Right[Collide_Row] + Collide_Left[Collide_Row] == 0 or insert_ypos - insert_offset_xpos == 0:
                    Collided = True
            if Collided == True:
                break
            Insert_Offset += 1          
        
        insert_ypos -= Insert_Offset


        # Loading the word in.
        load_ypos = -1
        while load_ypos != word_vbound - 1:
            load_ypos += 1
            load_xpos = -1
            while load_xpos != word_hbound - 1:
                load_xpos += 1
                Load_y_new = load_ypos * (1 if Word_Reading == "t" or Word_Reading == "d" else -1)  + (0 if Word_Reading == "t" or Word_Reading == "d" else -1)
                if Translated_Word[Load_y_new][load_xpos] != na:
                    Output_Sentence[Load_y_new][load_xpos + insert_ypos] = Translated_Word[Load_y_new][load_xpos]
        
    tile_trim(Output_Sentence)
    return Output_Sentence
    
    

def Reading_na(Word_vbound, input_str):
    
    Word_hbound = len(input_str)
    Output_Word = [[dc(na) for _ in range(Word_hbound)] for _ in range(Word_vbound)]
    Letter_index = -1
    Symbol_index = -1

    def pos_calc():
        nonlocal word_xpos, word_ypos
        word_xpos = Word_hbound - Symbol_index // Word_vbound - 1
        word_ypos = Word_vbound - Symbol_index % Word_vbound - 1 

    def double_tiles(horizontal_tile_start=dc(na), horizontal_tile_end=None, vertical_tile_middle=None, vertical_tile_start=None, vertical_tile_end=None, 
                    horizontal_connection=None, vertical_connection=None, horizontal_vertical_connection=None, bottom_tile_normal=dc(na), top_tile_normal=dc(na), normal_connection=None):

        nonlocal word_xpos, word_ypos, Symbol_index
        if Word_hbound - (Symbol_index+1) // Word_vbound -1 != word_xpos:
            Output_Word[word_ypos][word_xpos] = dc(horizontal_tile_start)
            left_connect (horizontal_connection, Output_Word, word_ypos, word_xpos)

            word_ypos_root = word_ypos
            if vertical_tile_start!=None:
                Symbol_index += 1
                pos_calc()
                Output_Word[word_ypos][word_xpos] = dc(vertical_tile_start)
                up_connect (vertical_connection, Output_Word, word_ypos, word_xpos)

            while True:
                Symbol_index += 1
                pos_calc()
                if word_ypos == word_ypos_root + 1:
                    if vertical_tile_end != None:
                        Output_Word[word_ypos][word_xpos] = dc(vertical_tile_end)
                    up_connect (horizontal_vertical_connection, Output_Word, word_ypos, word_xpos)

                    Symbol_index += 1
                    pos_calc()
                    Output_Word[word_ypos][word_xpos] = dc(horizontal_tile_end) # type: ignore
                    break
                if vertical_tile_middle != None:
                    Output_Word[word_ypos][word_xpos] = dc(vertical_tile_middle)
                up_connect (vertical_connection, Output_Word, word_ypos, word_xpos)
                
        else:
            Output_Word[word_ypos][word_xpos] = dc(bottom_tile_normal)
            up_connect(normal_connection, Output_Word, word_ypos, word_xpos)
            
            Symbol_index += 1
            pos_calc()
            Output_Word[word_ypos][word_xpos] = dc(top_tile_normal)

    while Letter_index != Word_hbound-1:
        Letter_index += 1
        Symbol_index += 1

        word_xpos = 0
        word_ypos = 0

        pos_calc()

        match input_str[Letter_index]:
            case "r":
                Output_Word[word_ypos][word_xpos] = dc(R)
            case "l":
                Output_Word[word_ypos][word_xpos] = dc(L)
            case "n":
                Output_Word[word_ypos][word_xpos] = dc(N)
            case "g":
                Output_Word[word_ypos][word_xpos] = dc(G)
            case "e":
                Output_Word[word_ypos][word_xpos] = dc(E)
            case "o":
                Output_Word[word_ypos][word_xpos] = dc(O)
            case "c":
                Output_Word[word_ypos][word_xpos] = dc(C)
            case "a":
                Output_Word[word_ypos][word_xpos] = dc(A)
            case "u":
                Output_Word[word_ypos][word_xpos] = dc(U)
            case "b":
                Output_Word[word_ypos][word_xpos] = dc(B)
            case "x":
                Output_Word[word_ypos][word_xpos] = dc(X)
            case "z":
                Output_Word[word_ypos][word_xpos] = dc(Z)
            case "i":
                Output_Word[word_ypos][word_xpos] = dc(I) 
            case "j":
                double_tiles(
                    horizontal_tile_start=horizontal_1, horizontal_connection=1, horizontal_tile_end=horizontal_1, 
                    vertical_tile_middle=vertical_1, vertical_tile_start=vertical_1, vertical_tile_end=corner_1, vertical_connection=1, 
                    bottom_tile_normal=vertical_1, top_tile_normal=horizontal_twin, normal_connection=1)
            case "f":
                double_tiles(
                    horizontal_tile_start=horizontal_1, horizontal_connection=1, horizontal_tile_end=horizontal_twin, 
                    vertical_tile_middle=vertical_3, vertical_tile_start=vertical_3, vertical_tile_end=vertical_3, vertical_connection=3, 
                    horizontal_vertical_connection=3, bottom_tile_normal=vertical_3, top_tile_normal=horizontal_twin, normal_connection=3)
            case "p":
                double_tiles(
                    horizontal_tile_start=horizontal_3, horizontal_connection=3, horizontal_tile_end=corner_2, 
                    vertical_tile_start=horizontal_3, 
                    bottom_tile_normal=horizontal_twin, top_tile_normal=vertical_1, normal_connection=1)
            case "k":
                double_tiles(
                    horizontal_tile_start=corner_3, horizontal_connection=3, horizontal_tile_end=horizontal_3, 
                    vertical_tile_start=horizontal_3, 
                    bottom_tile_normal=horizontal_twin, top_tile_normal=vertical_3, normal_connection=3)
            case "m":
                double_tiles(
                    horizontal_tile_start=corner_4, horizontal_connection=1, horizontal_tile_end=corner_1, 
                    vertical_tile_middle=vertical_2, vertical_tile_start=vertical_2, vertical_tile_end=vertical_2, vertical_connection=2, 
                    horizontal_vertical_connection=2,bottom_tile_normal=vertical_2, top_tile_normal=u_shape_1, normal_connection=2)
            case "q":
                double_tiles(
                    horizontal_tile_start=horizontal_3, horizontal_connection=3, horizontal_tile_end=horizontal_3, 
                    vertical_tile_middle=vertical_twin, vertical_tile_start=u_shape_2, vertical_tile_end=vertical_twin, vertical_connection=4, 
                    horizontal_vertical_connection=2, bottom_tile_normal=u_shape_2, top_tile_normal=vertical_2, normal_connection=2)
            case "w":
                double_tiles(
                    horizontal_tile_start=horizontal_3, horizontal_connection=3, horizontal_tile_end=horizontal_3, 
                    vertical_tile_middle=vertical_twin, vertical_tile_start=vertical_twin, vertical_tile_end=u_shape_1, vertical_connection=4, 
                    bottom_tile_normal=vertical_twin, top_tile_normal=horizontal_twin, normal_connection=4)
            case "y":
                double_tiles(
                    horizontal_tile_start=corner_4, horizontal_connection=1, horizontal_tile_end=corner_1, 
                    vertical_tile_start=horizontal_3, 
                    bottom_tile_normal=Y1, top_tile_normal=u_shape_1, normal_connection=4)
            case "h":
                double_tiles(
                    horizontal_tile_start=horizontal_1, horizontal_connection=1, horizontal_tile_end=H1, 
                    vertical_tile_middle=vertical_2, vertical_tile_start=t_shape_3, vertical_tile_end=vertical_2, vertical_connection=2, 
                    horizontal_vertical_connection=2, bottom_tile_normal=t_shape_3, top_tile_normal=H1, normal_connection=2)
            case "v":
                double_tiles(
                    horizontal_tile_start=horizontal_1, horizontal_connection=1, horizontal_tile_end=V1, 
                    vertical_tile_middle=vertical_3, vertical_tile_start=corner_3, vertical_tile_end=vertical_3, vertical_connection=3, 
                    horizontal_vertical_connection=3, bottom_tile_normal=V2, top_tile_normal=V1, normal_connection=4)
    return Output_Word

def Reading_s(Word_vbound, input_str):
    Word_hbound = len(input_str)
    Output_Word = [[dc(na) for _ in range(Word_hbound)] for _ in range(Word_vbound)]
    Letter_index = -1
    Symbol_index = -1

    def pos_calc():
        nonlocal word_xpos, word_ypos
        word_xpos = Symbol_index // Word_vbound
        word_ypos = Word_vbound - Symbol_index % Word_vbound - 1 

    def double_tiles(horizontal_tile_start=dc(na), horizontal_tile_end=None, vertical_tile_middle=None, vertical_tile_start=None, vertical_tile_end=None, 
                    horizontal_connection=None, vertical_connection=None, horizontal_vertical_connection=None, bottom_tile_normal=dc(na), top_tile_normal=dc(na), normal_connection=None):

        nonlocal word_xpos, word_ypos, Symbol_index
        if (Symbol_index + 1) // Word_vbound != word_xpos:
            Output_Word[word_ypos][word_xpos] = dc(horizontal_tile_start)
            word_ypos_root = word_ypos
            if vertical_tile_start!=None:
                Symbol_index += 1
                pos_calc()
                Output_Word[word_ypos][word_xpos] = dc(vertical_tile_start)
                up_connect(vertical_connection, Output_Word, word_ypos, word_xpos)  

            while True:
                Symbol_index += 1
                pos_calc()
                if word_ypos == word_ypos_root + 1:
                    if vertical_tile_end != None:
                        Output_Word[word_ypos][word_xpos] = dc(vertical_tile_end)
                    up_connect(horizontal_vertical_connection, Output_Word, word_ypos, word_xpos)
                    
                    Symbol_index += 1
                    pos_calc()
                    Output_Word[word_ypos][word_xpos] = dc(horizontal_tile_end) # type: ignore
                    left_connect(horizontal_connection, Output_Word, word_ypos, word_xpos)

                    break
                if vertical_tile_middle != None:
                    Output_Word[word_ypos][word_xpos] = dc(vertical_tile_middle)
                up_connect (vertical_connection, Output_Word, word_ypos, word_xpos)

        else:
            Output_Word[word_ypos][word_xpos] = dc(bottom_tile_normal)
            up_connect(normal_connection, Output_Word, word_ypos, word_xpos)

            Symbol_index += 1
            pos_calc()
            Output_Word[word_ypos][word_xpos] = dc(top_tile_normal)

    while Letter_index != Word_hbound-1:
        Letter_index += 1
        Symbol_index += 1

        word_xpos = 0
        word_ypos = 0
        pos_calc()

        match input_str[Letter_index]:
            case "r":
                Output_Word[word_ypos][word_xpos] = dc(R)
            case "l":
                Output_Word[word_ypos][word_xpos] = dc(L)
            case "n":
                Output_Word[word_ypos][word_xpos] = dc(N)
            case "g":
                Output_Word[word_ypos][word_xpos] = dc(G)
            case "e":
                Output_Word[word_ypos][word_xpos] = dc(E)
            case "o":
                Output_Word[word_ypos][word_xpos] = dc(O)
            case "c":
                Output_Word[word_ypos][word_xpos] = dc(C)
            case "a":
                Output_Word[word_ypos][word_xpos] = dc(A)
            case "u":
                Output_Word[word_ypos][word_xpos] = dc(U)
            case "b":
                Output_Word[word_ypos][word_xpos] = dc(B)
            case "x":
                Output_Word[word_ypos][word_xpos] = dc(X)
            case "z":
                Output_Word[word_ypos][word_xpos] = dc(Z)
            case "i":
                Output_Word[word_ypos][word_xpos] = dc(I) 
            case "t":
                Output_Word[word_ypos][word_xpos] = dc(T) 
            case "d":
                Output_Word[word_ypos][word_xpos] = dc(D) 
            case "s":
                Output_Word[word_ypos][word_xpos] = dc(S) 
            case "j":
                double_tiles(
                    horizontal_tile_start=horizontal_1, horizontal_connection=1, horizontal_tile_end=horizontal_1, 
                    vertical_tile_middle=vertical_1, vertical_tile_start=vertical_1, vertical_tile_end=corner_1, vertical_connection=1, 
                    bottom_tile_normal=vertical_1, top_tile_normal=horizontal_twin, normal_connection=1)
            case "f":
                double_tiles(
                    horizontal_tile_start=horizontal_twin, horizontal_connection=4, horizontal_tile_end=horizontal_twin, 
                    vertical_tile_middle=vertical_3, vertical_tile_start=vertical_3, vertical_tile_end=vertical_3, vertical_connection=3, 
                    horizontal_vertical_connection=3, bottom_tile_normal=vertical_3, top_tile_normal=horizontal_twin, normal_connection=3)
            case "p":
                double_tiles(
                    horizontal_tile_start=corner_2, horizontal_connection=3, horizontal_tile_end=horizontal_3, 
                    vertical_tile_start=horizontal_3, 
                    bottom_tile_normal=horizontal_twin, top_tile_normal=vertical_1, normal_connection=1)
            case "k":
                double_tiles(
                    horizontal_tile_start=horizontal_3, horizontal_connection=3, horizontal_tile_end=corner_3, 
                    vertical_tile_start=horizontal_3, 
                    bottom_tile_normal=horizontal_twin, top_tile_normal=vertical_3, normal_connection=3)
            case "m":
                double_tiles(
                    horizontal_tile_start=corner_1, horizontal_connection=1, horizontal_tile_end=corner_4, 
                    vertical_tile_middle=vertical_2, vertical_tile_start=vertical_2, vertical_tile_end=vertical_2, vertical_connection=2, 
                    horizontal_vertical_connection=2,bottom_tile_normal=vertical_2, top_tile_normal=u_shape_1, normal_connection=2)
            case "q":
                double_tiles(
                    horizontal_tile_start=horizontal_3, horizontal_connection=3, horizontal_tile_end=horizontal_3, 
                    vertical_tile_middle=vertical_twin, vertical_tile_start=u_shape_2, vertical_tile_end=vertical_twin, vertical_connection=4, 
                    horizontal_vertical_connection=2, bottom_tile_normal=u_shape_2, top_tile_normal=vertical_2, normal_connection=2)
            case "w":
                double_tiles(
                    horizontal_tile_start=horizontal_3, horizontal_connection=3, horizontal_tile_end=horizontal_3, 
                    vertical_tile_middle=vertical_twin, vertical_tile_start=vertical_twin, vertical_tile_end=u_shape_1, vertical_connection=4, 
                    bottom_tile_normal=vertical_twin, top_tile_normal=horizontal_twin, normal_connection=4)
            case "y":
                double_tiles(
                    horizontal_tile_start=corner_1, horizontal_connection=1, horizontal_tile_end=corner_4, 
                    vertical_tile_start=horizontal_3, 
                    bottom_tile_normal=Y1, top_tile_normal=u_shape_1, normal_connection=4)
            case "h":
                double_tiles(
                    horizontal_tile_start=horizontal_1, horizontal_connection=1, horizontal_tile_end=H1, 
                    vertical_tile_middle=vertical_2, vertical_tile_start=t_shape_3, vertical_tile_end=vertical_2, vertical_connection=2, 
                    horizontal_vertical_connection=2, bottom_tile_normal=t_shape_3, top_tile_normal=H1, normal_connection=2)
            case "v":
                double_tiles(
                    horizontal_tile_start=corner_1, horizontal_connection=1, horizontal_tile_end=V3, 
                    vertical_tile_middle=vertical_3, vertical_tile_start=corner_3, vertical_tile_end=vertical_3, vertical_connection=3, 
                    horizontal_vertical_connection=3, bottom_tile_normal=V2, top_tile_normal=V1, normal_connection=4)
    return Output_Word

def Reading_d(Word_vbound, input_str):
    Word_hbound = len(input_str)
    Output_Word = [[dc(na) for _ in range(Word_hbound)] for _ in range(Word_vbound)]
    Letter_index = -1
    Symbol_index = -1
    Cycle = 0
    Bound_Offset = 0

    def pos_calc():
        nonlocal Word_xpos, Word_ypos, Cycle, Output_Word, Bound_Offset
        Symbol_index_Ghost = Symbol_index % (Word_vbound**2)
        Bound_Hit = int(Symbol_index // (Word_vbound**2))
        Bound_Offset = Bound_Hit * Word_vbound

        if Symbol_index_Ghost**0.5 % 1 == 0:
            Cycle = int(Symbol_index_Ghost**0.5)
            Word_ypos = Cycle
            Word_xpos = -Cycle - 1
        elif (Symbol_index_Ghost > Cycle**2) and (Symbol_index_Ghost <= (Cycle**2 + Cycle)):
            Word_ypos = Cycle
            Word_xpos = -(Symbol_index_Ghost - Cycle**2)
        elif (Symbol_index_Ghost > Cycle**2 + Cycle) and (Symbol_index_Ghost < ((Cycle + 1)**2)):
            Word_xpos = -Cycle - 1
            Word_ypos = (Cycle + 1)**2 - Symbol_index_Ghost - 1 

        if Symbol_index_Ghost == 0 and Bound_Hit != 0:
            Output_Word += [[dc(na) for _ in range(Word_hbound)] for _ in range(Word_vbound)]
    
        Word_xpos, Word_ypos = int(Word_xpos) - Bound_Offset, int(Word_ypos) + Bound_Offset


    def double_tiles(top_tile_horizontal_left=None,  top_tile_horizontal_right=None,  bottom_top_connection_left=None,bottom_top_connection_right=None,
                    bottom_horizontal_left_tile_middle=None, bottom_horizontal_left_tile_start=None, bottom_horizontal_left_tile_end=None, bottom_horizontal_connection_left=None,
                    bottom_horizontal_right_tile_middle=None, bottom_horizontal_right_tile_start=None, bottom_horizontal_right_tile_end=None, bottom_horizontal_connection_right=None,
                    top_horizontal_tile_start=dc(na), top_horizontal_tile_end=None, vertical_tile_middle=None, vertical_tile_start=None, vertical_tile_end=None, 
                    top_horizontal_connection=None, vertical_connection=None, horizontal_vertical_connection=None, 
                    bottom_tile_normal=dc(na), top_tile_normal=dc(na), normal_connection=None):
        # Sorry
        nonlocal Word_xpos, Word_ypos, Symbol_index, Letter_index, Cycle
        if ((-Word_xpos - 1 > Word_ypos) and (Word_ypos != Bound_Offset)) or ((Word_ypos==Word_vbound + Bound_Offset - 1) and (-Word_xpos==Word_vbound + Bound_Offset)):
            #print (ypos, xpos, 'A')
            Output_Word[Word_ypos][Word_xpos] = dc(bottom_tile_normal)
            up_connect(normal_connection, Output_Word, Word_ypos, Word_xpos)
            Output_Word[Word_ypos-1][Word_xpos] = dc(top_tile_normal)
            Output_Word[Word_ypos-1][Word_xpos][0][0] = 1
            if (-Word_xpos-1 == Word_ypos):
                Output_Word[Word_ypos][Word_xpos][0][0] = ["r", bottom_horizontal_connection_right, bottom_top_connection_right, dc(bottom_horizontal_right_tile_middle), dc(bottom_horizontal_right_tile_start), dc(bottom_horizontal_right_tile_end), dc(top_tile_horizontal_right)] # type: ignore
            

        elif (-Word_xpos-1 <= Word_ypos) and (Word_ypos != Word_vbound + Bound_Offset - 1):
            #print (ypos, xpos, 'B')
            Output_Word[Word_ypos][Word_xpos] = dc(top_tile_normal)
            Output_Word[Word_ypos+1][Word_xpos] = dc(bottom_tile_normal)
            Output_Word[Word_ypos+1][Word_xpos][0][0] = 1
            if (-Word_xpos-1 == Word_ypos) and (Word_ypos != 0):
                Output_Word[Word_ypos+1][Word_xpos][0][0] = ["r", bottom_horizontal_connection_right, bottom_top_connection_right, dc(bottom_horizontal_right_tile_middle), dc(bottom_horizontal_right_tile_start), dc(bottom_horizontal_right_tile_end), dc(top_tile_horizontal_right)] # type: ignore
            else:
                Output_Word[Word_ypos+1][Word_xpos][0][0] = ["l", bottom_horizontal_connection_left, bottom_top_connection_left, dc(bottom_horizontal_left_tile_middle), dc(bottom_horizontal_left_tile_start), dc(bottom_horizontal_left_tile_end), dc(top_tile_horizontal_left)] # type: ignore
            up_connect(normal_connection, Output_Word, Word_ypos+1, Word_xpos)


        elif Word_ypos == Bound_Offset:
            #print (ypos, xpos, 'C')
            Output_Word[Word_ypos][Word_xpos] = dc(top_horizontal_tile_start) 
            left_connect (top_horizontal_connection, Output_Word, Word_ypos, Word_xpos)
            Word_ypos_root = Word_ypos

            Symbol_index += 1
            pos_calc()

            Output_Word[Word_ypos][Word_xpos] = dc(vertical_tile_start) # type: ignore
            up_connect (vertical_connection, Output_Word, Word_ypos, Word_xpos)

            Word_ypos_temp = Word_ypos
            while Word_ypos_temp > 1 + Word_ypos_root:
                Word_ypos_temp -= 1
                Output_Word[Word_ypos_temp][Word_xpos] = dc(vertical_tile_middle) # type: ignore
                Output_Word[Word_ypos_temp][Word_xpos][0][0] = 1
                up_connect (vertical_connection, Output_Word, Word_ypos_temp, Word_xpos)
            
            Output_Word[1 + Word_ypos_root][Word_xpos] = dc(vertical_tile_end) # type: ignore
            Output_Word[1 + Word_ypos_root][Word_xpos][0][0] = 1
            up_connect (horizontal_vertical_connection, Output_Word, 1 + Word_ypos_root, Word_xpos)

            Output_Word[Word_ypos_root][Word_xpos] = dc(top_horizontal_tile_end) # type: ignore
            Output_Word[Word_ypos_root][Word_xpos][0][0] = 1


        elif Word_ypos == Word_vbound + Bound_Offset - 1:
            #print (ypos, xpos, 'D', '--Skipped')
            Letter_index -= 1

        else:
            print ("Error: Failed all four cases of double_tiles()  :<")



    def After_Stretch():
        word_ypos = -1
        Word_vbound_full = len(Output_Word)
        Word_hbound_full = len(Output_Word[0])

        while word_ypos != Word_vbound_full - 1:
            word_ypos += 1
            word_xpos = -1
            while word_xpos != Word_hbound_full - 1:
                word_xpos += 1

                if (type(Output_Word[word_ypos][word_xpos][0][0]) == list):
                    indicator: list = Output_Word[word_ypos][word_xpos][0][0]  # type: ignore
                    stretched = False

                    # ["r", bothconr, bottopconr, dc(bothorir0), dc(bothorir1), dc(bothorir2), dc(tophorir)]
                    if indicator[0] == "r":
                        i = 1
                        while (Output_Word[word_ypos][word_xpos + i] == na) and (Output_Word[word_ypos-1][word_xpos + i] != na):
                            stretched = True
                            Output_Word[word_ypos][word_xpos + i] = indicator[3]
                            left_connect(indicator[1], Output_Word, word_ypos, word_xpos + i)
                            i += 1
                            if word_xpos + i == Word_hbound_full:
                                break
                        i -= 1
                        if stretched == True: 
                            Output_Word[word_ypos][word_xpos] = indicator[4]
                            Output_Word[word_ypos][word_xpos + i] = indicator[5]
                            Output_Word[word_ypos-1][word_xpos] = indicator[6]
                            up_connect(indicator[2], Output_Word, word_ypos, word_xpos)
                            left_connect(indicator[1], Output_Word, word_ypos, word_xpos + i)
                        

                    if indicator[0] == "l" and word_xpos != 0:
                        i = 1    
                        while (Output_Word[word_ypos][word_xpos - i] == na) and (Output_Word[word_ypos-1][word_xpos - i] != na):
                            stretched = True
                            Output_Word[word_ypos][word_xpos - i] = indicator[3]
                            left_connect(indicator[1], Output_Word, word_ypos, word_xpos)
                            i += 1
                            if word_xpos - i == -1:
                                break                          
                        i -= 1
                        if stretched == True:                             
                            Output_Word[word_ypos][word_xpos] = indicator[4]
                            Output_Word[word_ypos][word_xpos - i] = indicator[5]
                            Output_Word[word_ypos-1][word_xpos] = indicator[6]
                            up_connect(indicator[2], Output_Word, word_ypos, word_xpos)
                            left_connect(indicator[1], Output_Word, word_ypos, word_xpos)
                Output_Word[word_ypos][word_xpos][0][0] = 0                       


    while Letter_index != Word_hbound-1:
        Letter_index += 1
        Symbol_index += 1

        Word_xpos = 0
        Word_ypos = 0
        pos_calc()

        while Output_Word[Word_ypos][Word_xpos][0][0] != 0:
            Symbol_index += 1
            pos_calc()
            
            

        match input_str[Letter_index]:
            case "r":
                Output_Word[Word_ypos][Word_xpos] = dc(R)
            case "l":
                Output_Word[Word_ypos][Word_xpos] = dc(L)
            case "n":
                Output_Word[Word_ypos][Word_xpos] = dc(N)
            case "g":
                Output_Word[Word_ypos][Word_xpos] = dc(G)
            case "e":
                Output_Word[Word_ypos][Word_xpos] = dc(E)
            case "o":
                Output_Word[Word_ypos][Word_xpos] = dc(O)
            case "c":
                Output_Word[Word_ypos][Word_xpos] = dc(C)
            case "a":
                Output_Word[Word_ypos][Word_xpos] = dc(A)
            case "u":
                Output_Word[Word_ypos][Word_xpos] = dc(U)
            case "b":
                Output_Word[Word_ypos][Word_xpos] = dc(B)
            case "x":
                Output_Word[Word_ypos][Word_xpos] = dc(X)
            case "z":
                Output_Word[Word_ypos][Word_xpos] = dc(Z)
            case "i":
                Output_Word[Word_ypos][Word_xpos] = dc(I)
            case "t":
                Output_Word[Word_ypos][Word_xpos] = dc(T) 
            case "d":
                Output_Word[Word_ypos][Word_xpos] = dc(D) 
            case "s":
                Output_Word[Word_ypos][Word_xpos] = dc(S) 

            case "j":
                double_tiles(top_tile_horizontal_left=horizontal_1, top_tile_horizontal_right=horizontal_1,
                    bottom_horizontal_left_tile_middle=horizontal_1, bottom_horizontal_left_tile_start=horizontal_1, bottom_horizontal_left_tile_end=corner_1, bottom_horizontal_connection_left=1,
                    bottom_horizontal_right_tile_middle=horizontal_1, bottom_horizontal_right_tile_start=corner_1, bottom_horizontal_right_tile_end=horizontal_1, bottom_horizontal_connection_right=1,
                    top_horizontal_tile_start=horizontal_1, top_horizontal_tile_end=horizontal_1, vertical_tile_middle=vertical_1, vertical_tile_start=vertical_1, vertical_tile_end=corner_1, 
                    top_horizontal_connection=1, vertical_connection=1, 
                    bottom_tile_normal=vertical_1, top_tile_normal=horizontal_twin, normal_connection=1)
            case "f":
                double_tiles(top_tile_horizontal_left=horizontal_3, top_tile_horizontal_right=horizontal_3,
                    bottom_horizontal_left_tile_middle=horizontal_1, bottom_horizontal_left_tile_start=corner_4, bottom_horizontal_left_tile_end=horizontal_1, bottom_horizontal_connection_left=1,
                    bottom_horizontal_right_tile_middle=horizontal_1, bottom_horizontal_right_tile_start=horizontal_1, bottom_horizontal_right_tile_end=corner_4, bottom_horizontal_connection_right=1,
                    top_horizontal_tile_start=horizontal_1, top_horizontal_tile_end=horizontal_twin, vertical_tile_middle=vertical_3, vertical_tile_start=vertical_3, vertical_tile_end=vertical_3, 
                    top_horizontal_connection=1, vertical_connection=3, horizontal_vertical_connection=3, 
                    bottom_tile_normal=vertical_3, top_tile_normal=horizontal_twin, normal_connection=3)
            case "p":
                double_tiles(top_tile_horizontal_left=vertical_1, top_tile_horizontal_right=vertical_1, bottom_top_connection_left=1, bottom_top_connection_right=1,
                    bottom_horizontal_left_tile_middle=horizontal_3, bottom_horizontal_left_tile_start=horizontal_twin, bottom_horizontal_left_tile_end=horizontal_3, bottom_horizontal_connection_left=3,
                    bottom_horizontal_right_tile_middle=horizontal_twin, bottom_horizontal_right_tile_start=horizontal_twin, bottom_horizontal_right_tile_end=horizontal_twin, bottom_horizontal_connection_right=4,
                    top_horizontal_tile_start=horizontal_3, top_horizontal_tile_end=corner_2, vertical_tile_middle=dc(na), vertical_tile_start=horizontal_3, vertical_tile_end=dc(na),
                    top_horizontal_connection=3, 
                    bottom_tile_normal=horizontal_twin, top_tile_normal=vertical_1, normal_connection=1)
            case "k":
                double_tiles(top_tile_horizontal_left=vertical_3, top_tile_horizontal_right=vertical_3, bottom_top_connection_left=3, bottom_top_connection_right=3,
                    bottom_horizontal_left_tile_middle=horizontal_twin, bottom_horizontal_left_tile_start=horizontal_twin, bottom_horizontal_left_tile_end=horizontal_twin, bottom_horizontal_connection_left=4,
                    bottom_horizontal_right_tile_middle=horizontal_3, bottom_horizontal_right_tile_start=horizontal_twin, bottom_horizontal_right_tile_end=horizontal_3, bottom_horizontal_connection_right=3,
                    top_horizontal_tile_start=corner_3, top_horizontal_tile_end=horizontal_3, vertical_tile_middle=dc(na), vertical_tile_start=horizontal_3, vertical_tile_end=dc(na),
                    top_horizontal_connection=3, 
                    bottom_tile_normal=horizontal_twin, top_tile_normal=vertical_3, normal_connection=3)
            case "m":
                double_tiles(top_tile_horizontal_left=u_shape_1, top_tile_horizontal_right=u_shape_1, bottom_top_connection_left=2, bottom_top_connection_right=2,
                    bottom_horizontal_left_tile_middle=dc(na), bottom_horizontal_left_tile_start=vertical_2, bottom_horizontal_left_tile_end=dc(na), bottom_horizontal_connection_left=None,
                    bottom_horizontal_right_tile_middle=dc(na), bottom_horizontal_right_tile_start=vertical_2, bottom_horizontal_right_tile_end=dc(na), bottom_horizontal_connection_right=None,
                    top_horizontal_tile_start=corner_4, top_horizontal_tile_end=corner_1, vertical_tile_middle=vertical_2, vertical_tile_start=vertical_2, vertical_tile_end=vertical_2, 
                    top_horizontal_connection=1, vertical_connection=2, horizontal_vertical_connection=2, 
                    bottom_tile_normal=vertical_2, top_tile_normal=u_shape_1, normal_connection=2)
            case "q":
                double_tiles(top_tile_horizontal_left=vertical_2, top_tile_horizontal_right=vertical_2, bottom_top_connection_left=2, bottom_top_connection_right=2,
                    bottom_horizontal_left_tile_middle=horizontal_3, bottom_horizontal_left_tile_start=corner_3, bottom_horizontal_left_tile_end=corner_2, bottom_horizontal_connection_left=3,
                    bottom_horizontal_right_tile_middle=horizontal_3, bottom_horizontal_right_tile_start=corner_2, bottom_horizontal_right_tile_end=corner_3, bottom_horizontal_connection_right=3,
                    top_horizontal_tile_start=horizontal_3, top_horizontal_tile_end=horizontal_3, vertical_tile_middle=vertical_twin, vertical_tile_start=u_shape_2, vertical_tile_end=vertical_twin, 
                    top_horizontal_connection=3, vertical_connection=4, horizontal_vertical_connection=2,
                    bottom_tile_normal=u_shape_2, top_tile_normal=vertical_2, normal_connection=2)
            case "w":
                double_tiles(top_tile_horizontal_left=horizontal_3, top_tile_horizontal_right=horizontal_3,
                    bottom_horizontal_left_tile_middle=horizontal_1, bottom_horizontal_left_tile_start=corner_4, bottom_horizontal_left_tile_end=corner_1, bottom_horizontal_connection_left=1,
                    bottom_horizontal_right_tile_middle=horizontal_1, bottom_horizontal_right_tile_start=corner_1, bottom_horizontal_right_tile_end=corner_4, bottom_horizontal_connection_right=1,
                    top_horizontal_tile_start=horizontal_3, top_horizontal_tile_end=horizontal_3, vertical_tile_middle=vertical_twin, vertical_tile_start=vertical_twin, vertical_tile_end=u_shape_1, 
                    top_horizontal_connection=3, vertical_connection=4, 
                    bottom_tile_normal=vertical_twin, top_tile_normal=horizontal_twin, normal_connection=4)
            case "y":
                double_tiles(top_tile_horizontal_left=u_shape_1, top_tile_horizontal_right=u_shape_1, bottom_top_connection_left=4, bottom_top_connection_right=4,
                    bottom_horizontal_left_tile_middle=horizontal_3, bottom_horizontal_left_tile_start=Y1, bottom_horizontal_left_tile_end=horizontal_3, bottom_horizontal_connection_left=3,
                    bottom_horizontal_right_tile_middle=horizontal_3, bottom_horizontal_right_tile_start=Y1, bottom_horizontal_right_tile_end=horizontal_3, bottom_horizontal_connection_right=3,
                    top_horizontal_tile_start=corner_4, top_horizontal_tile_end=corner_1, vertical_tile_middle=dc(na), vertical_tile_start=horizontal_3, vertical_tile_end=dc(na),
                    top_horizontal_connection=1, 
                    bottom_tile_normal=Y1, top_tile_normal=u_shape_1, normal_connection=4)
            case "h":
                double_tiles(top_tile_horizontal_left=H1, top_tile_horizontal_right=H1, bottom_top_connection_left=2, bottom_top_connection_right=2,
                    bottom_horizontal_left_tile_middle=horizontal_3, bottom_horizontal_left_tile_start=t_shape_3, bottom_horizontal_left_tile_end=horizontal_3, bottom_horizontal_connection_left=3,
                    bottom_horizontal_right_tile_middle=horizontal_3, bottom_horizontal_right_tile_start=t_shape_3, bottom_horizontal_right_tile_end=horizontal_3, bottom_horizontal_connection_right=3,
                    top_horizontal_tile_start=horizontal_1, top_horizontal_tile_end=H1, vertical_tile_middle=vertical_2, vertical_tile_start=t_shape_3, vertical_tile_end=vertical_2, 
                    top_horizontal_connection=1, vertical_connection=2, horizontal_vertical_connection=2, 
                    bottom_tile_normal=t_shape_3, top_tile_normal=H1, normal_connection=2)
            case "v":
                double_tiles(top_tile_horizontal_left=V1,  top_tile_horizontal_right=corner_1,  bottom_top_connection_left=4, bottom_top_connection_right=1,
                    bottom_horizontal_left_tile_middle=horizontal_3, bottom_horizontal_left_tile_start=V2, bottom_horizontal_left_tile_end=horizontal_3, bottom_horizontal_connection_left=3,
                    bottom_horizontal_right_tile_middle=horizontal_3, bottom_horizontal_right_tile_start=V4, bottom_horizontal_right_tile_end=corner_3, bottom_horizontal_connection_right=3,
                    top_horizontal_tile_start=horizontal_1, top_horizontal_tile_end=V1, vertical_tile_middle=vertical_3, vertical_tile_start=corner_3, vertical_tile_end=vertical_3, 
                    top_horizontal_connection=1, vertical_connection=3, horizontal_vertical_connection=3, 
                    bottom_tile_normal=V2, top_tile_normal=V1, normal_connection=4)
    After_Stretch()

    return Output_Word

def Reading_t(Word_vbound, input_str):
    Word_hbound = len(input_str)
    Output_Word = [[dc(na) for _ in range(Word_hbound)] for _ in range(Word_vbound)]
    Letter_index = -1
    Symbol_index = -1

    def pos_calc():
        nonlocal word_xpos, word_ypos
        word_xpos = Symbol_index
        word_ypos = 0

    def double_tiles(top_horizontal_tile_right=None, bottom_top_connection_right=None,
            bottom_horizontal_tile_right_middle=None, bottom_horizontal_tile_right_start=None, bottom_horizontal_tile_right_end=None, bottom_horizontal_connection_right=None,
            bottom_tile_normal=dc(na), top_tile_normal=dc(na), connection_normal=None):
        ''' Note for my future self:
            - Anything with "con" is a connection, connection between tiles of a double tile symbol.
            - Anything that has "con" takes int to affect the axis. Anything that isn't is a tile, they take a 2D array.
            - Sorry.
        '''
        nonlocal word_xpos, word_ypos, Symbol_index
        Output_Word[word_ypos][word_xpos] = dc(top_tile_normal)
        Output_Word[word_ypos+1][word_xpos] = dc(bottom_tile_normal)
        Output_Word[word_ypos+1][word_xpos][0][0] = 1
        Output_Word[word_ypos+1][word_xpos][0][0] = ["r", bottom_horizontal_connection_right, bottom_top_connection_right, dc(bottom_horizontal_tile_right_middle), dc(bottom_horizontal_tile_right_start), dc(bottom_horizontal_tile_right_end), dc(top_horizontal_tile_right)] # type: ignore
        up_connect(connection_normal, Output_Word, word_ypos+1, word_xpos)


    def After_Stretch():
        word_ypos = -1
        word_vbound_full = len(Output_Word)
        word_hbound_full = len(Output_Word[0])

        while word_ypos != word_vbound_full - 1:
            word_ypos += 1
            word_xpos = -1
            while word_xpos != word_hbound_full - 1:
                word_xpos += 1
                if (type(Output_Word[word_ypos][word_xpos][0][0]) == list) and word_xpos != word_hbound_full - 1:
                    indicator: list = Output_Word[word_ypos][word_xpos][0][0]  # type: ignore
                    stretched = False

                    # ["r", bothconr, bottopconr, dc(bothorir0), dc(bothorir1), dc(bothorir2), dc(tophorir)]
                    i = 1
                    while (Output_Word[word_ypos][word_xpos + i] == na) and (Output_Word[word_ypos-1][word_xpos + i] != na):
                        stretched = True
                        Output_Word[word_ypos][word_xpos + i] = indicator[3]
                        left_connect(indicator[1], Output_Word, word_ypos, word_xpos + i)
                        i += 1
                        if word_xpos + i == word_hbound_full:
                            break
                    i -= 1
                    if stretched == True: 
                        Output_Word[word_ypos][word_xpos] = indicator[4]
                        Output_Word[word_ypos][word_xpos + i] = indicator[5]
                        Output_Word[word_ypos-1][word_xpos] = indicator[6]
                        up_connect(indicator[2], Output_Word, word_ypos, word_xpos)
                        left_connect(indicator[1], Output_Word, word_ypos, word_xpos + i)
                Output_Word[word_ypos][word_xpos][0][0] = 0

    while Letter_index != Word_hbound-1:
        Letter_index += 1
        Symbol_index += 1

        word_xpos = 0
        word_ypos = 0
        pos_calc()
        match input_str[Letter_index]:
            case "r":
                Output_Word[word_ypos][word_xpos] = dc(R)
            case "l":
                Output_Word[word_ypos][word_xpos] = dc(L)
            case "n":
                Output_Word[word_ypos][word_xpos] = dc(N)
            case "g":
                Output_Word[word_ypos][word_xpos] = dc(G)
            case "e":
                Output_Word[word_ypos][word_xpos] = dc(E)
            case "o":
                Output_Word[word_ypos][word_xpos] = dc(O)
            case "c":
                Output_Word[word_ypos][word_xpos] = dc(C)
            case "a":
                Output_Word[word_ypos][word_xpos] = dc(A)
            case "u":
                Output_Word[word_ypos][word_xpos] = dc(U)
            case "b":
                Output_Word[word_ypos][word_xpos] = dc(B)
            case "x":
                Output_Word[word_ypos][word_xpos] = dc(X)
            case "z":
                Output_Word[word_ypos][word_xpos] = dc(Z)
            case "i":
                Output_Word[word_ypos][word_xpos] = dc(I) 
            case "t":
                Output_Word[word_ypos][word_xpos] = dc(T) 
            case "d":
                Output_Word[word_ypos][word_xpos] = dc(D) 
            case "s":
                Output_Word[word_ypos][word_xpos] = dc(S) 
            
            case "j":
                double_tiles(top_horizontal_tile_right=horizontal_1,
                    bottom_horizontal_tile_right_middle=horizontal_1, bottom_horizontal_tile_right_start=corner_1, bottom_horizontal_tile_right_end=horizontal_1, bottom_horizontal_connection_right=1,
                    bottom_tile_normal=vertical_1, top_tile_normal=horizontal_twin, connection_normal=1)
            case "f":
                double_tiles(top_horizontal_tile_right=horizontal_3,
                    bottom_horizontal_tile_right_middle=horizontal_1, bottom_horizontal_tile_right_start=horizontal_1, bottom_horizontal_tile_right_end=corner_4, bottom_horizontal_connection_right=1,
                    bottom_tile_normal=vertical_3, top_tile_normal=horizontal_twin, connection_normal=3)
            case "p":
                double_tiles(top_horizontal_tile_right=vertical_1, bottom_top_connection_right=1,
                    bottom_horizontal_tile_right_middle=horizontal_twin, bottom_horizontal_tile_right_start=horizontal_twin, bottom_horizontal_tile_right_end=horizontal_twin, bottom_horizontal_connection_right=4,
                    bottom_tile_normal=horizontal_twin, top_tile_normal=vertical_1, connection_normal=1)
            case "k":
                double_tiles(top_horizontal_tile_right=vertical_3, bottom_top_connection_right=3,
                    bottom_horizontal_tile_right_middle=horizontal_3, bottom_horizontal_tile_right_start=horizontal_twin, bottom_horizontal_tile_right_end=horizontal_3, bottom_horizontal_connection_right=3,
                    bottom_tile_normal=horizontal_twin, top_tile_normal=vertical_3, connection_normal=3)
            case "m":
                double_tiles(top_horizontal_tile_right=u_shape_1, bottom_top_connection_right=2,
                    bottom_horizontal_tile_right_middle=dc(na), bottom_horizontal_tile_right_start=vertical_2, bottom_horizontal_tile_right_end=dc(na), bottom_horizontal_connection_right=None,
                    bottom_tile_normal=vertical_2, top_tile_normal=u_shape_1, connection_normal=2)
            case "q":
                double_tiles(top_horizontal_tile_right=vertical_2, bottom_top_connection_right=2,
                    bottom_horizontal_tile_right_middle=horizontal_3, bottom_horizontal_tile_right_start=corner_2, bottom_horizontal_tile_right_end=corner_3, bottom_horizontal_connection_right=3,
                    bottom_tile_normal=u_shape_2, top_tile_normal=vertical_2, connection_normal=2)
            case "w":
                double_tiles(top_horizontal_tile_right=horizontal_3,
                    bottom_horizontal_tile_right_middle=horizontal_1, bottom_horizontal_tile_right_start=corner_1, bottom_horizontal_tile_right_end=corner_4, bottom_horizontal_connection_right=1,
                    bottom_tile_normal=vertical_twin, top_tile_normal=horizontal_twin, connection_normal=4)
            case "y":
                double_tiles(top_horizontal_tile_right=u_shape_1, bottom_top_connection_right=4,
                    bottom_horizontal_tile_right_middle=horizontal_3, bottom_horizontal_tile_right_start=Y1, bottom_horizontal_tile_right_end=horizontal_3, bottom_horizontal_connection_right=3,
                    bottom_tile_normal=Y1, top_tile_normal=u_shape_1, connection_normal=4)
            case "h":
                double_tiles(top_horizontal_tile_right=H1, bottom_top_connection_right=2,
                    bottom_horizontal_tile_right_middle=horizontal_3, bottom_horizontal_tile_right_start=t_shape_3, bottom_horizontal_tile_right_end=horizontal_3, bottom_horizontal_connection_right=3,
                    bottom_tile_normal=t_shape_3, top_tile_normal=H1, connection_normal=2)
            case "v":
                double_tiles(top_horizontal_tile_right=corner_1, bottom_top_connection_right=1,
                    bottom_horizontal_tile_right_middle=horizontal_3, bottom_horizontal_tile_right_start=V4, bottom_horizontal_tile_right_end=corner_3, bottom_horizontal_connection_right=3,
                    bottom_tile_normal=V2, top_tile_normal=V1, connection_normal=4)
    After_Stretch()
    return Output_Word




def up_connect (connection, input_list, ypos, xpos, value=1):
    if connection != None and connection != 4:
        input_list[ypos][xpos][0][connection] = value
    if connection == 4:
        input_list[ypos][xpos][0][1] = value
        input_list[ypos][xpos][0][3] = value

def left_connect (connection, input_list, ypos, xpos, value=1):
    if connection != None and connection != 4:
        input_list[ypos][xpos][connection][0] = value
    if connection == 4:
        input_list[ypos][xpos][1][0] = value
        input_list[ypos][xpos][3][0] = value


def tile_trim(input_list):

    all_na = True
    while True:
        for tile_ypos in input_list:
            if tile_ypos[0] != na:
                all_na = False
                break 
        if all_na == False:
            break
        for tile_ypos in input_list:
            del tile_ypos[0]

    all_na = True
    while True:
        for tile_ypos in input_list:
            if tile_ypos[-1] != na:
                all_na = False
                break 
        if all_na == False:
            break
        for tile_ypos in input_list:
            del tile_ypos[-1]
    
    all_na = True
    while True:
        for tile_xpos in input_list[0]:
            if tile_xpos != na:
                all_na = False
                break 
        if all_na == False:
            break
        del input_list[0]
    
    all_na = True
    while True:
        for tile_xpos in input_list[-1]:
            if tile_xpos != na:
                all_na = False
                break 
        if all_na == False:
            break
        del input_list[-1]

    return input_list



def d_transpose(input_list):
    d4_length = len(input_list)
    d3_length = len(input_list[0])
    d2_length = len(input_list[0][0])
    d1_length = len(input_list[0][0][0])

    output_list = [[] for _ in range(d4_length * d2_length)]
    d4 = -1 
    while d4 < d4_length - 1:
        d4 += 1
        d2 = -1
        while d2 < d2_length - 1:
            d2 += 1
            d3 = -1
            while d3 < d3_length - 1:
                d3 += 1
                d1 = -1
                while d1 < d1_length - 1:
                    d1 += 1
                    output_list[d4 * d2_length + d2].append(input_list[d4][d3][d2][d1])

    # Trimming it down
    for _ in range(3):
        del output_list[0]
    for _ in range(2):
        del output_list[-1]
    for ypos in range(len(output_list)):
        for _ in range(3):
            del output_list[ypos][0]
        for _ in range(2):
            del output_list[ypos][-1]

    
    return output_list   


def hex_check(input_str):
    if input_str[0] == "#":
        input_str = input_str[1:]
    return bytes.fromhex(input_str)[::-1]




def bmp_convert(input_list, filename, text_color, border_color, background_color):
    text_color = hex_check(text_color)
    border_color = hex_check(border_color)
    background_color = hex_check(background_color)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, filename + ".bmp")
    height = len(input_list)
    width = len(input_list[0])

    row_bytes = width * 3 
    padding = (4 - (row_bytes % 4)) % 4
    pixel_data_size = (row_bytes + padding) * height
    
    file_size = 54 + pixel_data_size 

    with open(filename, 'wb') as f:
        f.write(struct.pack('<2sIHHI', b'BM', file_size, 0, 0, 54))
        
        f.write(struct.pack('<IiiHHIIIIII', 40, width, -height, 1, 24, 0, pixel_data_size, 0, 0, 0, 0))
        
        for row in input_list:
            for pixel in row:
                if pixel == 1:
                    color = text_color
                elif pixel == 0:
                    color = background_color
                elif pixel == 2:
                    color = border_color
                else:
                    color = background_color

                f.write(color)
                
            f.write(b'\x00' * padding)
            
    print("Saved Successfuly")



Full_Translate()

# Call the following function multiple time if you need multipple exports

# Full_Translate (

#         insert_text = '''Paste Text Here''',

#         filename         = "TDS_TranslatedText_2",

#         feel free to delete the styles under if you want to keep the same style throughout all your copies.

#         border_style     = "None",  # accept value "None" or "Tiles"

#         text_color       = "#ffffff",
#         border_color     = "#888888",
#         background_color = "#000000"   
# )







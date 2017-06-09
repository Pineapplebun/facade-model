import os
import math

idx = 5

cmd = ''

part1_cmd = ' th neuralstyle_seg.lua -content_image examples/input/in'+str(idx)+'.png -style_image examples/style/tar'+str(idx)+'.png -content_seg examples/segmentation/in'+str(idx)+'.png -style_seg examples/segmentation/tar'+str(idx)+'.png -index '+str(idx)+' -num_iterations 1000 -save_iter 100 -print_iter 1 -gpu 0 -serial examples/tmp_results -backend cudnn -cudnn_autotune'

part2_cmd = ' th deepmatting_seg.lua -content_image examples/input/in'+str(idx)+'.png -style_image examples/style/tar'+str(idx)+'.png -init_image examples/tmp_results/out'+str(idx)+'\_t_1000.png -content_seg examples/segmentation/in'+str(idx)+'.png -style_seg examples/segmentation/tar'+str(idx)+'.png -index '+str(idx)+' -num_iterations 1000 -save_iter 100 -print_iter 1 -gpu 0 -serial examples/final_results -f_radius 15 -f_edge 0.01 -backend cudnn -cudnn_autotune'

cmd = cmd + part1_cmd

cmd = cmd[1:len(cmd)-1]
print(cmd)
os.system(cmd)


# th neuralstyle_seg.lua -content_image examples/input/in5.png -style_image examples/style/tar5.png -content_seg examples/segmentation/in5.png -style_seg examples/segmentation/tar5.png -index 5 -num_iterations 1000 -save_iter 100 -print_iter 1 -gpu 0 -serial examples/tmp_results -backend cudnn -cudnn_autotune

# th deepmatting_seg.lua -content_image examples/input/in5.png -style_image examples/style/tar5.png -init_image examples/tmp_results/out5_t_1000.png -content_seg examples/segmentation/in5.png -style_seg examples/segmentation/tar5.png -index 5 -num_iterations 1000 -save_iter 100 -print_iter 1 -gpu 0 -serial examples/final_results -f_radius 15 -f_edge 0.01 -backend cudnn -cudnn_autotune

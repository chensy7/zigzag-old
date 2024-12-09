workload = {
32:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 16, 'G': 1, 'OX': 320, 'OY': 80, 'OZ': 16, 'C': 16, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 320, 'IY': 80, 'IZ': 16}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
33:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 96, 'G': 1, 'OX': 160, 'OY': 40, 'OZ': 8, 'C': 16, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 320, 'IY': 80, 'IZ': 16}, 'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy', 'iz=2*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
34:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 96, 'G': 1, 'OX': 160, 'OY': 40, 'OZ': 8, 'C': 96, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 160, 'IY': 40, 'IZ': 8}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
35:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 96, 'G': 1, 'OX': 160, 'OY': 40, 'OZ': 8, 'C': 96, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 160, 'IY': 40, 'IZ': 8}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
36:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 96, 'G': 1, 'OX': 160, 'OY': 40, 'OZ': 8, 'C': 96, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 160, 'IY': 40, 'IZ': 8}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
37:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 96, 'G': 1, 'OX': 160, 'OY': 40, 'OZ': 8, 'C': 96, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 160, 'IY': 40, 'IZ': 8}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
38:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 96, 'G': 1, 'OX': 160, 'OY': 40, 'OZ': 8, 'C': 96, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 160, 'IY': 40, 'IZ': 8}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
39:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 96, 'G': 1, 'OX': 160, 'OY': 40, 'OZ': 8, 'C': 96, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 160, 'IY': 40, 'IZ': 8}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
40:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 192, 'G': 1, 'OX': 80, 'OY': 20, 'OZ': 4, 'C': 96, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 160, 'IY': 40, 'IZ': 8}, 'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy', 'iz=2*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
41:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 192, 'G': 1, 'OX': 80, 'OY': 20, 'OZ': 4, 'C': 192, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 80, 'IY': 20, 'IZ': 4}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
42:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 192, 'G': 1, 'OX': 80, 'OY': 20, 'OZ': 4, 'C': 192, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 80, 'IY': 20, 'IZ': 4}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
43:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 192, 'G': 1, 'OX': 80, 'OY': 20, 'OZ': 4, 'C': 192, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 80, 'IY': 20, 'IZ': 4}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
44:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 192, 'G': 1, 'OX': 80, 'OY': 20, 'OZ': 4, 'C': 192, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 80, 'IY': 20, 'IZ': 4}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
45:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 192, 'G': 1, 'OX': 80, 'OY': 20, 'OZ': 4, 'C': 192, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 80, 'IY': 20, 'IZ': 4}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
46:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 192, 'G': 1, 'OX': 80, 'OY': 20, 'OZ': 4, 'C': 192, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 80, 'IY': 20, 'IZ': 4}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
47:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 384, 'G': 1, 'OX': 40, 'OY': 10, 'OZ': 2, 'C': 192, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 80, 'IY': 20, 'IZ': 4}, 'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy', 'iz=2*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
48:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 384, 'G': 1, 'OX': 40, 'OY': 10, 'OZ': 2, 'C': 384, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 40, 'IY': 10, 'IZ': 2}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
49:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 384, 'G': 1, 'OX': 40, 'OY': 10, 'OZ': 2, 'C': 384, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 40, 'IY': 10, 'IZ': 2}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
50:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 384, 'G': 1, 'OX': 40, 'OY': 10, 'OZ': 2, 'C': 384, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 40, 'IY': 10, 'IZ': 2}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
51:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 384, 'G': 1, 'OX': 40, 'OY': 10, 'OZ': 2, 'C': 384, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 40, 'IY': 10, 'IZ': 2}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
52:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 384, 'G': 1, 'OX': 40, 'OY': 10, 'OZ': 2, 'C': 384, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 40, 'IY': 10, 'IZ': 2}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
53:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 384, 'G': 1, 'OX': 40, 'OY': 10, 'OZ': 2, 'C': 384, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 40, 'IY': 10, 'IZ': 2}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
54:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 192, 'G': 1, 'OX': 80, 'OY': 20, 'OZ': 4, 'C': 384, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 80, 'IY': 20, 'IZ': 4}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
55:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 96, 'G': 1, 'OX': 160, 'OY': 40, 'OZ': 8, 'C': 192, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 160, 'IY': 40, 'IZ': 8}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
56:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 16, 'G': 1, 'OX': 320, 'OY': 80, 'OZ': 16, 'C': 96, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 320, 'IY': 80, 'IZ': 16}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
57:{'operator_type': 'Conv3d', 'equation': 'O[b][g][k][oz][oy][ox]+=W[g][k][c][fz][fy][fx]*I[b][g][c][iz][iy][ix]', 'loop_dim_size': {'B': 1, 'K': 1, 'G': 1, 'OX': 320, 'OY': 80, 'OZ': 16, 'C': 16, 'FX': 3, 'FY': 3, 'FZ': 3}, 'pr_loop_dim_size': {'IX': 320, 'IY': 80, 'IZ': 16}, 'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy', 'iz=1*oz+1*fz'], 'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8}, 'constant_operands': ['W'], 'padding': {'IZ': (1, 1, 1), 'IY': (1, 1, 1), 'IX': (1, 1, 1)}},
}
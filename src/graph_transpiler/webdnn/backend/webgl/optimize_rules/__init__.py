from webdnn.backend.webgl.optimize_rules import fix_sgemm_texture_shape
from webdnn.backend.webgl.optimize_rules import insert_transpose
from webdnn.backend.webgl.optimize_rules import optimize_channel_mode
from webdnn.backend.webgl.optimize_rules import replace_convolution_by_im2col
from webdnn.backend.webgl.optimize_rules import replace_linear_by_sgemm
from webdnn.backend.webgl.optimize_rules import webgl_optimize_rule

from graph_builder.backend.webgpu.optimize_rules.adjust_conv_weight_data_order import AdjustConvWeightDataOrder
from graph_builder.backend.webgpu.optimize_rules.conv_scale import ConvScale
from graph_builder.backend.webgpu.optimize_rules.replace_convolution_by_im2col import ReplaceConvolutionByIm2Col
from graph_builder.backend.webgpu.optimize_rules.sgemm_bias_relu import SgemmBiasRelu
from graph_builder.optimizer.optimizer import Optimizer


class WebGPUOptimizer(Optimizer):
    def __init__(self):
        super(WebGPUOptimizer, self).__init__()

        self.register_rule(ConvScale())
        self.register_rule(ReplaceConvolutionByIm2Col())
        self.register_rule(AdjustConvWeightDataOrder())
        self.register_rule(SgemmBiasRelu())

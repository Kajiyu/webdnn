from typing import Tuple

from webdnn.graph import traverse
from webdnn.graph.axis import Axis
from webdnn.graph.graph import Graph
from webdnn.graph.operators.linear import Linear
from webdnn.graph.operators.sgemm import Sgemm
from webdnn.graph.optimize_rule import OptimizeRule
from webdnn.graph.order import OrderNHWC, OrderHWCN, OrderNC, OrderCN


class ReplaceLinearBySgemm(OptimizeRule):
    """
    Replace Linear by Sgemm
    """

    def optimize(self, graph: Graph) -> Tuple[Graph, bool]:
        flag_changed = False
        for op in traverse.filter_nodes(traverse.listup_operators(graph), Linear):  # type: Linear
            x = op.inputs["x"]
            w = op.inputs["w"]
            y = op.outputs["y"]
            assert x.order == OrderNC or x.order == OrderNHWC, f"(x.order) = {x.order}"
            assert w.order == OrderCN or w.order == OrderHWCN, f"(x.order) = {w.order}"
            assert y.order == OrderNC or y.order == OrderNHWC, f"(x.order) = {y.order}"
            assert w.ndim == x.ndim

            flag_changed = True
            op.remove_all()

            sgemm = Sgemm(None,
                          M=y.shape_dict[Axis.N],
                          N=y.size // y.shape_dict[Axis.N],
                          K=x.size // x.shape_dict[Axis.N],
                          out_shape=y.shape,
                          out_order=y.order,
                          transpose_A=True,
                          transpose_B=True)
            new_y, = sgemm(x, w)

            sgemm.replace_output(new_y, y)

        return graph, flag_changed

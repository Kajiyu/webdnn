from webdnn.graph.axis import Axis
from webdnn.graph.operators.max import Max
from webdnn.graph.order import OrderNHWC, Order
from webdnn.graph.variable import Variable


def test():
    x = Variable([2, 3, 4, 5], OrderNHWC)
    y, = Max(None, axis=Axis.C)(x)

    assert y.order == Order([Axis.N, Axis.H, Axis.W])
    assert y.shape == [2, 3, 4]

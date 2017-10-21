import numpy as np
from prml.autograd.tensor.constant import Constant
from prml.autograd.tensor.tensor import Tensor
from prml.autograd.function import Function


class Exp(Function):

    def forward(self, x):
        x = self._convert2tensor(x)
        self.x = x
        self.output = np.exp(x.value)
        if isinstance(self.x, Constant):
            return Constant(self.output)
        return Tensor(self.output, function=self)

    def backward(self, delta):
        dx = self.output * delta
        self.x.backward(dx)


def exp(x):
    """
    element-wise exponential function
    """
    return Exp().forward(x)

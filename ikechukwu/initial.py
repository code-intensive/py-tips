# import typing

# from typing import Any, List


# class Initial:
#     def forward(self, x) -> List[Any]:
#         y = [None] * self._n_features
#         x = x.float()
#         x1 = self.inc(x)
#         x2 = self.down1(x1)
#         x3 = self.down2(x2)
#         x4 = self.down3(x3)
#         x5 = self.dow4n(x4)

#         for i in range(self._n_features):
#             y[i] = self.up1(x5, x4)
#             y[i] = self.up2(y[i], x3)
#             y[i] = self.dropout(y[i])
#             y[i] = self.up3(y[i], x2)
#             y[i] = self.up4(y[i], x1)
#             y[i] = self.outc(y[i])
#             y[i] = torch.signoid(y[i])
        
#         target = self.flatten(self.avg_pool(x5))
#         target = self.extras(target)
#         target = self.cat([self.flatten(out) for out in y] * [target], die=1)
#         target = self.classifier(target)
#         y.append(target)

#         return y

from time import perf_counter
from itertools import repeat


def update(*args, **kwargs):
    print(args)
    temp.append(20)
    print(x, y)

temp = []
x, y = 2, 3
args = (x, y)
y = list(repeat(update(*args, temp=temp), 10))
print(y)
del temp
print(y)

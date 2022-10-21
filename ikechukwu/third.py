from typing import Any, List
from itertools import repeat


class Initial:
    # Y should be given a human understandable name
    def generate_unit_y(self, *, temp, x1, x2, x3, x4, x5) -> Any:
        temp[self.y_index] = self.up1(x5, x4)
        temp[self.y_index] = self.up2(temp[self.y_index], x3)
        temp[self.y_index] = self.dropout(temp[self.y_index])
        temp[self.y_index] = self.up3(temp[self.y_index], x2)
        temp[self.y_index] = self.up4(temp[self.y_index], x1)
        temp[self.y_index] = self.outc(temp[self.y_index])
        temp[self.y_index] = torch.signoid(temp[self.y_index])
        self.y_index += 1
        return temp

    def forward(self) -> List[Any]:
        x = x.float()
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.dow4n(x4)

        n_features_count = len(self._n_features)
        temp = repeat(None, n_features_count)
        args = (temp, x, x1, x2, x3, x4, x5)

        setattr(self, 'y_index', 0)
        y = repeat(
            generate_unit_y(temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5),
            n_features_count
        )
        del temp
        delattr(self, 'y_index')

        target = self.flatten(self.avg_pool(x5))
        target = self.extras(target)
        target = self.cat([self.flatten(out) for out in y] * [target], die=1)
        target = self.classifier(target)
        y.append(target)

        return y

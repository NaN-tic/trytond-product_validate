# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.modules.product.product import STATES, DEPENDS

__all__ = ['Template', 'InvoiceLine', 'SaleLine', 'PurchaseLine']


class Template:
    __name__ = 'product.template'
    __metaclass__ = PoolMeta

    validated = fields.Boolean('Validated', states=STATES, depends=DEPENDS)


class ProductValidatedMixin:
    __metaclass__ = PoolMeta

    @classmethod
    def __setup__(cls):
        super(ProductValidatedMixin, cls).__setup__()
        cls.product.domain.append(('template.validated', '=', True))


class InvoiceLine(ProductValidatedMixin):
    __name__ = 'account.invoice.line'
    __metaclass__ = PoolMeta


class SaleLine(ProductValidatedMixin):
    __name__ = 'sale.line'
    __metaclass__ = PoolMeta


class PurchaseLine(ProductValidatedMixin):
    __name__ = 'purchase.line'
    __metaclass__ = PoolMeta

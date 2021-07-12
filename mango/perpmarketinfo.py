# # ⚠ Warning
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# [🥭 Mango Markets](https://mango.markets/) support is available at:
#   [Docs](https://docs.mango.markets/)
#   [Discord](https://discord.gg/67jySBhxrg)
#   [Twitter](https://twitter.com/mangomarkets)
#   [Github](https://github.com/blockworks-foundation)
#   [Email](mailto:hello@blockworks.foundation)

import typing

from decimal import Decimal
from solana.publickey import PublicKey

from .layouts import layouts


# # 🥭 PerpMarketInfo class
#


class PerpMarketInfo():
    def __init__(self, address: PublicKey, maint_asset_weight: Decimal, init_asset_weight: Decimal, maint_liab_weight: Decimal, init_liab_weight: Decimal, liquidation_fee: Decimal, base_lot_size: Decimal, quote_lot_size: Decimal):
        self.address: PublicKey = address
        self.maint_asset_weight: Decimal = maint_asset_weight
        self.init_asset_weight: Decimal = init_asset_weight
        self.maint_liab_weight: Decimal = maint_liab_weight
        self.init_liab_weight: Decimal = init_liab_weight
        self.liquidation_fee: Decimal = liquidation_fee
        self.base_lot_size: Decimal = base_lot_size
        self.quote_lot_size: Decimal = quote_lot_size

    def from_layout(layout: layouts.PERP_MARKET_INFO) -> "PerpMarketInfo":
        return PerpMarketInfo(layout.perp_market, layout.maint_asset_weight, layout.init_asset_weight, layout.maint_liab_weight, layout.init_liab_weight, layout.liquidation_fee, layout.base_lot_size, layout.quote_lot_size)

    def from_layout_or_none(layout: layouts.PERP_MARKET_INFO) -> typing.Optional["PerpMarketInfo"]:
        if layout.perp_market is None:
            return None

        return PerpMarketInfo.from_layout(layout)

    def __str__(self):
        return f"""« 𝙿𝚎𝚛𝚙𝙼𝚊𝚛𝚔𝚎𝚝𝙸𝚗𝚏𝚘 [{self.address}]
    Asset Weights: {self.init_asset_weight} / {self.maint_asset_weight}
    Liability Weights: {self.init_liab_weight} / {self.maint_liab_weight}
    Liquidation Fee: {self.liquidation_fee}
    Base Lot Size: {self.base_lot_size}
    Quote Lot Size: {self.quote_lot_size}
»"""

    @staticmethod
    def find_by_address(values: typing.Sequence[typing.Optional["PerpMarketInfo"]], address: PublicKey) -> "PerpMarketInfo":
        found = [value for value in values if value is not None and value.address == address]
        if len(found) == 0:
            raise Exception(f"PerpMarketInfo '{address}' not found in values: {values}")

        if len(found) > 1:
            raise Exception(f"PerpMarketInfo '{address}' matched multiple objects in values: {values}")

        return found[0]

    def __repr__(self) -> str:
        return f"{self}"

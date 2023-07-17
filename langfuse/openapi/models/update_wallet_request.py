import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWalletRequest")

@attr.s(auto_attribs=True)
class UpdateWalletRequest:
    """
    Attributes:
        wallet_id (str):
        user_id (Union[Unset, str]):
        balance (Union[Unset, float]):
    """

    wallet_id: str
    user_id: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wallet_id = self.wallet_id
        user_id = self.user_id
        balance = self.balance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "walletId": wallet_id,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if balance is not UNSET:
            field_dict["balance"] = balance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wallet_id = d.pop("walletId")

        user_id = d.pop("userId", UNSET)

        balance = d.pop("balance", UNSET)

        update_wallet_request = cls(
            wallet_id=wallet_id,
            user_id=user_id,
            balance=balance,
        )

        update_wallet_request.additional_properties = d
        return update_wallet_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

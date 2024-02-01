import operator
from unittest.mock import AsyncMock

import pytest
from aiogram.types import TelegramObject

from aiogram_dialog.widgets.kbd import Radio
from aiogram_dialog.widgets.text import Format


@pytest.mark.asyncio
async def test_check_radio(mock_manager) -> None:
    radio = Radio(
        Format("🔘 {item[1]}"),
        Format("⚪️ {item[1]}"),
        id="fruit",
        item_id_getter=operator.itemgetter(0),
        items=[("1", "Apple"), ("2", "Banana"), ("3", "Orange")],
    )

    current_checked_fruit = radio.get_checked(mock_manager)
    assert current_checked_fruit is None

    await radio.set_checked(TelegramObject(), "2", mock_manager)

    assert radio.is_checked("2", mock_manager)


@pytest.mark.asyncio
async def test_on_state_changed_radio(mock_manager) -> None:
    on_state_changed = AsyncMock()
    radio = Radio(
        Format("🔘 {item[1]}"),
        Format("⚪️ {item[1]}"),
        id="fruit",
        item_id_getter=operator.itemgetter(0),
        items=[("1", "Apple"), ("2", "Banana"), ("3", "Orange")],
        on_state_changed=on_state_changed,
    )

    await radio.set_checked(TelegramObject(), "2", mock_manager)

    on_state_changed.assert_called_once()

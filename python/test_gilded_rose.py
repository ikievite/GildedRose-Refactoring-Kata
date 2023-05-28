

"""Test GildedRose"""


from gilded_rose import Item, GildedRose


def test_gilded_rose():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"

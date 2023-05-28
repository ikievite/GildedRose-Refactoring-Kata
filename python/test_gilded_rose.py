"""Test GildedRose"""


from gilded_rose import Item, GildedRose


def test_gilded_rose():
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=48),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=40),
        Item(name="Conjured Mana Cake", sell_in=0, quality=6),
        Item(name="Conjured Mana Cake", sell_in=-1, quality=0),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "+5 Dexterity Vest"
    assert items[0].sell_in == 9
    assert items[0].quality == 19
    assert items[1].name == "Aged Brie"
    assert items[1].sell_in == 1
    assert items[1].quality == 1
    assert items[2].name == "Sulfuras, Hand of Ragnaros"
    assert items[2].sell_in == 0
    assert items[2].quality == 80
    assert items[3].name == "Backstage passes to a TAFKAL80ETC concert"
    assert items[3].sell_in == 9
    assert items[3].quality == 50
    assert items[4].name == "Backstage passes to a TAFKAL80ETC concert"
    assert items[4].sell_in == 4
    assert items[4].quality == 50
    assert items[5].name == "Backstage passes to a TAFKAL80ETC concert"
    assert items[5].sell_in == 4
    assert items[5].quality == 43
    assert items[6].name == "Conjured Mana Cake"
    assert items[6].sell_in == -1
    assert items[6].quality == 4
    assert items[7].name == "Conjured Mana Cake"
    assert items[7].sell_in == -2
    assert items[7].quality == 0

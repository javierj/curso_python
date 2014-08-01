__author__ = 'Javier'

from gilded_rose import Item, GildedRose

@given('Product "{name}" with quality "{quality}" and sell days "{sell_days}"')
def step_impl(context, name, quality, sell_days):
    context.item = Item(name, int(sell_days), int(quality))

@when('Updating the quality of products')
def step_impl(context):
    gilded_rose = GildedRose([context.item])
    gilded_rose.update_quality()

@then('Expected a quality of "{expected_quality}"')
def step_impl(context, expected_quality):
    assert context.item.quality == int(expected_quality)

@then('Expected sells days "{expected_days}"')
def step_impl(context, expected_days):
    assert context.item.sell_in == int(expected_days)
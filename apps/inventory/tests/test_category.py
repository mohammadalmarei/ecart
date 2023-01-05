from apps.inventory.models import Category


def test_create_single_category(single_category):

    new_category = single_category
    get_category = Category.objects.all().first()

    assert new_category.id == get_category.id


def test_create_category_with_child(category_with_child):

    new_sub_category = category_with_child
    get_category = Category.objects.all().first()

    assert new_sub_category.id == get_category.children.first().id
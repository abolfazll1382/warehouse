from django.db import migrations


def create_default_groups(apps, schema_editor):
    """
    Seed the role Groups every permission class in the project relies on.

    HasGroupPermission / StrictModelPermissions / IsCEO all key off these
    exact Group names, so they must exist for any access control to work.
    """
    Group = apps.get_model("auth", "Group")

    groups = [
        "CEO",
        "Purchasing",
        "WarehouseStaff",
        "InventoryManager",
    ]

    for group_name in groups:
        Group.objects.get_or_create(name=group_name)


def remove_default_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(
        name__in=[
            "CEO",
            "Purchasing",
            "WarehouseStaff",
            "InventoryManager",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0002_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_default_groups,
            reverse_code=remove_default_groups,
        ),
    ]

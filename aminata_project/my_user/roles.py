from django.contrib.auth.models import Permission
from users.models import Role, CustomUser
from users.groups import Group
from django.contrib.auth.models import Group


admin_role = Role.objects.create(name="Admin")
supplier_role = Role.objects.create(name="Supplier")
farmer_role = Role.objects.create(name="Farmer")

admin_user, created = CustomUser.objects.get_or_create(username='admin_username')
if created:
    admin_user.set_password('adminpass')
    admin_user.save()

admin_group, _ = Group.objects.get_or_create(name='Admin')
admin_user.groups.add(admin_group)

permissions_to_add_to_admin = [
    Permission.objects.get(codename='add_customuser'),
    Permission.objects.get(codename='change_customuser'),
    Permission.objects.get(codename='delete_customuser'),
    Permission.objects.get(codename='delete_equipment'),  
    Permission.objects.get(codename='change_equipment'),  
    Permission.objects.get(codename='view_user'),
    Permission.objects.get(codename='change_user'),
    Permission.objects.get(codename='delete_user'),
    Permission.objects.get(codename='view_role'),
    Permission.objects.get(codename='add_role'),
    Permission.objects.get(codename='change_role'),
    Permission.objects.get(codename='delete_role'),
    Permission.objects.get(codename='view_permission'),
    Permission.objects.get(codename='add_permission'),
    Permission.objects.get(codename='change_permission'),
    Permission.objects.get(codename='delete_permission'),
    Permission.objects.get(codename='manage_settings'),
    Permission.objects.get(codename='view_logs'),
    Permission.objects.get(codename='perform_maintenance'),
    Permission.objects.get(codename='view_reports'),
    Permission.objects.get(codename='view_admin_dashboard'),
]

admin_role.permissions.add(*permissions_to_add_to_admin)

supplier_user, created = CustomUser.objects.get_or_create(username='supplier_username')
if created:
    supplier_user.set_password('supplierpass')
    supplier_user.save()

supplier_group, _ = Group.objects.get_or_create(name='Supplier')
supplier_user.groups.add(supplier_group)

permissions_to_add_to_supplier = [
    Permission.objects.get(codename='view_supplier_profile'),
    Permission.objects.get(codename='update_supplier_profile'),
    Permission.objects.get(codename='add_product'),
    Permission.objects.get(codename='view_product'),
    Permission.objects.get(codename='manage_product'),
    Permission.objects.get(codename='view_reports'), 
]

supplier_role.permissions.add(*permissions_to_add_to_supplier)

farmer_user, created = CustomUser.objects.get_or_create(username='farmer_username')
if created:
    farmer_user.set_password('farmerpass')
    farmer_user.save()

farmer_group, _ = Group.objects.get_or_create(name='Farmer')
farmer_user.groups.add(farmer_group)

permissions_to_add_to_farmer = [
    Permission.objects.get(codename='view_farmer_profile'),
    Permission.objects.get(codename='update_farmer_profile'),
    Permission.objects.get(codename='add_equipment'),  
    Permission.objects.get(codename='view_equipment'),  
    Permission.objects.get(codename='manage_equipment'),  
    Permission.objects.get(codename='view_reports'),  
]

farmer_role.permissions.add(*permissions_to_add_to_farmer)



ROLES_PERMISSIONS = {
    "Admin": ["add_customuser","change_customuser","delete_customuser","delete_equipment","change_equipment","view_user","change_user","delete_user","view_role","add_role","change_role","delete_role","view_permission","add_permission","change_permission","delete_permission","manage_settings","view_logs","perform_maintenance","view_reports","view_admin_dashboard",],
    "Farmer": ["view_farmer_profile","update_farmer_profile","add_equipment","view_equipment","manage_equipment",],
    "Supplier": ["view_supplier_profile","update_supplier_profile","add_product","view_product","manage_product",],
}

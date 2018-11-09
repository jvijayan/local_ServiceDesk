from django.db import models
from django.utils import timezone
from user_management.models import UserGroupPermission

# SystemModule
class SystemModule(models.Model):
    name = models.CharField(max_length=45)

    class Meta():
        db_table = 'system_module'


# SystemModuleHasUserGroupPermission
class SystemModuleHasUserGroupPermission(models.Model):
    system_module = models.ForeignKey(SystemModule, on_delete=models.DO_NOTHING)
    usergrouppermission = models.ForeignKey(UserGroupPermission, on_delete=models.DO_NOTHING)

    class Meta():
        db_table = 'system_module_has_user_group_permission'

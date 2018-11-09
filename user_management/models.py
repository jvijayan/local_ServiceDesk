from django.db import models
from django.contrib.auth.models import AbstractUser
from company_management.models import Company, Branch, Department
from django.utils import timezone

# UserGroup
class UserGroup(models.Model):
    name = models.CharField(max_length=45)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'user_group'
        
class UserCategory(models.Model):
    CATEGORY_CHOICES = (
        ('Self', 'Self'),
        ('Client', 'Client'),
        ('Vendor', 'Vendor'),
        ('Partner', 'Partner'),
    )
    category_value = models.CharField(
        max_length=8,
        choices=CATEGORY_CHOICES,
        default='Self',
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_value

    class Meta():
        db_table = 'user_category'

# User
class User(AbstractUser):
    category = models.ForeignKey(UserCategory, default=1, on_delete=models.DO_NOTHING)
    usergroup = models.ForeignKey(UserGroup, default=1, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, default=1, on_delete=models.DO_NOTHING)
    branch = models.ForeignKey(Branch, default=1, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, default=2 ,on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default='Male',
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta():
        db_table = 'user'

# UserTeam
class UserTeam(models.Model):
    name = models.CharField(max_length=100, default='TeamName')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'user_team'

# UserTeamMember
class UserTeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    user_team = models.ForeignKey(UserTeam, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    
    class Meta():
        db_table = 'user_team_member'

# UserPhoneContact
class UserPhoneContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    phone_contact = models.CharField(max_length=13)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_contact

    class Meta():
        db_table = 'user_phone_contact'

# UserEmailAddress
class UserEmailAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email_address = models.CharField(max_length=45)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'user_email_address'

# UserGroupPermission
class UserGroupPermission(models.Model):
    permission_name = models.CharField(max_length=45)
    VALUE_CHOICES = (
        ('True', 'True'),
        ('False', 'False'),
    )
    permission_value = models.CharField(
        max_length=6,
        choices=VALUE_CHOICES,
        default='False',
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'user_group_permission'

# UserGroupHasUserGroupPermission
class UserGroupHasUserGroupPermission(models.Model):
    usergroup = models.ForeignKey(UserGroup, on_delete=models.DO_NOTHING)
    usergrouppermission = models.ForeignKey(UserGroupPermission, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'user_group_has_user_group_permission'
from django.db import models
from company_management.models import Company
from user_management.models import User, UserTeam, UserTeamMember

class Project(models.Model):
    STATUS_CHOICES = (
        ('New','New'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Terminated', 'Terminated'),
    )
    project_status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default='New',
    )
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100, null=True,)
    thumbnail = models.CharField(max_length=100, null=True,)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    actual_startdate = models.DateField(null=True, blank=True)
    actual_enddate = models.DateField(null=True, blank=True)
    client = models.ForeignKey(Company, related_name='client', on_delete=models.DO_NOTHING)
    vendor = models.ForeignKey(Company, related_name='vendor', null=True, on_delete=models.DO_NOTHING)
    cost = models.FloatField(null=True, blank=True)
    finalcost = models.FloatField(null=True, blank=True)
    project_manager = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    project_team = models.ForeignKey(UserTeam, on_delete=models.DO_NOTHING)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'project'

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/projects/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

# ProjectAttachments
class ProjectAttachments(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=45)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'project_attachment'

# ProjectsHasCompany
class ProjectsHasCompany(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    class Meta():
        db_table = 'projects_has_companies'

class Milestone(models.Model):
    STATUS_CHOICES = (
        ('New','New'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Terminated', 'Terminated'),
    )
    status = models.CharField(
        max_length=6,
        choices=STATUS_CHOICES,
        default='New',
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'milestone'
        
# MilestoneAttachment
class MilestoneAttachment(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta():
        db_table = 'milestone_attachment'

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    milestone = models.ForeignKey(Milestone, on_delete=models.DO_NOTHING)
#     assignee = models.ForeignKey(UserTeamMember, on_delete=models.DO_NOTHING, blank=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Ongoing', 'Ongoing'),
        ('Closed', 'Closed'),
    )
    status = models.CharField(
        max_length=6,
        choices=STATUS_CHOICES,
        default='Open',
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    actual_start_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'task'

# TaskAttachment
class TaskAttachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    attachment_name = models.CharField(max_length=45, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'task_attachment'

# Incident
class Incident(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=True)
    milestone = models.ForeignKey(Milestone, on_delete=models.DO_NOTHING, blank=True)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING, blank=True)
#     reportedby = models.ForeignKey(UserTeamMember, on_delete=models.DO_NOTHING)
#     assignee = models.ForeignKey(UserTeamMember, on_delete=models.DO_NOTHING, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    resolution_time = models.DateTimeField(null=True, auto_now=True)
    reopen_time = models.DateTimeField(null=True, auto_now=True)
    close_time = models.DateTimeField(null=True, auto_now=True)
    PRIORITY_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default='High',
    )
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )
    status = models.CharField(
        max_length=6,
        choices=STATUS_CHOICES,
        default='Open',
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'incident'

# IncidentAttachment
class IncidentAttachment(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.DO_NOTHING)
    attachment_name = models.CharField(max_length=45)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'incident_attachment'

# IncidentComment
class IncidentComment(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'incident_comment'


# IncidentCommentAttachments
class IncidentCommentAttachments(models.Model):
    comment = models.ForeignKey(IncidentComment, on_delete=models.DO_NOTHING)
    attachment_name = models.CharField(max_length=45)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'incident_comment_attachment'


# IncidentCommentReply
class IncidentCommentReply(models.Model):
    comment = models.ForeignKey(IncidentComment, on_delete=models.DO_NOTHING)
    reply = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'incident_comment_reply'

# IncidentCommentReplyAttachment
class IncidentCommentReplyAttachment(models.Model):
    comment_reply = models.ForeignKey(IncidentCommentReply, on_delete=models.DO_NOTHING)
    attachment_name = models.CharField(max_length=45)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'incident_comment_reply_attachment'

# ProjectForum
class ProjectForum(models.Model):
    projects_project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    class Meta():
        db_table = 'project_forum'


# ProjectForumMessages
class ProjectForumMessages(models.Model):
    projectforum_project_forum_id = models.ForeignKey(ProjectForum, on_delete=models.DO_NOTHING)
    projectteammembers_project_team_member_id = models.ForeignKey(UserTeamMember, on_delete=models.DO_NOTHING)
    project_forum_message_date = models.DateField()
    project_forum_message_time = models.TimeField()

    class Meta():
        db_table = 'project_forum_messages'


# ProjectForumMessageAttachments
class ProjectForumMessageAttachments(models.Model):
    projectforummessages_project_forum_message_id = models.ForeignKey(ProjectForumMessages, on_delete=models.DO_NOTHING)
    project_forum_message_attachment = models.CharField(max_length=45)

    class Meta():
        db_table = 'project_forum_message_attachments'


# ProjectForumMessageReplies
class ProjectForumMessageReplies(models.Model):
    projectforummessages_project_forum_message_id = models.ForeignKey(ProjectForumMessages, on_delete=models.DO_NOTHING)
    projectteammembers_project_team_member_id = models.ForeignKey(UserTeamMember, on_delete=models.DO_NOTHING)
    project_forum_message_reply_details = models.CharField(max_length=200)
    project_forum_message_reply_date = models.DateField()
    project_forum_message_reply_time = models.TimeField()

    class Meta():
        db_table = 'project_forum_message_replies'


# ProjectForumMessageReplyAttachments
class ProjectForumMessageReplyAttachments(models.Model):
    projectforummessagereplies_project_forum_message_reply_id = models.ForeignKey(ProjectForumMessageReplies,
                                                                                  on_delete=models.DO_NOTHING)
    project_forum_message_reply_attachment = models.CharField(max_length=45)

    class Meta():
        db_table = 'project_forum_message_reply_attachments'

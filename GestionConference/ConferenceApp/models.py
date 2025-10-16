from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.
class conference(models.Model):
    conference_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    THEME=[
        ("IA","Computer science & IA"),
        ("SE","Science and eng"),
        ("SC","Social sciences"),
    ]
    theme=models.CharField(max_length=255 , choices=THEME)
   
    location=models.CharField(max_length=50)
    description=models.TextField(validators=[MaxLengthValidator(30,message="cette phrase doit etre composee par 30 lettre")])
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def clean(self):
        if self.start_date > self.end_date :
            raise  ValidationError("la date de debut est inferieur a la date fin")
    
class OrganizingCommittee(models.Model):
    dommitee_role=models.CharField(max_length=255,choices=[("chair","chair"),("co-chair","co-chair"),("member","member")])
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.user",on_delete=models.CASCADE,
                        related_name="OrganizingCommittes")
    conference=models.ForeignKey(conference,on_delete=models.CASCADE,
                                related_name="OrganizingCommitte")


class submission(models.Model):
    submission_id=models.CharField(max_length=255,primary_key=True,unique=True,)
    title=models.CharField(max_length=50)
    abstract=models.TextField()
    keywords=models.TextField()
    paper=models.FileField(upload_to="papers/")
    STATUS=[
        ("submitted","submitted"),
        ("under review","under review"),
        ("accepted","accepted"),
        ("rejected","rejected")
    ]

    status=models.CharField(max_length=50,choices=STATUS)
    payed=models.BooleanField(default=False)
    submission_date=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.user",on_delete=models.CASCADE,
                        related_name="submissions")
    conference=models.ForeignKey(conference,on_delete=models.CASCADE,
                                related_name="submissions")
    
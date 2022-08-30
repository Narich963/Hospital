from django.db import models
region = (
    ("1", "Bishkek"),
    ("2", "Osh city"),
    ("3", "Batken"),
    ("4", "Djalal-Abad"),
    ("5", "Naryn"),
    ("6", "Osh"),
    ("7", "Talas"),
    ("8", "Chui"),
    ("9", "IK")
)

type_hp = (
    ("1", "государственная"),
    ("2", "частная")
)

type_doctor = (
    ("1", "терапевт"),
    ("2", "хирург")
)

class Hospital(models.Model):
    okpo = models.IntegerField(unique=True)
    region = models.CharField(max_length=222, choices=region)
    employees = models.CharField(max_length=100)
    state_or_private = models.CharField(max_length=222, choices=type_hp)


    def __str__(self):
        return str(self.okpo)

class Patient(models.Model):
    full_name = models.CharField(max_length=222)
    pin_code = models.CharField(max_length=14)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.full_name


class Nurse(models.Model):
    full_name = models.CharField(max_length=222)
    pin_code = models.CharField(max_length=14)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=25)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

def nurse_choice():
    nurse = Nurse.objects.all()
    nm = 0
    n1 = 1
    for i in nurse:
        if n1 > i.id:
            nm = i.id
    return nm


class Doctor(models.Model):
    type_dr = models.CharField(max_length=222, choices=type_doctor)
    full_name = models.CharField(max_length=222)
    pin_code = models.CharField(max_length=14)
    age = models.IntegerField()
    experience = models.IntegerField()
    phone_number = models.CharField(max_length=25)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.OneToOneField(Nurse, on_delete=models.CASCADE, default=nurse_choice())

    def __str__(self):
        return self.type_dr

class Chief_Physician(models.Model):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=222)
    pin_code = models.CharField(max_length=14)
    age = models.IntegerField()
    experience = models.IntegerField()
    phone_number = models.CharField(max_length=25)
    nurse = models.OneToOneField(Nurse, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
















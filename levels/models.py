from django.db import models
from django.contrib.auth.models import User

class TreasureHunt(models.Model):
    LEVEL_CHOICES = [
        (1, 'level1'),
        (2, 'level2'),
        (3, 'level3'),
        (4, 'level4'),
        (5,'level5'),
        (6,'level6'),
        (7,'level7'),
        (8,'level8')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    answer = models.CharField(max_length=255)
    score = models.IntegerField(default=5)
    totscore = models.IntegerField(default = 5)

    def __str__(self):
        return f"{self.user.username} - {self.level}"
    

# class UserAnswer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     level1_answer = models.CharField(max_length=255)
#     level2_answer = models.CharField(max_length=255)
#     level3_answer = models.CharField(max_length=255)
#     level4_answer = models.CharField(max_length=255)
#     level5_answer = models.CharField(max_length=255)
#     level6_answer = models.CharField(max_length=255)
#     level7_answer = models.CharField(max_length=255)
#     level8_answer = models.CharField(max_length=255)

#     def __str__(self):
#         return self.user.username
    


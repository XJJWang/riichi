from django.db import models


class Game(models.Model):
    competitor1 = models.ForeignKey(
        'Competitor',
        on_delete=models.CASCADE,
    )
    competitor2 = models.ForeignKey(
        'Competitor',
        on_delete=models.CASCADE,
    )
    competitor3 = models.ForeignKey(
        'Competitor',
        on_delete=models.CASCADE,
    )
    competitor4 = models.ForeignKey(
        'Competitor',
        on_delete=models.CASCADE,
    )
    date = models.DateField(auto_now=True, auto_now_add=False)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    score3 = models.IntegerField()
    socre4 = models.IntegerField()
    ranking1 = models.PositiveSmallIntegerField()
    ranking2 = models.PositiveSmallIntegerField()
    ranking3 = models.PositiveSmallIntegerField()
    ranking4 = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.date, self.competitor


class Competitor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

from django.db import models


class Game(models.Model):
    RANKINGS = (
        ("first_place", "一位"),
        ("second_place", "二位"),
        ("third_place", "三位"),
        ("fourth_place", "四位"),
    )
    player1 = models.ForeignKey(
        "Player",
        on_delete=models.CASCADE,
        related_name="first_player",
        default="Unknown Player",
        verbose_name="一位",
    )
    player2 = models.ForeignKey(
        "Player",
        on_delete=models.CASCADE,
        related_name="second_player",
        default="Unknown Player",
        verbose_name="二位",
    )
    player3 = models.ForeignKey(
        "Player",
        on_delete=models.CASCADE,
        related_name="third_player",
        default="Unknown Player",
        verbose_name="三位",
    )
    player4 = models.ForeignKey(
        "Player",
        on_delete=models.CASCADE,
        related_name="fourth_player",
        default="Unknown Player",
        verbose_name="四位",
    )
    date = models.DateField(auto_now=False, auto_now_add=False)
    score1 = models.IntegerField(default=25000, verbose_name="一位分数")
    score2 = models.IntegerField(default=25000, verbose_name="二位分数")
    score3 = models.IntegerField(default=25000, verbose_name="三位分数")
    score4 = models.IntegerField(default=25000, verbose_name="四位分数")

    def view_players_scores(self):
        template_string = f"{self.player1} {self.score1} | {self.player2} {self.score2} | {self.player3} {self.score3} | {self.player4} {self.score4}"
        return template_string

    def __str__(self):
        return (
            self.player1.name
            + self.player2.name
            + self.player3.name
            + self.player4.name
        )

    class Meta:
        ordering = ["-date"]


class Player(models.Model):
    IS_ACTIVED = (
        ("True", "已激活"),
        ("False", "未激活"),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    is_actived = models.CharField(max_length=24, choices=IS_ACTIVED, default="未激活")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "玩家"
        verbose_name_plural = "玩家"

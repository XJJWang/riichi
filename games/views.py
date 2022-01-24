import numpy
import pandas

from django.http import HttpResponse

from .models import Game


def add_record(request):
    return HttpResponse('')


def score_to_point(records):
    players = set([record[0] for record in records])

    score_records = []
    for record in records:
        if record[2] == 'first_place':
            score_records.append((record[0], (record[1] - 10000) / 1000))
        elif record[2] == 'second_place':
            score_records.append((record[0], (record[1] - 20000) / 1000))
        elif record[2] == 'third_place':
            score_records.append((record[0], (record[1] - 30000) / 1000))
        elif record[2] == 'fourth_place':
            score_records.append((record[0], (record[1] - 40000) / 1000))
    players_total_score = []
    for player in players:
        # print(player)
        player_total_score = [player, 0, 0]
        for score_record in score_records:
            if score_record[0] == player:
                player_total_score[1] += score_record[1]
                player_total_score[2] += 1
        player_total_score.append(player_total_score[1] / player_total_score[2])
        players_total_score.append(player_total_score)
    players_total_score = numpy.array(players_total_score)
    players_total_score = pandas.DataFrame(players_total_score).sort_values(by=3).to_numpy()
    players_total_score = pandas.DataFrame(players_total_score)
    players_total_score.columns = ["name", "total_score", "sessions", "avg_score"]

    writer = pandas.ExcelWriter('hhh.xlsx')
    players_total_score.to_excel(writer, 'page_1')
    writer.save()

    print(players_total_score)
    # players_total_score = player_total_score[players_total_score[:,3].argsort()]
    # print(players_total_score)


def index(request):
    games = Game.objects.all()
    records = []
    for g in games:
        records.append((str(g.player1), g.score1, 'first_place'))
        records.append((str(g.player2), g.score2, 'second_place'))
        records.append((str(g.player3), g.score3, 'third_place'))
        records.append((str(g.player4), g.score4, 'fourth_place'))
    score_to_point(records)
    return HttpResponse('')


def login(request):
    return HttpResponse('')


def register(request):
    return HttpResponse('')


def logout(request):
    return HttpResponse('')

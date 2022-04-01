import numpy
import pandas

from django.shortcuts import render

from django.http import HttpResponse

from .models import Game


def add_record(request):
    return HttpResponse('')


def score_to_point(records):
    players = set([record[0] for record in records])

    score_records = []
    for record in records:
        if record[2] == 'first_place':
            score_records.append((record[0], (record[1] + 20000) / 1000))
        elif record[2] == 'second_place':
            score_records.append((record[0], (record[1] - 20000) / 1000))
        elif record[2] == 'third_place':
            score_records.append((record[0], (record[1] - 40000) / 1000))
        elif record[2] == 'fourth_place':
            score_records.append((record[0], (record[1] - 60000) / 1000))
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
    # players_total_score = pandas.DataFrame(players_total_score).sort_values(by=2).to_numpy()
    # players_total_score = pandas.DataFrame(players_total_score)
    # players_total_score.columns = ["name", "total_points", "sessions", "avg_point"]

    # writer = pandas.ExcelWriter('hhh.xlsx')
    # players_total_score.to_excel(writer, 'page_1')
    # writer.save()
    players_total_score = [[i[0], round(i[1], 1), i[2], round(i[3], 1)]
                           for i in players_total_score]
    players_total_score = sorted(players_total_score, key=lambda x: x[3], reverse=True)
    # players_total_score = pandas.DataFrame(players_total_score)
    # players_total_score.columns = ["name", "total_points", "sessions", "avg_points"]
    print(players_total_score)
    return players_total_score

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
    # players_total_score = pandas.DataFrame(score_to_point(records)).to_numpy()
    players_total_score = score_to_point(records)
    players_total_score.insert(0, ['name', 'total_points', 'session', 'avg_points'])
    context = {'players_total_points': players_total_score}
    return render(request, 'rankings.html',context)


def login(request):
    return HttpResponse('')


def register(request):
    return HttpResponse('')


def logout(request):
    return HttpResponse('')


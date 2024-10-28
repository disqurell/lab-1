# cspell:ignore датакласс Параметры входныеПараметры

from dataclasses import dataclass


def датакласс(cls):
    return dataclass(cls)


@датакласс
class ДиапазонПараметров:
    Tn: tuple | int
    To: tuple | int
    Tz: tuple | int
    Tk: tuple | int
    Ts: tuple | int
    Tp: tuple | int
    Tu: tuple | int
    Tv: tuple | int
    Rm: tuple | int
    Ti: tuple | int
    Ta: tuple | int
    Tc: tuple | int
    R: tuple | int


@датакласс
class Читатель:
    время_прихода: float
    тип: str  # Тип читателя: 'студент', 'аспирант', 'дипломник', 'заочник'


диапазон_параметров = ДиапазонПараметров(
    Tn=(2, 7.3),
    To=(5, 15),
    Tz=(1, 29),
    Tk=0,
    Ts=(5, 17),
    Tp=(3, 5),
    Tu=(3, 5),
    Tv=(0, 2.5),
    Rm=(13, 0),
    Ti=(4, 9),
    Ta=(1, 7),
    Tc=(6, 18),
    R=9,
)

# print(параметры)

# Ohjelmistotuotanto

## SyntetisaattoriApp

Sovelluksella käyttäjä voi tietokoneen näppäimistöllä soittaa erilaisia ääniaaltoja. Käyttäjä pystyy muokkaamaan ääniaaltoja erilaisin muuttujien avulla, sekä tallentamaan ääniaallon tietokoneelleen tiedostoksi. 

## Dokumentaatio 

[Vaatimusmäärittely](https://github.com/tykovas/ot-harjoitustyo/blob/master/synthesizerApp/documentation/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/tykovas/ot-harjoitustyo/blob/master/synthesizerApp/documentation/tuntikirjanpito.md)

[Changelog](https://github.com/tykovas/ot-harjoitustyo/blob/master/synthesizerApp/documentation/changelog.md)

[Arkkitehtuuri](https://github.com/tykovas/ot-harjoitustyo/blob/master/synthesizerApp/documentation/Arkkitehtuuri.md)

## Releases

Release 1 [viikko 5](https://github.com/tykovas/ot-harjoitustyo/releases/tag/viiko5)

Release 2 [viikko 6](https://github.com/tykovas/ot-harjoitustyo/releases/tag/viikko6)

## Python -versio

Sovellus on testattu ja todettu toimivaksi Python-versiolla 3.8. Uudemmilla tai vanhemmilla versioilla ohjelma ei välttämättä toimi halutulla tavalla. 

## Asennus 

1. Asenna tarvittavat riippuvuudet komennolla:

```bash
poetry install
```

## Käytössä olevat komennot:

### Suorittaminen:

Ohjelman voi suorittaa komenolla:

```bash
poetry run invoke start
```

### Testaus:

Ohjelman testit voi ajaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuusraportti:

Raportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint 

Pylint tarkastuksen voi suorittaa komennoll:

```bash
poetry run invoke lint
```





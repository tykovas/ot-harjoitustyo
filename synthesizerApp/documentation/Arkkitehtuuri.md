# Arkkitehtuurikuvaus

## Rakenne ja sovelluslogiikka

Ohjelman päätoiminnallisuus on sijoitettu kahteen hakemistoon: synthesizer ja gui. Synthesizer sisältää äänen tuottamisesta ja kontrolloinnista vastaavat luokat. Gui sisältää ohjelman käyttöliittymän. 

Ohjelman toimminnallisuudesta vastaan seuraavat luokat:

![Luokkakaavio](https://raw.githubusercontent.com/tykovas/ot-harjoitustyo/master/synthesizerApp/documentation/Untitled%20Diagram.drawio.png)

Main luokka käynnistää sovelluksen ja kutsuu gui luokkaa. Gui luokka käsittelee käyttäjän antaman inputin. Synthesizer luokka vastaa ohjelman päätoiminnallisuudesta ja kutsuu tarvittaessa Oscillator ja wavetofile luokkia.

## Päätoiminnallisuus

Äänentuotannon toiminnallisuutta siniaaltoa muodostaessa kuvaa seuraava sekvenssikaavio:

```mermaid
sequenceDiagram
    GUI->> Synthesizer: Play()
    Synthesizer->> Oscillator: Oscillator()
    Synthesizer->> Oscillator: Get_Sine()
    Oscillator-->> Synthesizer: SineGenerator
    






```

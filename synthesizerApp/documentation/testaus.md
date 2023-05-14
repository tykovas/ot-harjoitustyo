# Testausdokumentti

Ohjelmaa on testattu kehityksen aikana manuaalisesti, sekä unittest ykiskkötesteillä.

## Unittest 

Yksikkötestejä on käytetty lähinnä sovelluslogiikan testaamiseen. Testien alustuksessa muodostetaan Oscillator objekti, jota käytetään useammassa testissä. 

Testeillä testataan, että Oscillator:in metodit get_sine ja get_square eivät palauta tyhjää, eli generaattoriobjektien muodostaminen onnistuu. 

Lisäksi testaan, että Synthesizer objektin metodi generate_sound palauttaa arrayn, joka sisältää oikean tyyppistä (int16) dataa. 

Testeillä varmistetaan myös, että Oscillator:ille kun antaa parametrinä tietyn taajuuden, se myös vaikuttaa tapahtuviin laskuihin.

Testaamatta jäivät main ja wavetofile luokat, sillä main luokka vain käynnistää käyttöliittymän ja wavetofile tallentaa tiedoston. 

## Järjestelmätestaus

Manuaalisesti suoritetulla järjestelmätestauksella on varmistettu käyttöliittymän toimivuus, sekä kaikki äänen mouodostukseen liittyvä hienosäätö. Kaikki määrittelydokumentissa luetelluista toiminnallisuuksista on testattu. 
 
Manuaalisesti suoritetut testit on suoritettu sekä Windows- että Linux-käyttöjärjestelmillä. 

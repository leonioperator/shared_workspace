# Automatizáció heartbeat checklist céged számára

## Mit kapsz ezzel
Ez a checklist abban segít, hogy a kritikus automatizációid ne csendben álljanak le. 15 perc alatt végigmész rajta, és látni fogod, hol nincs még kontrollréteg a működésedben.

## Checklist

### 1. Szedd össze a 10 kritikus workflow-t
Írd ki egy listába azt a 10 automatizációt, aminek a leállása azonnal pénzt, időt vagy hibát okoz.
Példák:
- lead beérkezés
- ajánlat kiküldés
- számla kiállítás
- riport generálás
- follow-up üzenet

### 2. Mindegyikhez rendelj egy életjelet
Minden workflow végén legyen egy egyértelmű státuszjel.
Példák:
- sikeres futás után Telegram üzenet
- log bejegyzés időbélyeggel
- napi összesítőbe bekerülő státusz

### 3. Döntsd el, mi számít csendnek
Workflow-nként írd le, mennyi idő után baj, ha nincs jel.
Példák:
- lead sync: 30 perc
- számlázás: 2 óra
- napi riport: reggel 8:00-ig

### 4. Állíts be riasztási szabályt
Ha a workflow nem küld életjelet az elvárt időben, kapj azonnali figyelmeztetést.
Minimum legyen benne:
- melyik folyamat állt meg
- mióta nincs jel
- ki nézzen rá

### 5. Ne csak hibát, sikert is logolj
Ha csak a hibát látod, nincs viszonyítási alapod.
Minden kritikus folyamatnál legyen meg:
- utolsó sikeres futás ideje
- utolsó hiba ideje
- mai futások száma

### 6. Készíts napi health reportot
A nap elején vagy végén kapj egy rövid összesítőt:
- mi futott rendben
- mi késett
- mi hibázott
- hol kell emberi beavatkozás

### 7. Legyen egy felelős minden workflow-ra
Minden kritikus automatizáció mellett legyen név.
Ha gond van, ne az legyen a kérdés, hogy ki foglalkozik vele.

### 8. Teszteld le direkt hibával
Kapcsold ki egyszer szándékosan az egyik workflow-t.
Ha 5 percen belül nem kapsz egyértelmű riasztást, a rendszer még nincs kész.

## Következő lépés
Ha ezt te is be akarod állítani a cégedben -> vinczetamas.hu/audit

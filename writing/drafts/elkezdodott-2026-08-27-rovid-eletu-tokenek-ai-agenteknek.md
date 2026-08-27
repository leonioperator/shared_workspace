---
id: elkezdodott-2026-08-27-rovid-eletu-tokenek-ai-agenteknek
title: "Rovid eletu tokenek AI agenteknek: kevesebb titok, kisebb kar"
site: elkezdodott
content_type: article
created_at: '2026-08-27T07:45:00+02:00'
status: draft
slug: rovid-eletu-tokenek-ai-agenteknek
quality_score: 4
source_signal: /writing/research/signals-2026-08-27.md
sources:
  - https://vercel.com/blog/the-end-of-credential-sprawl-for-agents
  - https://vercel.com/docs/connect
---

Az AI agentek egyik leggyakoribb vallalati kockazata nem maga a modell, hanem az, hogy milyen hozzafereseket kap. A Vercel Connect altalanosan elerheto lett, es rovid eletu, korlatozott tokeneket ad agenteknek kulso API-khoz, hosszu eletu szolgaltatoi titkok tarolasa nelkul.

# Rovid eletu tokenek AI agenteknek: kevesebb titok, kisebb kar

A Vercel bejelentese szerint a Connect celja, hogy az agentek es szolgaltatasok kulso API-kat, peldaul Slack, GitHub, Microsoft vagy Snowflake rendszereket hivjanak ugy, hogy az alkalmazas ne taroljon hosszu eletu szolgaltatoi titkokat. A dokumentacio szerint az agent futas kozben kerhet rovid eletu, scoped tokent, es azt azonnal felhasznalhatja az adott provider API-jahoz.

Ez nem csak fejlesztoi kenyelmi kerdes. Ha egy agent ugy kap hozzaferest, mint egy emberi admin, akkor egy hibas prompt, rosszul megirt workflow vagy kiszivargo token nagy kart okozhat. A rovid eletu token azt mondja: ez a hozzaferes csak adott feladatra, adott korben es adott ideig ervenyes.

## Mit jelent ez egy KKV CEO-nak?

Egy KKV-ban az AI agentek tipikus feladata nem futurisztikus: ajanlatot keszitenek, CRM-et frissitenek, ugyfelticketet osszegeznek, szamlazasi adatot ellenoriznek vagy belso riportot raknak ossze. Ezekhez hozza kell nyulniuk ceges rendszerekhez. A kerdes az, hogy teljes kulcsot kapnak-e, vagy csak annyi jogot, amennyi az adott lepeshez kell.

Konkret pelda: egy ertekesitesi agent Slack uzenetbol felismeri, hogy egy ugyfel ajanlatfrissitest kert. Lekeri a CRM-bol az ugyfel alapadatait, frissiti az ajanlat allapotat, majd letrehoz egy feladatot a projektmenedzsment rendszerben. Ha mindezt egy hosszu eletu, kornyezeti valtozoban tarolt API kulccsal teszi, akkor a kulcs kiszivargasa utan mas is hosszan hasznalhatja. Ha rovid eletu, feladatra korlatozott tokent kap, a kar merete kisebb es jobban naplozhato.

## A jo agent-hozzaferes nem egyetlen API kulcs

Az agenteknel a klasszikus "betesszuk az API kulcsot az env-be" minta gyors, de rosszul skalazodik. Harom kerdesre kell valaszolni:

1. Ki vagy mi kert hozzaferest?
2. Melyik feladathoz kellett?
3. Meddig volt ervenyes?

Ha ezekre nincs valasz, akkor az AI workflow auditja utolag talalgatas lesz. Ez kulonosen fontos akkor, ha az agent ugyfeladatot, penzugyi adatot vagy belso dokumentumot erint.

## Korlát és kockázat

A rovid eletu token nem old meg mindent. Ha rosszul vannak beallitva a jogosultsagi korok, egy rovid eletu token is tul sokat engedhet. Ha nincs emberi jovahagyas a nagy hatasu muveleteknel, az agent gyorsabban tud rossz dontest vegrehajtani. Ha a naplozas hianyos, a ceg csak azt latja, hogy "valami tortent".

Ezert a tokenkezeles csak egy resze a governance-nek. Kell melle jogosultsagi modell, muveleti naplo, hibakezeles es kulon szabaly arra, hogy az agent mikor alljon meg emberi jovahagyasert.

## Gyakorlati kovetkezo lepes

Erdemes egyetlen workflow-val kezdeni, peldaul CRM frissites vagy ugyfelszolgalati osszegzes. Ird le, mely rendszereket eri el az agent, milyen adatokat olvas, mit irhat vissza, es mely muvelethez kell jovahagyas. Ezutan minden integracional csereld le a tartos, teljes jogu kulcsokat feladathoz kotott, lejaratos hozzaferesre, ahol a hasznalt platform ezt tamogatja.

Minimum ellenorzolista:

- Ne legyen altalanos admin API kulcs agent workflow-ban.
- Kulon token kell olvasasra es irasra, ha a rendszer ezt engedi.
- Nagy hatasu muveletnel legyen emberi jovahagyas.
- Minden agent hivas legyen naplozva feladat, felhasznalo es rendszer szerint.
- A token lejarta utan az agent ne tudjon ujra probalkozni csendben.

## FAQ

### Ez csak nagyvallalatoknak fontos?

Nem. Egy KKV-nal gyakran kevesebb a formalizalt jogosultsagi folyamat, ezert egy rosszul kezelt API kulcs aranyosan nagyobb kart okozhat.

### A rovid eletu token kivaltja az emberi jovahagyast?

Nem. A token a hozzaferes idejet es hatokoret korlatozza. Az uzleti dontes, peldaul penzmozgatas, szerzodesmodositas vagy ugyfelnek kuldott vegleges valasz tovabbra is igenyelhet emberi kontrollt.

### Mit erdemes eloszor atnezni?

Azokat az agent workflow-kat, amelyek irasi joggal rendelkeznek CRM-ben, jegykezelo rendszerben, dokumentumtarban, penzugyi rendszerben vagy kommunikacios csatornaban.

### Mi a legfontosabb meroszam?

Az, hogy egy agent milyen aranyban hasznal feladatra korlatozott, lejaratos hozzaferest tartos, altalanos kulcs helyett. Ez jol mutatja, mennyire kontrollalt a ceg AI automatizalasa.

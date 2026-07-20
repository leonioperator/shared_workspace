---
title: Az AI agent akkor hasznos, ha nem mindent ő csinál
date: 2026-07-19
site: elkezdodott.hu
description: A jó agent rendszerben az LLM dönt és fogalmaz, a végrehajtás viszont
  scriptelt és ellenőrizhető.
tags:
- ai-agent
- kkv
- automatizalas
- governance
slug: ai-agent-deterministicus-vegrehajtas
id: elkezdod
content_type: article
created_at: '2026-07-20'
status: draft
updated_at: '2026-07-20T08:30:01.205654+00:00'
---

A legtöbb agent projekt ott csúszik el, hogy az LLM-re bízza a determinisztikus munkát is. A jobb modell egyszerű: döntés és szöveg LLM, ismétlődő végrehajtás script, minden fontos ponton auditnyom.

## Mi történt?

Az előző hét jelöltjei között több téma ugyanabba az irányba mutatott: AI agentek, workflow orchestration, agent trust, CRM és email automatizálás. A közös tanulság nem az, hogy mindenre kell egy új chatbot. Hanem az, hogy a céges rutinmunkákat kontrollált, mérhető agent workflow-ba kell rendezni.

Forrásjel: `candidates-2026-07-17.md`

> * **Attio:** Az agentic CRM. Ügynökökkel és automatizálással épít pipeline-t, követi a jeleket és előremozdítja az üzleteket. (ben's bites, szponzorált tartalom)

## Mit jelent ez egy KKV CEO-nak?

A CEO problémája nem az, hogy nincs elég AI eszköz. Az a gond, hogy túl sok apró döntés, utánkövetés, email, riport és admin ragad nála. Egy jól összerakott AI operátor ebből vesz le terhet.

De csak akkor, ha van keret:

- külön agent account,
- szűk jogosultság,
- naplózott művelet,
- emberi jóváhagyás pénz, jog és ügyfélkommunikáció előtt,
- determinisztikus script ott, ahol nincs szükség kreatív döntésre.

## Mi a rossz megközelítés?

Az, ha az LLM-re bízod az egész láncot. Ettől lesz törékeny, drága és nehezen auditálható.

## Jobb minta

1. Az LLM értelmez, rangsorol, fogalmaz.
2. A script futtat, ment, ellenőriz, commitol.
3. Az ember csak a kockázatos döntéseknél lép be.
4. A QC nem dísz, hanem fék.

## Gyors teszt

Ha holnap bevezetnéd, ezt kérdezd:

- melyik heti rutin visz el legalább 2 órát,
- van-e egyértelmű input és output,
- lehet-e először csak javaslatot készíttetni,
- van-e emberi jóváhagyási pont,
- mérhető-e az időnyereség.

## FAQ

### Mi a különbség chatbot és AI operátor között?

A chatbot válaszol. Az AI operátor figyel, előkészít, futtat, naplóz és csak szabályozott pontokon kér embert.

### Kell ehhez nagyvállalati rendszer?

Nem. Egy KKV-nál elég lehet email, Telegram, fájlrendszer, git és pár jól körülhatárolt script.

### Mi a legnagyobb kockázat?

A túl nagy jogosultság túl korán. Először olvasás, draft, javaslat. Csak később írás és küldés.

### Hol kezdjem?

Egyetlen folyamattal: inbox triage, heti riport, ajánlat utánkövetés vagy meeting utáni admin. Ne platformot építs első nap, hanem egy működő workflow-t.

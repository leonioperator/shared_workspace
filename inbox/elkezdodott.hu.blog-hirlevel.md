====elkezdodott.hu Hírlevél motor MVP

Készíts egy egyszerű, automatizált **hírlevél motort** az elkészült blogcikkekhez és trend insightokhoz.  
Feladatok:
1) Válassz és állíts be egy hírlevél szolgáltatót, szem előtt tartva az alacsony költségeket! (elsőnek az openclaw lehetőségeit vizsgáld meg, hogy miket támogat ilyen irányban és azt használd, ha van, továbbiak esetleg: MailerLite / Brevo / Sendinblue, vagy amit neten legjobbnak találsz). Erről kérek egy tervet telegram üzenetben (elkezdodott.hu hirlevél motor terv) mielőtt tovább lépsz!
2) Hozz létre egy hírlevél listát: "Elkzdodott – AI Insight".
3) Állíts be egy **feliratkozási űrlapot** az elkezdodott.hu-ra (WP sidebar vagy popup).
4) Kapcsold össze az űrlapot a listával.
5) Automatizáld, hogy heti **összegző hírlevelet** küldjön a heti blogdraftok + trend insightok alapján.
6) Mentsd el és dokumentáld a hírlevél-motor setup lépéseit a shared_workspace/ops mappában.
Kimenet legyen:
- Hírlevél szolgáltató neve
- Lista neve + ID
- Feliratkozási űrlap kódja
- Automatizált heti hírlevél flow beállítása

====Hírlevél logika

Alakíts ki egy **hírlevél logikát**, ami a heti tartalom alapján küldi az AI trend és blog összefoglalót:
1) Definiáld a hírlevél struktúrát:
   - Tárgy: hét témája + AI insight
   - Bevezető: rövid trend összefoglaló
   - Fő rész: heti blogcikkek kivonatai + tanulságok
   - CTA: Navibase demo + AI Audit letöltés
2) Írj egy **sablon hírlevél-minta-szöveget** (magyarul), amit automatikusan kitölt a rendszer minden héten a tartalom alapján.
3) Állíts be időzítést: minden hétfő reggel.
4) Mentsd el a hírlevél logikát és sablon mintát az ops mappába.
Kimenet:
- Hírlevél sablon
- Időzítés
- Lista + hírlevél kapcsolat

====Feliratkozó űrlap WP integráció

Integráld a kiválasztott hírlevél szolgáltató feliratkozó űrlapját az elkezdodott.hu WordPress oldalba:
1) Helyezd el az űrlapot:
   - oldalsávban
   - blogposztok alján
   - popup/képernyő középre
2) Gondoskodj arról, hogy az űrlap:
   - email cím + név mezőt kérjen
   - GDPR opt-in checkbox legyen
3) Teszteld a feliratkozást
4) Mentsd el a beállításokat és logold a működési szabályaid szerint!
Kimenet:
- Űrlap helye + kód
- GDPR-optin beállítás
- Teszt eredmény

# __Búa til nýa notendur og setja þá up__.

fyrst skaltu búa til notandan með skipunina adduser í terminalið ef þú vilt búa til notanda sem heitir Robert skaltu slá inn eftirfarandi skipun:

> ### sudo adduser Robert

Þegar þú slærð þetta in verður notandinn búinn til með grunnstillingum eins og heimamöppu og lykilorð sem þarf að setja.

til að setja notandann í rétta hópana notar þú skipunina "usermod" eins og ef þú vilt setja notandann Robert í hópinn "forritun" skaltu slá inn eftirfarandi skipun:

> ### sudo usermod -a -G forritun Robert

út af því Erlendur og Erla eru ekki byrjuð að vinna þá þarft þú að virka aðganga þeirra þegar þau koma þú getur gert það með því að bara nota þessar skipunir. 

> ### sudo passwd -u erlendur
> ### sudo passwd -u erla

Kveja

Daníel Aron


# __Dagbók__

1. fyrstu 2 dagana var ég að setta up linux virtualbox 

2. næsta dag bjó ég til hópana, nótenduna og möppurnar 

3. næsta dag setti ég réttindi á notenduna og læsti suma notendur og notað --expire til að hækt sé að breytta lykilorðin

4. ég fór yfir allt sem ég var búin að gera og passaði að ekkert vantaði 
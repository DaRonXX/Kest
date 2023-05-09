# __Búa til nýa notendur og setja þá up__.

fyrst skaltu búa til notandan með skipunina adduser í terminalið ef þú vilt búa til notanda sem heitir Robert skaltu slá inn eftirfarandi skipun:

> ### sudo adduser Robert

Þegar þú slærð þetta in verður notandinn búinn til með grunnstillingum eins og heimamöppu og lykilorð sem þarf að setja.

til að setja notandann í rétta hópana notar þú skipunina "usermod" eins og ef þú vilt setja notandann Robert í hópinn "forritun" skaltu slá inn eftirfarandi skipun:

> ### sudo usermod -a -G forritun Robert

út af því Erlendur og Erla eru ekki byrjuð að vinna þá þarft þú að virka aðganga þeirra þegar þau koma þú getur gert það með því að breyta stillingum í skránni "sshd_config" til að opna skrána notar þú skipunina

> ### "sudo nano /etc/ssh/sshd_config

leitaðu að línu sem byrjar á "AllowUsers" og bættu við notendurna erlu og erlendur með:

> ### AllowUsers erlendur erla

Þegar þú ert búin að bæta við notendum í skrána, vistaðu hana og endurbyrjaðu SSH með skipuninni 

> ### ___sudo service ssh restart___



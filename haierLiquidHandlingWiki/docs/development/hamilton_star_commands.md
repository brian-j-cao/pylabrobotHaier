# Hamilton STAR firmware command codes by module

This inventory lists two-letter firmware command identifiers used by the STAR backend in this repository. It’s derived from explicit send_command usages, grouped by module. It may not be exhaustive of the hardware’s full protocol, but it captures what the backend currently uses.

- Modules covered here:
  - C0 — Master/Controller
  - R0 — iSWAP robot
  - I0 — X-drive/gantry (input module)
  - H0 — Heater/Shaker bus scanner
  - P-channels — Pipetting channels (P1–PG). Commands apply per channel ID returned by STAR.channel_id().

If you need descriptions, we can enrich this list next.

## C0 (Master/Controller)

VI, RE, RF, RA, QB, MU, QW, VP, RQ, SR, QV, NS, HD, AZ, AB, AW, SI, AT, AG, AF, AJ, QT, RI, RO, RS, RJ, UJ, RM, RK, VD, BC, RX, QX, RU, UA, XX, XR, ZO, JE, ZA, RT, RL, QS, EV, QH, QI, VC, VB, II, IV, CI, CL, CB, CU, QA, ET, EJ, EL, FI, FY, GX, GY, GZ, GI, GF, RG, QP, QG, CO, HO, CD, CE, OS, QC, JZ

## R0 (iSWAP)

BA, BO, ZI, QW, WP, TP

## I0 (X-drive/gantry)

QW, XP

## H0 (Heat/Shaker bus)

QW

## P-channels (P1–PG)

- Observed explicit per-channel command in this backend:
  - SI (set instrument serial or per-channel init)
- Additional channel-related commands are assembled for pipetting operations and may use the channel module implicitly (e.g., PI, PO, ZH, ZL, JY, RZ), but most are sent via C0 with per-channel payload.

Notes:
- Some commands (e.g., PI, PO, ZH, ZL, JY, RZ, TT, AM, AV, AO, BT, AK, AE, DD, DI, TP, TR, AS, DS, ZT, ZS, ZP, ZR, ZM, KY, KZ, XL, JM, JP, RB, RD, EI, EP, ER, EA, ED, EM, CT, CR, CP, EH, GC, PG, PP, PR, PD, PM, PN, PT, PC) appear in command assembly blocks; many are ultimately issued under module C0 or per-channel context depending on operation. The list above focuses on explicit send_command module-targeted calls.

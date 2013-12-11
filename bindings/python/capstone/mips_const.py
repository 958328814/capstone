# For Capstone Engine. AUTO-GENERATED FILE, DO NOT EDIT [mips_const.py]

# Operand type for instruction's operands
MIPS_OP_INVALID = 0
MIPS_OP_REG = 1
MIPS_OP_IMM = 2
MIPS_OP_MEM = 3

# MIPS registers
MIPS_REG_INVALID = 0
MIPS_REG_0 = 1
MIPS_REG_1 = 2
MIPS_REG_2 = 3
MIPS_REG_3 = 4
MIPS_REG_4 = 5
MIPS_REG_5 = 6
MIPS_REG_6 = 7
MIPS_REG_7 = 8
MIPS_REG_8 = 9
MIPS_REG_9 = 10
MIPS_REG_10 = 11
MIPS_REG_11 = 12
MIPS_REG_12 = 13
MIPS_REG_13 = 14
MIPS_REG_14 = 15
MIPS_REG_15 = 16
MIPS_REG_16 = 17
MIPS_REG_17 = 18
MIPS_REG_18 = 19
MIPS_REG_19 = 20
MIPS_REG_20 = 21
MIPS_REG_21 = 22
MIPS_REG_22 = 23
MIPS_REG_23 = 24
MIPS_REG_24 = 25
MIPS_REG_25 = 26
MIPS_REG_26 = 27
MIPS_REG_27 = 28
MIPS_REG_28 = 29
MIPS_REG_29 = 30
MIPS_REG_30 = 31
MIPS_REG_31 = 32
MIPS_REG_DSPCCOND = 33
MIPS_REG_DSPCARRY = 34
MIPS_REG_DSPEFI = 35
MIPS_REG_DSPOUTFLAG = 36
MIPS_REG_DSPOUTFLAG16_19 = 37
MIPS_REG_DSPOUTFLAG20 = 38
MIPS_REG_DSPOUTFLAG21 = 39
MIPS_REG_DSPOUTFLAG22 = 40
MIPS_REG_DSPOUTFLAG23 = 41
MIPS_REG_DSPPOS = 42
MIPS_REG_DSPSCOUNT = 43
MIPS_REG_AC0 = 44
MIPS_REG_AC1 = 45
MIPS_REG_AC2 = 46
MIPS_REG_AC3 = 47
MIPS_REG_F0 = 48
MIPS_REG_F1 = 49
MIPS_REG_F2 = 50
MIPS_REG_F3 = 51
MIPS_REG_F4 = 52
MIPS_REG_F5 = 53
MIPS_REG_F6 = 54
MIPS_REG_F7 = 55
MIPS_REG_F8 = 56
MIPS_REG_F9 = 57
MIPS_REG_F10 = 58
MIPS_REG_F11 = 59
MIPS_REG_F12 = 60
MIPS_REG_F13 = 61
MIPS_REG_F14 = 62
MIPS_REG_F15 = 63
MIPS_REG_F16 = 64
MIPS_REG_F17 = 65
MIPS_REG_F18 = 66
MIPS_REG_F19 = 67
MIPS_REG_F20 = 68
MIPS_REG_F21 = 69
MIPS_REG_F22 = 70
MIPS_REG_F23 = 71
MIPS_REG_F24 = 72
MIPS_REG_F25 = 73
MIPS_REG_F26 = 74
MIPS_REG_F27 = 75
MIPS_REG_F28 = 76
MIPS_REG_F29 = 77
MIPS_REG_F30 = 78
MIPS_REG_F31 = 79
MIPS_REG_FCC0 = 80
MIPS_REG_FCC1 = 81
MIPS_REG_FCC2 = 82
MIPS_REG_FCC3 = 83
MIPS_REG_FCC4 = 84
MIPS_REG_FCC5 = 85
MIPS_REG_FCC6 = 86
MIPS_REG_FCC7 = 87
MIPS_REG_W0 = 88
MIPS_REG_W1 = 89
MIPS_REG_W2 = 90
MIPS_REG_W3 = 91
MIPS_REG_W4 = 92
MIPS_REG_W5 = 93
MIPS_REG_W6 = 94
MIPS_REG_W7 = 95
MIPS_REG_W8 = 96
MIPS_REG_W9 = 97
MIPS_REG_W10 = 98
MIPS_REG_W11 = 99
MIPS_REG_W12 = 100
MIPS_REG_W13 = 101
MIPS_REG_W14 = 102
MIPS_REG_W15 = 103
MIPS_REG_W16 = 104
MIPS_REG_W17 = 105
MIPS_REG_W18 = 106
MIPS_REG_W19 = 107
MIPS_REG_W20 = 108
MIPS_REG_W21 = 109
MIPS_REG_W22 = 110
MIPS_REG_W23 = 111
MIPS_REG_W24 = 112
MIPS_REG_W25 = 113
MIPS_REG_W26 = 114
MIPS_REG_W27 = 115
MIPS_REG_W28 = 116
MIPS_REG_W29 = 117
MIPS_REG_W30 = 118
MIPS_REG_W31 = 119
MIPS_REG_HI = 120
MIPS_REG_LO = 121
MIPS_REG_PC = 122
MIPS_REG_MAX = 123
MIPS_REG_ZERO = MIPS_REG_0
MIPS_REG_AT = MIPS_REG_1
MIPS_REG_V0 = MIPS_REG_2
MIPS_REG_V1 = MIPS_REG_3
MIPS_REG_A0 = MIPS_REG_4
MIPS_REG_A1 = MIPS_REG_5
MIPS_REG_A2 = MIPS_REG_6
MIPS_REG_A3 = MIPS_REG_7
MIPS_REG_T0 = MIPS_REG_8
MIPS_REG_T1 = MIPS_REG_9
MIPS_REG_T2 = MIPS_REG_10
MIPS_REG_T3 = MIPS_REG_11
MIPS_REG_T4 = MIPS_REG_12
MIPS_REG_T5 = MIPS_REG_13
MIPS_REG_T6 = MIPS_REG_14
MIPS_REG_T7 = MIPS_REG_15
MIPS_REG_S0 = MIPS_REG_16
MIPS_REG_S1 = MIPS_REG_17
MIPS_REG_S2 = MIPS_REG_18
MIPS_REG_S3 = MIPS_REG_19
MIPS_REG_S4 = MIPS_REG_20
MIPS_REG_S5 = MIPS_REG_21
MIPS_REG_S6 = MIPS_REG_22
MIPS_REG_S7 = MIPS_REG_23
MIPS_REG_T8 = MIPS_REG_24
MIPS_REG_T9 = MIPS_REG_25
MIPS_REG_K0 = MIPS_REG_26
MIPS_REG_K1 = MIPS_REG_27
MIPS_REG_GP = MIPS_REG_28
MIPS_REG_SP = MIPS_REG_29
MIPS_REG_FP = MIPS_REG_30
MIPS_REG_S8 = MIPS_REG_30
MIPS_REG_RA = MIPS_REG_31
MIPS_REG_HI0 = MIPS_REG_AC0
MIPS_REG_HI1 = MIPS_REG_AC1
MIPS_REG_HI2 = MIPS_REG_AC2
MIPS_REG_HI3 = MIPS_REG_AC3
MIPS_REG_LO0 = MIPS_REG_HI0
MIPS_REG_LO1 = MIPS_REG_HI1
MIPS_REG_LO2 = MIPS_REG_HI2
MIPS_REG_LO3 = MIPS_REG_HI3

# MIPS instruction
MIPS_INS_INVALID = 0
MIPS_INS_ABSQ_S = 1
MIPS_INS_ADD = 2
MIPS_INS_ADDQH = 3
MIPS_INS_ADDQH_R = 4
MIPS_INS_ADDQ = 5
MIPS_INS_ADDQ_S = 6
MIPS_INS_ADDSC = 7
MIPS_INS_ADDS_A = 8
MIPS_INS_ADDS_S = 9
MIPS_INS_ADDS_U = 10
MIPS_INS_ADDUH = 11
MIPS_INS_ADDUH_R = 12
MIPS_INS_ADDU = 13
MIPS_INS_ADDU_S = 14
MIPS_INS_ADDVI = 15
MIPS_INS_ADDV = 16
MIPS_INS_ADDWC = 17
MIPS_INS_ADD_A = 18
MIPS_INS_ADDI = 19
MIPS_INS_ADDIU = 20
MIPS_INS_AND = 21
MIPS_INS_ANDI = 22
MIPS_INS_APPEND = 23
MIPS_INS_ASUB_S = 24
MIPS_INS_ASUB_U = 25
MIPS_INS_AVER_S = 26
MIPS_INS_AVER_U = 27
MIPS_INS_AVE_S = 28
MIPS_INS_AVE_U = 29
MIPS_INS_BALIGN = 30
MIPS_INS_BC1F = 31
MIPS_INS_BC1T = 32
MIPS_INS_BCLRI = 33
MIPS_INS_BCLR = 34
MIPS_INS_BEQ = 35
MIPS_INS_BGEZ = 36
MIPS_INS_BGEZAL = 37
MIPS_INS_BGTZ = 38
MIPS_INS_BINSLI = 39
MIPS_INS_BINSL = 40
MIPS_INS_BINSRI = 41
MIPS_INS_BINSR = 42
MIPS_INS_BITREV = 43
MIPS_INS_BLEZ = 44
MIPS_INS_BLTZ = 45
MIPS_INS_BLTZAL = 46
MIPS_INS_BMNZI = 47
MIPS_INS_BMNZ = 48
MIPS_INS_BMZI = 49
MIPS_INS_BMZ = 50
MIPS_INS_BNE = 51
MIPS_INS_BNEGI = 52
MIPS_INS_BNEG = 53
MIPS_INS_BNZ = 54
MIPS_INS_BPOSGE32 = 55
MIPS_INS_BREAK = 56
MIPS_INS_BSELI = 57
MIPS_INS_BSEL = 58
MIPS_INS_BSETI = 59
MIPS_INS_BSET = 60
MIPS_INS_BZ = 61
MIPS_INS_BEQZ = 62
MIPS_INS_B = 63
MIPS_INS_BNEZ = 64
MIPS_INS_BTEQZ = 65
MIPS_INS_BTNEZ = 66
MIPS_INS_CEIL = 67
MIPS_INS_CEQI = 68
MIPS_INS_CEQ = 69
MIPS_INS_CFC1 = 70
MIPS_INS_CFCMSA = 71
MIPS_INS_CLEI_S = 72
MIPS_INS_CLEI_U = 73
MIPS_INS_CLE_S = 74
MIPS_INS_CLE_U = 75
MIPS_INS_CLO = 76
MIPS_INS_CLTI_S = 77
MIPS_INS_CLTI_U = 78
MIPS_INS_CLT_S = 79
MIPS_INS_CLT_U = 80
MIPS_INS_CLZ = 81
MIPS_INS_CMPGDU = 82
MIPS_INS_CMPGU = 83
MIPS_INS_CMPU = 84
MIPS_INS_CMP = 85
MIPS_INS_COPY_S = 86
MIPS_INS_COPY_U = 87
MIPS_INS_CTC1 = 88
MIPS_INS_CTCMSA = 89
MIPS_INS_CVT = 90
MIPS_INS_C = 91
MIPS_INS_CMPI = 92
MIPS_INS_DADD = 93
MIPS_INS_DADDI = 94
MIPS_INS_DADDIU = 95
MIPS_INS_DADDU = 96
MIPS_INS_DCLO = 97
MIPS_INS_DCLZ = 98
MIPS_INS_DERET = 99
MIPS_INS_DEXT = 100
MIPS_INS_DEXTM = 101
MIPS_INS_DEXTU = 102
MIPS_INS_DI = 103
MIPS_INS_DINS = 104
MIPS_INS_DINSM = 105
MIPS_INS_DINSU = 106
MIPS_INS_DIV_S = 107
MIPS_INS_DIV_U = 108
MIPS_INS_DMFC0 = 109
MIPS_INS_DMFC1 = 110
MIPS_INS_DMFC2 = 111
MIPS_INS_DMTC0 = 112
MIPS_INS_DMTC1 = 113
MIPS_INS_DMTC2 = 114
MIPS_INS_DMULT = 115
MIPS_INS_DMULTU = 116
MIPS_INS_DOTP_S = 117
MIPS_INS_DOTP_U = 118
MIPS_INS_DPADD_S = 119
MIPS_INS_DPADD_U = 120
MIPS_INS_DPAQX_SA = 121
MIPS_INS_DPAQX_S = 122
MIPS_INS_DPAQ_SA = 123
MIPS_INS_DPAQ_S = 124
MIPS_INS_DPAU = 125
MIPS_INS_DPAX = 126
MIPS_INS_DPA = 127
MIPS_INS_DPSQX_SA = 128
MIPS_INS_DPSQX_S = 129
MIPS_INS_DPSQ_SA = 130
MIPS_INS_DPSQ_S = 131
MIPS_INS_DPSUB_S = 132
MIPS_INS_DPSUB_U = 133
MIPS_INS_DPSU = 134
MIPS_INS_DPSX = 135
MIPS_INS_DPS = 136
MIPS_INS_DROTR = 137
MIPS_INS_DROTR32 = 138
MIPS_INS_DROTRV = 139
MIPS_INS_DSBH = 140
MIPS_INS_DDIV = 141
MIPS_INS_DSHD = 142
MIPS_INS_DSLL = 143
MIPS_INS_DSLL32 = 144
MIPS_INS_DSLLV = 145
MIPS_INS_DSRA = 146
MIPS_INS_DSRA32 = 147
MIPS_INS_DSRAV = 148
MIPS_INS_DSRL = 149
MIPS_INS_DSRL32 = 150
MIPS_INS_DSRLV = 151
MIPS_INS_DSUBU = 152
MIPS_INS_DDIVU = 153
MIPS_INS_DIV = 154
MIPS_INS_DIVU = 155
MIPS_INS_EI = 156
MIPS_INS_ERET = 157
MIPS_INS_EXT = 158
MIPS_INS_EXTP = 159
MIPS_INS_EXTPDP = 160
MIPS_INS_EXTPDPV = 161
MIPS_INS_EXTPV = 162
MIPS_INS_EXTRV_RS = 163
MIPS_INS_EXTRV_R = 164
MIPS_INS_EXTRV_S = 165
MIPS_INS_EXTRV = 166
MIPS_INS_EXTR_RS = 167
MIPS_INS_EXTR_R = 168
MIPS_INS_EXTR_S = 169
MIPS_INS_EXTR = 170
MIPS_INS_ABS = 171
MIPS_INS_FADD = 172
MIPS_INS_FCAF = 173
MIPS_INS_FCEQ = 174
MIPS_INS_FCLASS = 175
MIPS_INS_FCLE = 176
MIPS_INS_FCLT = 177
MIPS_INS_FCNE = 178
MIPS_INS_FCOR = 179
MIPS_INS_FCUEQ = 180
MIPS_INS_FCULE = 181
MIPS_INS_FCULT = 182
MIPS_INS_FCUNE = 183
MIPS_INS_FCUN = 184
MIPS_INS_FDIV = 185
MIPS_INS_FEXDO = 186
MIPS_INS_FEXP2 = 187
MIPS_INS_FEXUPL = 188
MIPS_INS_FEXUPR = 189
MIPS_INS_FFINT_S = 190
MIPS_INS_FFINT_U = 191
MIPS_INS_FFQL = 192
MIPS_INS_FFQR = 193
MIPS_INS_FILL = 194
MIPS_INS_FLOG2 = 195
MIPS_INS_FLOOR = 196
MIPS_INS_FMADD = 197
MIPS_INS_FMAX_A = 198
MIPS_INS_FMAX = 199
MIPS_INS_FMIN_A = 200
MIPS_INS_FMIN = 201
MIPS_INS_MOV = 202
MIPS_INS_FMSUB = 203
MIPS_INS_FMUL = 204
MIPS_INS_MUL = 205
MIPS_INS_NEG = 206
MIPS_INS_FRCP = 207
MIPS_INS_FRINT = 208
MIPS_INS_FRSQRT = 209
MIPS_INS_FSAF = 210
MIPS_INS_FSEQ = 211
MIPS_INS_FSLE = 212
MIPS_INS_FSLT = 213
MIPS_INS_FSNE = 214
MIPS_INS_FSOR = 215
MIPS_INS_FSQRT = 216
MIPS_INS_SQRT = 217
MIPS_INS_FSUB = 218
MIPS_INS_SUB = 219
MIPS_INS_FSUEQ = 220
MIPS_INS_FSULE = 221
MIPS_INS_FSULT = 222
MIPS_INS_FSUNE = 223
MIPS_INS_FSUN = 224
MIPS_INS_FTINT_S = 225
MIPS_INS_FTINT_U = 226
MIPS_INS_FTQ = 227
MIPS_INS_FTRUNC_S = 228
MIPS_INS_FTRUNC_U = 229
MIPS_INS_HADD_S = 230
MIPS_INS_HADD_U = 231
MIPS_INS_HSUB_S = 232
MIPS_INS_HSUB_U = 233
MIPS_INS_ILVEV = 234
MIPS_INS_ILVL = 235
MIPS_INS_ILVOD = 236
MIPS_INS_ILVR = 237
MIPS_INS_INS = 238
MIPS_INS_INSERT = 239
MIPS_INS_INSV = 240
MIPS_INS_INSVE = 241
MIPS_INS_J = 242
MIPS_INS_JAL = 243
MIPS_INS_JALR = 244
MIPS_INS_JR = 245
MIPS_INS_JRC = 246
MIPS_INS_JALRC = 247
MIPS_INS_LB = 248
MIPS_INS_LBUX = 249
MIPS_INS_LBU = 250
MIPS_INS_LD = 251
MIPS_INS_LDC1 = 252
MIPS_INS_LDC2 = 253
MIPS_INS_LDI = 254
MIPS_INS_LDL = 255
MIPS_INS_LDR = 256
MIPS_INS_LDXC1 = 257
MIPS_INS_LH = 258
MIPS_INS_LHX = 259
MIPS_INS_LHU = 260
MIPS_INS_LL = 261
MIPS_INS_LLD = 262
MIPS_INS_LSA = 263
MIPS_INS_LUXC1 = 264
MIPS_INS_LUI = 265
MIPS_INS_LW = 266
MIPS_INS_LWC1 = 267
MIPS_INS_LWC2 = 268
MIPS_INS_LWL = 269
MIPS_INS_LWR = 270
MIPS_INS_LWX = 271
MIPS_INS_LWXC1 = 272
MIPS_INS_LWU = 273
MIPS_INS_LI = 274
MIPS_INS_MADD = 275
MIPS_INS_MADDR_Q = 276
MIPS_INS_MADDU = 277
MIPS_INS_MADDV = 278
MIPS_INS_MADD_Q = 279
MIPS_INS_MAQ_SA = 280
MIPS_INS_MAQ_S = 281
MIPS_INS_MAXI_S = 282
MIPS_INS_MAXI_U = 283
MIPS_INS_MAX_A = 284
MIPS_INS_MAX_S = 285
MIPS_INS_MAX_U = 286
MIPS_INS_MFC0 = 287
MIPS_INS_MFC1 = 288
MIPS_INS_MFC2 = 289
MIPS_INS_MFHC1 = 290
MIPS_INS_MFHI = 291
MIPS_INS_MFLO = 292
MIPS_INS_MINI_S = 293
MIPS_INS_MINI_U = 294
MIPS_INS_MIN_A = 295
MIPS_INS_MIN_S = 296
MIPS_INS_MIN_U = 297
MIPS_INS_MODSUB = 298
MIPS_INS_MOD_S = 299
MIPS_INS_MOD_U = 300
MIPS_INS_MOVE = 301
MIPS_INS_MOVF = 302
MIPS_INS_MOVN = 303
MIPS_INS_MOVT = 304
MIPS_INS_MOVZ = 305
MIPS_INS_MSUB = 306
MIPS_INS_MSUBR_Q = 307
MIPS_INS_MSUBU = 308
MIPS_INS_MSUBV = 309
MIPS_INS_MSUB_Q = 310
MIPS_INS_MTC0 = 311
MIPS_INS_MTC1 = 312
MIPS_INS_MTC2 = 313
MIPS_INS_MTHC1 = 314
MIPS_INS_MTHI = 315
MIPS_INS_MTHLIP = 316
MIPS_INS_MTLO = 317
MIPS_INS_MULEQ_S = 318
MIPS_INS_MULEU_S = 319
MIPS_INS_MULQ_RS = 320
MIPS_INS_MULQ_S = 321
MIPS_INS_MULR_Q = 322
MIPS_INS_MULSAQ_S = 323
MIPS_INS_MULSA = 324
MIPS_INS_MULT = 325
MIPS_INS_MULTU = 326
MIPS_INS_MULV = 327
MIPS_INS_MUL_Q = 328
MIPS_INS_MUL_S = 329
MIPS_INS_NLOC = 330
MIPS_INS_NLZC = 331
MIPS_INS_NMADD = 332
MIPS_INS_NMSUB = 333
MIPS_INS_NOR = 334
MIPS_INS_NORI = 335
MIPS_INS_NOT = 336
MIPS_INS_OR = 337
MIPS_INS_ORI = 338
MIPS_INS_PACKRL = 339
MIPS_INS_PCKEV = 340
MIPS_INS_PCKOD = 341
MIPS_INS_PCNT = 342
MIPS_INS_PICK = 343
MIPS_INS_PRECEQU = 344
MIPS_INS_PRECEQ = 345
MIPS_INS_PRECEU = 346
MIPS_INS_PRECRQU_S = 347
MIPS_INS_PRECRQ = 348
MIPS_INS_PRECRQ_RS = 349
MIPS_INS_PRECR = 350
MIPS_INS_PRECR_SRA = 351
MIPS_INS_PRECR_SRA_R = 352
MIPS_INS_PREPEND = 353
MIPS_INS_RADDU = 354
MIPS_INS_RDDSP = 355
MIPS_INS_RDHWR = 356
MIPS_INS_REPLV = 357
MIPS_INS_REPL = 358
MIPS_INS_ROTR = 359
MIPS_INS_ROTRV = 360
MIPS_INS_ROUND = 361
MIPS_INS_RESTORE = 362
MIPS_INS_SAT_S = 363
MIPS_INS_SAT_U = 364
MIPS_INS_SB = 365
MIPS_INS_SC = 366
MIPS_INS_SCD = 367
MIPS_INS_SD = 368
MIPS_INS_SDC1 = 369
MIPS_INS_SDC2 = 370
MIPS_INS_SDL = 371
MIPS_INS_SDR = 372
MIPS_INS_SDXC1 = 373
MIPS_INS_SEB = 374
MIPS_INS_SEH = 375
MIPS_INS_SH = 376
MIPS_INS_SHF = 377
MIPS_INS_SHILO = 378
MIPS_INS_SHILOV = 379
MIPS_INS_SHLLV = 380
MIPS_INS_SHLLV_S = 381
MIPS_INS_SHLL = 382
MIPS_INS_SHLL_S = 383
MIPS_INS_SHRAV = 384
MIPS_INS_SHRAV_R = 385
MIPS_INS_SHRA = 386
MIPS_INS_SHRA_R = 387
MIPS_INS_SHRLV = 388
MIPS_INS_SHRL = 389
MIPS_INS_SLDI = 390
MIPS_INS_SLD = 391
MIPS_INS_SLL = 392
MIPS_INS_SLLI = 393
MIPS_INS_SLLV = 394
MIPS_INS_SLT = 395
MIPS_INS_SLTI = 396
MIPS_INS_SLTIU = 397
MIPS_INS_SLTU = 398
MIPS_INS_SPLATI = 399
MIPS_INS_SPLAT = 400
MIPS_INS_SRA = 401
MIPS_INS_SRAI = 402
MIPS_INS_SRARI = 403
MIPS_INS_SRAR = 404
MIPS_INS_SRAV = 405
MIPS_INS_SRL = 406
MIPS_INS_SRLI = 407
MIPS_INS_SRLRI = 408
MIPS_INS_SRLR = 409
MIPS_INS_SRLV = 410
MIPS_INS_ST = 411
MIPS_INS_SUBQH = 412
MIPS_INS_SUBQH_R = 413
MIPS_INS_SUBQ = 414
MIPS_INS_SUBQ_S = 415
MIPS_INS_SUBSUS_U = 416
MIPS_INS_SUBSUU_S = 417
MIPS_INS_SUBS_S = 418
MIPS_INS_SUBS_U = 419
MIPS_INS_SUBUH = 420
MIPS_INS_SUBUH_R = 421
MIPS_INS_SUBU = 422
MIPS_INS_SUBU_S = 423
MIPS_INS_SUBVI = 424
MIPS_INS_SUBV = 425
MIPS_INS_SUXC1 = 426
MIPS_INS_SW = 427
MIPS_INS_SWC1 = 428
MIPS_INS_SWC2 = 429
MIPS_INS_SWL = 430
MIPS_INS_SWR = 431
MIPS_INS_SWXC1 = 432
MIPS_INS_SYNC = 433
MIPS_INS_SYSCALL = 434
MIPS_INS_SAVE = 435
MIPS_INS_TEQ = 436
MIPS_INS_TEQI = 437
MIPS_INS_TGE = 438
MIPS_INS_TGEI = 439
MIPS_INS_TGEIU = 440
MIPS_INS_TGEU = 441
MIPS_INS_TLT = 442
MIPS_INS_TLTI = 443
MIPS_INS_TLTIU = 444
MIPS_INS_TLTU = 445
MIPS_INS_TNE = 446
MIPS_INS_TNEI = 447
MIPS_INS_TRUNC = 448
MIPS_INS_VSHF = 449
MIPS_INS_WAIT = 450
MIPS_INS_WRDSP = 451
MIPS_INS_WSBH = 452
MIPS_INS_XOR = 453
MIPS_INS_XORI = 454
MIPS_INS_NOP = 455
MIPS_INS_NEGU = 456
MIPS_INS_MAX = 457

# Group of MIPS instructions
MIPS_GRP_INVALID = 0
MIPS_GRP_BITCOUNT = 1
MIPS_GRP_DSP = 2
MIPS_GRP_DSPR2 = 3
MIPS_GRP_FPIDX = 4
MIPS_GRP_MSA = 5
MIPS_GRP_MIPS32R2 = 6
MIPS_GRP_MIPS64 = 7
MIPS_GRP_MIPS64R2 = 8
MIPS_GRP_SEINREG = 9
MIPS_GRP_STDENC = 10
MIPS_GRP_SWAP = 11
MIPS_GRP_MICROMIPS = 12
MIPS_GRP_MIPS16MODE = 13
MIPS_GRP_FP64BIT = 14
MIPS_GRP_NONANSFPMATH = 15
MIPS_GRP_NOTFP64BIT = 16
MIPS_GRP_NOTINMICROMIPS = 17
MIPS_GRP_JUMP = 18
MIPS_GRP_MAX = 19

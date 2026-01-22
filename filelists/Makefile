## TODO: fill in the correct module MSNs below

## Get global settings; TRACKS (e26...), REV (FRINGE), REL (0), SITE (mpifr), EXPROOT (/Exps)
include ../Makefile.inc

M6DIRS := /cluster/difx/directories/

all:
	@echo "Options:  'make bonn'  or  'make hays'"

mk6dir2filelist = grep "^e26" $(M6DIRS)/$(3).filelist | sort -k 2 | sed -e 's/^/\/$(1)_fuse\/$(2)\//' | cut -d' ' -f 1,2,3 > $(4)

bonn: aa_b1 aa_b4 ax_b1 ax_b4 gl_b1 gl_b4 mm_b1 mm_b4 mg_b1 mg_b4 \
	kt_b1 kt_b4 lm_b1 lm_b4 pv_b1 pv_b4 nn_b1 nn_b4 sw_b1 sw_b4 sz_b1 sz_b4

hays: pv_b2 pv_b3

## ALMA - infos by email

aa_b1:
	$(call mk6dir2filelist,mark6-10,12,EHT%1231,ALMA_b1.12.filelist)
	$(call mk6dir2filelist,mark6-10,34,EHT%1233,ALMA_b1.34.filelist)

aa_b2:
	$(call mk6dir2filelist,mark6-10,12,EHT%1246,ALMA_b2.12.filelist)
	$(call mk6dir2filelist,mark6-10,34,EHT%1248,ALMA_b2.34.filelist)

aa_b3:
	$(call mk6dir2filelist,mark6-10,12,EHT%1259,ALMA_b3.12.filelist)
	$(call mk6dir2filelist,mark6-10,34,EHT%1261,ALMA_b3.34.filelist)

aa_b4:
	$(call mk6dir2filelist,mark6-10,12,EHT%1250,ALMA_b4.12.filelist)
	$(call mk6dir2filelist,mark6-10,34,MPI%1205,ALMA_b4.34.filelist)

## APEX - https://eventhorizontelescope.mywikis.wiki/wiki/APEX_setup_2026

ax_b1:
	$(call mk6dir2filelist,mark6-09,12,EHT%0078,APEX_b1.12.filelist)
	$(call mk6dir2filelist,mark6-09,34,EHT%0080,APEX_b1.34.filelist)

ax_b2:
	$(call mk6dir2filelist,mark6-09,12,BHC%0114,APEX_b2.12.filelist)
	$(call mk6dir2filelist,mark6-09,34,BHC%0116,APEX_b2.34.filelist)

ax_b3:
	$(call mk6dir2filelist,mark6-09,12,BHC%0122,APEX_b3.12.filelist)
	$(call mk6dir2filelist,mark6-09,34,BHC%0130,APEX_b3.34.filelist)

ax_b4:
	$(call mk6dir2filelist,mark6-10,12,BHC%0106,APEX_b4.12.filelist)
	$(call mk6dir2filelist,mark6-10,34,BHC%0109,APEX_b4.34.filelist)

## GLT - https://eventhorizontelescope.mywikis.wiki/wiki/GLT_(Gl)_setup_2026

gl_b1:
	$(call mk6dir2filelist,mark6-06,12,EHT%1101,GLT_b1.12.filelist)
	$(call mk6dir2filelist,mark6-06,34,EHT%1201,GLT_b1.34.filelist)

gl_b2:
	$(call mk6dir2filelist,mark6-06,12,EHT%1203,GLT_b2.12.filelist)
	$(call mk6dir2filelist,mark6-06,34,EHT%1212,GLT_b2.34.filelist)

gl_b3:
	$(call mk6dir2filelist,mark6-06,12,EHT%1218,GLT_b3.12.filelist)
	$(call mk6dir2filelist,mark6-06,34,EHT%1220,GLT_b3.34.filelist)

gl_b4:
	$(call mk6dir2filelist,mark6-06,12,EHT%1223,GLT_b4.12.filelist)
	$(call mk6dir2filelist,mark6-06,34,EHT%1225,GLT_b4.34.filelist)

## JCMT - https://eventhorizontelescope.mywikis.wiki/wiki/JCMT_setup_2026

mm_b1:
	$(call mk6dir2filelist,mark6-11,12,EHT%0084,JCMT_b1.12.filelist)
	$(call mk6dir2filelist,mark6-11,34,EHT%0086,JCMT_b1.34.filelist)

mm_b2:
	$(call mk6dir2filelist,mark6-11,12,BHC%0041,JCMT_b2.12.filelist)
	$(call mk6dir2filelist,mark6-11,34,BHC%0071,JCMT_b2.34.filelist)

mm_b3:
	$(call mk6dir2filelist,mark6-11,12,EHT%0088,JCMT_b3.12.filelist)
	$(call mk6dir2filelist,mark6-11,34,EHT%0090,JCMT_b3.34.filelist)

mm_b4:
	$(call mk6dir2filelist,mark6-08,12,BHC%0077,JCMT_b4.12.filelist)
	$(call mk6dir2filelist,mark6-08,34,SHAO%008,JCMT_b4.34.filelist)

## Kitt Peak - https://eventhorizontelescope.mywikis.wiki/wiki/KP_setup_2026

kt_b1:
	$(call mk6dir2filelist,mark6-02,12,EHT%1235,KT_b1.12.filelist)
	$(call mk6dir2filelist,mark6-02,34,EHT%1237,KT_b1.34.filelist)

kt_b2:
	$(call mk6dir2filelist,mark6-02,12,EHT%1241,KT_b2.12.filelist)
	$(call mk6dir2filelist,mark6-02,34,EHT%1243,KT_b2.34.filelist)

kt_b3:
	$(call mk6dir2filelist,mark6-02,12,EHT%1252,KT_b3.12.filelist)
	$(call mk6dir2filelist,mark6-02,34,EHT%1254,KT_b3.34.filelist)

kt_b4:
	$(call mk6dir2filelist,mark6-02,12,EHT%1256,KT_b4.12.filelist)
	$(call mk6dir2filelist,mark6-02,34,EHT%1258,KT_b4.34.filelist)

## LMT - https://eventhorizontelescope.mywikis.wiki/wiki/LMT_2026_Apr_setup

lm_b1:
	$(call mk6dir2filelist,mark6-07,12,BHC%0001,LMT_b4.12.filelist)
	$(call mk6dir2filelist,mark6-07,34,BHC%0003,LMT_b4.34.filelist)

lm_b4:
	$(call mk6dir2filelist,mark6-07,12,BHC%0157,LMT_b1.12.filelist)
	$(call mk6dir2filelist,mark6-07,34,BHC%0159,LMT_b1.34.filelist)

## NOEMA - https://eventhorizontelescope.mywikis.wiki/wiki/NOEMA_setup_2026
	
nn_b1:
	$(call mk6dir2filelist,mark6-09,1,IRAM%005,NOEMA_b1.1.filelist)
	$(call mk6dir2filelist,mark6-09,2,IRAM%006,NOEMA_b1.2.filelist)
	$(call mk6dir2filelist,mark6-09,3,IRAM%007,NOEMA_b1.3.filelist)
	$(call mk6dir2filelist,mark6-09,4,IRAM%008,NOEMA_b1.4.filelist)

nn_b2:
	$(call mk6dir2filelist,mark6-09,1,MPI%8010,NOEMA_b2.1.filelist)
	$(call mk6dir2filelist,mark6-09,2,MPI%8035,NOEMA_b2.2.filelist)
	$(call mk6dir2filelist,mark6-09,3,MPI%8057,NOEMA_b2.3.filelist)
	$(call mk6dir2filelist,mark6-09,4,MPI%8058,NOEMA_b2.4.filelist)

nn_b3:
	$(call mk6dir2filelist,mark6-09,1,SHAO%016,NOEMA_b3.1.filelist)
	$(call mk6dir2filelist,mark6-09,2,SHAO%037,NOEMA_b3.2.filelist)
	$(call mk6dir2filelist,mark6-09,3,SHAO%049,NOEMA_b3.3.filelist)
	$(call mk6dir2filelist,mark6-09,4,SHAO%050,NOEMA_b3.4.filelist)

nn_b4:
	$(call mk6dir2filelist,mark6-09,1,BHC%0144,NOEMA_b4.1.filelist)
	$(call mk6dir2filelist,mark6-09,2,BHC%0145,NOEMA_b4.2.filelist)
	$(call mk6dir2filelist,mark6-09,3,BHC%0146,NOEMA_b4.3.filelist)
	$(call mk6dir2filelist,mark6-09,4,BHC%0147,NOEMA_b4.4.filelist)

## Pico - https://eventhorizontelescope.mywikis.wiki/wiki/IRAM30m_setup_2026

pv_b1:
	$(call mk6dir2filelist,mark6-05,12,BHC%0078,Pico_b1.12.filelist)
	$(call mk6dir2filelist,mark6-05,34,BHC%0082,Pico_b1.34.filelist)

pv_b2:
	$(call mk6dir2filelist,mark6-05,12,EHT%0077,Pico_b2.12.filelist)
	$(call mk6dir2filelist,mark6-05,34,EHT%0092,Pico_b2.34.filelist)

pv_b3:
	$(call mk6dir2filelist,mark6-05,12,EHT%0076,Pico_b3.12.filelist)
	$(call mk6dir2filelist,mark6-05,34,EHT%0098,Pico_b3.34.filelist)

pv_b4:
	$(call mk6dir2filelist,mark6-05,12,MPI%6400,Pico_b4.12.filelist)
	$(call mk6dir2filelist,mark6-05,34,MPI%6422,Pico_b4.34.filelist)

## SMA APHIDS - https://eventhorizontelescope.mywikis.wiki/wiki/SMA_setup_2026

sw_b1: # todo post-APHIDS MSNs
	#$(call mk6dir2filelist,mark6-05,12,...,SMA_b1.12.filelist)
	#$(call mk6dir2filelist,mark6-05,34,...,SMA_b1.34.filelist)

sw_b4: # todo post-APHIDS MSNs
	#$(call mk6dir2filelist,mark6-05,12,...,SMA_b4.12.filelist)
	#$(call mk6dir2filelist,mark6-05,34,...,SMA_b4.34.filelist)

## SMT - https://eventhorizontelescope.mywikis.wiki/wiki/SMT_setup_2026

mg_b1:
	$(call mk6dir2filelist,mark6-04,12,EHT%1205,SMT_b1.12.filelist)
	$(call mk6dir2filelist,mark6-04,34,EHT%1207,SMT_b1.34.filelist)

mg_b2:
	$(call mk6dir2filelist,mark6-04,12,EHT%1209,SMT_b2.12.filelist)
	$(call mk6dir2filelist,mark6-04,34,EHT%1211,SMT_b2.34.filelist)

mg_b3:
	$(call mk6dir2filelist,mark6-04,12,EHT%1227,SMT_b3.12.filelist)
	$(call mk6dir2filelist,mark6-04,34,EHT%1229,SMT_b3.34.filelist)

mg_b4:
	$(call mk6dir2filelist,mark6-04,12,EHT%1215,SMT_b4.12.filelist)
	$(call mk6dir2filelist,mark6-04,34,EHT%1217,SMT_b4.34.filelist)

## SPT

sz_b1: # todo
	#$(call mk6dir2filelist,mark6-04,12,ALMA%029,SPT_b1.12.filelist)
	#$(call mk6dir2filelist,mark6-04,34,ALMA%031,SPT_b1.34.filelist)

sz_b4: # todo
	#$(call mk6dir2filelist,mark6-04,12,MPI%8051,SPT_b4.34.filelist)
	#$(call mk6dir2filelist,mark6-04,34,MPI%8053,SPT_b4.12.filelist)

## KVN Yonsei

# todo - just band3, and e-transferred to Haystack?


## CHECKING

buglist:
	# All scans that have unexpected time stamps
	grep -v " 607\| 608" *.filelist || true
	grep " 51544." *.filelist || true


## COPY

install:
	for exptname in $(TRACKS_230G) $(TRACKS_345G); do \
		mkdir -p /Exps/$${exptname}/$(REV)/b1/ /Exps/$${exptname}/$(REV)/b1/ ; \
		mkdir -p /Exps/$${exptname}/$(REV)/b2/ /Exps/$${exptname}/$(REV)/b2/ ; \
		mkdir -p /Exps/$${exptname}/$(REV)/b3/ /Exps/$${exptname}/$(REV)/b3/ ; \
		mkdir -p /Exps/$${exptname}/$(REV)/b4/ /Exps/$${exptname}/$(REV)/b4/ ; \
	done
	#
	for exptname in $(TRACKS_230G) $(TRACKS_345G); do \
		cp -a *_b1.* /Exps/$${exptname}/$(REV)/b1/ ;	\
		cp -a *_b2.* /Exps/$${exptname}/$(REV)/b2/ ;	\
		cp -a *_b3.* /Exps/$${exptname}/$(REV)/b3/ ;	\
		cp -a *_b4.* /Exps/$${exptname}/$(REV)/b4/;		\
	done

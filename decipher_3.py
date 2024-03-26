# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:23:15 2024

@author: hkopansk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
import math 

alphabet_number = list(range(1, 27))

alphabet_array = []

for i in range(26):
    #temp_list = 
    alphabet_array.append(alphabet_number[i:] + alphabet_number[0:i])

alphabet_array = np.array(alphabet_array)

chr_convert = lambda x: chr(x + 96)
ord_convert = lambda x: ord(x) - 96

def shift_decipher(x, n):
    if ord(x) + n > 122:
        result_1 = chr(ord(x) + n - 26)
    else:
        result_1 = chr(ord(x) + n)
        
    return result_1
    

alpha_list = list(map(chr_convert, alphabet_number))

np_chr_convert = np.vectorize(chr_convert)

alphabet_array2 = np_chr_convert(alphabet_array)

df_v_table = pd.DataFrame(alphabet_array2)
df_v_table.index = alpha_list
df_v_table.columns = alpha_list

key_word = 'benice'

row_1 =  'tvbscnrwdlrnlgpf'
row_2 =  'adnfbnrucbqprnoi'
row_3 =  'pbshfrcavqsnhpad'
row_4 =  'imrhlxebipkrcnbc'
row_5 =  'gtzarsirbospavql'
row_6 =  'pxtqmiahsrbaqowo'
row_7 =  'pbwncnvcqrrszpnr'
row_8 =  'sriernndxcadpmny'
row_9 =  'ebnpocpbvascaest'
row_10 = 'srcaxsrierangmse'
row_11 = 'rmtvsntfbargqlcn'
row_12 = 'btpupbvaqmsnecoq'
row_13 = 'srtvsnirzpipblah'
row_14 = 'apqrhtaqxlglclco'
row_15 = 'pqhagaqorpaepksn'
row_16 = 'tfqhwpbalivrbnsn'

full_string = row_1 + row_2 + row_3 + row_4 + row_5 + row_6 + row_7 + row_8 + row_9 + row_10 + row_11 + row_12 +row_13 + row_14 + row_15 + row_16
be_nice_pt = row_1 + row_2 + row_3 + row_4 + row_5 + row_6 + row_7
play_fair_pt = row_8 + row_9 + row_10 + row_11 + row_12 + row_13 + row_14 + row_15 + row_16
  
def key_word_mul(kw, mul):
    mul_floor = math.floor(mul/len(kw))
    frac_mul = int(round(len(kw)*(mul/len(kw) - mul_floor)))
    temp_word = kw*mul_floor
    for i in range(frac_mul):
        temp_word = temp_word + kw[i]
    return temp_word

def decipher_code(key_w, e_text):
    de_text = ''
    finder_1 = key_word_mul(key_w, len(e_text))
    for i in range(len(e_text)):
        de_text = de_text + df_v_table[df_v_table[finder_1[i]] == e_text[i]].values[0][0]
    return de_text    

full_string_bn = decipher_code(key_word, full_string)
full_string_bn_pf = decipher_code('nice', row_1)

print(full_string_bn_pf)

benice_freq = []
playfair_freq = []

for i in string.ascii_lowercase:
    benice_freq.append([i, be_nice_pt.count(i)])
    playfair_freq.append([i, play_fair_pt.count(i)])

df_bn_freq = pd.DataFrame(benice_freq)
df_bn_freq.columns = ['Letter', 'Count']

df_pf_freq = pd.DataFrame(playfair_freq)
df_pf_freq.columns = ['Letter', 'Count']

fig, ax = plt.subplots(ncols = 2, dpi = 250)

sns.barplot(x = 'Count', y = 'Letter', 
            data = df_bn_freq.sort_values(by = 'Count', ascending = False), 
            ax = ax[0])

sns.barplot(x = 'Count', y = 'Letter', 
            data = df_pf_freq.sort_values(by = 'Count', ascending = False), 
            ax = ax[1])

long_text = r'JUSTBEFORESUNRISE,LOUISHUNNINCKwokeupataresearchcenterinTanzania’sSerengetiNationalPark.Heclimbedintoanoff-roadvehicle,joinedbyanassistant,androdethroughthescrubbyequatoriallandscapeuntiltheysawagroupofreddish-brownantelopecalledimpalas.Theystoppedandjottedlocationnotes:thetime,weather,otherspeciesinthevicinity.Theycountedtheslendercreatures,breakingthemdownbyagegroupandseparatingthemales,withtheirlyre-shapedhorns,fromthefemales.“Andthenwewaitedfortheimpalatodefecate,”saysHunninck,aconservationbiologistnowattheUniversityofIllinoisUrbana–Champaign.“Basically,topoop.”Thefecalsamplestheycollected(storedoniceuntilbroughttoaUniversityofMassachusetts–Dartmouthlab)containedatroveofinformationabouthowmuchstresstheimpalaswereunder.Bymeasuringtheconcentrationsofstress-relatedhormonesandanalyzingthemalongsidetheenvironmentaldata,Hunninckcouldinferwhichhumanactivitiestooktheheaviesttollontheimpalas’bodies.Calledwildlife-stressphysiology,thisbranchofsciencehasbeenflourishinglately—withbigimplicationsforconservation.Measuringhowstressaffectsindividualcreatures,scientistssay,couldserveasanearly-warningsystemforpopulationsintrouble.“Thetraditionalapproachisthatwemonitorpopulations,andweseethattheyaredeclining.Andthatoftentakesseveralyears,”Hunnincksays.“Andthenwetrytofigureoutwhatiscausingthis.Andonlythendowetryandfigureouthowtostopthatthreat.Andthatcantakemanydecades.”Yetthreatscanbesublethalbeforetheybecomelethal,andthat’swherestressresearchcomesin.“Ifyoucanpredictwhathumanactivities—whetherthat’shuntingortourismorbuildingroads—willdotoananimalpopulationbylookingatwhatitdoestothephysiologyofoneanimalorgroupofanimals,”Hunnincksays,“youcanstarttopreventpopulationdeclinesbeforetheyhappen.”In2020,HunninckpublishedsomeofhisfindingsinConservationPhysiology.Byexaminingstresshormonescalledglucocorticoids,hefoundthatconcentrationswerehighestduringweekswithoutrainfall,whenthevegetationimpalaseatdriedupandshedsomenutritionalvalue.Climatechangeislikelytobringmoresuchdroughtsinthefuture.Hunnincklookedatlocalfactors,too,includingtheproximityofMaasaicattlegrazers,wholiveinclustersofthatched-roofhuts.Impalaslivingneardenserhumansettlementshadhigherglucocorticoidlevels.Butthosesettlementshadasmallerimpactthanthedryweatherandparchedgrasslands—suggestingthatimpalasurvivaldependsprimarilyonaddressingglobalissuessuchasclimatedisruption.“Evenwiththisgrazingpressure,theMaasaiarenottheissuehere,”Hunnincksays.“Itisbiggerdriversofchangethataremoreimportant.”StressinthecityItshouldcomeasnosurprisethatwildlife-stressphysiologyisenjoyingamoment.Twocriticalfactorshaveconverged:theneedandthetechnology.First,there’sgrowingpublicalarmoverclimatechange,pollutionandhabitatdestruction—humanactivitiesthatthreatenwildanimalpopulations.It’sclearsomethingneedstobedone,butfirstresearchersneedtounderstandtheproblems.Meanwhile,toolstomeasurestresshavegrownmoresophisticated,lessinvasiveandeasiertouseinthefield.“Insteadofassumingthatsomeecologicalstressorisgoingtobebadorgoodforananimal,”saysMichaelSheriff,aphysiologicalecologistattheUniversityofMassachusetts–Dartmouth,“wecanactuallygoandasktheanimalitself.”nepromisingtoolusestelomeres,thecapsthatanchortheendsofchromosomesandkeepthemfromdegrading.Inmanyanimals,includinghumans,telomeresshortenovertime,likeabiologicaltimercountingdown.Thefastertheyshrink,thefasterananimalages.“Whenyouhaveenvironmentalstress,thetelomereswillshortenatamuchfasterrate,”saysCarolineIsaksson,anecophysiologistatLundUniversityinSweden.Isakssonstudiesgreattits,Europeansongbirdswithblackstripesrunningdowntheiryellowchestsandsqueakycallsthatsoundlikebicyclepumps.Rangingacrossthecontinent,theyhaveexpandedfromwoodlandsintocitiesandsuburbs.Buturbanareasarefullofstressors:noise,dirtyair,artificiallights.There’splentyoffood(amplewhitebread,forexample),butit’slessnutritiousthanwhatruralbirdseat.Toexaminethebirds’chromosomes,IsakssondrewbloodsamplesandextractedDNA.Greattitsraisedincities,shediscovered,hadshortertelomeres.WhenIsakssonnest-swapped2-day-oldtits—movingcountry-hatchedbirdsintocitynestboxesandviceversa—shefoundtheplaceoforigindidn’tmatter.Itwaswherethebirdsgrewupthatgovernedtheirtelomerelengths.“Soit’sreallyanenvironmentaleffect,”shesays.Followingthesamebirdsintothenextseason,shelearnedthattheshorteritstelomeres,thelesslikelyachickwouldgrowintoabreedingadult.Butchicksthatdidreachadulthoodseemedtoadapt,andIsakssonsaysthatinheritancemightplaysomerole.InastudypublishedlastyearinNatureCommunications,sheanalyzedtheDNAofgreattitsfromnineEuropeancities—includingGlasgow,Barcelona,ParisandMilan—andtheirruraloutskirts.Nomatterwheretheylived,theurbanbirdshadevolvedquickly,particularlyingeneslinkedtocognition,circadianrhythmsandbehaviorssuchasaggression.Theyweremoresimilartooneanother,infact,thantotheirclosestruralneighbors.“Theyhavetobetougherandmoreresilient,”Isakssonsays,“tolivewithhighdensitiesofhumansandtrafficandnoiseandallthesedifferentfactorsthatnormallywouldfreakthemout.”“Adaptivebenefits”ofstressStressisnotalwaysbad.Thiscanbeeasytoforgetbecausechronicstressexhaustsus.Itmakesusrestlessandirritable.Ittakesatollonourthinking,mentalhealthandimmunesystems.Butmoderatestresskeepsusalert.Itpowersusthroughdeadlinesandhelpsusrespondtocrises.Likewise,forwildlife,stressistwosided.Itcanbelethalatitsworse,saysSheriff.Butatlowerlevelsitcanhave“adaptivebenefits,”helpinganimalscopewithpunishingenvironments.Sheriffhasstudiedsnowshoehares,whichliveinNorthAmericanborealforestsinaviolentpasdedeuxwithCanadalynx.Thehareshavecamouflagedcoatsthatchangewiththeseasonandgianthindlegsthatleap12feetatatime—toolsforevadingtheirfelinepredators.Butlynxhavesharpears,goodeyesandreflexesthathaveevolvedtocatchhares,whichmakeupthemajorityoftheirdiet.Thetwomammalpopulationsoscillateintandem.FromtheU.S.RockiesandAppalachiansintoCanadaandallthewayuptoAlaska,abundantharesprovideafeastforlynx,whosepopulationsurgesinresponse.Thenthehares’numbersplummet,andtheirpredators’numberssoonfollow.AsaPh.D.studentinthe2000s,Sheriffwonderedifstressplaysaroleinthesefluctuations.TravelingtospruceandwillowforestsoftheYukon,helivetrappedharesandcollectedbloodandfecalsamplestomeasureglucocorticoids.Whenlynxwereplentiful,hediscovered,hareshadelevatedhormonelevels.Inanexperiment,Sheriffsimulatedhighpredationriskbypenningsomeoftheharesandexposingthemtoatraineddog.Justseeingandsmellingthedogreducedtheirsurvivalrates,eventhoughtheyhadnodirectcontact.“So,beingscaredtodeath,”hesays,bluntly.Inthewild,stressedfemalehareshadfewerandsmalleroffspring.Thismightsoundlikeaproblem,butSheriffcallsitadaptive:Feweryoungcutsdowntheamountoftimemothersmustforagetofeedthem.“Lighterbabieseatless,”hesays.“Fewerbabieseatless.Soitallowsmomtonothavetoexposeherselftopredatorsasmuch.Becauseifmomdies,itdoesn’tmatterhowbigyouare.Ifmomdies,youdie.”Sheriffalsodiscoveredthattheoffspringofstressedmothershadhighglucocorticoidlevelsaswell,eveniftheyhadneverseenalynxthemselves.Thosehormonesarelinkedtofearbehaviorssuchashiding,whichhespeculateshelptheyoungsurvive.“Ifthosebabiesweren’tfearfulatall,buttherewereawholebunchofpredatorswanderingaround,allthosebabiesaregoingtobeeaten,”hesays.“Theyjustwanderupthemeadowandgetpickedoff.”Scientificcross-fertilizationTodiscusssomeoftherecentfindingsfromwildlife-stressresearch—alongwithimplicationsofthework—BernhardVoelkl,abiologistatSwitzerland’sUniversityofBern,invited11colleaguestoaSwissmountainchaletlastyear.Participants,includingIsaksson(viaZoom)andSheriff,talkedaboutadvancesinwildlife-stressbiomarkersaswellastheirownresearchonanimalspeciesrangingfrompandas,polarbearsandgrizzliestosquirrels,snowshoeharesandbirds.Manyofthescientistswereconcernedprimarilywithpopulationhealth.Othershadadifferentfocus:thewell-beingofindividualanimals.Thesetwobranchesofsciencetendtooperateindependently,andsomeofthoseatthegatheringhopedthatabitofcross-fertilizationmightbenefiteveryone(includingtheanimals).Thisshiftstheparadigmabit.“Ourconcernforanimalwelfarehasbeenlimitedtoanimalsinourcustody:farmanimals,labanimals,pets,zooanimals,circusanimals,”saysHannoWürbel,ananimal-welfarescientistalsoattheUniversityofBern.Buthumansplayagrowingroleinmanagingwildpopulationsandtheecosystemstheyinhabit.“Andsotheboundarybetweenwildlifeandanimalsunderourcareisbecomingincreasinglyblurry,”Würbelsays.What’smore,headds,wildlifeandwelfarescientistshaveeachdevelopedtoolsthatcanhelptheother.ForVoelkl,thereisamoralcomponent.“Weacknowledgethatanimalsaresentientbeings,”hesays.“Thereisabroadsocietalconsentthathumansshouldnotinflictunnecessarypainandsuffering.”Theplightofasinglecreaturecanarousethepublic—aswithapopular2017videoofanemaciatedpolarbearintheCanadianArctic.Nomatterwhythatparticularbearwasstarving,thevideomadeaconvincingcasethatmeltingseaicecausedbyclimatechangethreatenstodecimatethespecies.Thatcanmakeithardtoseparateconservationandwelfare.“Veryoften,whatisgoodfortheindividualturnsouttobegoodforthepopulationandviceversa,”Voelklsays.Scientificcollaboration,itseems,couldonlybenefitboth.'

long_text_freq = []

for i in string.ascii_lowercase:
    long_text_freq.append([i, long_text.count(i)])
    
df_lt_freq = pd.DataFrame(long_text_freq)
df_lt_freq.columns = ['Letter', 'Count']

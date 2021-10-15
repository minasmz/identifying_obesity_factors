import pysubgroup as ps
import pandas as pd
import re, csv
#from statistics import stdev
#import statsmodels.api as sm
#from scipy.stats import norm
#import pylab
#'MEN', 'WOMEN', 'COMMERCIAL',


#feature_name = ['MEN', 'WOMEN', 'COMMERCIAL', 'SELF_PAY', 'MEDICARE', 'MEDICAID', 'METRO', 'METRO_ADJUNCENT', 'RURAL', 'LOW_INCOME', 'MED_INCOME', 'HIGH_INCOME',
#                'LATINO', 'AFRICAN_AMERICAN', 'WHITE', 'OTHER_RACE', 'UNDER_THIRTY', 'THIRTIES', 'FOURTIES', 'FIFTIES', 'SIXTIES', 'SEVENTIES']
feature_name = ["All"]

ii = [3, 4, 5]
jj = [2000, 5000, 10000]

#beamSearch_medication_level_5000_3WRAccQF_MEDICARE

def feature_quality_to_csv (feature_quality_dictionary, i, j, feature_k):
    print(i, j, feature_k)
    with open('avg_quality_0005_medication_level_' + str(j) + '_' + str(i) + '_WRAccQF_om_' + str(feature_k) + '.csv', 'w') as f:
        fieldNames = ['key', 'quality']
        writer = csv.DictWriter(f, fieldnames=fieldNames)
        #f.write("%s,%s\n" % ('key', 'frequency'))
        writer.writeheader()
        for key in feature_quality_dictionary.keys():
            writer.writerow({'key': key, 'quality': feature_quality_dictionary[key]})
        print (j, i, feature_k)

def calc_quality_count_quality(feature_list, i_value, j_value, feature_k):
    #df = pd.read_csv('updated_obesity_incident_result_' + str(j_value) + '_' + str(i_value) + '_WRAccQF_om_' + str(feature_k) +'.csv')
    df = pd.read_csv('beamSearch_medication_level_' + str(jj[j]) + '_' + str(ii[i]) + 'WRAccQF_' + str(
        feature_name[kkkkk]) + '.csv')

    df = df[df.quality > 0.0005]

    feature_quality_dictionary = {}
    for each_feature in feature_list:
        contain_feature = df[df['subgroup'].str.contains(each_feature)]
        feature_quality = sum(list(contain_feature['quality']))
        number_of_SD = len(list(contain_feature['quality']))
        avg_feature_quality = float(feature_quality)/float(number_of_SD)
        feature_quality_dictionary[each_feature] = avg_feature_quality
        #feature_quality_dictionary[each_feature] = float(len(list(contain_feature)))/float(len(df))
    feature_quality_to_csv(feature_quality_dictionary, i_value, j_value, feature_k)



for kkkkk in range (1):
    for i in range (3):
        for j in range (3):
            df = pd.read_csv('beamSearch_medication_level_' + str(jj[j]) + '_' + str(ii[i]) + 'WRAccQF_'+ str(feature_name[kkkkk]) +'.csv')
            #df = pd.read_csv('updated_obesity_incident_result_' + str(jj[j]) + '_' + str(ii[i]) + '_WRAccQF_om_'+ str(feature_name[kkkkk]) +'.csv')
            df_subgroup = df['subgroup']
            for m in range(len(df_subgroup)):
                # print (df_subgroup[ii])
                df_subgroup[m] = df_subgroup[m].replace(
                    'Antidepressant - Selective Serotonin Reuptake Inhibitors (SSRIs)', 'SSRIs')
                df_subgroup[m] = df_subgroup[m].replace(
                    'Antidepressant-Norepinephrine and Dopamine Reuptake Inhibitors (NDRIs)', 'NDRIs')
                df_subgroup[m] = df_subgroup[m].replace(
                    'Antidepressant - Serotonin-Norepinephrine Reuptake Inhibitors (SNRIs)', 'SNRIs')
                df_subgroup[m] = df_subgroup[m].replace(
                    'Antidepressant-Norepinephrine and Dopamine Reuptake Inhibitors (NDRIs)', 'NDRIs')
                df_subgroup[m] = df_subgroup[m].replace('Antihyperlipidemic - HMG CoA Reductase Inhibitors (statins)',
                                                        'statins')
                df_subgroup[m] = df_subgroup[m].replace(
                    'Antidepressant - Serotonin-2 Antagonist-Reuptake Inhibitors (SARIs)', 'SARIs')
                df_subgroup[m] = df_subgroup[m].replace(
                    'Antidepressant-Tricyclics and Related (Non-Select Reuptake Inhibitors)', 'NSRIs')
                df_subgroup[m] = df_subgroup[m].replace('Antidepressant - Alpha-2 Receptor Antagonists (NaSSA)',
                                                        'NaSSA')
                df_subgroup[m] = df_subgroup[m].replace('Antihyperglycemic - Insulin Response Enhancers', 'IREs')
                df_subgroup[m] = df_subgroup[m].replace('ACE Inhibitors (ACEIs) Combinations', 'ACEIs')
                df_subgroup[m] = df_subgroup[m].replace('Angiotensin II Receptor Blocker (ARBs) and ARB Combinations',
                                                        'ARBs Combinators')
                df_subgroup[m] = df_subgroup[m].replace('Angiotensin II Receptor Blocker (ARBs)', 'ARBs')
                df_subgroup[m] = df_subgroup[m].replace('Angiotensin II Receptor Blockers (ARBs)', 'ARBs')
                df_subgroup[m] = df_subgroup[m].replace('Angiotensin II Receptor Blocker (ARB)-Diuretic Combinations',
                                                        'ARBs Diuretic')
                df_subgroup[m] = df_subgroup[m].replace('ACE Inhibitor and Diuretic Combinations', 'ACE Diuretic Comb')
                df_subgroup[m] = df_subgroup[m].replace('Antihyperglycemic (Antidiabetic) Combinations', 'Antidiabetic')

            df['subgroup'] = df_subgroup

            df = df[df.quality > 0.0005]
            #df['quality'].hist()
            #df['quality'].plot(kind='box')


            #sm.qqplot(df['quality'], line='45')
            #pylab.show()

            #quality_list = list(df['quality'])
            #quality_mean = float(sum(quality_list))/float(len(quality_list))
            #quality_std = stdev(quality_list)

            dfh_sg = df['subgroup']
            dfh_sg_list = list(dfh_sg)
            feature_list = []
            for iii in dfh_sg_list:
                sg = iii.split('AND')
                for jjj in sg:
                    jjj = jjj.strip()
                    jjj = re.sub('==1.0', '', jjj)
                    jjj = re.sub('==1', '', jjj)
                    feature_list.append(jjj)
            feature_list = list(set(feature_list))

            '''
            feature_quality_dictionary = {}
            for each_feature in feature_list:
                contain_feature = df[df['subgroup'].str.contains(each_feature)]
                feature_quality = sum(list(contain_feature['quality']))
                #number_of_SD = len(list(contain_feature['quality']))
                #avg_feature_quality = float(feature_quality) / float(number_of_SD)
                feature_quality_dictionary[each_feature] = feature_quality
            feature_quality_to_csv(feature_quality_dictionary, ii[i], jj[j], feature_name[kkkkk])
            '''
            calc_quality_count_quality(feature_list, ii[i], jj[j], feature_name[kkkkk])



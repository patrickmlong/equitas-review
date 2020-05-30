"""
Scripts below adopted from https://github.com/dssg/aequitas
"""

from equitas.bias import Bias
from aequitas.plotting import Plot

aqp = Plot()

fpr_plot = aqp.plot_group_metric(xtab, 'fpr', min_group_size=0.05)


b = Bias()
bdf = b.get_dsiparity_predified_groups(
xtab,
original_df = df,
ref_groups_dict = {"race":"Caucasian",  "sex":"Male", "age_cat":"25-45"},
alpha = 0.05,
check_signficance = False)


fpr_disparity = aqp.plot_disparity(bdf, group_metric='fpr_disparity',
                                       attribute_name='race')

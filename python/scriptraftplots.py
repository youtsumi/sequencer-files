import os
from raftstats import *
import scope

#datadir = '/Users/nayman/Documents/REB/TS8/RTM1/3764/Fe55Bias'
#datadir = '/Users/nayman/Documents/REB/TS8/RTM2/4876D'
#datadir = '/Users/nayman/Documents/REB/TS8/RTM2/4875D/28475'
#datadir = '/Users/nayman/Documents/REB/TS8/RTM1/RefitRuns/run-5190D'
datadir = '/Users/nayman/Documents/REB/TS8/RTM8/run-5929'

#l = sorted([os.path.join(datadir, f) for f in os.listdir(datadir) if os.path.splitext(f)[1] in [".fits", ".fz"]])
#ccd154 = 'E2V-CCD250-154-Dev_fe55_bias_000_4876D_20170427035453.fits'
#ccd252 = 'E2V-CCD250-252-Dev_fe55_bias_000_4876D_20170427035453.fits'
#l = [os.path.join(datadir, f) for f in [ccd154, ccd252]]

l = get_fits_raft(inputfile='', datadir=datadir)

#plothisto_overscan(l[0])

plot_corrcoef_raft(l[0], ROIrows=slice(190, 1990), ROIcols=slice(522, 576), xylabels=l[1], title='run-5929')

#write_header_stats(l, ROIrows=slice(700,1400))


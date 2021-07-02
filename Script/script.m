ncdisp('77DN200508_00001_00002_ctd.nc')
Temp1 = ncread('77DN200508_00001_00002_ctd.nc','temperature');

%% 
ncdisp('77DN200508_00030_00004_ctd.nc')

%% 
%Te = ncread('77DN200508_00012_00003_ctd.nc','temperature');


%%
st1  = ncread('77DN200508_00001_00002_ctd.nc','temperature');
st2  = ncread('77DN200508_00002_00003_ctd.nc','temperature');
st3  = ncread('77DN200508_00003_00001_ctd.nc','temperature');
st4  = ncread('77DN200508_00004_00001_ctd.nc','temperature');
st5  = ncread('77DN200508_00005_00001_ctd.nc','temperature');
st6  = ncread('77DN200508_00006_00002_ctd.nc','temperature');
st7  = ncread('77DN200508_00007_00001_ctd.nc','temperature');
st8  = ncread('77DN200508_00008_00001_ctd.nc','temperature');
st9  = ncread('77DN200508_00009_00001_ctd.nc','temperature');
st11 = ncread('77DN200508_00011_00001_ctd.nc','temperature');
st12  = ncread('77DN200508_00012_00001_ctd.nc','temperature');
st14  = ncread('77DN200508_00014_00001_ctd.nc','temperature');
st15  = ncread('77DN200508_00015_00001_ctd.nc','temperature');
st17  = ncread('77DN200508_00017_00001_ctd.nc','temperature');
st19  = ncread('77DN200508_00019_00001_ctd.nc','temperature');
st20  = ncread('77DN200508_00020_00001_ctd.nc','temperature');
st21  = ncread('77DN200508_00021_00001_ctd.nc','temperature');
st23  = ncread('77DN200508_00023_00001_ctd.nc','temperature');
st25 = ncread('77DN200508_00025_00001_ctd.nc','temperature');
st26 = ncread('77DN200508_00026_00001_ctd.nc','temperature');
st29 = ncread('77DN200508_00029_00001_ctd.nc','temperature');
st30 = ncread('77DN200508_00030_00001_ctd.nc','temperature');
st31  = ncread('77DN200508_00031_00001_ctd.nc','temperature');
st32  = ncread('77DN200508_00032_00001_ctd.nc','temperature');
st33 = ncread('77DN200508_00033_00001_ctd.nc','temperature');
st34 = ncread('77DN200508_00034_00001_ctd.nc','temperature');
st35 = ncread('77DN200508_00035_00001_ctd.nc','temperature');
st36 = ncread('77DN200508_00036_00001_ctd.nc','temperature');
st37  = ncread('77DN200508_00037_00001_ctd.nc','temperature');
st38  = ncread('77DN200508_00038_00001_ctd.nc','temperature');
st39  = ncread('77DN200508_00039_00001_ctd.nc','temperature');
st40 = ncread('77DN200508_00040_00001_ctd.nc','temperature');
st41  = ncread('77DN200508_00041_00001_ctd.nc','temperature');
st42 = ncread('77DN200508_00042_00001_ctd.nc','temperature');
st43  = ncread('77DN200508_00043_00003_ctd.nc','temperature');
st44 = ncread('77DN200508_00044_00001_ctd.nc','temperature');
st46  = ncread('77DN200508_00046_00001_ctd.nc','temperature');
st47 = ncread('77DN200508_00047_00001_ctd.nc','temperature');
st49 = ncread('77DN200508_00049_00001_ctd.nc','temperature');
st50 = ncread('77DN200508_00050_00003_ctd.nc','temperature');
st51  = ncread('77DN200508_00051_00001_ctd.nc','temperature');
st53  = ncread('77DN200508_00053_00001_ctd.nc','temperature');
%%

ncdisp('77DN200508_00033_00001_ctd.nc')

%%
%T = table(st1,st2,st3,st4,st5,st6,st7,st8,st9,st11,st12,st14,st15,st17,st19,st20,st21,st23,st25,st26,st29,st30,st31,st32,st33,st34,st35,st36,st37,st38,st39,st40,st41,st42,st43,st44,st46,st47,st49,st50,st51,st53)










%%
% kl=linspace(1,km,km+1);
% 
% for jj=1:km+1;
%     temp(jj)=ncread('77DN200508_00001_00002_ctd.nc','temperature')
%     term2(jj)=Xd(jj,1)*sin(wm2*kl(1,jj)*delt);
%     
% end  

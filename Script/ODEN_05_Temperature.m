ncdisp('77DN200508_00001_00002_ctd.nc');
Temp1 = ncread('77DN200508_00001_00002_ctd.nc','temperature');

%% 
ncdisp('77DN200508_00001_00002_ctd.nc')
%% 
%Te = ncread('77DN200508_00012_00003_ctd.nc','temperature');


%%
ncdisp('77DN200508_00002_00003_ctd.nc','temperature');

%%
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

P51  = ncread('77DN200508_00051_00001_ctd.nc','pressure');
P53  = ncread('77DN200508_00053_00001_ctd.nc','pressure');

%%
tm1=mean(st1)
tm2=mean(st2)
tm3=mean(st3)
tm4=mean(st4)
tm5=mean(st5)
tm6=mean(st6)
tm7=mean(st7)
tm8=mean(st8)
tm9=mean(st9)
tm11=mean(st11)
tm12=mean(st12)
tm14=mean(st14)
tm15=mean(st15)
tm17=mean(st17)
tm19=mean(st19)
tm20=mean(st20)
tm21=mean(st21)
tm23=mean(st23)
tm25=mean(st25)
tm26=mean(st26)
tm29=mean(st29)
tm30=mean(st30)
tm31=mean(st31)
tm32=mean(st32)
tm33=mean(st33)
tm34=mean(st34)
tm35=mean(st36)
tm36=mean(st36)
tm37=mean(st37)
tm38=mean(st38)
tm39=mean(st39)
tm40=mean(st40)
tm41=mean(st41)
tm42=mean(st42)
tm43=mean(st43)
tm44=mean(st44)
tm46=mean(st46)
tm47=mean(st47)
tm49=mean(st49)
tm50=mean(st50)
tm51=mean(st51)
tm53=mean(st53)



%%
T= [tm1,tm2,tm3,tm4,tm5,tm6,tm7,tm8,tm9,tm11,tm12,tm14,tm15,tm17,tm19,tm20,tm21,tm23,tm25,tm26,tm29,tm30,tm31,tm32,tm33,tm34,tm35,tm36,tm37,tm38,tm39,tm40,tm41,tm42,tm43,tm44,tm46,tm47,tm49,tm50,tm51,tm53];
%%
% meantemp=mean(T)
%%
kll=linspace(1:53);
for j=1:ks+1;
    tm(j)=mean(st(j));
    
end  


tm1=mean(st1)

%%
worldmap([75 90], [-180 180])
load coast
land = shaperead('landareas.shp', 'UseGeoCoords', true);
geoshow(land, 'FaceColor', [0.15 0.5 0.15])







% Map of Antarctica
%     ax=worldmap('North Pole')
%     land = shaperead('landareas', 'UseGeoCoords', true);
  
    
%     arcticocean = shaperead('landareas', 'UseGeoCoords', true,...
%         'Selector',{@(name) strcmp(name,'Arctic'), 'Name'});
    %patchm(Polarocean.Lat, Polarocean.Lon, [0.5 1 0.5])

    
    
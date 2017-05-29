i = imread('3.png');
%imshow(a);
%imcrop(a);
a = imcrop(i,[13.5 10.5 65 13]);
b = imcrop(i,[55.5 11.5 23 36]);
c = imcrop(i,[64.5 51.5 26 75]);
d = imcrop(i,[25.5 108.5 60 28]);
e = imcrop(i,[12.5 65.5 18 41]);
f = imcrop(i,[12.5 22.5 18 34]);
g = imcrop(i,[17.5 47.5 54 17]);

aa = mean(a);
bb = mean(b);
cc = mean(c);
dd = mean(d);
ee = mean(e);
ff = mean(f);
gg = mean(g);

am = (max(aa(:,:,2))-min(aa(:,:,2)));
bm = (max(bb(:,:,2))-min(bb(:,:,2)));
cm = (max(cc(:,:,2))-min(cc(:,:,2)));
dm = (max(dd(:,:,2))-min(dd(:,:,2)));
em = (max(ee(:,:,2))-min(ee(:,:,2)));
fm = (max(ff(:,:,2))-min(ff(:,:,2)));
gm = (max(gg(:,:,2))-min(gg(:,:,2)));

if(am>0)
    bia = 1;
else
    bia = 0;
end;    
if(bm>0)
    bib = 1;
else
    bib = 0;
end;
if(cm>0)
    bic = 1;
else
    bic = 0;
end;
if(dm>0)
    bid = 1;
else
    bid = 0;
end;
if(em>0)
    bie = 1;
else
    bie = 0;
end;
if(fm>0)
    bif = 1;
else
    bif = 0;
end;
if(gm>0)
    big = 1;
else
    big = 0;
end;
arr = [bia,bib,bic,bid,big,bif,bie];
disp(arr);

pkg load signal;

s=char(97:122)
filename="Character Spikes";
fid=fopen(filename, "w");

for i=1:length(s)
  
  %[y,Fs]=audioread([s(i),'.wav']);
  [y,Fs]=audioread([s(i),'1.wav']);
  %[y,Fs]=audioread([s(i),'2.wav']);

  Y=double(y)/(max(abs(y))+1);
  n=length(Y);
  t=(0:n-1)/Fs;
  p=abs(fft(Y));
  f=(0:n-1)*(Fs/n);
  plot(f,p);
  
  %N=Fs*2;
  %X=fft(y,N);
  %plot(abs(X));
  
  pk=findpeaks(abs(p(:,1)));
  myData=sprintf('%c spikes at: %f\n', s(i), max(pk));
  fputs(fid, myData);
  
  title(s(i))
  print(s(i),'-dpdf' )
end  

fclose(fid);
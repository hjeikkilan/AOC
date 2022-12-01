fid = fopen('input1.txt','rt');
invidualSum = [];
allSums = [];
while true
  line = fgetl(fid);
  line;
  if ~ischar(line); break; end  %end of file

  if isempty(line)
      allSums = [allSums; sum(invidualSum)];
      invidualSum = [];
  else
      invidualSum = [invidualSum;str2double(line)];
  end
end
fclose(fid);

max(allSums)
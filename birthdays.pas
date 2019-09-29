var 
    filetext,file_OUT: text;
    star,mlad:string;
    month: array[1..13] of integer;
    star_day, star_month, star_year, mlad_day, mlad_month, mlad_year, difference: integer;
    function day_col(day,months:integer):integer;
    var i, d:integer;
    begin
    month[1]:=0;
    month[2]:=31;
    month[3]:=28;
    month[4]:=31;
    month[5]:=30;
    month[6]:=31;
    month[7]:=30;
    month[8]:=31;
    month[9]:=31;
    month[10]:=30;
    month[11]:=31;
    month[12]:=30;
    month[13]:=31;
    d:=day;
    for i:=1 to months do d:=d + month[i];
    day_col:=d;
    end;
begin
assign(filetext,'./INPUT.txt');
reset(filetext);
readln(filetext,star);
readln(filetext,mlad);
close(filetext);
star_day:=(ord(star[1])-48)*10+(ord(star[2])-48);
star_month:=(ord(star[4])-48)*10+(ord(star[5])-48);
star_year:=(ord(star[7])-48)*10+(ord(star[8])-48);
mlad_day:=(ord(mlad[1])-48)*10+(ord(mlad[2])-48);
mlad_month:=(ord(mlad[4])-48)*10+(ord(mlad[5])-48);
mlad_year:=(ord(mlad[7])-48)*10+(ord(mlad[8])-48);
difference:=day_col(mlad_day,mlad_month)-day_col(star_day,star_month);
if mlad_year<>star_year then difference:=difference+(mlad_year-star_year)*365;
assign(file_OUT, './OUTPUT.txt');
rewrite(file_OUT);
writeln(file_OUT, difference);   
close(file_OUT);
end.
